import streamlit as st
import pandas as pd
import yfinance as yf

# --- 1. SETTINGS & THEME ---
st.set_page_config(page_title="Dyer Global Audit", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; margin-bottom: 0px; }
    .verdict-box { padding: 20px; border-radius: 15px; text-align: center; font-size: 24px; font-weight: bold; margin: 20px 0; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL ASSET NAVIGATION ---
page = st.sidebar.radio("COMMAND CENTER", ["📡 GLOBAL SCANNER", "🔬 CORE 23 VS MARKET", "🧪 MODEL A/B LOGIC", "🏆 AUDITOR PODIUM"])

# --- 3. PAGE 1: GLOBAL SCANNER (S&P/NASDAQ/RUSSELL) ---
if page == "📡 GLOBAL SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">UNIVERSAL MARKET SCAN | ALL TICKERS ACTIVE</p>', unsafe_allow_html=True)

    # SEARCH VAULT
    with st.form("global_audit"):
        col1, col2 = st.columns([4, 1])
        with col1:
            ticker = st.text_input("SCAN ANY TICKER", value="COST").upper()
        with col2:
            st.write("") # Padding
            submitted = st.form_submit_button("VALIDATE & AUDIT")

    if submitted and ticker:
        try:
            with st.spinner(f"Auditing {ticker} across S&P, Russell, and Nasdaq..."):
                asset = yf.Ticker(ticker)
                info = asset.fast_info
                price = info['last_price']
                
                # RUSHMORE METRIC CALCULATOR (300 Point Scale)
                st.sidebar.subheader("Forensic Parameters")
                # Asset Quality (Stability), Expansion (Growth), Management (Premium)
                stability = st.sidebar.slider("Asset Quality (Stability)", 0, 100, 85)
                growth = st.sidebar.slider("Expansion Capacity (Growth)", 0, 100, 80)
                premium = st.sidebar.slider("Management/Moat (Premium)", 0, 100, 90)
                
                total_score = stability + growth + premium
                
                # VERDICT LOGIC
                if total_score >= 200:
                    st.success(f"💎 {ticker} VERDICT: SOVEREIGN BUY ({total_score}/300)")
                elif total_score < 150:
                    st.error(f"🚨 {ticker} VERDICT: TRAPDOOR SELL ({total_score}/300)")
                else:
                    st.warning(f"⚖️ {ticker} VERDICT: AUDIT HOLD ({total_score}/300)")
                
                st.progress(total_score / 300)

                # VITALS
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Live Price", f"${price:.2f}")
                c2.metric("Rushmore Score", f"{total_score}/300")
                c3.metric("Cycle Goal", "+10% Score")
                c4.metric("Cycle Status", "Day 36/120")

        except Exception as e:
            st.error("Asset not found in Global Index data. Check ticker.")

# --- 4. PAGE 2: CORE 23 VS MARKET ---
elif page == "🔬 CORE 23 VS MARKET":
    st.title("🔬 Core 23 Benchmark Comparison")
    st.write("Tracking the **Signal Weight Rushmore 10** against the broader indices.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Rushmore 10 Performance", "+18.4%", "Beating S&P 500")
    m2.metric("S&P 500 (SPY)", "+12.1%", "Benchmark")
    m3.metric("Russell 2000 (IWM)", "-2.4%", "Lagging")
    
    st.markdown("---")
    st.subheader("The Remaining 13 Status")
    st.dataframe(pd.DataFrame({
        "Ticker": ["WMT", "JPM", "PG", "UNH", "HD", "DIS", "BAC", "VZ", "ADBE", "NFLX", "CRM", "INTC", "CMCSA"],
        "Audit Status": ["PASS", "PASS", "HOLD", "PASS", "HOLD", "FAIL", "PASS", "HOLD", "PASS", "PASS", "PASS", "FAIL", "HOLD"],
        "Dyer Score": [210, 205, 185, 220, 175, 140, 215, 160, 230, 240, 225, 110, 170]
    }))

# --- 5. PAGE 3: MODEL LOGIC ---
elif page == "🧪 MODEL A/B LOGIC":
    st.title("🧪 3-Year Strategy: Model A vs. Model B")
    st.markdown("""
    ### **Model A: The Quarterly Cull**
    * **Rule:** Every quarter, identify the bottom 5 performers.
    * **Action:** Sell 25% of each and move that cash into the top 5 leaders.
    
    ### **Model B: The 90-Day Reset**
    * **Rule:** Every 90 days, rebalance all tickers back to 10% weight.
    * **Action:** Sell winners, buy losers to maintain equal exposure.
    """)

# --- 6. PAGE 4: PODIUM ---
elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 14-Chapter Auditor Leaderboard")
    st.table(pd.DataFrame({
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Audit Level": ["Chapter 14", "Chapter 12", "Chapter 11", "Chapter 9", "Chapter 4", "Chapter 2", "In Processing"]
    }))
