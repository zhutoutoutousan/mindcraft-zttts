#!/usr/bin/env python3
"""
非洲皮革贸易 - 从零开始的具体行动计划
Africa Leather Trade - Concrete Step-by-Step Action Plan with Real Maps
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import pandas as pd
import numpy as np
from pathlib import Path
import requests
from PIL import Image
from io import BytesIO

class ConcreteActionPlanVisualizer:
    """具体行动计划可视化器"""
    
    def __init__(self, output_dir='concrete_plan'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 更大的字体设置
        plt.rcParams.update({
            'font.size': 14,
            'axes.titlesize': 18,
            'axes.labelsize': 16,
            'xtick.labelsize': 14,
            'ytick.labelsize': 14,
            'legend.fontsize': 13
        })
    
    def create_world_map_routes(self):
        """创建真实世界地图上的航线"""
        print("🗺️  Creating world map with shipping routes...")
        
        fig, ax = plt.subplots(figsize=(20, 12))
        
        # 使用简化的世界地图轮廓
        # 主要海运路线：中国 → 非洲
        routes = [
            {
                'name': '上海 → 拉各斯',
                'start': (121.47, 31.23),  # 上海
                'end': (3.39, 6.45),       # 拉各斯
                'color': '#FF6B6B',
                'transit': '35天',
                'cost': '$4,500'
            },
            {
                'name': '深圳 → 德班',
                'start': (114.06, 22.54),  # 深圳
                'end': (31.02, -29.86),    # 德班
                'color': '#4ECDC4',
                'transit': '28天',
                'cost': '$3,800'
            },
            {
                'name': '广州 → 蒙巴萨',
                'start': (113.26, 23.13),  # 广州
                'end': (39.67, -4.04),     # 蒙巴萨
                'color': '#95E1D3',
                'transit': '25天',
                'cost': '$3,200'
            }
        ]
        
        # 绘制世界地图背景
        ax.set_xlim(-180, 180)
        ax.set_ylim(-60, 70)
        ax.set_facecolor('#E8F4F8')
        
        # 绘制大陆轮廓（简化）
        # 亚洲
        asia_x = [70, 150, 150, 140, 130, 120, 110, 100, 90, 80, 70]
        asia_y = [10, 10, 50, 50, 45, 40, 30, 20, 15, 15, 10]
        ax.fill(asia_x, asia_y, color='#D5E8D4', alpha=0.6, edgecolor='black', linewidth=1)
        
        # 非洲
        africa_x = [-20, 50, 50, 40, 35, 30, 20, 10, -20, -20]
        africa_y = [35, 35, -35, -35, -30, -25, -10, 0, 0, 35]
        ax.fill(africa_x, africa_y, color='#FFE6CC', alpha=0.6, edgecolor='black', linewidth=1)
        
        # 标注大陆
        ax.text(110, 35, 'CHINA\n中国', fontsize=22, fontweight='bold', 
               ha='center', va='center', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
        
        ax.text(20, 0, 'AFRICA\n非洲', fontsize=22, fontweight='bold',
               ha='center', va='center', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
        
        # 绘制航线
        for idx, route in enumerate(routes):
            start_lon, start_lat = route['start']
            end_lon, end_lat = route['end']
            
            # 航线曲线
            mid_lon = (start_lon + end_lon) / 2
            mid_lat = (start_lat + end_lat) / 2 + 15  # 弧形
            
            # 绘制曲线
            t = np.linspace(0, 1, 100)
            lons = (1-t)**2 * start_lon + 2*(1-t)*t * mid_lon + t**2 * end_lon
            lats = (1-t)**2 * start_lat + 2*(1-t)*t * mid_lat + t**2 * end_lat
            
            ax.plot(lons, lats, linewidth=4, color=route['color'], 
                   label=f"{route['name']} ({route['transit']}, {route['cost']})",
                   alpha=0.8)
            
            # 起点标记
            ax.plot(start_lon, start_lat, 'o', markersize=15, color=route['color'],
                   markeredgecolor='black', markeredgewidth=2)
            
            # 终点标记
            ax.plot(end_lon, end_lat, 's', markersize=15, color=route['color'],
                   markeredgecolor='black', markeredgewidth=2)
            
            # 箭头
            arrow_lon = lons[75]
            arrow_lat = lats[75]
            dx = lons[76] - lons[74]
            dy = lats[76] - lats[74]
            ax.arrow(arrow_lon, arrow_lat, dx*2, dy*2, 
                    head_width=3, head_length=2, fc=route['color'], 
                    ec='black', linewidth=1.5)
        
        ax.set_xlabel('经度 Longitude', fontsize=18, fontweight='bold')
        ax.set_ylabel('纬度 Latitude', fontsize=18, fontweight='bold')
        ax.set_title('中国 → 非洲 主要海运路线\nChina → Africa Major Shipping Routes\n40英尺集装箱 (40ft Container)', 
                    fontsize=24, fontweight='bold', pad=20)
        ax.legend(loc='lower left', fontsize=14, framealpha=0.95)
        ax.grid(True, alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'world_map_routes.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ World map with routes created")
    
    def create_zero_to_first_container_roadmap(self):
        """创建从零到第一个集装箱的详细路线图"""
        print("📋 Creating zero-to-first-container roadmap...")
        
        fig, ax = plt.subplots(figsize=(22, 16))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 24)
        ax.axis('off')
        
        # 标题
        title_box = FancyBboxPatch((0.5, 22), 9, 1.5, 
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#2C3E50', 
                                   facecolor='#3498DB', 
                                   linewidth=3)
        ax.add_patch(title_box)
        ax.text(5, 22.75, '从零到第一个集装箱：60天详细计划\nZero to First Container: 60-Day Detailed Plan',
               fontsize=26, fontweight='bold', ha='center', va='center', color='white')
        
        # 阶段1：前期准备 (第1-14天)
        y_start = 20
        
        # 阶段标题
        phase1_box = FancyBboxPatch((0.5, y_start), 9, 1.2,
                                    boxstyle="round,pad=0.1",
                                    edgecolor='#E74C3C',
                                    facecolor='#E74C3C',
                                    linewidth=2)
        ax.add_patch(phase1_box)
        ax.text(5, y_start + 0.6, '阶段1：前期准备 (第1-14天) | Phase 1: Preparation',
               fontsize=20, fontweight='bold', ha='center', va='center', color='white')
        
        y_start -= 1.5
        
        # 步骤1：中国供应商
        step_box = FancyBboxPatch((0.8, y_start), 4, 2.2,
                                  boxstyle="round,pad=0.15",
                                  edgecolor='#3498DB',
                                  facecolor='#EBF5FB',
                                  linewidth=2)
        ax.add_patch(step_box)
        
        ax.text(2.8, y_start + 1.8, '步骤1：找到中国皮革供应商',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(0.9, y_start + 1.3, '• 广州/深圳皮革批发市场\n• 通过阿里巴巴1688寻找工厂\n• 要求样品 + 质检报告\n• 谈判价格：目标 ¥35-40/平米',
               fontsize=13, ha='left', va='top')
        ax.text(2.8, y_start + 0.1, '中方解决：质量 + 价格 + 出口文件',
               fontsize=13, fontweight='bold', ha='center', 
               bbox=dict(boxstyle='round', facecolor='#FFD93D', alpha=0.8))
        
        # 步骤2：Justice父亲酒店网络
        step_box2 = FancyBboxPatch((5.2, y_start), 4, 2.2,
                                   boxstyle="round,pad=0.15",
                                   edgecolor='#27AE60',
                                   facecolor='#EAFAF1',
                                   linewidth=2)
        ax.add_patch(step_box2)
        
        ax.text(7.2, y_start + 1.8, '步骤2：利用Justice父亲的酒店关系',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(5.3, y_start + 1.3, '• 五星级酒店 = 高端客户接触点\n• 酒店采购部：家具皮革需求\n• 客人网络：商务人士、富裕阶层\n• 酒店展示样品，收集订单',
               fontsize=13, ha='left', va='top')
        ax.text(7.2, y_start + 0.1, '非洲方解决：客户 + 信任 + 本地分销',
               fontsize=13, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#6C5CE7', alpha=0.8, edgecolor='white'))
        
        # 阶段2：资金与物流 (第15-30天)
        y_start -= 3
        
        phase2_box = FancyBboxPatch((0.5, y_start), 9, 1.2,
                                    boxstyle="round,pad=0.1",
                                    edgecolor='#F39C12',
                                    facecolor='#F39C12',
                                    linewidth=2)
        ax.add_patch(phase2_box)
        ax.text(5, y_start + 0.6, '阶段2：资金与物流 (第15-30天) | Phase 2: Funding & Logistics',
               fontsize=20, fontweight='bold', ha='center', va='center', color='white')
        
        y_start -= 1.5
        
        # 步骤3：资金筹措
        step_box3 = FancyBboxPatch((0.8, y_start), 4, 2.5,
                                   boxstyle="round,pad=0.15",
                                   edgecolor='#E74C3C',
                                   facecolor='#FADBD8',
                                   linewidth=2)
        ax.add_patch(step_box3)
        
        ax.text(2.8, y_start + 2.1, '步骤3：筹集启动资金',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(0.9, y_start + 1.6, '总需要：$52,700 (一个集装箱)\n• 皮革采购：$44,200\n• 海运费用：$4,500\n• 关税：$3,200\n• 本地物流：$800',
               fontsize=13, ha='left', va='top')
        ax.text(2.8, y_start + 0.1, '💡 Justice兄弟提供：前期资金',
               fontsize=13, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#FFEAA7'))
        
        # 步骤4：预订货物
        step_box4 = FancyBboxPatch((5.2, y_start), 4, 2.5,
                                   boxstyle="round,pad=0.15",
                                   edgecolor='#8E44AD',
                                   facecolor='#F4ECF7',
                                   linewidth=2)
        ax.add_patch(step_box4)
        
        ax.text(7.2, y_start + 2.1, '步骤4：预订货物与航运',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(5.3, y_start + 1.6, '• 通过货代预订40ft集装箱舱位\n• 选择目的港：拉各斯/德班/蒙巴萨\n• 购买海运保险 (110% CIF)\n• 准备出口文件：发票、装箱单',
               fontsize=13, ha='left', va='top')
        ax.text(7.2, y_start + 0.1, '🚢 运输时间：25-35天',
               fontsize=13, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#74B9FF'))
        
        # 阶段3：运输与清关 (第31-45天)
        y_start -= 4
        
        phase3_box = FancyBboxPatch((0.5, y_start), 9, 1.2,
                                    boxstyle="round,pad=0.1",
                                    edgecolor='#16A085',
                                    facecolor='#16A085',
                                    linewidth=2)
        ax.add_patch(phase3_box)
        ax.text(5, y_start + 0.6, '阶段3：运输与清关 (第31-45天) | Phase 3: Shipping & Customs',
               fontsize=20, fontweight='bold', ha='center', va='center', color='white')
        
        y_start -= 1.5
        
        # 步骤5：海运中
        step_box5 = FancyBboxPatch((0.8, y_start), 4, 2,
                                   boxstyle="round,pad=0.15",
                                   edgecolor='#3498DB',
                                   facecolor='#D6EAF8',
                                   linewidth=2)
        ax.add_patch(step_box5)
        
        ax.text(2.8, y_start + 1.6, '步骤5：货物在海上运输',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(0.9, y_start + 1.1, '• 实时跟踪集装箱位置 (GPS)\n• 联系本地清关代理\n• 准备清关文件\n• 通知Justice父亲准备展示空间',
               fontsize=13, ha='left', va='top')
        
        # 步骤6：到港清关
        step_box6 = FancyBboxPatch((5.2, y_start), 4, 2,
                                   boxstyle="round,pad=0.15",
                                   edgecolor='#E67E22',
                                   facecolor='#FAE5D3',
                                   linewidth=2)
        ax.add_patch(step_box6)
        
        ax.text(7.2, y_start + 1.6, '步骤6：到港与清关',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(5.3, y_start + 1.1, '• 支付关税 (~20-25%)\n• 雇佣本地清关代理\n• 检验货物质量\n• 运输到Justice父亲酒店仓库',
               fontsize=13, ha='left', va='top')
        
        # 阶段4：销售与回款 (第46-60天)
        y_start -= 3
        
        phase4_box = FancyBboxPatch((0.5, y_start), 9, 1.2,
                                    boxstyle="round,pad=0.1",
                                    edgecolor='#27AE60',
                                    facecolor='#27AE60',
                                    linewidth=2)
        ax.add_patch(phase4_box)
        ax.text(5, y_start + 0.6, '阶段4：销售与回款 (第46-60天) | Phase 4: Sales & Collection',
               fontsize=20, fontweight='bold', ha='center', va='center', color='white')
        
        y_start -= 1.5
        
        # 步骤7：酒店展示销售
        step_box7 = FancyBboxPatch((0.8, y_start), 8.4, 2.5,
                                   boxstyle="round,pad=0.15",
                                   edgecolor='#2ECC71',
                                   facecolor='#D5F4E6',
                                   linewidth=2)
        ax.add_patch(step_box7)
        
        ax.text(5, y_start + 2.1, '步骤7：利用Justice父亲五星级酒店销售',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(0.9, y_start + 1.5, '🏨 酒店销售渠道（关键优势）：\n'
               '• 在酒店大堂/会议室设置皮革样品展示\n'
               '• 目标客户：酒店采购部 (家具翻新)\n'
               '• 目标客户：住店商务人士 (鞋厂、家具厂老板)\n'
               '• 目标客户：酒店餐饮供应商 (皮革座椅)',
               fontsize=13, ha='left', va='top')
        ax.text(5.5, y_start + 1.5, '🎯 批发客户（主要销售）：\n'
               '• 当地鞋厂 (Footwear manufacturers)\n'
               '• 家具工厂 (Furniture makers)\n'
               '• 箱包工坊 (Bag workshops)\n'
               '• 汽车装饰店 (Car upholstery)',
               fontsize=13, ha='left', va='top')
        ax.text(5, y_start + 0.1, '💰 目标：2-3周内销售60-70%货物，回款 ~$90,000',
               fontsize=14, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#55EFC4', edgecolor='#00B894', linewidth=2))
        
        # 底部总结
        y_start -= 3.5
        summary_box = FancyBboxPatch((0.5, y_start), 9, 2,
                                     boxstyle="round,pad=0.15",
                                     edgecolor='#2C3E50',
                                     facecolor='#F8F9FA',
                                     linewidth=3)
        ax.add_patch(summary_box)
        
        ax.text(5, y_start + 1.5, '🎉 第一个集装箱完成！预期结果：',
               fontsize=18, fontweight='bold', ha='center')
        ax.text(5, y_start + 0.8, '投资：$52,700  |  收入：$130,000  |  利润：$77,300  |  ROI：147%',
               fontsize=16, fontweight='bold', ha='center', color='#27AE60')
        ax.text(5, y_start + 0.2, '✅ 建立供应商关系  ✅ 验证市场需求  ✅ 利用酒店网络优势  ✅ 回收资金继续第二轮',
               fontsize=13, ha='center')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'zero_to_first_container.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Zero-to-first-container roadmap created")
    
    def create_partner_roles_diagram(self):
        """创建合作伙伴角色分工图"""
        print("🤝 Creating partner roles diagram...")
        
        fig, ax = plt.subplots(figsize=(20, 12))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')
        
        # 标题
        title_box = FancyBboxPatch((0.5, 10.5), 9, 1.2,
                                   boxstyle="round,pad=0.1",
                                   edgecolor='#2C3E50',
                                   facecolor='#34495E',
                                   linewidth=3)
        ax.add_patch(title_box)
        ax.text(5, 11.1, '合作伙伴角色分工 | Partner Role Distribution',
               fontsize=24, fontweight='bold', ha='center', va='center', color='white')
        
        # 中国供应商角色
        china_box = FancyBboxPatch((0.5, 5.5), 4, 4.5,
                                   boxstyle="round,pad=0.2",
                                   edgecolor='#E74C3C',
                                   facecolor='#FADBD8',
                                   linewidth=3)
        ax.add_patch(china_box)
        
        ax.text(2.5, 9.5, '🇨🇳 中国合作方\nChina Partner',
               fontsize=20, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#E74C3C', edgecolor='white', linewidth=2))
        
        ax.text(0.7, 8.8, '核心职责 Core Responsibilities:',
               fontsize=16, fontweight='bold', ha='left')
        ax.text(0.7, 8.3, '✓ 寻找可靠的皮革工厂\n'
               '  Find reliable leather manufacturers\n\n'
               '✓ 质量控制 + 验货\n'
               '  Quality control + inspection\n\n'
               '✓ 价格谈判 (目标: ¥35-40/㎡)\n'
               '  Price negotiation (Target: ¥35-40/㎡)\n\n'
               '✓ 出口文件准备\n'
               '  Export documentation\n\n'
               '✓ 集装箱装柜监督\n'
               '  Container loading supervision',
               fontsize=13, ha='left', va='top', linespacing=1.5)
        
        ax.text(2.5, 5.9, '解决的问题：供应链上游',
               fontsize=14, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#FFD93D'))
        
        # Justice父亲/非洲方角色
        africa_box = FancyBboxPatch((5.5, 5.5), 4, 4.5,
                                    boxstyle="round,pad=0.2",
                                    edgecolor='#27AE60',
                                    facecolor='#D5F4E6',
                                    linewidth=3)
        ax.add_patch(africa_box)
        
        ax.text(7.5, 9.5, '🌍 Justice父亲 (非洲方)\nJustice\'s Father (Africa)',
               fontsize=20, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#27AE60', edgecolor='white', linewidth=2))
        
        ax.text(5.7, 8.8, '核心职责 Core Responsibilities:',
               fontsize=16, fontweight='bold', ha='left')
        ax.text(5.7, 8.3, '🏨 利用五星级酒店网络\n'
               '   Leverage 5-star hotel network\n\n'
               '✓ 提供展示/仓储空间\n'
               '  Provide showroom/storage\n\n'
               '✓ 引荐高端客户 (酒店采购部)\n'
               '  Introduce high-end clients\n\n'
               '✓ 本地清关与物流协调\n'
               '  Local customs & logistics\n\n'
               '✓ 收款与资金安全\n'
               '  Payment collection & security',
               fontsize=13, ha='left', va='top', linespacing=1.5)
        
        ax.text(7.5, 5.9, '解决的问题：本地分销 + 客户信任',
               fontsize=14, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#6C5CE7', edgecolor='white'))
        
        # Justice兄弟角色
        justice_box = FancyBboxPatch((2, 1), 6, 3.8,
                                      boxstyle="round,pad=0.2",
                                      edgecolor='#3498DB',
                                      facecolor='#D6EAF8',
                                      linewidth=3)
        ax.add_patch(justice_box)
        
        ax.text(5, 4.3, '💼 Justice兄弟 (协调方)\nJustice\'s Brother (Coordinator)',
               fontsize=20, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#3498DB', edgecolor='white', linewidth=2))
        
        ax.text(2.2, 3.7, '核心职责 Core Responsibilities:',
               fontsize=16, fontweight='bold', ha='left')
        ax.text(2.2, 3.2, '✓ 协调中国供应商 + 非洲分销\n'
               '  Coordinate China suppliers + Africa distribution\n\n'
               '✓ 管理现金流 (前期投资 $52,700)\n'
               '  Manage cash flow (Initial investment $52,700)\n\n'
               '✓ 跟踪集装箱物流\n'
               '  Track container logistics\n\n'
               '✓ 联络酒店批发客户\n'
               '  Contact hotel wholesale clients\n\n'
               '✓ 利润分配管理\n'
               '  Profit distribution management',
               fontsize=13, ha='left', va='top', linespacing=1.5)
        
        ax.text(5, 1.4, '关键角色：资金 + 协调 + 执行',
               fontsize=14, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#FFEAA7'))
        
        # 连接箭头
        arrow1 = FancyArrowPatch((4.5, 7.5), (5.5, 7.5),
                                arrowstyle='->', mutation_scale=40,
                                linewidth=3, color='#2C3E50')
        ax.add_patch(arrow1)
        ax.text(5, 7.8, '货物流动', fontsize=12, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='white'))
        
        arrow2 = FancyArrowPatch((2.5, 5.5), (4.5, 4.8),
                                arrowstyle='<->', mutation_scale=30,
                                linewidth=2.5, color='#E74C3C', linestyle='--')
        ax.add_patch(arrow2)
        
        arrow3 = FancyArrowPatch((7.5, 5.5), (5.5, 4.8),
                                arrowstyle='<->', mutation_scale=30,
                                linewidth=2.5, color='#27AE60', linestyle='--')
        ax.add_patch(arrow3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'partner_roles.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Partner roles diagram created")
    
    def create_hotel_advantage_infographic(self):
        """创建酒店优势信息图"""
        print("🏨 Creating hotel advantage infographic...")
        
        fig, ax = plt.subplots(figsize=(18, 14))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        ax.axis('off')
        
        # 标题
        title_box = FancyBboxPatch((0.5, 12.5), 9, 1.2,
                                   boxstyle="round,pad=0.1",
                                   edgecolor='#8E44AD',
                                   facecolor='#8E44AD',
                                   linewidth=3)
        ax.add_patch(title_box)
        ax.text(5, 13.1, '🏨 Justice父亲五星级酒店优势\nJustice\'s Father 5-Star Hotel Advantage',
               fontsize=24, fontweight='bold', ha='center', va='center', color='white')
        
        # 优势1：展示空间
        adv1_box = FancyBboxPatch((0.5, 9.5), 4.5, 2.5,
                                  boxstyle="round,pad=0.15",
                                  edgecolor='#E74C3C',
                                  facecolor='#FADBD8',
                                  linewidth=2)
        ax.add_patch(adv1_box)
        ax.text(2.75, 11.5, '优势1：高端展示空间',
               fontsize=18, fontweight='bold', ha='center')
        ax.text(0.7, 11, '• 酒店大堂样品陈列\n• 商务会议室产品展示\n• 高端环境提升产品档次\n• 接触高净值客户',
               fontsize=14, ha='left', va='top')
        
        # 优势2：客户网络
        adv2_box = FancyBboxPatch((5.5, 9.5), 4, 2.5,
                                  boxstyle="round,pad=0.15",
                                  edgecolor='#3498DB',
                                  facecolor='#D6EAF8',
                                  linewidth=2)
        ax.add_patch(adv2_box)
        ax.text(7.5, 11.5, '优势2：客户网络',
               fontsize=18, fontweight='bold', ha='center')
        ax.text(5.7, 11, '• 酒店VIP客人数据库\n• 商务人士 (工厂老板)\n• 供应商网络\n• 口碑传播渠道',
               fontsize=14, ha='left', va='top')
        
        # 优势3：信任背书
        adv3_box = FancyBboxPatch((0.5, 6.5), 4.5, 2.5,
                                  boxstyle="round,pad=0.15",
                                  edgecolor='#27AE60',
                                  facecolor='#D5F4E6',
                                  linewidth=2)
        ax.add_patch(adv3_box)
        ax.text(2.75, 8.5, '优势3：信任背书',
               fontsize=18, fontweight='bold', ha='center')
        ax.text(0.7, 8, '• 五星级酒店 = 信誉保证\n• 本地知名人士\n• 降低交易风险\n• 便于账期谈判',
               fontsize=14, ha='left', va='top')
        
        # 优势4：仓储物流
        adv4_box = FancyBboxPatch((5.5, 6.5), 4, 2.5,
                                  boxstyle="round,pad=0.15",
                                  edgecolor='#F39C12',
                                  facecolor='#FAE5D3',
                                  linewidth=2)
        ax.add_patch(adv4_box)
        ax.text(7.5, 8.5, '优势4：仓储便利',
               fontsize=18, fontweight='bold', ha='center')
        ax.text(5.7, 8, '• 酒店仓库空间\n• 安全保管货物\n• 便于客户看货\n• 灵活配送安排',
               fontsize=14, ha='left', va='top')
        
        # 具体实施方案
        impl_box = FancyBboxPatch((0.5, 3), 9, 3,
                                  boxstyle="round,pad=0.15",
                                  edgecolor='#2C3E50',
                                  facecolor='#ECF0F1',
                                  linewidth=3)
        ax.add_patch(impl_box)
        
        ax.text(5, 5.6, '🎯 具体实施方案 Implementation Plan',
               fontsize=20, fontweight='bold', ha='center')
        
        ax.text(0.7, 5, '第1周：酒店大堂设置样品展示台 (2-3平米)\n'
               '第2周：通过酒店采购部联系本地工厂 (家具、鞋厂)\n'
               '第3周：在酒店举办"皮革产品展示会" - 邀请10-15个潜在批发商\n'
               '第4周：跟进订单，安排送货，收取款项',
               fontsize=14, ha='left', va='top', linespacing=1.8)
        
        ax.text(5, 3.5, '💡 关键：利用酒店的"信任溢价"快速打开市场',
               fontsize=16, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#FFEAA7', edgecolor='#F39C12', linewidth=2))
        
        # 底部总结
        summary_box = FancyBboxPatch((0.5, 0.5), 9, 2,
                                     boxstyle="round,pad=0.15",
                                     edgecolor='#8E44AD',
                                     facecolor='#F4ECF7',
                                     linewidth=3)
        ax.add_patch(summary_box)
        
        ax.text(5, 2, '🏆 竞争优势总结',
               fontsize=18, fontweight='bold', ha='center')
        ax.text(5, 1.4, '普通批发商：需要租仓库 + 找客户 + 建立信任 (3-6个月)',
               fontsize=14, ha='center', color='#7F8C8D')
        ax.text(5, 0.8, 'Justice优势：现成空间 + 现成客户 + 现成信任 (2-3周快速回款)',
               fontsize=15, ha='center', fontweight='bold', color='#27AE60')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'hotel_advantage.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Hotel advantage infographic created")
    
    def generate_all(self):
        """生成所有具体计划可视化"""
        print("🚀 Starting concrete action plan visualization...")
        print("=" * 70)
        
        self.create_world_map_routes()
        self.create_zero_to_first_container_roadmap()
        self.create_partner_roles_diagram()
        self.create_hotel_advantage_infographic()
        
        print("=" * 70)
        print("✅ All concrete plan visualizations generated!")
        print(f"📁 Output directory: {self.output_dir}")

if __name__ == '__main__':
    visualizer = ConcreteActionPlanVisualizer()
    visualizer.generate_all()
