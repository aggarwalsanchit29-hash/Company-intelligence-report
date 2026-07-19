"""
Company Intelligence Dashboard
--------------------------------
Generates AI-powered company intelligence reports across
Banking, Healthcare, Retail, and Energy sectors.

Run: streamlit run app.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from sectors import SECTORS, get_sector_kpis, get_sector_context
from prompts import generate_company_report
import time

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Company Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS Styling ───────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');

    /* Global */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main background */
    .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #161b22 0%, #0d1117 100%);
        border-right: 1px solid #30363d;
    }

    [data-testid="stSidebar"] * {
        color: #e6edf3 !important;
    }

    /* Hero header */
    .hero {
        background: linear-gradient(135deg, #161b22 0%, #1c2128 100%);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 2rem 2.5rem;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }

    .hero::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #2ea043, #1f6feb, #8957e5);
    }

    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #e6edf3;
        margin: 0 0 0.5rem 0;
    }

    .hero p {
        color: #8b949e;
        margin: 0;
        font-size: 0.95rem;
    }

    /* Metric cards */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }

    .metric-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 1.2rem;
        transition: border-color 0.2s;
    }

    .metric-card:hover {
        border-color: #1f6feb;
    }

    .metric-label {
        font-size: 0.75rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.4rem;
    }

    .metric-value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #e6edf3;
        line-height: 1;
    }

    .metric-delta {
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }

    .delta-up { color: #2ea043; }
    .delta-down { color: #f85149; }
    .delta-neutral { color: #8b949e; }

    /* Section cards */
    .section-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .section-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .section-title::after {
        content: '';
        flex: 1;
        height: 1px;
        background: #30363d;
    }

    /* Report content */
    .report-content {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 2rem;
        line-height: 1.8;
        color: #c9d1d9;
    }

    .report-content h2 {
        color: #e6edf3;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 1.5rem 0 0.5rem 0;
        padding-bottom: 0.3rem;
        border-bottom: 1px solid #21262d;
    }

    .report-content h2:first-child {
        margin-top: 0;
    }

    /* Sector badge */
    .sector-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Generate button */
    .stButton > button {
        background: linear-gradient(135deg, #1f6feb, #388bfd) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        width: 100% !important;
        transition: opacity 0.2s !important;
    }

    .stButton > button:hover {
        opacity: 0.85 !important;
    }

    /* Input fields */
    .stTextInput > div > div > input {
        background: #21262d !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        color: #e6edf3 !important;
        font-size: 1rem !important;
        padding: 0.6rem 1rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #1f6feb !important;
        box-shadow: 0 0 0 3px rgba(31, 111, 235, 0.15) !important;
    }

    /* Selectbox */
    .stSelectbox > div > div {
        background: #21262d !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        color: #e6edf3 !important;
    }

    /* Divider */
    hr {
        border-color: #30363d !important;
    }

    /* Spinner */
    .stSpinner > div {
        border-top-color: #1f6feb !important;
    }

    /* Status indicator */
    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 6px;
    }
    .status-live { background: #2ea043; animation: pulse 2s infinite; }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }

    /* Company header */
    .company-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }

    .company-avatar {
        width: 56px;
        height: 56px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 700;
        flex-shrink: 0;
    }

    .company-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #e6edf3;
        margin: 0;
    }

    .company-meta {
        color: #8b949e;
        font-size: 0.85rem;
        margin: 0.2rem 0 0 0;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background: #161b22;
        border-radius: 8px;
        padding: 4px;
        gap: 4px;
        border: 1px solid #30363d;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 6px;
        color: #8b949e;
        font-weight: 500;
        font-size: 0.85rem;
    }

    .stTabs [aria-selected="true"] {
        background: #21262d !important;
        color: #e6edf3 !important;
    }

    /* Info box */
    .info-box {
        background: rgba(31, 111, 235, 0.08);
        border: 1px solid rgba(31, 111, 235, 0.3);
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
        color: #79c0ff;
        font-size: 0.875rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
    <div style="padding: 1rem 0 1.5rem 0; border-bottom: 1px solid #30363d; margin-bottom: 1.5rem;">
        <div style="font-size: 1.1rem; font-weight: 700; color: #e6edf3;">📊 Company Intel</div>
        <div style="font-size: 0.75rem; color: #8b949e; margin-top: 0.25rem;">
            <span class="status-dot status-live"></span>AI-Powered · Free
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("**🏢 Company**")
    company_name = st.text_input(
        "Company name",
        placeholder="e.g. JP Morgan, NHS, Tesco...",
        label_visibility="collapsed",
    )

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    st.markdown("**🏭 Sector**")

    sector_options = list(SECTORS.keys())
    sector_icons = {s: SECTORS[s]["icon"] for s in sector_options}

    selected_sector = st.selectbox(
        "Sector",
        sector_options,
        format_func=lambda x: f"{sector_icons[x]} {x}",
        label_visibility="collapsed",
    )

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    st.markdown("**📋 Report Type**")
    report_type = st.selectbox(
        "Report Type",
        [
            "Full Intelligence Report",
            "KPI Snapshot",
            "Strategic Position",
            "Risk Assessment",
        ],
        label_visibility="collapsed",
    )

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    generate_btn = st.button("⚡ Generate Report", use_container_width=True)

    st.markdown(
        "<div style='margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid #30363d;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <div style="font-size: 0.75rem; color: #8b949e; line-height: 1.6;">
        <strong style="color: #e6edf3;">How it works</strong><br>
        AI generates structured intelligence reports using sector-specific frameworks and KPI benchmarks.
        <br><br>
        <strong style="color: #e6edf3;">Sectors covered</strong><br>
        🏦 Banking & FS<br>
        🏥 Healthcare<br>
        🛒 Retail & FMCG<br>
        ⚡ Energy & Utilities
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ── Main Content ──────────────────────────────────────────────────────────────

# Hero
sector_data = SECTORS[selected_sector]
st.markdown(
    f"""
<div class="hero">
    <h1>Company Intelligence Dashboard</h1>
    <p>AI-generated strategic intelligence reports across Banking, Healthcare, Retail & Energy sectors</p>
</div>
""",
    unsafe_allow_html=True,
)

# Welcome state
if not generate_btn or not company_name:
    col1, col2, col3, col4 = st.columns(4)
    sectors_list = list(SECTORS.items())

    for col, (sector_name, data) in zip([col1, col2, col3, col4], sectors_list):
        with col:
            st.markdown(
                f"""
            <div class="metric-card" style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{data["icon"]}</div>
                <div style="font-weight: 600; color: #e6edf3; margin-bottom: 0.5rem;">{sector_name}</div>
                <div style="font-size: 0.75rem; color: #8b949e;">{data["description"]}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div class="info-box">
        💡 <strong>How to use:</strong> Enter a company name in the sidebar, select its sector, choose your report type, and click Generate Report.
        Works for any company globally — FTSE 100, Fortune 500, NHS trusts, and more.
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Example companies
    st.markdown(
        """
    <div class="section-card">
        <div class="section-title">Example Companies to Try</div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem;">
            <div>
                <div style="font-size: 0.75rem; color: #8b949e; margin-bottom: 0.5rem;">🏦 Banking</div>
                <div style="font-size: 0.85rem; color: #c9d1d9;">JP Morgan<br>Barclays<br>HSBC<br>Goldman Sachs</div>
            </div>
            <div>
                <div style="font-size: 0.75rem; color: #8b949e; margin-bottom: 0.5rem;">🏥 Healthcare</div>
                <div style="font-size: 0.85rem; color: #c9d1d9;">NHS<br>Bupa<br>Johnson & Johnson<br>AstraZeneca</div>
            </div>
            <div>
                <div style="font-size: 0.75rem; color: #8b949e; margin-bottom: 0.5rem;">🛒 Retail</div>
                <div style="font-size: 0.85rem; color: #c9d1d9;">Tesco<br>Amazon<br>Marks & Spencer<br>Walmart</div>
            </div>
            <div>
                <div style="font-size: 0.75rem; color: #8b949e; margin-bottom: 0.5rem;">⚡ Energy</div>
                <div style="font-size: 0.85rem; color: #c9d1d9;">BP<br>Shell<br>National Grid<br>Ørsted</div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Generate Report
if generate_btn and company_name:
    sector_info = SECTORS[selected_sector]
    kpis = get_sector_kpis(selected_sector)
    context = get_sector_context(selected_sector)

    # Company header
    initials = "".join([w[0] for w in company_name.split()[:2]]).upper()
    avatar_color = sector_info["color"]

    st.markdown(
        f"""
    <div class="company-header">
        <div class="company-avatar" style="background: {avatar_color}20; color: {avatar_color}; border: 1px solid {avatar_color}40;">
            {initials}
        </div>
        <div>
            <p class="company-name">{company_name}</p>
            <p class="company-meta">{sector_info["icon"]} {selected_sector} · {report_type}</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Tabs
    tab1, tab2, tab3 = st.tabs(
        ["📋 Intelligence Report", "📊 KPI Framework", "🎯 Strategic Lens"]
    )

    with tab1:
        with st.spinner(f"Generating {report_type} for {company_name}..."):
            report = generate_company_report(
                company=company_name,
                sector=selected_sector,
                report_type=report_type,
                context=context,
                kpis=kpis,
            )

        if report.startswith("Error") or report.startswith("⚠️"):
            st.error(report)
            st.info("Make sure your GROQ_API_KEY is set in the .env file")
        else:
            st.markdown(
                f'<div class="report-content">{report}</div>', unsafe_allow_html=True
            )

            # Download button
            st.download_button(
                label="⬇️ Download Report",
                data=report,
                file_name=f"{company_name.replace(' ', '_')}_{selected_sector}_Intelligence_Report.md",
                mime="text/markdown",
            )

    with tab2:
        st.markdown(
            f"""
        <div class="section-card">
            <div class="section-title">Key Performance Indicators — {selected_sector}</div>
        """,
            unsafe_allow_html=True,
        )

        cols = st.columns(3)
        for i, kpi in enumerate(kpis):
            with cols[i % 3]:
                delta_class = (
                    "delta-up"
                    if kpi.get("trend") == "up"
                    else "delta-down"
                    if kpi.get("trend") == "down"
                    else "delta-neutral"
                )
                delta_icon = (
                    "↑"
                    if kpi.get("trend") == "up"
                    else "↓"
                    if kpi.get("trend") == "down"
                    else "→"
                )
                st.markdown(
                    f"""
                <div class="metric-card">
                    <div class="metric-label">{kpi["name"]}</div>
                    <div class="metric-value">{kpi["benchmark"]}</div>
                    <div class="metric-delta {delta_class}">{delta_icon} Industry benchmark</div>
                    <div style="font-size: 0.75rem; color: #8b949e; margin-top: 0.3rem;">{kpi["description"]}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown(
            f"""
        <div class="section-card">
            <div class="section-title">Strategic Framework — {selected_sector}</div>
            <div style="color: #c9d1d9; font-size: 0.9rem; line-height: 1.8;">
                {context}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Strategic dimensions
        dimensions = sector_info.get("dimensions", [])
        if dimensions:
            cols = st.columns(len(dimensions))
            for col, dim in zip(cols, dimensions):
                with col:
                    st.markdown(
                        f"""
                    <div class="metric-card" style="text-align: center;">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{dim["icon"]}</div>
                        <div style="font-weight: 600; color: #e6edf3; font-size: 0.85rem; margin-bottom: 0.3rem;">{dim["name"]}</div>
                        <div style="font-size: 0.75rem; color: #8b949e;">{dim["desc"]}</div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
