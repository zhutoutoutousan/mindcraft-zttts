#!/usr/bin/env python3
"""
Africa Leather Trade - Data Visualization
生成酷炫的数据可视化图表和地图
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import seaborn as sns
from pathlib import Path
import json

class AfricaLeatherVisualizer:
    """非洲皮革贸易数据可视化器"""
    
    def __init__(self, data_dir='data', output_dir='figures'):
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Set style
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        
    def create_shipping_routes_map(self):
        """创建海运路线地图"""
        print("📊 Creating shipping routes map...")
        
        df = pd.read_csv(self.data_dir / 'shipping_routes.csv')
        
        fig, ax = plt.subplots(figsize=(16, 10))
        
        # World map background (simplified)
        ax.set_xlim(-20, 140)
        ax.set_ylim(-40, 50)
        ax.set_facecolor('#E8F4F8')
        
        # Plot routes
        colors = plt.cm.rainbow(np.linspace(0, 1, len(df)))
        
        for idx, row in df.iterrows():
            # Parse coordinates
            origin_coords = eval(row['origin_coords'])
            dest_coords = eval(row['destination_coords'])
            
            # Draw route line
            ax.plot([origin_coords[1], dest_coords[1]], 
                   [origin_coords[0], dest_coords[0]],
                   'o-', color=colors[idx], linewidth=2, markersize=8,
                   label=f"{row['origin_port'].split()[0]} → {row['destination_port'].split()[0]}")
            
            # Add arrow
            dx = dest_coords[1] - origin_coords[1]
            dy = dest_coords[0] - origin_coords[0]
            mid_x = origin_coords[1] + dx * 0.5
            mid_y = origin_coords[0] + dy * 0.5
            
            ax.annotate('', xy=(dest_coords[1], dest_coords[0]), 
                       xytext=(mid_x, mid_y),
                       arrowprops=dict(arrowstyle='->', lw=2, color=colors[idx]))
        
        ax.set_xlabel('Longitude', fontsize=12, fontweight='bold')
        ax.set_ylabel('Latitude', fontsize=12, fontweight='bold')
        ax.set_title('China → Africa Shipping Routes\n中国→非洲海运路线', 
                    fontsize=16, fontweight='bold', pad=20)
        ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'shipping_routes_map.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: shipping_routes_map.png")
    
    def create_market_comparison(self):
        """创建市场对比图"""
        print("📊 Creating market comparison charts...")
        
        df = pd.read_csv(self.data_dir / 'market_data.csv')
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # 1. Market Size
        ax1 = axes[0, 0]
        bars = ax1.barh(df['country'], df['market_size_usd_m'], color=plt.cm.viridis(np.linspace(0.3, 0.9, len(df))))
        ax1.set_xlabel('Market Size (Million USD)', fontweight='bold')
        ax1.set_title('Leather Market Size by Country\n各国皮革市场规模', fontweight='bold', pad=10)
        ax1.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax1.text(width, bar.get_y() + bar.get_height()/2, f'${width:.0f}M',
                    ha='left', va='center', fontsize=9, fontweight='bold')
        
        # 2. Growth Rate
        ax2 = axes[0, 1]
        growth_pct = df['annual_growth_rate'] * 100
        bars = ax2.barh(df['country'], growth_pct, color=plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(df))))
        ax2.set_xlabel('Annual Growth Rate (%)', fontweight='bold')
        ax2.set_title('Market Annual Growth Rate\n市场年增长率', fontweight='bold', pad=10)
        ax2.grid(axis='x', alpha=0.3)
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax2.text(width, bar.get_y() + bar.get_height()/2, f'{width:.1f}%',
                    ha='left', va='center', fontsize=9, fontweight='bold')
        
        # 3. Chinese Import Share
        ax3 = axes[1, 0]
        share_pct = df['chinese_import_share'] * 100
        bars = ax3.barh(df['country'], share_pct, color=plt.cm.Oranges(np.linspace(0.4, 0.9, len(df))))
        ax3.set_xlabel('Chinese Import Share (%)', fontweight='bold')
        ax3.set_title('Chinese Leather Import Share\n中国皮革进口份额', fontweight='bold', pad=10)
        ax3.grid(axis='x', alpha=0.3)
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax3.text(width, bar.get_y() + bar.get_height()/2, f'{width:.1f}%',
                    ha='left', va='center', fontsize=9, fontweight='bold')
        
        # 4. Market Attractiveness Score (composite)
        ax4 = axes[1, 1]
        df['attractiveness'] = (
            df['market_size_usd_m'] / df['market_size_usd_m'].max() * 0.4 +
            df['annual_growth_rate'] / df['annual_growth_rate'].max() * 0.3 +
            df['chinese_import_share'] / df['chinese_import_share'].max() * 0.3
        ) * 10
        
        df_sorted = df.sort_values('attractiveness')
        bars = ax4.barh(df_sorted['country'], df_sorted['attractiveness'], 
                       color=plt.cm.plasma(np.linspace(0.2, 0.9, len(df))))
        ax4.set_xlabel('Attractiveness Score (0-10)', fontweight='bold')
        ax4.set_title('Market Attractiveness Score\n市场吸引力评分', fontweight='bold', pad=10)
        ax4.grid(axis='x', alpha=0.3)
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax4.text(width, bar.get_y() + bar.get_height()/2, f'{width:.1f}',
                    ha='left', va='center', fontsize=9, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'market_comparison.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: market_comparison.png")
    
    def create_product_analysis(self):
        """创建产品分析图"""
        print("📊 Creating product analysis charts...")
        
        df = pd.read_csv(self.data_dir / 'product_categories.csv')
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # 1. Margin Analysis
        ax1 = axes[0, 0]
        margin_pct = df['margin_pct'] * 100
        bars = ax1.bar(range(len(df)), margin_pct, color=plt.cm.Greens(np.linspace(0.4, 0.9, len(df))))
        ax1.set_xticks(range(len(df)))
        ax1.set_xticklabels(df['category'], rotation=45, ha='right')
        ax1.set_ylabel('Gross Margin (%)', fontweight='bold')
        ax1.set_title('Profit Margin by Product Category\n各产品类别利润率', fontweight='bold', pad=10)
        ax1.grid(axis='y', alpha=0.3)
        
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, height, f'{height:.0f}%',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        # 2. Demand vs Competition
        ax2 = axes[0, 1]
        competition_map = {'Low-Medium': 3, 'Medium': 5, 'Medium-High': 7, 'High': 8, 'Very High': 9}
        df['competition_score'] = df['competition_level'].map(competition_map)
        
        scatter = ax2.scatter(df['demand_score'], df['competition_score'], 
                            s=df['avg_price_per_sqm_usd']*50, 
                            c=margin_pct, cmap='RdYlGn', 
                            alpha=0.7, edgecolors='black', linewidth=2)
        
        for idx, row in df.iterrows():
            ax2.annotate(row['category'].replace(' Leather', ''), 
                        (row['demand_score'], row['competition_score']),
                        fontsize=8, ha='center', va='bottom')
        
        ax2.set_xlabel('Demand Score', fontweight='bold')
        ax2.set_ylabel('Competition Level', fontweight='bold')
        ax2.set_title('Demand vs Competition Matrix\n需求与竞争矩阵 (Bubble size = Price)', 
                     fontweight='bold', pad=10)
        ax2.grid(True, alpha=0.3)
        
        cbar = plt.colorbar(scatter, ax=ax2)
        cbar.set_label('Margin %', fontweight='bold')
        
        # 3. Price Comparison
        ax3 = axes[1, 0]
        x = np.arange(len(df))
        width = 0.35
        
        bars1 = ax3.bar(x - width/2, df['china_export_price_usd'], width, 
                       label='China Export', color='#FF6B6B')
        bars2 = ax3.bar(x + width/2, df['africa_retail_price_usd'], width,
                       label='Africa Retail', color='#4ECDC4')
        
        ax3.set_xticks(x)
        ax3.set_xticklabels(df['category'], rotation=45, ha='right')
        ax3.set_ylabel('Price per sqm (USD)', fontweight='bold')
        ax3.set_title('Export vs Retail Price Comparison\n出口价与零售价对比', 
                     fontweight='bold', pad=10)
        ax3.legend()
        ax3.grid(axis='y', alpha=0.3)
        
        # 4. ROI Potential
        ax4 = axes[1, 1]
        df['absolute_margin_usd'] = df['africa_retail_price_usd'] - df['china_export_price_usd']
        df['roi_score'] = df['absolute_margin_usd'] * df['demand_score']
        
        df_sorted = df.sort_values('roi_score')
        bars = ax4.barh(df_sorted['category'], df_sorted['roi_score'],
                       color=plt.cm.coolwarm(np.linspace(0.2, 0.9, len(df))))
        ax4.set_xlabel('ROI Potential Score', fontweight='bold')
        ax4.set_title('ROI Potential Ranking\n投资回报潜力排名', fontweight='bold', pad=10)
        ax4.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'product_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: product_analysis.png")
    
    def create_container_economics(self):
        """创建集装箱经济分析图"""
        print("📊 Creating container economics visualization...")
        
        df = pd.read_csv(self.data_dir / 'container_routes_economics.csv')
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # 1. Cost Breakdown
        ax1 = axes[0, 0]
        cost_categories = ['shipping_cost_usd', 'customs_duty_usd', 'local_logistics_usd']
        cost_data = df[cost_categories].values
        routes = [r.split(' → ')[1].split(' (')[0] for r in df['route']]
        
        x = np.arange(len(routes))
        width = 0.25
        
        colors = ['#FF6B6B', '#4ECDC4', '#95E1D3']
        labels = ['Shipping', 'Customs', 'Logistics']
        
        for i, (cost_cat, color, label) in enumerate(zip(cost_categories, colors, labels)):
            ax1.bar(x + i*width, df[cost_cat], width, label=label, color=color)
        
        ax1.set_xticks(x + width)
        ax1.set_xticklabels(routes, rotation=45, ha='right')
        ax1.set_ylabel('Cost (USD)', fontweight='bold')
        ax1.set_title('40ft Container Cost Breakdown\n40英尺集装箱成本分解', 
                     fontweight='bold', pad=10)
        ax1.legend()
        ax1.grid(axis='y', alpha=0.3)
        
        # 2. Revenue vs Investment
        ax2 = axes[0, 1]
        x_pos = np.arange(len(routes))
        
        bars1 = ax2.bar(x_pos - width/2, df['total_investment_usd']/1000, width,
                       label='Total Investment', color='#FFB6B9')
        bars2 = ax2.bar(x_pos + width/2, df['total_revenue_usd']/1000, width,
                       label='Total Revenue', color='#82D173')
        
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(routes, rotation=45, ha='right')
        ax2.set_ylabel('Amount (Thousand USD)', fontweight='bold')
        ax2.set_title('Investment vs Revenue per Container\n每集装箱投资与收入对比', 
                     fontweight='bold', pad=10)
        ax2.legend()
        ax2.grid(axis='y', alpha=0.3)
        
        # 3. ROI Comparison
        ax3 = axes[1, 0]
        roi_pct = df['roi_pct'] * 100
        bars = ax3.barh(routes, roi_pct, color=plt.cm.RdYlGn(np.linspace(0.4, 0.9, len(df))))
        ax3.set_xlabel('Return on Investment (%)', fontweight='bold')
        ax3.set_title('ROI by Destination\n各目的地投资回报率', fontweight='bold', pad=10)
        ax3.grid(axis='x', alpha=0.3)
        
        for i, bar in enumerate(bars):
            width_val = bar.get_width()
            ax3.text(width_val, bar.get_y() + bar.get_height()/2, f'{width_val:.0f}%',
                    ha='left', va='center', fontsize=10, fontweight='bold')
        
        # 4. Profit Waterfall
        ax4 = axes[1, 1]
        
        # Use Nigeria route as example
        nigeria = df[df['route'].str.contains('Nigeria')].iloc[0]
        
        categories = ['Revenue', 'Cost of\nGoods', 'Shipping', 'Customs', 'Logistics', 'Net\nProfit']
        values = [
            nigeria['total_revenue_usd'],
            -nigeria['total_purchase_usd'],
            -nigeria['shipping_cost_usd'],
            -nigeria['customs_duty_usd'],
            -nigeria['local_logistics_usd'],
            nigeria['gross_profit_usd']
        ]
        
        cumulative = np.cumsum([0] + values[:-1])
        colors_wf = ['#82D173' if v > 0 else '#FF6B6B' for v in values]
        colors_wf[-1] = '#4ECDC4'  # Special color for net profit
        
        ax4.bar(categories, values, bottom=cumulative, color=colors_wf, edgecolor='black', linewidth=1.5)
        
        # Connect bars
        for i in range(len(values)-1):
            ax4.plot([i+0.4, i+0.6], [cumulative[i+1], cumulative[i+1]], 'k--', alpha=0.5)
        
        ax4.set_ylabel('Amount (USD)', fontweight='bold')
        ax4.set_title(f'Profit Waterfall: {routes[0]} (Example)\n利润瀑布图示例', 
                     fontweight='bold', pad=10)
        ax4.grid(axis='y', alpha=0.3)
        ax4.axhline(0, color='black', linewidth=0.8)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'container_economics.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: container_economics.png")
    
    def create_pestel_analysis(self):
        """创建PESTEL分析雷达图"""
        print("📊 Creating PESTEL analysis radar chart...")
        
        with open(self.data_dir / 'pestel_analysis.json', 'r', encoding='utf-8') as f:
            pestel = json.load(f)
        
        categories = list(pestel.keys())
        scores = [pestel[cat]['score'] for cat in categories]
        
        # Radar chart
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        scores_plot = scores + [scores[0]]
        angles += angles[:1]
        
        ax.plot(angles, scores_plot, 'o-', linewidth=3, color='#FF6B6B', markersize=10)
        ax.fill(angles, scores_plot, alpha=0.25, color='#FF6B6B')
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=12, fontweight='bold')
        ax.set_ylim(0, 10)
        ax.set_yticks([2, 4, 6, 8, 10])
        ax.set_yticklabels(['2', '4', '6', '8', '10'], size=10)
        ax.grid(True, alpha=0.3)
        
        ax.set_title('PESTEL Analysis Radar Chart\nPESTEL宏观环境分析', 
                    size=16, fontweight='bold', pad=30)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'pestel_radar.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: pestel_radar.png")
    
    def create_risk_matrix(self):
        """创建风险矩阵"""
        print("📊 Creating risk matrix...")
        
        df = pd.read_csv(self.data_dir / 'risk_analysis.csv')
        
        # Map probability and impact to numbers
        prob_map = {'Low': 2, 'Low-Medium': 3.5, 'Medium': 5, 'Medium-High': 6.5, 'High': 8}
        impact_map = {'Low': 2, 'Medium': 5, 'High': 7, 'Very High': 9}
        
        df['prob_score'] = df['probability'].map(prob_map)
        df['impact_score'] = df['impact'].map(impact_map)
        
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Create risk zones
        ax.axhspan(0, 3.5, 0, 0.35, alpha=0.2, color='green')  # Low risk
        ax.axhspan(3.5, 6.5, 0.35, 0.65, alpha=0.2, color='yellow')  # Medium risk
        ax.axhspan(6.5, 10, 0.65, 1, alpha=0.2, color='red')  # High risk
        
        # Plot risks
        scatter = ax.scatter(df['prob_score'], df['impact_score'], 
                           s=df['risk_score']*80, c=df['risk_score'], 
                           cmap='RdYlGn_r', alpha=0.7, edgecolors='black', linewidth=2)
        
        # Add risk labels
        for idx, row in df.iterrows():
            ax.annotate(row['risk_factor'], 
                       (row['prob_score'], row['impact_score']),
                       fontsize=8, ha='center', va='bottom',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
        
        ax.set_xlabel('Probability', fontsize=14, fontweight='bold')
        ax.set_ylabel('Impact', fontsize=14, fontweight='bold')
        ax.set_title('Risk Assessment Matrix\n风险评估矩阵', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.grid(True, alpha=0.3)
        
        # Legend
        legend_elements = [
            mpatches.Patch(facecolor='green', alpha=0.2, label='Low Risk'),
            mpatches.Patch(facecolor='yellow', alpha=0.2, label='Medium Risk'),
            mpatches.Patch(facecolor='red', alpha=0.2, label='High Risk')
        ]
        ax.legend(handles=legend_elements, loc='upper left', fontsize=10)
        
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Risk Score', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'risk_matrix.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: risk_matrix.png")
    
    def generate_all_visualizations(self):
        """生成所有可视化图表"""
        print("🎨 Starting visualization generation...")
        print("=" * 60)
        
        self.create_shipping_routes_map()
        self.create_market_comparison()
        self.create_product_analysis()
        self.create_container_economics()
        self.create_pestel_analysis()
        self.create_risk_matrix()
        
        print("=" * 60)
        print("✅ All visualizations generated!")
        print(f"📁 Output directory: {self.output_dir}")

if __name__ == '__main__':
    viz = AfricaLeatherVisualizer()
    viz.generate_all_visualizations()
