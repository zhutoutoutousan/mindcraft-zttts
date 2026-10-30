# WhatsApp Business Cloud API -> Qoder-MCP-Bridge (Route B)

Stand: 2026-10-06. Ziel: eigener Connector, mit dem der Agent Nachrichten senden und eingehende Kunden-Chats lesen kann.

## Entscheidungstor (zuerst klaeren!)

- WhatsApp-Kanal (Broadcast, Verkaufskanal): Stand heute keine offizielle API, weder Lesen noch Posten. Route B hilft dann NICHT; es bleibt Export/Screenshot (Route C) oder die inoffizielle Route A mit Ban-Risiko.
- WhatsApp-Business-Chat (Kunden schreiben dich an, du schreibst zurueck): dafuer ist die Cloud API gebaut -> Route B funktioniert.
- Mischform: Kanal als Schaufenster + Business-Nummer fuer Anfragen -> die API deckt nur den Anfrage-Teil ab.

## Phase 0 - Konto und Nummer (30 min)

1. business.facebook.com -> Business-Portfolio anlegen/pruefen (Name, Adresse, spaeter Handelsregister-Nr. fuer die Verifizierung).
2. Neue Nummer (Prepaid/eSIM) besorgen. Sie wird dauerhaft an die API gebunden und laeuft danach nicht mehr in der normalen WhatsApp-App. Nie die private Nummer nehmen.
3. developers.facebook.com -> App erstellen -> Typ Business -> Produkt WhatsApp hinzufuegen.
4. Notieren: App-ID, App-Secret, Phone-Number-ID, WABA-ID.

## Phase 1 - Testmodus (15 min, kein Review)

5. App-Dashboard: WhatsApp -> API Setup -> Testnummer + temporaerer Token (24 h gueltig).
6. Empfaenger: bis zu 5 Nummern, vorher als verifiziert eintragen.
7. Erste Textnachricht, alles in einer Zeile, Platzhalter ersetzen:

~~~bash
curl -X POST "https://graph.facebook.com/v21.0/<PHONE_NUMBER_ID>/messages" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d "{\"messaging_product\":\"whatsapp\",\"to\":\"+49...\",\"type\":\"text\",\"text\":{\"body\":\"Test aus dem Terminal\"}}"
~~~

Version v21.0 oder die im Dashboard angezeigte aktuelle Version.
8. Erfolg = messages[0].id im Response. Sendepfad bewiesen.

## Phase 2 - Webhook fuer eingehende Nachrichten (1-2 h)

Die API kennt kein "alte Chats abholen" - eingehende Nachrichten kommen nur als Push.

9. Kleiner Server (Python/FastAPI oder Node/Express) mit oeffentlichem HTTPS-Endpunkt. Zum Testen ngrok/cloudflared, produktiv VPS (EU/US) + Caddy/Traefik fuer TLS.
10. Verifizierungs-GET beantworten: hub.mode=subscribe, hub.verify_token vergleichen, hub.challenge zurueckgeben.
11. Im Dashboard Webhook-URL + Verify Token eintragen, Felder abonnieren: messages, message_statuses.
12. Jeden POST pruefen: X-Hub-Signature-256 = HMAC-SHA256(body, App-Secret), sonst verwerfen.
13. Payloads lokal persistieren (SQLite oder JSONL) + Message-ID-Dedup, Meta sendet Retries.

Minimalbeispiel in Python:

~~~python
import hashlib, hmac, json, os
from fastapi import FastAPI, Request, Response

app = FastAPI()
VERIFY = os.environ["WA_VERIFY_TOKEN"]
SECRET = os.environ["WA_APP_SECRET"].encode()

@app.get("/webhook")
async def verify(hub_mode: str = "", hub_verify_token: str = "", hub_challenge: str = ""):
    ok = hub_mode == "subscribe" and hub_verify_token == VERIFY
    return Response(hub_challenge if ok else "forbidden", status_code=200 if ok else 403)

@app.post("/webhook")
async def receive(request: Request):
    body = await request.body()
    sig = request.headers.get("X-Hub-Signature-256", "")
    if sig != "sha256=" + hmac.new(SECRET, body, hashlib.sha256).hexdigest():
        return Response("bad signature", status_code=401)
    data = json.loads(body)
    for entry in data.get("entry", []):
        for change in entry.get("changes", []):
            for msg in change.get("value", {}).get("messages", []):
                with open("inbox.jsonl", "a", encoding="utf-8") as f:
                    f.write(json.dumps(msg, ensure_ascii=False) + "\n")
    return {"status": "ok"}
~~~

## Phase 3 - Business Verification + dauerhafter Token (1-3 Tage Wartezeit)

14. Business Verification im Business Portfolio (Handelsregister, Ausweis, Rechnung mit Adresse). Ohne sie: Testnummer und niedrige Limits.
15. Eigene Nummer registrieren: Display-Name festlegen (nicht generisch wie "Shop"), dann SMS- oder Sprachcode.
16. System User anlegen (Business Settings -> Benutzer -> Systembenutzer) und Token mit den Scopes whatsapp_business_messaging + whatsapp_business_management erzeugen. Kein persoenlicher User-Token.
17. Messaging-Limits: 1K -> 10K -> 100K -> unbegrenzt, abhaengig von Quality-Rating und Volumen.

## Phase 4 - Templates fuer proaktive Nachrichten

18. Im 24-h-Kundenfenster sind freie Texte erlaubt; danach oder unaufgefordert nur genehmigte Vorlagen.
19. Vorlage anlegen (Kategorie Marketing, Utility oder Authentication), Variablen {{1}} und {{2}}; Freigabe dauert Minuten bis Stunden.
20. Kosten: Abrechnung pro Template-Nachricht, Service-Fenster meist gratis; Preise pro Land im Dashboard pruefen.

## Phase 5 - MCP-Bridge, der eigentliche Connector

21. MCP-Server mit vier Tools: wa_send_text(to, body) nur im 24-h-Fenster, wa_send_template(to, template, vars) proaktiv, wa_list_incoming(since, limit) liest inbox.jsonl, wa_status(message_id) fuer Zustellung und Gelesen.
22. Python-Kern mit FastMCP:

~~~python
import json, os, httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("whatsapp-bridge")
GRAPH = "https://graph.facebook.com/v21.0"
PNID = os.environ["WA_PHONE_NUMBER_ID"]
TOKEN = os.environ["WA_TOKEN"]

@mcp.tool()
def wa_send_text(to: str, body: str) -> dict:
    r = httpx.post(
        GRAPH + "/" + PNID + "/messages",
        headers={"Authorization": "Bearer " + TOKEN},
        json={"messaging_product": "whatsapp", "to": to,
              "type": "text", "text": {"body": body}},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()

@mcp.tool()
def wa_list_incoming(since: str = "", limit: int = 50) -> list:
    out = []
    with open("inbox.jsonl", encoding="utf-8") as f:
        for line in f:
            m = json.loads(line)
            if not since or m.get("timestamp", "") >= since:
                out.append(m)
    return out[-limit:]

if __name__ == "__main__":
    mcp.run(transport="stdio")
~~~

23. Secrets nur in .private/wa.env (gitignored): WA_TOKEN, WA_APP_SECRET, WA_VERIFY_TOKEN, WA_PHONE_NUMBER_ID, WA_WABA_ID. Nie in Repo, Chat oder Logs.
24. In Qoder eintragen: mcp-config-Skill nutzen oder die MCP-Settings manuell pflegen. command = python, args = Pfad zu server.py, env = WA_TOKEN_FILE mit Pfad zu .private/wa.env. Token beim Start aus der Datei lesen, nicht als Klartext in die Config schreiben.

## Phase 6 - Betrieb von China aus (ab 2026-10-31)

25. graph.facebook.com ist in Festland-China blockiert, also Bridge und Webhook auf einem EU/US-VPS betreiben.
26. Qoder ruft den MCP-Server ueber SSH auf, stdio laeuft durch den Tunnel: command = ssh, args = wa-vps, python, /opt/wa-bridge/server.py.
27. Der Webhook zeigt auf die VPS-Domain mit HTTPS, nicht auf den Laptop. ngrok nur fuer Tests, nie dauerhaft mit Echtdaten.
28. VPS-Betrieb: inbox.jsonl oder SQLite sichern, Systemd-Unit mit Restart=always, Log-Rotation ohne Token-Ausgaben.

## Abnahme-Checkliste

- [ ] Testnachricht per curl angekommen
- [ ] Webhook-GET verifiziert, POST-Signatur geprueft
- [ ] Eingehende Nachricht landet in inbox.jsonl
- [ ] System-User-Token statt User-Token, nur in .private
- [ ] Template genehmigt und proaktive Nachricht getestet
- [ ] MCP-Tool wa_send_text aus Qoder aufgerufen
- [ ] VPS-Neustart ueberlebt, Bridge laeuft ohne lokalen Rechner
- [ ] Kanal-Frage geklaert: Broadcast-Kanal ist nicht API-tauglich

## Typische Fallen

- Private Nummer registriert: App-Zugriff weg, Nummer nicht mehr normal nutzbar.
- Persoenlicher User-Token produktiv: kippt bei Passwort- oder Rechteaenderung.
- Signaturpruefung weggelassen: offener Endpunkt, jeder kann Nachrichten faken.
- Kanal-Inhalte per API erwartet: gibt es nicht, Export bleibt der Weg.
- Marketing-Templates ohne Opt-in: Quality-Rating sinkt, Limits schrumpfen, Sperre moeglich.

## Quellen

- Meta: WhatsApp Business Platform und Cloud API (developers.facebook.com/docs/whatsapp)
- Meta: Webhooks und Signaturpruefung (developers.facebook.com/docs/whatsapp/cloud-api/webhooks)
- Meta: Message Templates und Limits (developers.facebook.com/docs/whatsapp/message-templates)
- Model Context Protocol SDK (modelcontextprotocol.io)
