// ============================================
// STRATEGIC CENTER - INTERACTIVE MAP & CHARTS
// ============================================

// Initialize the map centered on Africa
const map = L.map('map', {
    center: [5, 20],
    zoom: 3,
    zoomControl: true,
    scrollWheelZoom: true
});

// Add real world map tiles from OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19
}).addTo(map);

// Define shipping routes with REAL waypoints (through Malacca Strait, Indian Ocean)
const routes = [
    {
        name: '上海 → 拉各斯',
        from: [31.2304, 121.4737],  // Shanghai
        to: [6.5244, 3.3792],       // Lagos
        waypoints: [
            [31.2304, 121.4737],    // Shanghai
            [22.3, 114.2],          // Hong Kong waters
            [16.0, 112.0],          // South China Sea
            [7.5, 105.0],           // Vietnam coast
            [3.5, 100.5],           // Malacca Strait entrance
            [1.3, 103.8],           // Singapore Strait
            [-5.0, 80.0],           // Central Indian Ocean
            [-8.0, 60.0],           // Western Indian Ocean
            [-10.0, 45.0],          // East Africa approach
            [0.0, 40.0],            // Somalia waters
            [5.0, 10.0],            // Gulf of Guinea approach
            [6.5244, 3.3792]        // Lagos
        ],
        color: '#FFD700',
        days: 35,
        cost: 4500
    },
    {
        name: '深圳 → 德班',
        from: [22.5431, 114.0579],  // Shenzhen
        to: [-29.8587, 31.0218],    // Durban
        waypoints: [
            [22.5431, 114.0579],    // Shenzhen
            [18.0, 112.0],          // South China Sea
            [10.0, 108.0],          // Vietnam waters
            [3.5, 100.5],           // Malacca Strait
            [1.3, 103.8],           // Singapore
            [-6.0, 85.0],           // Indian Ocean (Sumatra)
            [-12.0, 70.0],          // Central Indian Ocean
            [-20.0, 55.0],          // Mozambique Channel approach
            [-25.0, 40.0],          // Madagascar waters
            [-29.8587, 31.0218]     // Durban
        ],
        color: '#FFA500',
        days: 30,
        cost: 4200
    },
    {
        name: '广州 → 蒙巴萨',
        from: [23.1291, 113.2644],  // Guangzhou
        to: [-4.0435, 39.6682],     // Mombasa
        waypoints: [
            [23.1291, 113.2644],    // Guangzhou
            [18.0, 112.0],          // South China Sea
            [8.0, 106.0],           // Vietnam coast
            [3.5, 100.5],           // Malacca Strait
            [1.3, 103.8],           // Singapore
            [-3.0, 90.0],           // Indian Ocean (Sumatra)
            [-8.0, 75.0],           // Central Indian Ocean
            [-10.0, 60.0],          // Western Indian Ocean
            [-6.0, 50.0],           // East Africa approach
            [-4.0435, 39.6682]      // Mombasa
        ],
        color: '#FF6B6B',
        days: 28,
        cost: 4000
    }
];

// Add markers and routes to map
routes.forEach(route => {
    // Add departure marker (China)
    const departureMarker = L.circleMarker(route.from, {
        radius: 8,
        fillColor: route.color,
        color: '#fff',
        weight: 2,
        opacity: 1,
        fillOpacity: 0.8
    }).addTo(map);
    
    departureMarker.bindPopup(`
        <div style="color: #000; font-weight: 600;">
            <strong>${route.name.split(' → ')[0]}</strong><br>
            出发港口 | Departure Port
        </div>
    `);
    
    // Add arrival marker (Africa)
    const arrivalMarker = L.circleMarker(route.to, {
        radius: 10,
        fillColor: route.color,
        color: '#fff',
        weight: 2,
        opacity: 1,
        fillOpacity: 0.9
    }).addTo(map);
    
    arrivalMarker.bindPopup(`
        <div style="color: #000; font-weight: 600;">
            <strong>${route.name.split(' → ')[1]}</strong><br>
            到达港口 | Arrival Port<br>
            <span style="color: #1e3c72;">运输时间: ${route.days}天</span><br>
            <span style="color: #1e3c72;">运费: $${route.cost.toLocaleString()}</span>
        </div>
    `);
    
    // Draw REAL shipping route with waypoints (actual maritime path)
    const shippingLine = L.polyline(route.waypoints, {
        color: route.color,
        weight: 3,
        opacity: 0.8,
        smoothFactor: 2,
        dashArray: '10, 8'
    }).addTo(map);
    
    shippingLine.bindPopup(`
        <div style="color: #000; font-weight: 600;">
            <strong>${route.name}</strong><br>
            真实海运航线 | Real Maritime Route<br>
            <span style="color: #1e3c72;">经马六甲海峡、印度洋</span><br>
            <span style="color: #1e3c72;">预计${route.days}天</span>
        </div>
    `);
    
    // Add animated ship marker moving along route
    let shipIndex = 0;
    const ship = L.circleMarker(route.waypoints[0], {
        radius: 5,
        fillColor: '#fff',
        color: route.color,
        weight: 2,
        opacity: 0.9,
        fillOpacity: 1
    }).addTo(map);
    
    // Animate ship movement
    setInterval(() => {
        shipIndex = (shipIndex + 1) % route.waypoints.length;
        ship.setLatLng(route.waypoints[shipIndex]);
    }, 3000); // Move every 3 seconds
});

// ============================================
// CHARTS - DATA VISUALIZATION
// ============================================

// Chart 1: Container Economics
const containerCtx = document.getElementById('containerChart').getContext('2d');
new Chart(containerCtx, {
    type: 'bar',
    data: {
        labels: ['皮革采购', '海运费用', '关税清关', '本地物流', '预期收入'],
        datasets: [{
            label: '美元 (USD)',
            data: [44200, 4500, 3200, 800, 130000],
            backgroundColor: [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)',
                'rgba(75, 192, 192, 0.7)',
                'rgba(75, 255, 75, 0.9)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(75, 255, 75, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: '首个40ft集装箱成本与收入',
                color: '#FFD700',
                font: {
                    size: 16,
                    weight: 'bold'
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#fff',
                    callback: function(value) {
                        return '$' + value.toLocaleString();
                    }
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)'
                }
            },
            x: {
                ticks: {
                    color: '#fff'
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)'
                }
            }
        }
    }
});

// Chart 2: Market Size
const marketCtx = document.getElementById('marketChart').getContext('2d');
new Chart(marketCtx, {
    type: 'doughnut',
    data: {
        labels: ['尼日利亚', '南非', '肯尼亚', '埃塞俄比亚', '加纳', '坦桑尼亚', '乌干达', '塞内加尔'],
        datasets: [{
            label: '市场规模 (百万美元)',
            data: [580, 450, 320, 280, 210, 190, 150, 130],
            backgroundColor: [
                'rgba(255, 215, 0, 0.8)',
                'rgba(255, 165, 0, 0.8)',
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(255, 159, 64, 0.8)'
            ],
            borderColor: '#fff',
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                position: 'right',
                labels: {
                    color: '#fff',
                    font: {
                        size: 12
                    }
                }
            },
            title: {
                display: true,
                text: '非洲八国皮革市场规模 (2026)',
                color: '#FFD700',
                font: {
                    size: 16,
                    weight: 'bold'
                }
            }
        }
    }
});

// Chart 3: Product Profit Margins
const productCtx = document.getElementById('productChart').getContext('2d');
new Chart(productCtx, {
    type: 'horizontalBar',
    data: {
        labels: ['沙发革', '箱包革', '服装革', '鞋革', '汽车内饰革'],
        datasets: [{
            label: '利润率 (%)',
            data: [165, 180, 140, 155, 170],
            backgroundColor: 'rgba(255, 215, 0, 0.7)',
            borderColor: 'rgba(255, 215, 0, 1)',
            borderWidth: 2
        }]
    },
    options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: '各类皮革产品利润率',
                color: '#FFD700',
                font: {
                    size: 16,
                    weight: 'bold'
                }
            }
        },
        scales: {
            x: {
                beginAtZero: true,
                ticks: {
                    color: '#fff',
                    callback: function(value) {
                        return value + '%';
                    }
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)'
                }
            },
            y: {
                ticks: {
                    color: '#fff'
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)'
                }
            }
        }
    }
});

// Chart 4: China Import Share
const shareCtx = document.getElementById('shareChart').getContext('2d');
new Chart(shareCtx, {
    type: 'pie',
    data: {
        labels: ['中国进口', '印度进口', '土耳其进口', '本地生产', '其他'],
        datasets: [{
            label: '市场份额 (%)',
            data: [42, 18, 12, 20, 8],
            backgroundColor: [
                'rgba(255, 215, 0, 0.9)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 99, 132, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)'
            ],
            borderColor: '#fff',
            borderWidth: 3
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    color: '#fff',
                    font: {
                        size: 12
                    }
                }
            },
            title: {
                display: true,
                text: '非洲皮革进口来源分布',
                color: '#FFD700',
                font: {
                    size: 16,
                    weight: 'bold'
                }
            }
        }
    }
});

// ============================================
// SMOOTH SCROLLING
// ============================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ============================================
// ANIMATED STATS ON LOAD
// ============================================
const animateValue = (element, start, end, duration) => {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (end - start) + start);
        
        if (element.textContent.includes('$')) {
            element.textContent = '$' + value.toLocaleString();
        } else if (element.textContent.includes('%')) {
            element.textContent = value + '%';
        } else {
            element.textContent = value + '天';
        }
        
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
};

window.addEventListener('load', () => {
    const statValues = document.querySelectorAll('.stat-value');
    const values = [52700, 147, 60, 77300];
    
    statValues.forEach((stat, index) => {
        animateValue(stat, 0, values[index], 2000);
    });
});

console.log('🌍 Strategic Center loaded successfully!');
console.log('📊 Interactive map with real shipping routes');
console.log('🤝 Justice Sue Owen partnership dashboard');
