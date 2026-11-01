#!/usr/bin/env python3
"""
创建真实的世界地图与航线
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon, FancyArrowPatch
import numpy as np
from pathlib import Path

def create_detailed_world_map():
    """创建详细的世界地图与航线"""
    
    fig, ax = plt.subplots(figsize=(24, 14))
    
    # 设置范围
    ax.set_xlim(-20, 150)
    ax.set_ylim(-50, 60)
    ax.set_facecolor('#87CEEB')  # 海洋蓝色
    
    # 更详细的大陆绘制
    
    # 非洲大陆
    africa_coast = np.array([
        [-17, 33], [-10, 36], [0, 37], [10, 37], [15, 32], [20, 30],
        [25, 31], [32, 31], [37, 27], [42, 20], [45, 15], [48, 12],
        [50, 5], [51, 0], [51, -10], [48, -20], [40, -30], [32, -34],
        [25, -34], [20, -29], [18, -22], [16, -17], [15, -10],
        [12, -5], [10, 0], [8, 5], [5, 10], [3, 15], [0, 20],
        [-5, 23], [-10, 25], [-15, 28], [-17, 33]
    ])
    africa = Polygon(africa_coast, facecolor='#F4E4C1', edgecolor='#8B4513', linewidth=2.5, alpha=0.9)
    ax.add_patch(africa)
    
    # 亚洲大陆 (聚焦中国区域)
    asia_coast = np.array([
        [70, 5], [75, 8], [80, 12], [85, 15], [90, 18], [95, 20],
        [100, 22], [105, 24], [110, 26], [115, 28], [120, 30],
        [125, 32], [130, 35], [135, 38], [140, 40], [145, 42],
        [147, 45], [147, 50], [145, 52], [140, 53], [135, 52],
        [130, 50], [125, 48], [120, 45], [115, 42], [110, 40],
        [105, 38], [100, 35], [95, 32], [90, 28], [85, 25],
        [80, 20], [75, 15], [70, 10], [70, 5]
    ])
    asia = Polygon(asia_coast, facecolor='#E8DCC4', edgecolor='#8B4513', linewidth=2.5, alpha=0.9)
    ax.add_patch(asia)
    
    # 欧洲（简化）
    europe_coast = np.array([
        [-10, 36], [0, 40], [10, 43], [20, 45], [30, 48], [40, 50],
        [50, 52], [60, 54], [65, 55], [65, 50], [60, 45], [55, 42],
        [50, 40], [45, 38], [40, 37], [30, 36], [20, 36], [10, 37],
        [0, 37], [-10, 36]
    ])
    europe = Polygon(europe_coast, facecolor='#D4C5AA', edgecolor='#8B4513', linewidth=2, alpha=0.9)
    ax.add_patch(europe)
    
    # 中东（简化）
    middle_east = np.array([
        [35, 15], [40, 18], [45, 20], [50, 23], [55, 25], [60, 27],
        [65, 28], [70, 28], [70, 20], [68, 15], [65, 12], [60, 10],
        [55, 10], [50, 12], [45, 13], [40, 14], [35, 15]
    ])
    me = Polygon(middle_east, facecolor='#E8D4B8', edgecolor='#8B4513', linewidth=2, alpha=0.9)
    ax.add_patch(me)
    
    # 印度次大陆
    india_coast = np.array([
        [68, 8], [70, 10], [72, 15], [75, 20], [78, 24], [82, 28],
        [85, 30], [88, 30], [90, 28], [88, 24], [86, 20], [84, 16],
        [82, 12], [80, 9], [77, 7], [73, 6], [70, 7], [68, 8]
    ])
    india = Polygon(india_coast, facecolor='#DCC9AA', edgecolor='#8B4513', linewidth=2, alpha=0.9)
    ax.add_patch(india)
    
    # 标注大陆名称
    ax.text(25, 5, 'AFRICA\n非洲', fontsize=32, fontweight='bold', 
           ha='center', va='center', color='#654321',
           bbox=dict(boxstyle='round,pad=0.8', facecolor='white', alpha=0.85, edgecolor='#8B4513', linewidth=2))
    
    ax.text(115, 35, 'CHINA\n中国', fontsize=32, fontweight='bold',
           ha='center', va='center', color='#8B0000',
           bbox=dict(boxstyle='round,pad=0.8', facecolor='white', alpha=0.85, edgecolor='#8B4513', linewidth=2))
    
    # 主要城市标记
    cities = {
        '上海\nShanghai': (121.47, 31.23),
        '深圳\nShenzhen': (114.06, 22.54),
        '广州\nGuangzhou': (113.26, 23.13),
        '拉各斯\nLagos': (3.39, 6.45),
        '德班\nDurban': (31.02, -29.86),
        '蒙巴萨\nMombasa': (39.67, -4.04),
    }
    
    for city, (lon, lat) in cities.items():
        ax.plot(lon, lat, 'o', markersize=14, color='red', 
               markeredgecolor='darkred', markeredgewidth=2, zorder=10)
        ax.text(lon, lat+3, city, fontsize=13, fontweight='bold', 
               ha='center', va='bottom',
               bbox=dict(boxstyle='round,pad=0.4', facecolor='yellow', alpha=0.9, edgecolor='black', linewidth=1.5))
    
    # 航线
    routes = [
        {
            'start': (121.47, 31.23),  # 上海
            'end': (3.39, 6.45),       # 拉各斯
            'color': '#FF0000',
            'label': '上海 → 拉各斯\n35天 | $4,500'
        },
        {
            'start': (114.06, 22.54),  # 深圳
            'end': (31.02, -29.86),    # 德班
            'color': '#00CED1',
            'label': '深圳 → 德班\n28天 | $3,800'
        },
        {
            'start': (113.26, 23.13),  # 广州
            'end': (39.67, -4.04),     # 蒙巴萨
            'color': '#32CD32',
            'label': '广州 → 蒙巴萨\n25天 | $3,200'
        }
    ]
    
    # 绘制航线
    for idx, route in enumerate(routes):
        start_lon, start_lat = route['start']
        end_lon, end_lat = route['end']
        
        # 创建曲线
        if 'Lagos' in route['label'] or '拉各斯' in route['label']:
            # 上海到拉各斯：向西南弯曲
            mid_lon = (start_lon + end_lon) / 2 - 20
            mid_lat = (start_lat + end_lat) / 2 + 5
        elif 'Durban' in route['label'] or '德班' in route['label']:
            # 深圳到德班：向南弯曲
            mid_lon = (start_lon + end_lon) / 2 + 15
            mid_lat = (start_lat + end_lat) / 2 - 10
        else:
            # 广州到蒙巴萨：中间偏西
            mid_lon = (start_lon + end_lon) / 2
            mid_lat = (start_lat + end_lat) / 2 - 5
        
        # 贝塞尔曲线
        t = np.linspace(0, 1, 100)
        lons = (1-t)**2 * start_lon + 2*(1-t)*t * mid_lon + t**2 * end_lon
        lats = (1-t)**2 * start_lat + 2*(1-t)*t * mid_lat + t**2 * end_lat
        
        ax.plot(lons, lats, linewidth=4, color=route['color'], 
               alpha=0.8, label=route['label'], zorder=5)
        
        # 箭头
        arrow_idx = 75
        dx = lons[arrow_idx+1] - lons[arrow_idx-1]
        dy = lats[arrow_idx+1] - lats[arrow_idx-1]
        ax.arrow(lons[arrow_idx], lats[arrow_idx], dx*2, dy*2,
                head_width=3, head_length=2.5, fc=route['color'], 
                ec='black', linewidth=1.5, zorder=6)
    
    # 网格和标签
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=1)
    ax.set_xlabel('经度 Longitude', fontsize=20, fontweight='bold')
    ax.set_ylabel('纬度 Latitude', fontsize=20, fontweight='bold')
    
    # 标题
    title_text = '中国 → 非洲主要海运路线\nChina → Africa Major Shipping Routes\n40英尺集装箱海运 (40ft Container Shipping)'
    ax.set_title(title_text, fontsize=28, fontweight='bold', pad=25, 
                bbox=dict(boxstyle='round,pad=1', facecolor='#FFE4B5', alpha=0.9, edgecolor='#8B4513', linewidth=3))
    
    # 图例
    ax.legend(loc='lower left', fontsize=16, framealpha=0.95, 
             edgecolor='black', fancybox=True, shadow=True)
    
    # 添加指南针
    compass_x, compass_y = 140, 50
    ax.text(compass_x, compass_y, 'N\n↑', fontsize=24, fontweight='bold', 
           ha='center', va='center',
           bbox=dict(boxstyle='circle,pad=0.5', facecolor='white', edgecolor='black', linewidth=2))
    
    plt.tight_layout()
    
    output_path = Path('concrete_plan/world_map_routes_detailed.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ 详细世界地图已创建: {output_path}")
    return output_path

if __name__ == '__main__':
    create_detailed_world_map()
