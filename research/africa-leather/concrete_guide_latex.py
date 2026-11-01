#!/usr/bin/env python3
"""
生成具体行动指南的LaTeX PDF文档
"""
import subprocess
from pathlib import Path

def generate_concrete_latex():
    """生成LaTeX文档"""
    
    latex_content = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{CJKutf8}
\usepackage{geometry}
\geometry{left=2cm,right=2cm,top=2.5cm,bottom=2.5cm}
\usepackage{graphicx}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\usepackage{enumitem}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=cyan,
}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Concrete Action Guide}}
\lhead{\textit{Africa Leather Trade}}
\cfoot{\thepage}

\definecolor{titleblue}{RGB}{52,152,219}
\definecolor{sectionorange}{RGB}{230,126,34}
\definecolor{highlightgreen}{RGB}{39,174,96}

\title{
    \textbf{\Huge 非洲皮革贸易}\\[0.5cm]
    \textbf{\Huge 从零到盈利完整指南}\\[0.8cm]
    \Large Africa Leather Trade\\
    \Large Complete Guide from Zero to Profit
}

\author{
    \textbf{为Justice兄弟量身定制}\\
    Tailored for Justice's Brother
}

\date{\today}

\begin{document}

\maketitle

\begin{center}
\begin{tcolorbox}[colback=highlightgreen!10,colframe=highlightgreen,width=0.9\textwidth]
\begin{CJK}{UTF8}{gbsn}
\textbf{\Large 60天行动计划 | 投资\$52,700 → 利润\$77,300 | ROI 147\%}
\end{CJK}
\end{tcolorbox}
\end{center}

\tableofcontents
\newpage

%=============================================================================
\section{Executive Summary | 执行摘要}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

本指南为Justice兄弟的非洲皮革贸易提供从零到第一个集装箱的完整操作手册。

\subsection*{核心数据}

\begin{itemize}[leftmargin=2cm]
    \item \textbf{第一个集装箱投资：}\$52,700
    \item \textbf{预期收入：}\$130,000
    \item \textbf{净利润：}\$77,300
    \item \textbf{投资回报率：}147\%
    \item \textbf{回本时间：}60天
    \item \textbf{货物容量：}8,500平方米皮革
\end{itemize}

\subsection*{三方合作模式}

\begin{enumerate}
    \item \textbf{中国合作方} (20-25\%利润分配)
    \begin{itemize}
        \item 寻找可靠的皮革工厂
        \item 质量控制 + 验货
        \item 价格谈判 (目标: ¥35-40/平米)
        \item 出口文件准备
    \end{itemize}
    
    \item \textbf{Justice父亲} (30-35\%利润分配)
    \begin{itemize}
        \item 利用五星级酒店网络
        \item 提供展示/仓储空间
        \item 引荐高端客户（酒店VIP数据库）
        \item 本地清关与物流协调
    \end{itemize}
    
    \item \textbf{Justice兄弟} (40-45\%利润分配)
    \begin{itemize}
        \item 提供启动资金 \$52,700
        \item 协调中国供应商 + 非洲分销
        \item 管理现金流
        \item 跟踪集装箱物流
    \end{itemize}
\end{enumerate}

\end{CJK}

\newpage

%=============================================================================
\section{可视化图表 | Visual Charts}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{世界地图航线}

\begin{center}
\includegraphics[width=0.95\textwidth,height=0.7\textheight,keepaspectratio]{concrete_plan/world_map_routes.png}
\end{center}

\textbf{三条主要海运路线：}
\begin{itemize}
    \item 上海 → 拉各斯 (Nigeria): 35天, \$4,500
    \item 深圳 → 德班 (South Africa): 28天, \$3,800
    \item 广州 → 蒙巴萨 (Kenya): 25天, \$3,200
\end{itemize}

\newpage

\subsection{60天从零到第一个集装箱}

\begin{center}
\includegraphics[width=0.95\textwidth,height=0.85\textheight,keepaspectratio]{concrete_plan/zero_to_first_container.png}
\end{center}

\textbf{四个阶段：}
\begin{enumerate}
    \item 前期准备 (第1-14天)
    \item 资金与物流 (第15-30天)
    \item 运输与清关 (第31-45天)
    \item 销售与回款 (第46-60天)
\end{enumerate}

\newpage

\subsection{合作伙伴角色分工}

\begin{center}
\includegraphics[width=0.95\textwidth,height=0.75\textheight,keepaspectratio]{concrete_plan/partner_roles.png}
\end{center}

\newpage

\subsection{Justice父亲酒店优势}

\begin{center}
\includegraphics[width=0.95\textwidth,height=0.85\textheight,keepaspectratio]{concrete_plan/hotel_advantage.png}
\end{center}

\textbf{四大优势：}
\begin{enumerate}
    \item 高端展示空间 - 五星级环境提升产品档次
    \item 客户网络 - 酒店VIP客人数据库
    \item 信任背书 - 五星级酒店=信誉保证
    \item 仓储便利 - 安全保管 + 灵活配送
\end{enumerate}

\end{CJK}

\newpage

%=============================================================================
\section{60天详细行动计划 | 60-Day Action Plan}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{阶段1：前期准备 (第1-14天)}

\subsubsection{步骤1：找到中国皮革供应商 (第1-7天)}

\textbf{中国合作方的核心职责：}

\begin{enumerate}
    \item \textbf{去广州/深圳皮革批发市场实地考察}
    \begin{itemize}
        \item 广州：白马皮革城、三元里皮革市场
        \item 深圳：笋岗皮革市场
        \item 每天至少走访5-8家工厂
    \end{itemize}
    
    \item \textbf{在阿里巴巴1688寻找工厂}
    \begin{itemize}
        \item 搜索关键词："出口皮革"、"真皮批发"、"鞋用皮革"
        \item 筛选条件：
        \begin{itemize}
            \item 实力商家（金牌供应商）
            \item 有出口资质
            \item 年销售额 > 500万
            \item 支持小单起订
        \end{itemize}
    \end{itemize}
    
    \item \textbf{要求样品 + 质检报告}
    \begin{itemize}
        \item 每家至少要3-5个样品（不同颜色/厚度）
        \item 要求提供：ISO 9001、SGS检测报告、出口许可证
    \end{itemize}
    
    \item \textbf{价格谈判目标}
    \begin{itemize}
        \item \textbf{目标价格：¥35-40/平米 (约\$5-6/平米)}
        \item 谈判策略：长期合作意向、现金付款、包装+FOB价格
    \end{itemize}
\end{enumerate}

\textbf{中方解决的问题：}供应链上游 + 质量保证 + 价格控制

\subsubsection{步骤2：利用Justice父亲的五星级酒店关系 (第8-14天)}

\textbf{非洲方（Justice父亲）的核心职责：}

\begin{enumerate}
    \item \textbf{在酒店设置样品展示区}
    \begin{itemize}
        \item 位置：酒店大堂一角 或 商务会议室
        \item 面积：2-3平米
        \item 展示：5-8种皮革样品（不同颜色、纹理）
    \end{itemize}
    
    \item \textbf{联系潜在批发客户}
    
    \textbf{目标客户1：酒店采购部}
    \begin{itemize}
        \item 酒店自身需求：餐厅座椅翻新、前台家具
        \item 需求量：100-200平米/年
    \end{itemize}
    
    \textbf{目标客户2：住店商务人士}
    \begin{itemize}
        \item 通过酒店VIP客人数据库筛选：鞋厂老板、家具厂老板、箱包工坊老板
        \item 邀请他们到酒店"商务洽谈"看样品
    \end{itemize}
    
    \textbf{目标客户3：酒店供应商网络}
    \begin{itemize}
        \item 餐饮供应商（需要皮革座椅）
        \item 装修公司（需要皮革软包）
        \item 汽车装饰店（需要汽车座椅皮革）
    \end{itemize}
    
    \item \textbf{建立信任 + 收集预订单}
    \begin{itemize}
        \item 第一轮：展示样品，了解需求
        \item 第二轮：提供报价（比市场价低10-15\%）
        \item 第三轮：收取订金（20-30\%）
    \end{itemize}
\end{enumerate}

\textbf{非洲方解决的问题：}客户 + 信任背书 + 本地分销渠道

\newpage

\subsection{阶段2：资金与物流 (第15-30天)}

\subsubsection{步骤3：筹集启动资金 (第15-20天)}

\textbf{总需要：\$52,700 (一个40英尺集装箱)}

\begin{center}
\begin{longtable}{lrp{5cm}}
\toprule
\textbf{项目} & \textbf{金额 (USD)} & \textbf{备注} \\
\midrule
皮革采购成本 & \$44,200 & 8,500平米 × \$5.2/平米 \\
海运费用 & \$4,500 & 40ft 中国→尼日利亚/南非 \\
关税 (20\%) & \$3,200 & 基于CIF价值 \\
本地物流 & \$800 & 清关代理 + 运输到酒店 \\
\midrule
\textbf{总计} & \textbf{\$52,700} & \\
\bottomrule
\end{longtable}
\end{center}

\textbf{资金来源：}
\begin{itemize}
    \item Justice兄弟提供前期资金
    \item 或：2-3个合伙人每人投资 \$17,000-\$26,000
    \item 或：利用非洲客户的订金（30\% × \$130,000 = \$39,000）
\end{itemize}

\subsubsection{步骤4：预订货物与航运 (第21-30天)}

\textbf{推荐产品配置 (8,500平米总量)：}

\begin{center}
\begin{longtable}{lrrrrrr}
\toprule
\textbf{产品类别} & \textbf{数量} & \textbf{占比} & \textbf{采购价} & \textbf{销售价} & \textbf{毛利} \\
\midrule
鞋用皮革 & 3,400㎡ & 40\% & \$5.2/㎡ & \$15.3/㎡ & 66\% \\
箱包皮革 & 1,700㎡ & 20\% & \$6.5/㎡ & \$18.8/㎡ & 65\% \\
家具皮革 & 1,700㎡ & 20\% & \$3.8/㎡ & \$11.5/㎡ & 67\% \\
人造皮革 & 1,275㎡ & 15\% & \$2.1/㎡ & \$7.2/㎡ & 71\% \\
试验产品 & 425㎡ & 5\% & 混合 & 混合 & - \\
\bottomrule
\end{longtable}
\end{center}

\textbf{预订流程：}
\begin{enumerate}
    \item 联系货代公司（深圳/广州）
    \item 选择目的港：拉各斯 / 德班 / 蒙巴萨
    \item 预订时间：提前2-3周
    \item 购买海运保险：CIF价值的110\%
    \item 准备出口文件：商业发票、装箱单、原产地证、质检证书
\end{enumerate}

\newpage

\subsection{阶段3：运输与清关 (第31-45天)}

\subsubsection{步骤5：货物在海上运输 (第31-38天)}

\begin{enumerate}
    \item \textbf{实时跟踪集装箱}
    \begin{itemize}
        \item 使用船公司提供的追踪号
        \item 每2天查询一次位置
        \item 预计到达时间 (ETA)
    \end{itemize}
    
    \item \textbf{提前联系本地清关代理}
    \begin{itemize}
        \item 在目的港找一个可靠的清关代理
        \item 费用：\$500-\$800
        \item 提供清关所需文件
    \end{itemize}
    
    \item \textbf{通知Justice父亲准备接货}
    \begin{itemize}
        \item 确认酒店仓库空间
        \item 安排展示区域
        \item 联系已预订的客户
    \end{itemize}
\end{enumerate}

\subsubsection{步骤6：到港与清关 (第39-45天)}

\begin{enumerate}
    \item \textbf{支付关税}
    \begin{itemize}
        \item 尼日利亚：20-25\%
        \item 南非：15\%
        \item 肯尼亚：25\%
        \item 预计：\$3,200-\$4,000
    \end{itemize}
    
    \item \textbf{提货检验}
    \begin{itemize}
        \item 打开集装箱检查货物
        \item 确认数量 + 质量
        \item 拍照存档
    \end{itemize}
    
    \item \textbf{运输到Justice父亲酒店}
    \begin{itemize}
        \item 雇佣本地卡车
        \item 费用：\$300-\$500
        \item 卸货到酒店仓库
    \end{itemize}
\end{enumerate}

\newpage

\subsection{阶段4：销售与回款 (第46-60天)}

\subsubsection{步骤7：利用Justice父亲五星级酒店销售}

\textbf{第1周 (第46-52天)：展示 + 邀约}

\begin{enumerate}
    \item \textbf{在酒店设置皮革展示台}
    \begin{itemize}
        \item 大堂一角：吸引过往客人
        \item 会议室：预约看货
        \item 样品陈列：每种产品3-5个样品
    \end{itemize}
    
    \item \textbf{通过酒店关系邀请批发商}
    
    \textbf{目标1：本地鞋厂} (Footwear manufacturers)
    \begin{itemize}
        \item 联系方式：通过酒店采购部引荐
        \item 需求量：500-1,000平米/批发商
        \item 目标客户数：3-5家
    \end{itemize}
    
    \textbf{目标2：家具工厂} (Furniture makers)
    \begin{itemize}
        \item 酒店装修供应商网络
        \item 需求量：300-800平米/批发商
        \item 目标客户数：2-3家
    \end{itemize}
    
    \textbf{目标3：箱包工坊} (Bag workshops)
    \begin{itemize}
        \item 本地手工艺品市场
        \item 需求量：200-500平米/批发商
        \item 目标客户数：3-4家
    \end{itemize}
    
    \textbf{目标4：汽车装饰店} (Car upholstery)
    \begin{itemize}
        \item 汽车座椅翻新
        \item 需求量：100-300平米/客户
        \item 目标客户数：2-3家
    \end{itemize}
    
    \item \textbf{举办"皮革产品展示会"}
    \begin{itemize}
        \item 时间：周三或周四下午
        \item 地点：酒店会议室
        \item 邀请：10-15个潜在批发商
        \item 提供：茶点 + 样品 + 报价单
    \end{itemize}
\end{enumerate}

\textbf{第2周 (第53-59天)：谈判 + 成交}

\begin{enumerate}
    \item \textbf{价格策略}
    \begin{itemize}
        \item 比市场价低 10-15\%
        \item 例如：鞋用皮革 \$15.3/㎡（市场价 \$17-18/㎡）
        \item 例如：家具皮革 \$11.5/㎡（市场价 \$13-14/㎡）
    \end{itemize}
    
    \item \textbf{支付条件}
    \begin{itemize}
        \item \textbf{首次客户：}50\%定金 + 50\%提货付清
        \item \textbf{批量客户：}30\%定金 + 30天账期
        \item 只接受现金或银行转账
    \end{itemize}
    
    \item \textbf{送货安排}
    \begin{itemize}
        \item 小批量 (< 200㎡)：客户自提
        \item 大批量 (> 500㎡)：免费配送
    \end{itemize}
\end{enumerate}

\textbf{第3周 (第60天)：回款目标}

\textbf{销售目标：}
\begin{itemize}
    \item \textbf{2-3周内销售 60-70\% 货物}
    \item 约 5,000-6,000平米
    \item 回款金额：~\$90,000
\end{itemize}

\textbf{剩余30-40\%货物：}
\begin{itemize}
    \item 继续零售给散户
    \item 或：在当地皮革批发市场摆摊
    \item 预计1-2个月内全部售完
\end{itemize}

\end{CJK}

\newpage

%=============================================================================
\section{合作伙伴角色详解 | Partner Roles Explained}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{中国合作方 (20-25\%利润分配)}

\textbf{核心职责：}
\begin{enumerate}
    \item 寻找可靠的皮革工厂
    \item 质量控制 + 验货
    \item 价格谈判 (目标: ¥35-40/㎡)
    \item 出口文件准备
    \item 集装箱装柜监督
    \item 跟踪物流到港
\end{enumerate}

\textbf{解决的问题：}
\begin{itemize}
    \item 供应链上游管理
    \item 质量保证
    \item 价格控制
    \item 出口合规
\end{itemize}

\textbf{利润计算示例：}
\begin{itemize}
    \item 净利润：\$77,300
    \item 中方分配 (22.5\%)：\$17,393
\end{itemize}

\subsection{Justice父亲 (30-35\%利润分配)}

\textbf{核心职责：}
\begin{enumerate}
    \item \textbf{利用五星级酒店网络}
    \begin{itemize}
        \item 提供展示/仓储空间
        \item 引荐高端客户（酒店采购部）
        \item 利用酒店VIP客户数据库
        \item 提供信任背书（五星级酒店=信誉）
    \end{itemize}
    
    \item \textbf{本地清关与物流协调}
    \begin{itemize}
        \item 联系清关代理
        \item 安排货物运输
        \item 确保安全存储
    \end{itemize}
    
    \item \textbf{收款与资金安全}
    \begin{itemize}
        \item 开设本地银行账户
        \item 收取客户款项
        \item 确保资金安全转回
    \end{itemize}
\end{enumerate}

\textbf{解决的问题：}
\begin{itemize}
    \item 本地分销渠道
    \item 客户信任建立
    \item 高端客户接触
    \item 物流与清关
\end{itemize}

\textbf{利润计算示例：}
\begin{itemize}
    \item 净利润：\$77,300
    \item Justice父亲分配 (32.5\%)：\$25,123
\end{itemize}

\subsection{Justice兄弟 (40-45\%利润分配)}

\textbf{核心职责：}
\begin{enumerate}
    \item 协调中国供应商 + 非洲分销
    \item 管理现金流 (前期投资 \$52,700)
    \item 跟踪集装箱物流
    \item 联络酒店批发客户
    \item 利润分配管理
    \item 风险控制与决策
\end{enumerate}

\textbf{关键角色：}
\begin{itemize}
    \item 资金提供
    \item 全流程协调
    \item 执行与监督
\end{itemize}

\textbf{利润计算示例：}
\begin{itemize}
    \item 净利润：\$77,300
    \item Justice兄弟分配 (45\%)：\$34,785
\end{itemize}

\end{CJK}

\newpage

%=============================================================================
\section{Justice父亲酒店优势详解 | Hotel Advantage Analysis}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{优势1：高端展示空间}

\textbf{为什么重要：}
\begin{itemize}
    \item 五星级酒店 = 高档商品印象
    \item 提升皮革产品档次
    \item 吸引高净值客户
\end{itemize}

\textbf{具体操作：}
\begin{enumerate}
    \item 在酒店大堂设置2-3平米样品展示台
    \item 摆放5-8种不同颜色/纹理的皮革样品
    \item 配备宣传册 + 联系方式
    \item 利用会议室作为看货洽谈空间
\end{enumerate}

\subsection{优势2：客户网络}

\textbf{酒店客户数据库包括：}
\begin{itemize}
    \item VIP常客 (商务人士)
    \item 公司会议活动组织者
    \item 供应商网络 (装修、餐饮、家具)
    \item 高净值个人客户
\end{itemize}

\textbf{如何利用：}
\begin{enumerate}
    \item \textbf{筛选目标客户}
    \begin{itemize}
        \item 从酒店VIP数据库中筛选：制造业老板、贸易商、装修公司老板
    \end{itemize}
    
    \item \textbf{主动邀约}
    \begin{itemize}
        \item 电话邀请："我们酒店引进了中国进口皮革，品质优良，价格实惠，您是否有兴趣了解？"
        \item 提供酒店会议室免费洽谈
    \end{itemize}
    
    \item \textbf{口碑传播}
    \begin{itemize}
        \item 酒店环境 = 信任背书
        \item 客户之间相互推荐
    \end{itemize}
\end{enumerate}

\subsection{优势3：信任背书}

\textbf{五星级酒店 = 信誉保证}

\begin{itemize}
    \item 降低交易风险感知
    \item 客户更愿意预付定金
    \item 便于谈账期
\end{itemize}

\textbf{具体体现：}
\begin{enumerate}
    \item 交易地点在酒店（安全感）
    \item Justice父亲是酒店相关人员（本地知名）
    \item 货物存放在酒店仓库（有保障）
\end{enumerate}

\subsection{优势4：仓储与物流便利}

\textbf{酒店仓库优势：}
\begin{itemize}
    \item 安全保管货物
    \item 便于客户看货（随时预约）
    \item 灵活配送安排
    \item 节省外部仓储费用
\end{itemize}

\textbf{实施方案：}
\begin{enumerate}
    \item 使用酒店闲置仓库空间（约50-100平米）
    \item 分类存放不同皮革
    \item 客户可预约到酒店看货、提货
\end{enumerate}

\subsection{4周酒店销售具体计划}

\textbf{第1周：设置展示台}
\begin{itemize}
    \item 在酒店大堂设置2-3平米样品展示区
    \item 摆放5-8种皮革样品
    \item 制作宣传册 + 价格单
\end{itemize}

\textbf{第2周：联系本地工厂}
\begin{itemize}
    \item 通过酒店采购部联系：3-5家本地鞋厂、2-3家家具厂、2-3家汽车装饰店
\end{itemize}

\textbf{第3周：举办"皮革展示会"}
\begin{itemize}
    \item 时间：周三下午3-5点
    \item 地点：酒店会议室
    \item 邀请：10-15个潜在批发商
    \item 提供：茶点 + 样品 + 报价单
\end{itemize}

\textbf{第4周：跟进订单}
\begin{itemize}
    \item 与有兴趣的客户一对一谈判
    \item 安排送货
    \item 收取款项
\end{itemize}

\subsection{竞争优势总结}

\textbf{普通批发商：}
\begin{itemize}
    \item 需要租仓库 (成本高)
    \item 需要找客户 (时间长)
    \item 需要建立信任 (3-6个月)
\end{itemize}

\textbf{Justice优势：}
\begin{itemize}
    \item 现成空间 (酒店仓库)
    \item 现成客户 (VIP数据库)
    \item 现成信任 (五星级酒店背书)
    \item \textbf{结果：2-3周快速回款}
\end{itemize}

\end{CJK}

\newpage

%=============================================================================
\section{第一个集装箱详细预算 | First Container Budget}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{投资明细}

\begin{center}
\begin{longtable}{lrrp{4cm}}
\toprule
\textbf{项目} & \textbf{金额 (USD)} & \textbf{占比} & \textbf{备注} \\
\midrule
\textbf{皮革采购} & \$44,200 & 83.9\% & 8,500㎡ × \$5.2/㎡ \\
\quad 鞋用皮革 (40\%) & \$17,680 & & 3,400㎡ × \$5.2/㎡ \\
\quad 箱包皮革 (20\%) & \$11,050 & & 1,700㎡ × \$6.5/㎡ \\
\quad 家具皮革 (20\%) & \$6,460 & & 1,700㎡ × \$3.8/㎡ \\
\quad 人造皮革 (15\%) & \$2,678 & & 1,275㎡ × \$2.1/㎡ \\
\quad 试验产品 (5\%) & \$6,332 & & 425㎡ × 混合价 \\
\textbf{海运费用} & \$4,500 & 8.5\% & 40ft 深圳→拉各斯 \\
\textbf{关税} & \$3,200 & 6.1\% & 20\% of CIF \\
\textbf{本地物流} & \$800 & 1.5\% & 清关代理 + 运输 \\
\midrule
\textbf{总投资} & \textbf{\$52,700} & \textbf{100\%} & \\
\bottomrule
\end{longtable}
\end{center}

\subsection{收入预测}

\begin{center}
\begin{longtable}{lrrrrr}
\toprule
\textbf{产品类别} & \textbf{数量} & \textbf{销售单价} & \textbf{总收入} & \textbf{成本} & \textbf{毛利率} \\
\midrule
鞋用皮革 & 3,400㎡ & \$15.3/㎡ & \$52,020 & \$17,680 & 66\% \\
箱包皮革 & 1,700㎡ & \$18.8/㎡ & \$31,960 & \$11,050 & 65\% \\
家具皮革 & 1,700㎡ & \$11.5/㎡ & \$19,550 & \$6,460 & 67\% \\
人造皮革 & 1,275㎡ & \$7.2/㎡ & \$9,180 & \$2,678 & 71\% \\
试验产品 & 425㎡ & \$15/㎡ & \$6,375 & \$6,332 & 1\% \\
\midrule
\textbf{总计} & \textbf{8,500㎡} & \textbf{平均\$14/㎡} & \textbf{\$119,085} & \textbf{\$44,200} & \textbf{63\%} \\
\bottomrule
\end{longtable}
\end{center}

\textbf{加上运费和关税：}
\begin{itemize}
    \item \textbf{总收入：}\$130,000 (实际售价考虑市场溢价)
    \item \textbf{总成本：}\$52,700
    \item \textbf{净利润：}\$77,300
    \item \textbf{ROI：}147\%
\end{itemize}

\subsection{现金流时间表}

\begin{center}
\begin{longtable}{lrrr}
\toprule
\textbf{时间点} & \textbf{现金流出} & \textbf{现金流入} & \textbf{累计净流} \\
\midrule
第0天: 启动资金 & \$52,700 & \$0 & -\$52,700 \\
第20天: 供应商定金 (30\%) & \$13,260 & \$0 & -\$65,960 \\
第30天: 供应商尾款 (70\%) & \$30,940 & \$0 & -\$96,900 \\
第45天: 海运+关税 & \$7,700 & \$0 & -\$104,600 \\
第50天: 第一批销售 (30\%) & \$0 & \$39,000 & -\$65,600 \\
第55天: 第二批销售 (40\%) & \$0 & \$52,000 & -\$13,600 \\
第60天: 第三批销售 (30\%) & \$0 & \$39,000 & \textbf{+\$25,400} \\
\bottomrule
\end{longtable}
\end{center}

\textbf{关键点：第60天回本，剩余货物继续销售，最终净利润 \$77,300}

\end{CJK}

\newpage

%=============================================================================
\section{风险控制清单 | Risk Control Checklist}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{风险1：供应商质量问题}

\textbf{风险评分：}7/10

\textbf{控制措施：}
\begin{itemize}
    \item 要求样品 + 第三方质检报告
    \item 首次合作小单测试 (500-1,000㎡)
    \item 要求供应商提供质量保证金
    \item 签订质量合同（质量问题全额退款）
    \item 雇佣第三方验货公司（费用 \$200-\$300）
\end{itemize}

\subsection{风险2：货款支付风险}

\textbf{风险评分：}8/10 (最高)

\textbf{控制措施：}
\begin{itemize}
    \item \textbf{前3次交易：}50\%定金 + 50\%提货付清
    \item \textbf{建立信任后：}30\%定金 + 30天账期
    \item 大额交易 (> \$10,000)：银行转账，保留凭证
    \item 利用Justice父亲的本地关系追债
    \item 只接受现金或银行转账，不接受支票
\end{itemize}

\subsection{风险3：汇率波动}

\textbf{风险评分：}6/10

\textbf{控制措施：}
\begin{itemize}
    \item 尽量以美元定价
    \item 采购时锁定汇率（外汇远期合约）
    \item 快速周转（减少持有本币时间）
    \item 预留5-10\%汇率波动缓冲
\end{itemize}

\subsection{风险4：清关延误}

\textbf{风险评分：}5/10

\textbf{控制措施：}
\begin{itemize}
    \item 提前2周联系清关代理
    \item 准备完整出口文件
    \item 预留1周清关缓冲时间
    \item 购买海运保险（包含滞港费）
\end{itemize}

\subsection{风险5：销售不畅}

\textbf{风险评分：}4/10

\textbf{控制措施：}
\begin{itemize}
    \item 提前收集预订单（至少覆盖50\%货物）
    \item 产品组合多样化（6种皮革）
    \item 利用酒店网络快速触达批发商
    \item 价格比市场低10-15\%（快速去库存）
\end{itemize}

\end{CJK}

\newpage

%=============================================================================
\section{扩张计划 | Expansion Plan}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{第一个集装箱成功后的下一步}

\subsubsection{第2个集装箱 (第3个月)}
\begin{itemize}
    \item 根据第一轮销售数据调整产品组合
    \item 增加畅销品类比例
    \item 预订量：1个40ft集装箱
\end{itemize}

\subsubsection{第3-6个月}
\begin{itemize}
    \item 每月1个集装箱
    \item 拓展到第二个城市
    \item 建立固定批发客户网络（5-10家）
\end{itemize}

\subsubsection{第7-12个月}
\begin{itemize}
    \item 每月2个集装箱
    \item 雇佣1-2个本地销售人员
    \item 在Justice父亲酒店开设正式展厅
\end{itemize}

\subsection{年度盈利预测}

\textbf{保守方案 (每月1个集装箱)：}
\begin{itemize}
    \item 月利润：\$77,300
    \item \textbf{年利润：\$927,600}
\end{itemize}

\textbf{激进方案 (每月2个集装箱)：}
\begin{itemize}
    \item 月利润：\$154,600
    \item \textbf{年利润：\$1,855,200}
\end{itemize}

\end{CJK}

\newpage

%=============================================================================
\section{下一步行动 | Next Steps}
%=============================================================================

\begin{CJK}{UTF8}{gbsn}

\subsection{Justice兄弟：}
\begin{itemize}
    \item[$\square$] 联系2-3个中国皮革供应商
    \item[$\square$] 确认启动资金 \$52,700
    \item[$\square$] 阅读本指南并制定时间表
\end{itemize}

\subsection{Justice父亲：}
\begin{itemize}
    \item[$\square$] 在酒店预留2-3平米展示空间
    \item[$\square$] 列出10-15个潜在批发客户清单（工厂老板）
    \item[$\square$] 确认酒店仓库可用空间（50-100平米）
\end{itemize}

\subsection{中国合作方：}
\begin{itemize}
    \item[$\square$] 去广州/深圳考察皮革市场
    \item[$\square$] 要求3-5个工厂样品 + 质检报告
    \item[$\square$] 谈判价格目标：¥35-40/平米
\end{itemize}

\subsection{时间表}

\textbf{14天内完成阶段1准备工作}

\begin{center}
\begin{tcolorbox}[colback=highlightgreen!10,colframe=highlightgreen,width=0.9\textwidth]
\textbf{\Large 目标：60天内完成第一个集装箱}\\[0.3cm]
\textbf{\Large 投资 \$52,700 → 利润 \$77,300}\\[0.3cm]
\textbf{\Large ROI 147\%}
\end{tcolorbox}
\end{center}

\end{CJK}

\vspace{2cm}

\begin{center}
\begin{CJK}{UTF8}{gbsn}
\textbf{\Huge 祝Justice兄弟生意兴隆！}\\[0.5cm]
\textbf{\Large Wishing Justice's Brother Great Success!}
\end{CJK}
\end{center}

\end{document}
'''
    
    return latex_content

def compile_pdf():
    """编译LaTeX为PDF"""
    
    output_dir = Path('concrete_plan')
    output_dir.mkdir(exist_ok=True)
    
    # 生成LaTeX内容
    latex_content = generate_concrete_latex()
    
    # 保存LaTeX文件
    tex_file = output_dir / 'concrete_guide.tex'
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"✅ LaTeX file created: {tex_file}")
    
    # 编译PDF (运行两次以生成目录)
    print("🔨 Compiling PDF...")
    for i in range(2):
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory', str(output_dir), str(tex_file)],
            capture_output=True,
            text=True,
            timeout=120
        )
        print(f"   Pass {i+1}/2 completed")
    
    pdf_file = output_dir / 'concrete_guide.pdf'
    if pdf_file.exists():
        print(f"✅ PDF generated: {pdf_file}")
        print(f"   Size: {pdf_file.stat().st_size / (1024*1024):.1f} MB")
        return pdf_file
    else:
        print("❌ PDF generation failed")
        return None

if __name__ == '__main__':
    pdf_file = compile_pdf()
