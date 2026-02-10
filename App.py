import streamlit as st
import pandas as pd

# --- 1. INTERFACE SETTINGS ---
st.set_page_config(page_title="Dyer Score Terminal", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; }
    .metric-header { color: #00FF41; font-weight: bold; font-size: 20px; border-bottom: 1px solid #30363D; margin-bottom: 10px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. COMMAND NAVIGATION ---
page = st.sidebar.radio("COMMAND", ["📡 DYER SCANNER", "🔬 CORE 23 HUB", "🏆 AUDITOR PODIUM"])

if page == "📡 DYER SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">300-POINT RUSHMORE METRIC | CHAPTER 14 AUDIT</p>', unsafe_allow_html=True)

    # SEARCH
    ticker = st.text_input("ENTER COMPANY NAME OR TICKER", "COSTCO").upper()

    # THE THREE BUCKETS (Sidebar Controls)
    st.sidebar.header("📊 Audit Sliders")
    s_score = st.sidebar.slider("Stability (Asset Quality)", 0, 100, 85)
    g_score = st.sidebar.slider("Growth (Expansion Capacity)", 0, 100, 75)
    p_score = st.sidebar.slider("Premium (Management/Moat)", 0, 100, 90)
    
    total_score = s_score + g_score + p_score

    if st.button("CALCULATE DYER SCORE"):
        st.markdown("---")
        
        # FINAL VERDICT HEADER
        if total_score >= 200:
            st.success(f"💎 {ticker} VERDICT: SOVEREIGN BUY ({total_score}/300)")
        elif total_score < 150:
            st.error(f"🚨 {ticker} VERDICT: TRAPDOOR SELL ({total_score}/300)")
        else:
            st.warning(f"⚖️ {ticker} VERDICT: AUDIT HOLD ({total_score}/300)")

        # SUB-PART FORENSIC BREAKDOWN
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="metric-header">STABILITY (Asset Quality)</div>', unsafe_allow_html=True)
            st.write(f"**Score:** {s_score}/100")
            st.write("1. Operating Margin Trend")
            st.write("2. ROIC Consistency")
            st.write("3. Debt-to-Equity Shield")

        with col2:
            st.markdown('<div class="metric-header">GROWTH (Expansion)</div>', unsafe_allow_html=True)
            st.write(f"**Score:** {g_score}/100")
            st.write("1. Revenue Growth Rate")
            st.write("2. Market Share Velocity")
            st.write("3. Capex Efficiency")

        with col3:
            st.markdown('<div class="metric-header">PREMIUM (Management)</div>', unsafe_allow_html=True)
            st.write(f"**Score:** {p_score}/100")
            st.write("1. Founder/CEO Alignment")
            st.write("2. Brand Pricing Power")
            st.write("3. Entry Barrier (Moat)")

elif page == "🔬 CORE 23 HUB":
    st.title("🔬 Core 23 Audit Cycle")
    st.info("Goal: 10% Score Improvement every 120 days.")
    st.table(pd.DataFrame({
        "Ticker": ["COST", "MSFT", "V", "WM", "DE"],
        "Last Audit": ["275", "260", "250", "230", "220"],
        "Current Audit": [s_score+g_score+p_score if ticker=="COST" else "---" for _ in range(5)],
        "120-Day Delta": ["Pending", "Pending", "Pending", "Pending", "Pending"]
    }))
