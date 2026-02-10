import streamlit as st
import pandas as pd

# --- 1. SYSTEM SETTINGS ---
st.set_page_config(page_title="Dyer Global Audit", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; margin-bottom: 0px; }
    .metric-header { color: #00FF41; font-weight: bold; font-size: 22px; border-bottom: 2px solid #30363D; margin-bottom: 10px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. COMMAND NAVIGATION ---
page = st.sidebar.radio("COMMAND CENTER", ["📡 DYER SCANNER", "🔬 5* MODELS HUB", "🧪 STRATEGY LOGIC", "🏆 AUDITOR PODIUM"])

# --- 3. PAGE 1: SCANNER & SUB-PARTS ---
if page == "📡 DYER SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">UNIVERSAL NAME-TO-TICKER FORENSIC SEARCH</p>', unsafe_allow_html=True)

    # SEARCH & MANUAL ENTRY
    ticker_input = st.text_input("ENTER COMPANY NAME (Autofill: Costco, Microsoft, etc.)", "COSTCO").upper()
    
    # Bucket Inputs (Replacing Sliders with precise entry)
    st.markdown("### 📥 Input 300-Point Rushmore Buckets")
    c1, c2, c3 = st.columns(3)
    with c1: s_score = st.number_input("STABILITY (Asset Quality)", 0, 100, 85)
    with c2: g_score = st.number_input("GROWTH (Expansion Capacity)", 0, 100, 80)
    with c3: p_score = st.number_input("PREMIUM (Management/Moat)", 0, 100, 90)
    
    total = s_score + g_score + p_score

    if st.button("CALCULATE DYER SCORE"):
        st.markdown("---")
        # VERDICT BANNERS
        if total >= 200: st.success(f"💎 {ticker_input} VERDICT: SOVEREIGN BUY ({total}/300)")
        elif total < 150: st.error(f"🚨 {ticker_input} VERDICT: TRAPDOOR SELL ({total}/300)")
        else: st.warning(f"⚖️ {ticker_input} VERDICT: AUDIT HOLD ({total}/300)")

        # TOP 3 METRICS PER SCORE
        st.markdown("### 🔬 Forensic Sub-Part Breakdown")
        f1, f2, f3 = st.columns(3)
        
        with f1:
            st.markdown('<div class="metric-header">STABILITY</div>', unsafe_allow_html=True)
            st.markdown(f"**Score: {s_score}/100**")
            st.info("1. Operating Margin\n\n2. ROIC (Invested Capital)\n\n3. Debt-to-Equity Ratio")
            
        with f2:
            st.markdown('<div class="metric-header">GROWTH</div>', unsafe_allow_html=True)
            st.markdown(f"**Score: {g_score}/100**")
            st.info("1. Revenue Growth Rate\n\n2. Market Share Capture\n\n3. Capex Efficiency")
            
        with f3:
            st.markdown('<div class="metric-header">PREMIUM</div>', unsafe_allow_html=True)
            st.markdown(f"**Score: {p_score}/100**")
            st.info("1. Founder Alignment\n\n2. Brand Pricing Power\n\n3. Competitive Moat")

# --- 4. PAGE 2: 5* MODELS HUB ---
elif page == "🔬 5* MODELS HUB":
    st.title("🔬 The 5* Models Dashboard")
    st.write("Tracking the **Signal Weight Rushmore 10** vs the **Remaining 13** across all structures.")
    
    m_tab1, m_tab2, m_tab3, m_tab4, m_tab5 = st.tabs(["Model A (Cull)", "Model B (Rebalance)", "Model C", "Model D", "Model E (Anti)"])
    
    with m_tab1:
        st.subheader("Quarterly Cull Model")
        st.write("Cull bottom 5 performers by 25% → Move to top 5 leaders.")
        st.table(pd.DataFrame({"Ticker": ["COST", "MSFT", "AAPL"], "Dyer Score": [285, 278, 260], "Audit Status": ["Pass", "Pass", "Pass"]}))
        
    with m_tab2:
        st.subheader("90-Day Rebalance Model")
        st.write("Rebalance to 10% each ticker every 90 days. Sell winners, buy losers.")
        
    with m_tab5:
        st.subheader("Model E: The Anti-Model")
        st.error("Assets failing the 120-day 10% Dyer Score improvement threshold.")
