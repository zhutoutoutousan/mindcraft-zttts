// ============================================
// INTERNATIONALIZATION (i18n)
// 支持：中文、English、Deutsch、Русский
// ============================================

const translations = {
    zh: {
        // Header
        title: "Justice Sue Owen 战略中心",
        subtitle: "非洲皮革贸易战略中心",
        nav: {
            map: "🗺️ 全球航线",
            data: "📊 数据分析",
            partners: "🤝 合作伙伴",
            timeline: "⏱️ 60天计划"
        },
        
        // Hero
        hero: {
            title: "中国 → 非洲皮革贸易",
            description: "利用五星级酒店网络优势，打造高效的中非皮革供应链",
            stats: {
                investment: "首个集装箱投资",
                roi: "投资回报率 ROI",
                period: "回本周期",
                profit: "净利润"
            }
        },
        
        // Map Section
        map: {
            title: "全球海运路线图",
            description: "真实的互动式世界地图 - 中国到非洲的三条主要海运路线",
            route1: "上海 → 拉各斯",
            route2: "深圳 → 德班",
            route3: "广州 → 蒙巴萨",
            departure: "出发港口",
            arrival: "到达港口",
            shippingTime: "运输时间",
            cost: "运费",
            days: "天",
            realRoute: "真实海运航线",
            viaStrait: "经马六甲海峡、印度洋"
        },
        
        // Data Section
        data: {
            title: "数据分析与市场情报",
            chart1: "集装箱经济模型",
            chart1Subtitle: "首个40ft集装箱成本与收入",
            chart2: "市场规模对比",
            chart2Subtitle: "非洲八国皮革市场规模 (2026)",
            chart3: "产品利润率",
            chart3Subtitle: "各类皮革产品利润率",
            chart4: "中国进口份额",
            chart4Subtitle: "非洲皮革进口来源分布",
            costs: {
                leather: "皮革采购",
                shipping: "海运费用",
                duty: "关税清关",
                local: "本地物流",
                revenue: "预期收入"
            },
            countries: {
                nigeria: "尼日利亚",
                southAfrica: "南非",
                kenya: "肯尼亚",
                ethiopia: "埃塞俄比亚",
                ghana: "加纳",
                tanzania: "坦桑尼亚",
                uganda: "乌干达",
                senegal: "塞内加尔"
            },
            products: {
                sofa: "沙发革",
                bag: "箱包革",
                garment: "服装革",
                shoe: "鞋革",
                auto: "汽车内饰革"
            },
            sources: {
                china: "中国进口",
                india: "印度进口",
                turkey: "土耳其进口",
                local: "本地生产",
                other: "其他"
            }
        },
        
        // Partners Section
        partners: {
            title: "三方合作伙伴角色",
            china: {
                name: "中国合作方",
                role: "供应链上游管理",
                responsibilities: "核心职责：",
                tasks: [
                    "✓ 寻找可靠的皮革工厂",
                    "✓ 质量控制 + 验货",
                    "✓ 价格谈判 (目标: ¥35-40/㎡)",
                    "✓ 出口文件准备",
                    "✓ 集装箱装柜监督"
                ]
            },
            father: {
                name: "Justice父亲",
                role: "五星级酒店网络 + 本地分销",
                advantages: "核心优势：",
                tasks: [
                    "🏨 五星级酒店展示空间",
                    "👔 VIP客户数据库",
                    "🤝 信任背书 (酒店=信誉)",
                    "📦 仓储与物流便利",
                    "🎯 本地清关协调"
                ]
            },
            brother: {
                name: "Justice兄弟",
                role: "资金 + 协调 + 执行",
                keyRole: "关键角色：",
                tasks: [
                    "💰 提供启动资金 $52,700",
                    "🔗 协调中国供应商 + 非洲分销",
                    "📊 管理现金流",
                    "🚢 跟踪集装箱物流",
                    "⚖️ 利润分配管理"
                ]
            },
            profitShare: "利润分配"
        },
        
        // Timeline Section
        timeline: {
            title: "60天行动计划",
            phase1: "阶段1：前期准备 (第1-14天)",
            phase2: "阶段2：资金与物流 (第15-30天)",
            phase3: "阶段3：运输与清关 (第31-45天)",
            phase4: "阶段4：销售与回款 (第46-60天)",
            steps: {
                step1: "中国合作方考察广州/深圳皮革市场，要求样品+质检报告",
                step2: "Justice父亲在酒店设置展示区，联系VIP客户",
                step3: "筹集 $52,700 启动资金",
                step4: "预订货物 (8,500㎡皮革) + 集装箱舱位",
                step5: "购买海运保险 + 准备出口文件",
                step6: "货物海上运输 (25-35天)",
                step7: "到港清关，支付关税 (~$3,200)",
                step8: "运输到Justice父亲酒店仓库",
                step9: "在酒店大堂设置皮革展示台",
                step10: "举办"皮革产品展示会"，邀请10-15个批发商",
                step11: "2-3周内销售60-70%货物，回款 ~$90,000"
            },
            goal: "目标：",
            result: "结果：",
            goal1: "完成供应商选择 + 收集预订单",
            result1: "第60天回本，净利润 $77,300"
        },
        
        // Footer
        footer: {
            copyright: "© 2026 Justice Sue Owen Strategic Center. All Rights Reserved.",
            tagline: "非洲皮革贸易战略中心 | Powered by Real-Time Market Intelligence"
        }
    },
    
    en: {
        // Header
        title: "Justice Sue Owen Strategic Center",
        subtitle: "Africa Leather Trade Intelligence",
        nav: {
            map: "🗺️ Global Routes",
            data: "📊 Data Analysis",
            partners: "🤝 Partners",
            timeline: "⏱️ 60-Day Plan"
        },
        
        // Hero
        hero: {
            title: "China → Africa Leather Trade",
            description: "Leveraging 5-star hotel networks to build an efficient China-Africa leather supply chain",
            stats: {
                investment: "First Container Investment",
                roi: "Return on Investment",
                period: "Payback Period",
                profit: "Net Profit"
            }
        },
        
        // Map Section
        map: {
            title: "Global Shipping Routes Map",
            description: "Interactive real-world map - Three major maritime routes from China to Africa",
            route1: "Shanghai → Lagos",
            route2: "Shenzhen → Durban",
            route3: "Guangzhou → Mombasa",
            departure: "Departure Port",
            arrival: "Arrival Port",
            shippingTime: "Shipping Time",
            cost: "Freight Cost",
            days: "days",
            realRoute: "Real Maritime Route",
            viaStrait: "Via Malacca Strait, Indian Ocean"
        },
        
        // Data Section
        data: {
            title: "Data Analysis & Market Intelligence",
            chart1: "Container Economics Model",
            chart1Subtitle: "First 40ft Container Costs vs Revenue",
            chart2: "Market Size Comparison",
            chart2Subtitle: "Africa's 8-Country Leather Market Size (2026)",
            chart3: "Product Profit Margins",
            chart3Subtitle: "Profit Margins by Leather Product Type",
            chart4: "China Import Share",
            chart4Subtitle: "Africa Leather Import Sources",
            costs: {
                leather: "Leather Purchase",
                shipping: "Shipping Cost",
                duty: "Customs Duty",
                local: "Local Logistics",
                revenue: "Expected Revenue"
            },
            countries: {
                nigeria: "Nigeria",
                southAfrica: "South Africa",
                kenya: "Kenya",
                ethiopia: "Ethiopia",
                ghana: "Ghana",
                tanzania: "Tanzania",
                uganda: "Uganda",
                senegal: "Senegal"
            },
            products: {
                sofa: "Sofa Leather",
                bag: "Bag Leather",
                garment: "Garment Leather",
                shoe: "Shoe Leather",
                auto: "Auto Interior Leather"
            },
            sources: {
                china: "China Imports",
                india: "India Imports",
                turkey: "Turkey Imports",
                local: "Local Production",
                other: "Other"
            }
        },
        
        // Partners Section
        partners: {
            title: "Three-Party Partnership Roles",
            china: {
                name: "China Partner",
                role: "Upstream Supply Chain Management",
                responsibilities: "Core Responsibilities:",
                tasks: [
                    "✓ Find reliable leather factories",
                    "✓ Quality control + Inspection",
                    "✓ Price negotiation (Target: ¥35-40/sqm)",
                    "✓ Export documentation",
                    "✓ Container loading supervision"
                ]
            },
            father: {
                name: "Justice's Father",
                role: "5-Star Hotel Network + Local Distribution",
                advantages: "Core Advantages:",
                tasks: [
                    "🏨 5-star hotel showroom space",
                    "👔 VIP customer database",
                    "🤝 Trust endorsement (hotel=credibility)",
                    "📦 Warehouse & logistics convenience",
                    "🎯 Local customs coordination"
                ]
            },
            brother: {
                name: "Justice's Brother",
                role: "Funding + Coordination + Execution",
                keyRole: "Key Role:",
                tasks: [
                    "💰 Provide startup capital $52,700",
                    "🔗 Coordinate China supplier + Africa distribution",
                    "📊 Cash flow management",
                    "🚢 Track container logistics",
                    "⚖️ Profit distribution management"
                ]
            },
            profitShare: "Profit Share"
        },
        
        // Timeline Section
        timeline: {
            title: "60-Day Action Plan",
            phase1: "Phase 1: Preparation (Days 1-14)",
            phase2: "Phase 2: Funding & Logistics (Days 15-30)",
            phase3: "Phase 3: Shipping & Customs (Days 31-45)",
            phase4: "Phase 4: Sales & Collection (Days 46-60)",
            steps: {
                step1: "China partner surveys Guangzhou/Shenzhen leather markets, requests samples + quality reports",
                step2: "Justice's father sets up hotel showroom, contacts VIP customers",
                step3: "Raise $52,700 startup capital",
                step4: "Order goods (8,500 sqm leather) + container space",
                step5: "Purchase marine insurance + prepare export documents",
                step6: "Sea freight (25-35 days)",
                step7: "Port clearance, pay customs duty (~$3,200)",
                step8: "Transport to Justice's father's hotel warehouse",
                step9: "Set up leather display in hotel lobby",
                step10: "Hold 'Leather Product Exhibition', invite 10-15 wholesalers",
                step11: "Sell 60-70% goods in 2-3 weeks, collect ~$90,000"
            },
            goal: "Goal:",
            result: "Result:",
            goal1: "Complete supplier selection + collect pre-orders",
            result1: "Break even Day 60, net profit $77,300"
        },
        
        // Footer
        footer: {
            copyright: "© 2026 Justice Sue Owen Strategic Center. All Rights Reserved.",
            tagline: "Africa Leather Trade Strategic Center | Powered by Real-Time Market Intelligence"
        }
    },
    
    de: {
        // Header
        title: "Justice Sue Owen Strategiezentrum",
        subtitle: "Afrikanischer Lederhandel Intelligenz",
        nav: {
            map: "🗺️ Globale Routen",
            data: "📊 Datenanalyse",
            partners: "🤝 Partner",
            timeline: "⏱️ 60-Tage-Plan"
        },
        
        // Hero
        hero: {
            title: "China → Afrika Lederhandel",
            description: "Nutzung von 5-Sterne-Hotelnetzwerken für eine effiziente China-Afrika-Leder-Lieferkette",
            stats: {
                investment: "Erste Container-Investition",
                roi: "Kapitalrendite",
                period: "Amortisationszeit",
                profit: "Nettogewinn"
            }
        },
        
        // Map Section
        map: {
            title: "Globale Schifffahrtsroutenkarte",
            description: "Interaktive Weltkarte - Drei Hauptseewege von China nach Afrika",
            route1: "Shanghai → Lagos",
            route2: "Shenzhen → Durban",
            route3: "Guangzhou → Mombasa",
            departure: "Abfahrtshafen",
            arrival: "Zielhafen",
            shippingTime: "Transportzeit",
            cost: "Frachtkosten",
            days: "Tage",
            realRoute: "Echte Seeroute",
            viaStrait: "Via Straße von Malakka, Indischer Ozean"
        },
        
        // Data Section
        data: {
            title: "Datenanalyse & Marktintelligenz",
            chart1: "Container-Wirtschaftsmodell",
            chart1Subtitle: "Erste 40ft Container Kosten vs. Einnahmen",
            chart2: "Marktgrößenvergleich",
            chart2Subtitle: "Afrikas 8-Länder-Ledermarktgröße (2026)",
            chart3: "Produktgewinnmargen",
            chart3Subtitle: "Gewinnmargen nach Lederprodukttyp",
            chart4: "China-Importanteil",
            chart4Subtitle: "Afrika-Lederimportquellen",
            costs: {
                leather: "Lederkauf",
                shipping: "Versandkosten",
                duty: "Zollgebühren",
                local: "Lokale Logistik",
                revenue: "Erwartete Einnahmen"
            },
            countries: {
                nigeria: "Nigeria",
                southAfrica: "Südafrika",
                kenya: "Kenia",
                ethiopia: "Äthiopien",
                ghana: "Ghana",
                tanzania: "Tansania",
                uganda: "Uganda",
                senegal: "Senegal"
            },
            products: {
                sofa: "Sofaleder",
                bag: "Taschenleder",
                garment: "Bekleidungsleder",
                shoe: "Schuhleder",
                auto: "Auto-Innenraumleder"
            },
            sources: {
                china: "China-Importe",
                india: "Indien-Importe",
                turkey: "Türkei-Importe",
                local: "Lokale Produktion",
                other: "Andere"
            }
        },
        
        // Partners Section
        partners: {
            title: "Drei-Parteien-Partnerschaftsrollen",
            china: {
                name: "China-Partner",
                role: "Upstream-Lieferkettenmanagement",
                responsibilities: "Hauptverantwortlichkeiten:",
                tasks: [
                    "✓ Zuverlässige Lederfabriken finden",
                    "✓ Qualitätskontrolle + Inspektion",
                    "✓ Preisverhandlung (Ziel: ¥35-40/qm)",
                    "✓ Exportdokumentation",
                    "✓ Container-Ladeüberwachung"
                ]
            },
            father: {
                name: "Justices Vater",
                role: "5-Sterne-Hotelnetzwerk + Lokaler Vertrieb",
                advantages: "Hauptvorteile:",
                tasks: [
                    "🏨 5-Sterne-Hotel-Ausstellungsraum",
                    "👔 VIP-Kundendatenbank",
                    "🤝 Vertrauensbestätigung (Hotel=Glaubwürdigkeit)",
                    "📦 Lager- und Logistikbequemlichkeit",
                    "🎯 Lokale Zollkoordination"
                ]
            },
            brother: {
                name: "Justices Bruder",
                role: "Finanzierung + Koordination + Ausführung",
                keyRole: "Schlüsselrolle:",
                tasks: [
                    "💰 Startkapital bereitstellen $52.700",
                    "🔗 China-Lieferant + Afrika-Vertrieb koordinieren",
                    "📊 Cashflow-Management",
                    "🚢 Container-Logistik verfolgen",
                    "⚖️ Gewinnverteilungsmanagement"
                ]
            },
            profitShare: "Gewinnanteil"
        },
        
        // Timeline Section
        timeline: {
            title: "60-Tage-Aktionsplan",
            phase1: "Phase 1: Vorbereitung (Tage 1-14)",
            phase2: "Phase 2: Finanzierung & Logistik (Tage 15-30)",
            phase3: "Phase 3: Versand & Zoll (Tage 31-45)",
            phase4: "Phase 4: Verkauf & Einzug (Tage 46-60)",
            steps: {
                step1: "China-Partner untersucht Guangzhou/Shenzhen-Ledermärkte, fordert Muster + Qualitätsberichte an",
                step2: "Justices Vater richtet Hotel-Ausstellungsraum ein, kontaktiert VIP-Kunden",
                step3: "Startkapital von $52.700 aufbringen",
                step4: "Waren bestellen (8.500 qm Leder) + Containerplatz",
                step5: "Seeversicherung kaufen + Exportdokumente vorbereiten",
                step6: "Seefracht (25-35 Tage)",
                step7: "Hafenabfertigung, Zollgebühren zahlen (~$3.200)",
                step8: "Transport zum Hotel-Lager von Justices Vater",
                step9: "Leder-Ausstellung in Hotellobby aufbauen",
                step10: "'Lederprodukt-Ausstellung' veranstalten, 10-15 Großhändler einladen",
                step11: "60-70% der Waren in 2-3 Wochen verkaufen, ~$90.000 einziehen"
            },
            goal: "Ziel:",
            result: "Ergebnis:",
            goal1: "Lieferantenauswahl abschließen + Vorbestellungen sammeln",
            result1: "Break-even Tag 60, Nettogewinn $77.300"
        },
        
        // Footer
        footer: {
            copyright: "© 2026 Justice Sue Owen Strategiezentrum. Alle Rechte vorbehalten.",
            tagline: "Afrikanisches Lederhandels-Strategiezentrum | Powered by Echtzeit-Marktintelligenz"
        }
    },
    
    ru: {
        // Header
        title: "Стратегический центр Justice Sue Owen",
        subtitle: "Разведка африканской кожаной торговли",
        nav: {
            map: "🗺️ Глобальные маршруты",
            data: "📊 Анализ данных",
            partners: "🤝 Партнеры",
            timeline: "⏱️ 60-дневный план"
        },
        
        // Hero
        hero: {
            title: "Китай → Африка торговля кожей",
            description: "Использование сети 5-звездочных отелей для эффективной китайско-африканской цепочки поставок кожи",
            stats: {
                investment: "Первые инвестиции в контейнер",
                roi: "Рентабельность инвестиций",
                period: "Период окупаемости",
                profit: "Чистая прибыль"
            }
        },
        
        // Map Section
        map: {
            title: "Карта глобальных судоходных маршрутов",
            description: "Интерактивная карта мира - три основных морских маршрута из Китая в Африку",
            route1: "Шанхай → Лагос",
            route2: "Шэньчжэнь → Дурбан",
            route3: "Гуанчжоу → Момбаса",
            departure: "Порт отправления",
            arrival: "Порт прибытия",
            shippingTime: "Время доставки",
            cost: "Стоимость фрахта",
            days: "дней",
            realRoute: "Реальный морской маршрут",
            viaStrait: "Через Малаккский пролив, Индийский океан"
        },
        
        // Data Section
        data: {
            title: "Анализ данных и рыночная разведка",
            chart1: "Экономическая модель контейнера",
            chart1Subtitle: "Первый 40-футовый контейнер: затраты vs доходы",
            chart2: "Сравнение размеров рынков",
            chart2Subtitle: "Размер рынка кожи 8 африканских стран (2026)",
            chart3: "Маржа прибыли продуктов",
            chart3Subtitle: "Маржа прибыли по типам кожаных изделий",
            chart4: "Доля китайского импорта",
            chart4Subtitle: "Источники импорта кожи в Африку",
            costs: {
                leather: "Покупка кожи",
                shipping: "Стоимость доставки",
                duty: "Таможенные пошлины",
                local: "Местная логистика",
                revenue: "Ожидаемый доход"
            },
            countries: {
                nigeria: "Нигерия",
                southAfrica: "Южная Африка",
                kenya: "Кения",
                ethiopia: "Эфиопия",
                ghana: "Гана",
                tanzania: "Танзания",
                uganda: "Уганда",
                senegal: "Сенегал"
            },
            products: {
                sofa: "Диванная кожа",
                bag: "Сумочная кожа",
                garment: "Одёжная кожа",
                shoe: "Обувная кожа",
                auto: "Автомобильная кожа"
            },
            sources: {
                china: "Импорт из Китая",
                india: "Импорт из Индии",
                turkey: "Импорт из Турции",
                local: "Местное производство",
                other: "Прочие"
            }
        },
        
        // Partners Section
        partners: {
            title: "Роли трехсторонного партнерства",
            china: {
                name: "Китайский партнер",
                role: "Управление верхней частью цепочки поставок",
                responsibilities: "Основные обязанности:",
                tasks: [
                    "✓ Найти надежные кожевенные фабрики",
                    "✓ Контроль качества + проверка",
                    "✓ Ценовые переговоры (цель: ¥35-40/кв.м)",
                    "✓ Экспортная документация",
                    "✓ Надзор за загрузкой контейнеров"
                ]
            },
            father: {
                name: "Отец Джастиса",
                role: "Сеть 5-звездочных отелей + местный дистрибьюшн",
                advantages: "Основные преимущества:",
                tasks: [
                    "🏨 Выставочное пространство в 5-звездочном отеле",
                    "👔 База VIP-клиентов",
                    "🤝 Доверительная поддержка (отель=доверие)",
                    "📦 Складская и логистическая удобство",
                    "🎯 Координация местной таможни"
                ]
            },
            brother: {
                name: "Брат Джастиса",
                role: "Финансирование + координация + исполнение",
                keyRole: "Ключевая роль:",
                tasks: [
                    "💰 Предоставить стартовый капитал $52.700",
                    "🔗 Координировать китайского поставщика + африканскую дистрибуцию",
                    "📊 Управление денежным потоком",
                    "🚢 Отслеживать логистику контейнеров",
                    "⚖️ Управление распределением прибыли"
                ]
            },
            profitShare: "Доля прибыли"
        },
        
        // Timeline Section
        timeline: {
            title: "60-дневный план действий",
            phase1: "Фаза 1: Подготовка (дни 1-14)",
            phase2: "Фаза 2: Финансирование и логистика (дни 15-30)",
            phase3: "Фаза 3: Доставка и таможня (дни 31-45)",
            phase4: "Фаза 4: Продажи и инкассация (дни 46-60)",
            steps: {
                step1: "Китайский партнер изучает рынки кожи в Гуанчжоу/Шэньчжэнь, запрашивает образцы + отчеты о качестве",
                step2: "Отец Джастиса организует выставочный зал в отеле, связывается с VIP-клиентами",
                step3: "Собрать стартовый капитал $52.700",
                step4: "Заказать товары (8.500 кв.м кожи) + место в контейнере",
                step5: "Купить морскую страховку + подготовить экспортные документы",
                step6: "Морская перевозка (25-35 дней)",
                step7: "Портовое оформление, оплата таможенных пошлин (~$3.200)",
                step8: "Транспортировка на склад отеля отца Джастиса",
                step9: "Установить выставку кожи в холле отеля",
                step10: "Провести 'Выставку кожаных изделий', пригласить 10-15 оптовиков",
                step11: "Продать 60-70% товаров за 2-3 недели, собрать ~$90.000"
            },
            goal: "Цель:",
            result: "Результат:",
            goal1: "Завершить выбор поставщика + собрать предзаказы",
            result1: "Окупаемость на 60-й день, чистая прибыль $77.300"
        },
        
        // Footer
        footer: {
            copyright: "© 2026 Стратегический центр Justice Sue Owen. Все права защищены.",
            tagline: "Стратегический центр африканской кожаной торговли | Работает на рыночной разведке в реальном времени"
        }
    }
};

// Current language (default: English)
let currentLang = 'en';

// Get translation
function t(key) {
    const keys = key.split('.');
    let value = translations[currentLang];
    
    for (const k of keys) {
        value = value[k];
        if (!value) return key;
    }
    
    return value;
}

// Change language
function setLanguage(lang) {
    if (!translations[lang]) return;
    currentLang = lang;
    updatePageText();
    localStorage.setItem('preferredLanguage', lang);
    
    // Update active state
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-lang="${lang}"]`).classList.add('active');
}

// Update all text on page
function updatePageText() {
    // Header
    document.querySelector('.logo-text h1').textContent = t('title');
    document.querySelector('.logo-text p').textContent = t('subtitle');
    
    // Navigation
    document.querySelectorAll('.nav a').forEach((link, i) => {
        const keys = ['map', 'data', 'partners', 'timeline'];
        link.innerHTML = t(`nav.${keys[i]}`);
    });
    
    // Hero
    document.querySelector('.hero h2').textContent = t('hero.title');
    document.querySelector('.hero > p').textContent = t('hero.description');
    
    const statLabels = document.querySelectorAll('.stat-label');
    statLabels[0].textContent = t('hero.stats.investment');
    statLabels[1].textContent = t('hero.stats.roi');
    statLabels[2].textContent = t('hero.stats.period');
    statLabels[3].textContent = t('hero.stats.profit');
    
    // Sections
    document.querySelector('#map-section .section-title').textContent = t('map.title');
    document.querySelector('#data-section .section-title').textContent = t('data.title');
    document.querySelector('#partners-section .section-title').textContent = t('partners.title');
    document.querySelector('#timeline-section .section-title').textContent = t('timeline.title');
    
    // Map description
    document.querySelector('#map-section > p').textContent = t('map.description');
    
    // Chart titles
    const chartTitles = document.querySelectorAll('.chart-title');
    chartTitles[0].textContent = t('data.chart1');
    chartTitles[1].textContent = t('data.chart2');
    chartTitles[2].textContent = t('data.chart3');
    chartTitles[3].textContent = t('data.chart4');
    
    // Partners
    const partnerNames = document.querySelectorAll('.partner-name');
    partnerNames[0].textContent = t('partners.china.name');
    partnerNames[1].textContent = t('partners.father.name');
    partnerNames[2].textContent = t('partners.brother.name');
    
    const partnerRoles = document.querySelectorAll('.partner-role');
    partnerRoles[0].textContent = t('partners.china.role');
    partnerRoles[1].textContent = t('partners.father.role');
    partnerRoles[2].textContent = t('partners.brother.role');
    
    // Timeline
    const timelinePhases = document.querySelectorAll('.timeline-phase');
    timelinePhases[0].textContent = t('timeline.phase1');
    timelinePhases[1].textContent = t('timeline.phase2');
    timelinePhases[2].textContent = t('timeline.phase3');
    timelinePhases[3].textContent = t('timeline.phase4');
    
    // Footer
    document.querySelectorAll('.footer p')[0].textContent = t('footer.copyright');
    document.querySelectorAll('.footer p')[1].textContent = t('footer.tagline');
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    // Load saved language preference
    const savedLang = localStorage.getItem('preferredLanguage');
    if (savedLang && translations[savedLang]) {
        currentLang = savedLang;
        const activeBtn = document.querySelector(`[data-lang="${savedLang}"]`);
        if (activeBtn) {
            document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
            activeBtn.classList.add('active');
        }
    }
    
    updatePageText();
});

// Expose setLanguage to global scope for onclick handlers
window.setLanguage = setLanguage;
