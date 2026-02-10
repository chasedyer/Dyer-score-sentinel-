import streamlit as st
import pandas as pd

# --- 1. INTERFACE SETTINGS ---
st.set_page_config(page_title="Dyer Score Terminal", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; }
    .metric-header { color: #00FF41; font-weight: bold; font-size: 22px; border-bottom: 2px solid #30363D; margin-bottom: 10px; padding-top: 10px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; }
    .verdict-text { font-size: 28px; font-weight: bold; text-align: center; padding: 20px; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. COMMAND NAVIGATION ---
page = st.sidebar.radio("COMMAND", ["📡 DYER SCANNER", "🔬 CORE 23 HUB", "🧪 MODEL A/B LOGIC"])

if page == "📡 DYER SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">300-POINT RUSHMORE METRIC | FORENSIC SUB-PARTS</p>', unsafe_allow_html=True)

    # SEARCH & INPUTS
    col_a, col_b = st.columns([2, 1])
    with col_a:
        ticker = st.text_input("ENTER COMPANY NAME OR TICKER", "COSTCO").upper()
    with col_b:
        audit_date = st.date_input("AUDIT DATE")

    st.markdown("### 📥 Input Bucket Scores")
    c1, c2, c3 = st.columns(3)
    with c1:
        s_score = st.number_input("Stability (0-100)", 0, 100, 85)
    with c2:
        g_score = st.number_input("Growth (0-100)", 0, 100, 75)
    with c3:
        p_score = st.number_input("Premium (0-100)", 0, 100, 90)
    
    total_score = s_score + g_score + p_score

    if st.button("CALCULATE DYER SCORE"):
        st.markdown("---")
        
        # FINAL VERDICT
        if total_score >= 200:
            st.markdown(f'<div class="verdict-text" style="background-color: rgba(0, 255, 65, 0.2); border: 1px solid #00FF41;">💎 {ticker} VERDICT: SOVEREIGN BUY ({total_score}/300)</div>', unsafe_allow_html=True)
        elif total_score < 150:
            st.markdown(f'<div class="verdict-text" style="background-color: rgba(255, 0, 0, 0.2); border: 1px solid #FF0000;">🚨 {ticker} VERDICT: TRAPDOOR SELL ({total_score}/300)</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="verdict-text" style="background-color: rgba(255, 165, 0, 0.2); border: 1px solid #FFA500;">⚖️ {ticker} VERDICT: AUDIT HOLD ({total_score}/300)</div>', unsafe_allow_html=True)

        # SUB-PART FORENSIC BREAKDOWN
        f1, f2, f3 = st.columns(3)

        with f1:
            st.markdown('<div class="metric-header">STABILITY (Asset Quality)</div>', unsafe_allow_html=True)
            st.markdown(f"**Current Bucket Score: {s_score}/100**")
            st.info("1. Operating Margin Trend\n\n2. ROIC Consistency\n\n3. Debt-to-Equity Shield")

        with f2:
            st.markdown('<div class="metric-header">GROWTH (Expansion)</div>', unsafe_allow_html=True)
            st.markdown(f"**Current Bucket Score: {g_score}/100**")
            st.info("1. Revenue Growth Rate\n\n2. Market Share Velocity\n\n3. Capex Efficiency")

        with f3:
            st.markdown('<div class="metric-header">PREMIUM (Management)</div>', unsafe_allow_html=True)
            st.markdown(f"**Current Bucket Score: {p_score}/100**")
            st.info("1. Founder/CEO Alignment\n\n2. Brand Pricing Power\n\n3. Entry Barrier (Moat)")

elif page == "🔬 CORE 23 HUB":
    st.title("🔬 Core 23 Audit Tracking")
    st.write("Current Audit Cycle: **120 Days** | Requirement: **+10% Dyer Score**")
    
    # Tracking logic for the Core 23
    data = {
        "Ticker": ["COST", "MSFT", "V", "WM", "DE", "AAPL", "NVDA", "GOOGL", "AMZN", "META"],
        "Last Dyer Score": [285, 278, 270, 265, 260, 255, 288, 240, 245, 250],
        "Cycle Status": ["Day 36", "Day 36", "Day 36", "Day 36", "Day 36", "Day 36", "Day 36", "Day 36", "Day 36", "Day 36"],
        "Flag for Steve": ["-", "-", "-", "HOLD", "-", "-", "-", "LOW GROWTH", "-", "-"]
    }
    st.table(pd.DataFrame(data))
