#!/bin/bash
# Quick view script for generated reports

echo "📊 Africa Leather Trade Research - Report Viewer"
echo "================================================"
echo ""

if [ -f "reports/africa_leather_report.pdf" ]; then
    echo "✅ PDF Report Found:"
    ls -lh reports/africa_leather_report.pdf
    echo ""
    echo "📄 To view:"
    echo "   Linux:   xdg-open reports/africa_leather_report.pdf"
    echo "   macOS:   open reports/africa_leather_report.pdf"
    echo "   Windows: start reports/africa_leather_report.pdf"
    echo ""
fi

if [ -f "summary_report.md" ]; then
    echo "✅ Markdown Summary Found:"
    ls -lh summary_report.md
    echo ""
fi

echo "📁 Data Files:"
ls -1 data/ 2>/dev/null || echo "  (none)"
echo ""

echo "🖼️  Visualizations:"
ls -1 figures/ 2>/dev/null || echo "  (none)"
echo ""

echo "🌐 To regenerate:"
echo "   python3 run_full_research.py"
