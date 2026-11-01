#!/usr/bin/env python3
"""
Africa Leather Trade Research - Full Pipeline
完整研究流程：数据收集 → 可视化 → 报告生成
"""
from data_collector import AfricaLeatherDataCollector
from visualizer import AfricaLeatherVisualizer
from report_generator import MultilingualReportGenerator
from pathlib import Path
import sys

def main():
    """运行完整研究流程"""
    
    print("=" * 70)
    print("🌍 AFRICA LEATHER TRADE MARKET RESEARCH")
    print("   非洲皮革贸易市场研究")
    print("=" * 70)
    print()
    
    try:
        # Step 1: Data Collection
        print("STEP 1: DATA COLLECTION")
        print("-" * 70)
        collector = AfricaLeatherDataCollector()
        data = collector.run_full_collection()
        print()
        
        # Step 2: Visualization
        print("STEP 2: VISUALIZATION GENERATION")
        print("-" * 70)
        visualizer = AfricaLeatherVisualizer()
        visualizer.generate_all_visualizations()
        print()
        
        # Step 3: Report Generation
        print("STEP 3: MULTILINGUAL REPORT GENERATION")
        print("-" * 70)
        report_gen = MultilingualReportGenerator()
        pdf_file = report_gen.generate_report()
        print()
        
        # Summary
        print("=" * 70)
        print("✅ RESEARCH COMPLETE!")
        print("=" * 70)
        print()
        print("📁 Output Files:")
        print(f"   Data:          {Path('data').absolute()}/")
        print(f"   Visualizations: {Path('figures').absolute()}/")
        print(f"   Reports:       {Path('reports').absolute()}/")
        print()
        
        if pdf_file and pdf_file.exists():
            print(f"📄 Main Report (PDF): {pdf_file.absolute()}")
            print(f"   Size: {pdf_file.stat().st_size / (1024*1024):.1f} MB")
        else:
            print("📄 Main Report (LaTeX): reports/africa_leather_report.tex")
            print("   (PDF requires pdflatex to compile)")
        
        print()
        print("📊 Summary Report (Markdown): summary_report.md")
        print()
        print("🎉 Ready for business analysis!")
        print()
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during research: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
