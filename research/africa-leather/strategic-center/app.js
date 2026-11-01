// ============================================
// STRATEGIC CENTER - INTERACTIVE MAP & CHARTS
// ============================================

// Global chart instances (exposed to window for testing)
window.containerChart = null;
window.marketChart = null;
window.productChart = null;
window.shareChart = null;
window.ganttChart = null;
window.transportChart = null;

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
// Carefully avoiding land masses
const routes = [
    {
        name: '上海 → 拉各斯',
        from: [31.2304, 121.4737],  // Shanghai
        to: [6.5244, 3.3792],       // Lagos
        waypoints: [
            [31.2304, 121.4737],    // Shanghai
            [25.0, 120.0],          // Taiwan Strait
            [20.0, 118.0],          // South China Sea north
            [15.0, 115.0],          // South China Sea central
            [10.0, 110.0],          // South China Sea south
            [5.0, 105.0],           // Approaching Malacca
            [2.5, 102.0],           // Malacca Strait north entrance
            [1.0, 100.0],           // Malacca Strait
            [-1.0, 98.0],           // Malacca Strait south exit
            [-5.0, 90.0],           // East Indian Ocean
            [-10.0, 80.0],          // Central Indian Ocean
            [-15.0, 70.0],          // Mid Indian Ocean
            [-20.0, 60.0],          // South Indian Ocean
            [-25.0, 50.0],          // Approaching South Africa
            [-30.0, 35.0],          // Off Durban
            [-35.0, 20.0],          // Cape of Good Hope (好望角)
            [-33.0, 15.0],          // Rounding the Cape
            [-25.0, 10.0],          // Atlantic Ocean, west of SA
            [-15.0, 5.0],           // South Atlantic
            [-5.0, 2.0],            // Equatorial Atlantic
            [0.0, 2.5],             // Crossing Equator
            [3.0, 3.0],             // Gulf of Guinea south
            [6.5244, 3.3792]        // Lagos
        ],
        color: '#0F0',
        days: 35,
        cost: 4500
    },
    {
        name: '深圳 → 德班',
        from: [22.5431, 114.0579],  // Shenzhen
        to: [-29.8587, 31.0218],    // Durban
        waypoints: [
            [22.5431, 114.0579],    // Shenzhen
            [18.0, 115.0],          // South China Sea
            [12.0, 112.0],          // South China Sea mid
            [6.0, 108.0],           // South China Sea south
            [2.5, 102.0],           // Malacca Strait entrance
            [1.0, 100.0],           // Malacca Strait
            [-1.0, 98.0],           // Malacca Strait exit
            [-5.0, 92.0],           // Sumatra west
            [-10.0, 85.0],          // East Indian Ocean
            [-15.0, 75.0],          // Central Indian Ocean
            [-20.0, 65.0],          // South Indian Ocean
            [-25.0, 55.0],          // Approaching Mozambique Channel
            [-28.0, 45.0],          // Madagascar east
            [-30.0, 35.0],          // Mozambique Channel
            [-29.8587, 31.0218]     // Durban
        ],
        color: '#0F0',
        days: 30,
        cost: 4200
    },
    {
        name: '广州 → 蒙巴萨',
        from: [23.1291, 113.2644],  // Guangzhou
        to: [-4.0435, 39.6682],     // Mombasa
        waypoints: [
            [23.1291, 113.2644],    // Guangzhou
            [18.0, 114.0],          // South China Sea
            [12.0, 111.0],          // South China Sea mid
            [6.0, 107.0],           // South China Sea south
            [2.5, 102.0],           // Malacca Strait entrance
            [1.0, 100.0],           // Malacca Strait
            [-1.0, 98.0],           // Malacca Strait exit
            [-4.0, 93.0],           // Sumatra southwest
            [-6.0, 88.0],           // East Indian Ocean
            [-8.0, 80.0],           // Central Indian Ocean
            [-10.0, 70.0],          // Mid Indian Ocean
            [-8.0, 60.0],           // West Indian Ocean
            [-5.0, 50.0],           // East Africa approach
            [-4.0435, 39.6682]      // Mombasa
        ],
        color: '#0F0',
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
// Charts will be initialized by initializeCharts() function
// which is called after i18n is loaded

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

// Function to initialize/update all charts with current language
window.initializeCharts = function(lang) {
    lang = lang || 'en';
    console.log('Initializing charts with language:', lang);
    
    // Get translations - access from window.translations
    const t = window.translations?.[lang];
    if (!t) {
        console.error('Translations not found for language:', lang);
        return;
    }
    
    // Destroy existing charts
    if (window.containerChart) window.containerChart.destroy();
    if (window.marketChart) window.marketChart.destroy();
    if (window.productChart) window.productChart.destroy();
    if (window.shareChart) window.shareChart.destroy();
    if (window.ganttChart) window.ganttChart.destroy();
    if (window.transportChart) window.transportChart.destroy();
    
    // Get canvas contexts
    const containerCtx = document.getElementById('containerChart')?.getContext('2d');
    const marketCtx = document.getElementById('marketChart')?.getContext('2d');
    const productCtx = document.getElementById('productChart')?.getContext('2d');
    const shareCtx = document.getElementById('shareChart')?.getContext('2d');
    const ganttCtx = document.getElementById('ganttChart')?.getContext('2d');
    const transportCtx = document.getElementById('transportChart')?.getContext('2d');
    
    if (!containerCtx || !marketCtx || !productCtx || !shareCtx || !ganttCtx || !transportCtx) {
        console.error('One or more chart canvases not found');
        return;
    }
    
    // Chart 1: Container Economics
    window.containerChart = new Chart(containerCtx, {
        type: 'bar',
        data: {
            labels: [
                t.data.costs.leather,
                t.data.costs.shipping,
                t.data.costs.duty,
                t.data.costs.local,
                t.data.costs.revenue
            ],
            datasets: [{
                label: 'USD',
                data: [44200, 4500, 3200, 800, 130000],
                backgroundColor: [
                    'rgba(0, 255, 0, 0.6)',
                    'rgba(0, 255, 0, 0.7)',
                    'rgba(0, 255, 0, 0.5)',
                    'rgba(0, 255, 0, 0.6)',
                    'rgba(0, 255, 0, 0.9)'
                ],
                borderColor: '#0F0',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text: t.data.chart1Subtitle,
                    color: '#0F0',
                    font: { size: 16, weight: 'bold', family: "'Courier New', monospace" }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { color: '#0F0', font: { family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                },
                x: {
                    ticks: { color: '#0F0', font: { family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                }
            }
        }
    });
    
    // Chart 2: Market Size
    window.marketChart = new Chart(marketCtx, {
        type: 'doughnut',
        data: {
            labels: [
                t.data.countries.nigeria,
                t.data.countries.southAfrica,
                t.data.countries.kenya,
                t.data.countries.ethiopia,
                t.data.countries.ghana,
                t.data.countries.tanzania,
                t.data.countries.uganda,
                t.data.countries.senegal
            ],
            datasets: [{
                label: lang === 'zh' ? '市场规模 (百万美元)' : lang === 'de' ? 'Marktgröße (Mio. USD)' : lang === 'ru' ? 'Размер рынка (млн USD)' : 'Market Size (M USD)',
                data: [580, 450, 320, 280, 210, 190, 150, 130],
                backgroundColor: [
                    'rgba(0, 255, 0, 0.9)',
                    'rgba(0, 255, 0, 0.8)',
                    'rgba(0, 255, 0, 0.7)',
                    'rgba(0, 255, 0, 0.6)',
                    'rgba(0, 255, 0, 0.5)',
                    'rgba(0, 200, 0, 0.8)',
                    'rgba(0, 200, 0, 0.7)',
                    'rgba(0, 200, 0, 0.6)'
                ],
                borderColor: '#000',
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
                        color: '#0F0',
                        font: { size: 12, family: "'Courier New', monospace" }
                    }
                },
                title: {
                    display: true,
                    text: t.data.chart2Subtitle,
                    color: '#0F0',
                    font: { size: 16, weight: 'bold', family: "'Courier New', monospace" }
                }
            }
        }
    });
    
    // Chart 3: Product Margins
    window.productChart = new Chart(productCtx, {
        type: 'bar',
        data: {
            labels: [
                t.data.products.sofa,
                t.data.products.bag,
                t.data.products.garment,
                t.data.products.shoe,
                t.data.products.auto
            ],
            datasets: [{
                label: lang === 'zh' ? '利润率 (%)' : lang === 'de' ? 'Gewinnmarge (%)' : lang === 'ru' ? 'Маржа (%)' : 'Profit Margin (%)',
                data: [165, 180, 140, 155, 170],
                backgroundColor: 'rgba(0, 255, 0, 0.7)',
                borderColor: '#0F0',
                borderWidth: 2
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text: t.data.chart3Subtitle,
                    color: '#0F0',
                    font: { size: 16, weight: 'bold', family: "'Courier New', monospace" }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: { color: '#0F0', font: { family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                },
                y: {
                    ticks: { color: '#0F0', font: { family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                }
            }
        }
    });
    
    // Chart 4: Import Share
    window.shareChart = new Chart(shareCtx, {
        type: 'pie',
        data: {
            labels: [
                t.data.sources.china,
                t.data.sources.india,
                t.data.sources.turkey,
                t.data.sources.local,
                t.data.sources.other
            ],
            datasets: [{
                label: lang === 'zh' ? '市场份额 (%)' : lang === 'de' ? 'Marktanteil (%)' : lang === 'ru' ? 'Доля рынка (%)' : 'Market Share (%)',
                data: [42, 18, 12, 20, 8],
                backgroundColor: [
                    'rgba(0, 255, 0, 0.9)',
                    'rgba(0, 255, 0, 0.7)',
                    'rgba(0, 255, 0, 0.5)',
                    'rgba(0, 200, 0, 0.8)',
                    'rgba(0, 200, 0, 0.6)'
                ],
                borderColor: '#000',
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
                        color: '#0F0',
                        font: { size: 12, family: "'Courier New', monospace" }
                    }
                },
                title: {
                    display: true,
                    text: t.data.chart4Subtitle,
                    color: '#0F0',
                    font: { size: 16, weight: 'bold', family: "'Courier New', monospace" }
                }
            }
        }
    });
    
    // Chart 5: Gantt Chart  
    const ganttLabels = lang === 'zh' ? [
        '市场调研与寻源', '供应商谈判', '资金筹集', '订单下达', '生产与质检',
        '运输文档', '海运 (25-35天)', '清关', '港口→酒店运输', '展厅布置', '展销会', '回款'
    ] : lang === 'de' ? [
        'Marktforschung', 'Lieferantenverhandlung', 'Kapitalbeschaffung', 'Auftragserteilung', 'Produktion & QK',
        'Versanddokumentation', 'Seefracht (25-35 Tage)', 'Zollabfertigung', 'Hafen→Hotel Transport', 'Showroom-Einrichtung', 'Ausstellung & Verkauf', 'Zahlungseinzug'
    ] : lang === 'ru' ? [
        'Исследование рынка', 'Переговоры с поставщиками', 'Привлечение капитала', 'Размещение заказа', 'Производство и КК',
        'Документация доставки', 'Морская перевозка (25-35 дней)', 'Таможенная очистка', 'Порт→Отель транспорт', 'Настройка выставки', 'Выставка и продажи', 'Сбор платежей'
    ] : [
        'Market Research & Sourcing', 'Supplier Negotiation', 'Capital Raising', 'Order Placement', 'Production & QC',
        'Shipping Documentation', 'Sea Freight (25-35 days)', 'Customs Clearance', 'Port → Hotel Transport', 'Showroom Setup', 'Exhibition & Sales', 'Cash Collection'
    ];
    
    window.ganttChart = new Chart(ganttCtx, {
        type: 'bar',
        data: {
            labels: ganttLabels,
            datasets: [{
                label: lang === 'zh' ? '持续时间 (天)' : lang === 'de' ? 'Dauer (Tage)' : lang === 'ru' ? 'Продолжительность (дни)' : 'Duration (days)',
                data: [7, 7, 15, 5, 10, 5, 30, 3, 2, 5, 14, 14],
                backgroundColor: [
                    'rgba(0, 255, 0, 0.7)', 'rgba(0, 255, 0, 0.6)', 'rgba(0, 200, 0, 0.7)',
                    'rgba(0, 255, 0, 0.5)', 'rgba(0, 255, 0, 0.8)', 'rgba(0, 200, 0, 0.6)',
                    'rgba(0, 255, 0, 0.9)', 'rgba(0, 255, 0, 0.7)', 'rgba(0, 200, 0, 0.8)',
                    'rgba(0, 255, 0, 0.6)', 'rgba(0, 255, 0, 0.5)', 'rgba(0, 200, 0, 0.7)'
                ],
                borderColor: '#0F0',
                borderWidth: 2
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text: lang === 'zh' ? '60天甘特图' : lang === 'de' ? '60-Tage Gantt-Diagramm' : lang === 'ru' ? 'Диаграмма Ганта 60 дней' : '60-Day Gantt Chart',
                    color: '#0F0',
                    font: { size: 18, weight: 'bold', family: "'Courier New', monospace" }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: { color: '#0F0', font: { family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                },
                y: {
                    ticks: { color: '#0F0', font: { size: 11, family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                }
            }
        }
    });
    
    // Chart 6: Transport Comparison
    const transportLabels = lang === 'zh' ? ['海运', '空运', '铁路', '陆运 (本地)'] :
                            lang === 'de' ? ['Seefracht', 'Luftfracht', 'Bahn', 'Straße (Lokal)'] :
                            lang === 'ru' ? ['Морской транспорт', 'Авиаперевозки', 'Железная дорога', 'Автомобильный (местный)'] :
                            ['Sea Freight', 'Air Freight', 'Rail', 'Road (Local)'];
    
    window.transportChart = new Chart(transportCtx, {
        type: 'bar',
        data: {
            labels: transportLabels,
            datasets: [
                {
                    label: lang === 'zh' ? '成本 ($)' : lang === 'de' ? 'Kosten ($)' : lang === 'ru' ? 'Стоимость ($)' : 'Cost ($)',
                    data: [4250, 30000, 9000, 650],
                    backgroundColor: 'rgba(0, 255, 0, 0.6)',
                    borderColor: '#0F0',
                    borderWidth: 2,
                    yAxisID: 'y'
                },
                {
                    label: lang === 'zh' ? '时间 (天)' : lang === 'de' ? 'Zeit (Tage)' : lang === 'ru' ? 'Время (дни)' : 'Time (days)',
                    data: [30, 5, 21.5, 2],
                    backgroundColor: 'rgba(0, 200, 0, 0.6)',
                    borderColor: '#0A0',
                    borderWidth: 2,
                    yAxisID: 'y1'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            interaction: { mode: 'index', intersect: false },
            plugins: {
                legend: {
                    position: 'top',
                    labels: { color: '#0F0', font: { size: 12, family: "'Courier New', monospace" } }
                },
                title: {
                    display: true,
                    text: lang === 'zh' ? '运输方式对比' : lang === 'de' ? 'Transportmittelvergleich' : lang === 'ru' ? 'Сравнение видов транспорта' : 'Transport Mode Comparison',
                    color: '#0F0',
                    font: { size: 16, weight: 'bold', family: "'Courier New', monospace" }
                }
            },
            scales: {
                y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    beginAtZero: true,
                    ticks: { color: '#0F0', font: { family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                },
                y1: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    beginAtZero: true,
                    ticks: { color: '#0A0', font: { family: "'Courier New', monospace" } },
                    grid: { drawOnChartArea: false }
                },
                x: {
                    ticks: { color: '#0F0', font: { family: "'Courier New', monospace" } },
                    grid: { color: 'rgba(0, 255, 0, 0.1)' }
                }
            }
        }
    });
    
    console.log('✅ All charts initialized with language:', lang);
};
