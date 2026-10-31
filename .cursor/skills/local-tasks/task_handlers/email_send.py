"""
Email send handler for local execution.
Uses local SMTP client or opens draft in default email client.
"""
import smtplib
import webbrowser
import tempfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

def execute(task_data):
    """Execute email send task."""
    
    payload = task_data.get('payload', {})
    emails = payload.get('emails', [])
    
    print(f"📧 Preparing to send {len(emails)} email(s)...")
    
    results = []
    for email_data in emails:
        try:
            result = send_email(email_data, payload.get('smtp_config', {}))
            results.append(result)
        except Exception as e:
            results.append({"status": "error", "message": str(e)})
    
    all_success = all(r.get('status') == 'success' for r in results)
    
    return {
        "status": "success" if all_success else "partial",
        "emails_sent": len([r for r in results if r.get('status') == 'success']),
        "details": results
    }

def send_email(email_data, smtp_config):
    """Send a single email."""
    
    from_addr = email_data['from']
    to_addrs = email_data['to']
    cc_addrs = email_data.get('cc', [])
    subject = email_data['subject']
    body = email_data['body']
    attachments = email_data.get('attachments', [])
    
    print(f"\n  To: {', '.join(to_addrs)}")
    if cc_addrs:
        print(f"  CC: {', '.join(cc_addrs)}")
    print(f"  Subject: {subject}")
    print(f"  Attachments: {len(attachments)}")
    
    # Create email
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)
    if cc_addrs:
        msg['Cc'] = ', '.join(cc_addrs)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach files
    for att in attachments:
        att_path = Path(att.get('local_fallback') or att['r2_path'])
        if not att_path.exists():
            print(f"    ⚠️  Attachment not found: {att_path}")
            continue
        
        with open(att_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={att["name"]}')
            msg.attach(part)
            print(f"    ✓ {att['name']}")
    
    # Try SMTP or fallback to mailto:
    method = smtp_config.get('method', 'smtp')
    
    if method == 'webmail_or_outlook':
        # Save as .eml and open
        eml_file = Path(tempfile.gettempdir()) / f"{subject[:30]}.eml"
        with open(eml_file, 'w') as f:
            f.write(msg.as_string())
        
        print(f"  📄 Saved as: {eml_file}")
        print(f"  🌐 Opening in default email client...")
        
        try:
            webbrowser.open(str(eml_file))
            return {"status": "success", "method": "eml_file", "file": str(eml_file)}
        except:
            return {"status": "success", "method": "manual", "message": f"Open {eml_file} manually"}
    
    else:
        # SMTP send
        try:
            host = smtp_config.get('host', 'smtp.secureserver.net')
            port = smtp_config.get('port', 587)
            
            server = smtplib.SMTP(host, port, timeout=10)
            server.starttls()
            
            # Read password from local .private/imap-triage.env
            import os
            password = os.environ.get('IMAP_PASSWORD')
            if not password:
                with open('.private/imap-triage.env') as f:
                    for line in f:
                        if 'IMAP_PASSWORD=' in line:
                            password = line.split('=', 1)[1].strip()
            
            server.login(from_addr, password)
            
            recipients = to_addrs + cc_addrs
            server.sendmail(from_addr, recipients, msg.as_string())
            server.quit()
            
            print(f"  ✅ Sent via SMTP")
            return {"status": "success", "method": "smtp"}
        
        except Exception as e:
            print(f"  ❌ SMTP failed: {e}")
            return {"status": "error", "method": "smtp", "message": str(e)}
