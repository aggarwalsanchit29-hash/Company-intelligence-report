"""
sectors.py
----------
Sector configurations, KPI benchmarks, and strategic context
for Banking, Healthcare, Retail, and Energy sectors.
"""

SECTORS = {
    "Banking & Financial Services": {
        "icon": "🏦",
        "color": "#1f6feb",
        "description": "Retail, investment & digital banking intelligence",
        "dimensions": [
            {"icon": "💰", "name": "Capital Strength", "desc": "CET1, leverage ratios"},
            {
                "icon": "⚡",
                "name": "Digital Maturity",
                "desc": "Digital adoption & NPS",
            },
            {"icon": "📉", "name": "Cost Efficiency", "desc": "Cost-to-income ratio"},
            {"icon": "🔒", "name": "Risk Profile", "desc": "NPL, provisions coverage"},
        ],
    },
    "Healthcare": {
        "icon": "🏥",
        "color": "#2ea043",
        "description": "NHS, private healthcare & MedTech analysis",
        "dimensions": [
            {"icon": "🛏️", "name": "Capacity", "desc": "Bed occupancy & throughput"},
            {"icon": "⏱️", "name": "Access", "desc": "Wait times & RTT"},
            {"icon": "😊", "name": "Quality", "desc": "Patient satisfaction & CQC"},
            {"icon": "💷", "name": "Finance", "desc": "Cost per episode & deficit"},
        ],
    },
    "Retail & FMCG": {
        "icon": "🛒",
        "color": "#e3b341",
        "description": "Grocery, fashion & consumer goods intelligence",
        "dimensions": [
            {
                "icon": "📦",
                "name": "Availability",
                "desc": "In-stock & shrinkage rates",
            },
            {"icon": "🛍️", "name": "Customer", "desc": "Basket size & conversion"},
            {"icon": "🏪", "name": "Footprint", "desc": "Revenue per sq ft"},
            {"icon": "🌍", "name": "Omnichannel", "desc": "Online penetration %"},
        ],
    },
    "Energy & Utilities": {
        "icon": "⚡",
        "color": "#f78166",
        "description": "Oil & gas, renewables & utilities intelligence",
        "dimensions": [
            {"icon": "🌱", "name": "Net Zero", "desc": "Carbon intensity & targets"},
            {"icon": "⚙️", "name": "Operations", "desc": "Plant efficiency & uptime"},
            {"icon": "💹", "name": "Economics", "desc": "EBITDA & capex allocation"},
            {"icon": "🔋", "name": "Transition", "desc": "Renewables mix & investment"},
        ],
    },
}


def get_sector_kpis(sector: str) -> list:
    kpis = {
        "Banking & Financial Services": [
            {
                "name": "CET1 Capital Ratio",
                "benchmark": "13-15%",
                "trend": "up",
                "description": "Core equity tier 1 capital as % of risk-weighted assets",
            },
            {
                "name": "Cost-to-Income Ratio",
                "benchmark": "50-60%",
                "trend": "down",
                "description": "Operating costs as % of operating income — lower is better",
            },
            {
                "name": "Return on Equity",
                "benchmark": "10-15%",
                "trend": "up",
                "description": "Net profit as % of shareholder equity",
            },
            {
                "name": "Net Interest Margin",
                "benchmark": "2.0-3.5%",
                "trend": "neutral",
                "description": "Difference between lending and deposit rates",
            },
            {
                "name": "Non-Performing Loans",
                "benchmark": "<2%",
                "trend": "down",
                "description": "Loans at risk of default as % of total loan book",
            },
            {
                "name": "Digital Active Users",
                "benchmark": "60-75%",
                "trend": "up",
                "description": "% of customers using digital channels monthly",
            },
            {
                "name": "Customer NPS",
                "benchmark": "+30 to +50",
                "trend": "up",
                "description": "Net Promoter Score — likelihood to recommend",
            },
            {
                "name": "Loan-to-Deposit Ratio",
                "benchmark": "70-90%",
                "trend": "neutral",
                "description": "Total loans as % of total deposits",
            },
            {
                "name": "Tier 1 Leverage Ratio",
                "benchmark": ">4%",
                "trend": "up",
                "description": "Tier 1 capital as % of total exposure",
            },
        ],
        "Healthcare": [
            {
                "name": "Bed Occupancy Rate",
                "benchmark": "85-90%",
                "trend": "up",
                "description": "% of available beds occupied — above 85% creates pressure",
            },
            {
                "name": "RTT 18-Week Standard",
                "benchmark": ">92%",
                "trend": "down",
                "description": "% of patients treated within 18 weeks of referral",
            },
            {
                "name": "A&E 4-Hour Standard",
                "benchmark": ">95%",
                "trend": "down",
                "description": "% of A&E patients seen within 4 hours",
            },
            {
                "name": "Patient Satisfaction",
                "benchmark": "85-90%",
                "trend": "up",
                "description": "% of patients rating care as good or excellent",
            },
            {
                "name": "Cost Per Episode",
                "benchmark": "£2,500-£4,000",
                "trend": "neutral",
                "description": "Average cost per inpatient episode",
            },
            {
                "name": "Staff Vacancy Rate",
                "benchmark": "<8%",
                "trend": "down",
                "description": "% of funded posts currently unfilled",
            },
            {
                "name": "Hospital Acquired Infections",
                "benchmark": "<0.5%",
                "trend": "down",
                "description": "Infections acquired during hospital stay per 1,000 bed days",
            },
            {
                "name": "Day Case Rate",
                "benchmark": ">85%",
                "trend": "up",
                "description": "% of elective procedures done as day cases",
            },
            {
                "name": "EBITDA Margin",
                "benchmark": "2-5%",
                "trend": "neutral",
                "description": "Operating surplus as % of total income",
            },
        ],
        "Retail & FMCG": [
            {
                "name": "Like-for-Like Sales Growth",
                "benchmark": "2-5%",
                "trend": "up",
                "description": "Sales growth from existing stores/channels year-on-year",
            },
            {
                "name": "Gross Margin",
                "benchmark": "25-40%",
                "trend": "neutral",
                "description": "Revenue minus cost of goods sold as % of revenue",
            },
            {
                "name": "Revenue per Sq Ft",
                "benchmark": "£500-£1,200",
                "trend": "up",
                "description": "Annual revenue generated per square foot of retail space",
            },
            {
                "name": "Online Penetration",
                "benchmark": "25-40%",
                "trend": "up",
                "description": "% of total sales through digital/online channels",
            },
            {
                "name": "Basket Size",
                "benchmark": "£20-£60",
                "trend": "up",
                "description": "Average transaction value per customer visit",
            },
            {
                "name": "Inventory Shrinkage",
                "benchmark": "<1.5%",
                "trend": "down",
                "description": "Stock losses due to theft, damage or admin error",
            },
            {
                "name": "Customer NPS",
                "benchmark": "+40 to +60",
                "trend": "up",
                "description": "Net Promoter Score across all channels",
            },
            {
                "name": "In-Stock Rate",
                "benchmark": ">97%",
                "trend": "up",
                "description": "% of SKUs available when customers want to buy",
            },
            {
                "name": "EBITDA Margin",
                "benchmark": "6-12%",
                "trend": "neutral",
                "description": "Earnings before interest, tax, depreciation & amortisation",
            },
        ],
        "Energy & Utilities": [
            {
                "name": "Carbon Intensity",
                "benchmark": "<50 gCO2/kWh",
                "trend": "down",
                "description": "Grams of CO2 emitted per kilowatt-hour of energy produced",
            },
            {
                "name": "Renewables Mix",
                "benchmark": "30-60%",
                "trend": "up",
                "description": "% of total energy generation from renewable sources",
            },
            {
                "name": "Plant Availability",
                "benchmark": ">90%",
                "trend": "up",
                "description": "% of time generation assets are available to operate",
            },
            {
                "name": "EBITDA Margin",
                "benchmark": "20-35%",
                "trend": "neutral",
                "description": "Operating earnings as % of revenue",
            },
            {
                "name": "Capex / Revenue",
                "benchmark": "15-25%",
                "trend": "up",
                "description": "Capital expenditure as % of revenue — higher = more investment",
            },
            {
                "name": "Customer Churn Rate",
                "benchmark": "<15%",
                "trend": "down",
                "description": "% of customers switching supplier annually",
            },
            {
                "name": "Network Reliability",
                "benchmark": ">99.9%",
                "trend": "up",
                "description": "% uptime of distribution network",
            },
            {
                "name": "Scope 1 & 2 Emissions",
                "benchmark": "Net Zero by 2050",
                "trend": "down",
                "description": "Direct and indirect greenhouse gas emissions",
            },
            {
                "name": "Return on Capital",
                "benchmark": "8-12%",
                "trend": "up",
                "description": "Returns generated relative to capital invested",
            },
        ],
    }
    return kpis.get(sector, [])


def get_sector_context(sector: str) -> str:
    contexts = {
        "Banking & Financial Services": """
        The global banking sector is navigating a complex environment shaped by higher-for-longer interest rates,
        accelerating digital transformation, and intensifying regulatory pressure. Key strategic priorities include
        core banking modernisation, open banking monetisation, AI-driven personalisation, and ESG integration.
        Challenger banks and fintechs continue to disrupt traditional business models, forcing incumbents to
        rethink their operating models, distribution strategies, and cost structures. The shift to digital-first
        banking, embedded finance, and real-time payments is reshaping how institutions compete for customer
        relationships and fee income.
        """,
        "Healthcare": """
        The healthcare sector faces a dual challenge of rising demand and constrained resources. In the UK,
        the NHS is managing record waiting lists, workforce shortages, and an ageing population, while pursuing
        its Long Term Plan commitments around digital transformation, prevention, and integrated care.
        Privately, healthcare providers are investing in digital health, telehealth, and AI-assisted diagnostics
        to improve access and outcomes. The shift from acute, episodic care to preventative, community-based
        models is a defining strategic theme. Value-based care, interoperability, and data-driven clinical
        decision-making are central to the sector's transformation agenda.
        """,
        "Retail & FMCG": """
        The retail sector is being reshaped by structural shifts in consumer behaviour, channel fragmentation,
        and supply chain volatility. Omnichannel integration, personalisation at scale, and sustainability
        credentials are table-stakes for competitive differentiation. The rise of quick commerce, social
        commerce, and retail media is creating new revenue streams and customer touchpoints. Cost pressures
        from inflation, energy costs, and labour are squeezing margins, forcing retailers to accelerate
        automation and operational efficiency programmes. Private label growth, loyalty monetisation, and
        data-driven merchandising are key levers for margin defence and customer retention.
        """,
        "Energy & Utilities": """
        The energy sector is undergoing its most significant structural transformation in a century, driven
        by the net zero imperative, energy security concerns, and the falling cost of renewables. Incumbent
        utilities and oil majors face a strategic dilemma: managing profitable legacy assets while allocating
        capital to low-carbon growth. The growth of distributed energy resources, battery storage, and smart
        grids is decentralising the sector. Customer expectations around green tariffs, EV charging, and
        smart home integration are reshaping the retail energy proposition. Regulatory frameworks, carbon
        pricing, and government policy remain critical variables shaping investment decisions and competitive
        dynamics.
        """,
    }
    return contexts.get(sector, "")
