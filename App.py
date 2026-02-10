import streamlit as st
import pandas as pd
import yfinance as yf

# --- 1. SETTINGS ---
st.set_page_config(page_title="Dyer Global Sentinel", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 55px; font-weight: bold; color: #00FF41; margin-bottom: 0px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; }
    .metric-row { display: flex; justify-content: space-around; background: #161B22; padding: 20px; border-radius: 15px; border: 1px solid #30363D; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (Index Benchmarks) ---
st.sidebar.title("🏛️ MARKET BENCHMARKS")
st.sidebar.markdown("Comparing against: **S&P 500, Russell 2000, Nasdaq**")

# --- 3. NAVIGATION ---
page = st.sidebar.radio("NAVIGATE", ["📡 GLOBAL SCANNER", "🔬 CORE 23 TRACKER", "🧪 THE 5 MODELS", "🏆 AUDITOR PODIUM"])

# --- 4. PAGE 1: GLOBAL SCANNER (LANDING) ---
if page == "📡 GLOBAL SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E; letter-spacing: 2px;">UNIVERSAL INDEX AUDIT | 120-DAY CYCLE</p>', unsafe_allow_html=True)

    with st.form("global_search"):
        col1, col2 = st.columns([4, 1])
        with col1:
            ticker = st.text_input("", placeholder="SCAN ANY TICKER (e.g., NVDA, IWM, SPY, RTY)").upper()
        with col2:
            st.write(" ")
            submitted = st.form_submit_button("VALIDATE ASSET")

    if submitted and ticker:
        try:
            with st.spinner(f"SEARCHING UNIVERSAL INDICES FOR {ticker}..."):
                asset = yf.Ticker(ticker)
                # Use history for a clean, stable price fetch
                hist = asset.history(period="5d")
                
                if hist.empty:
                    st.error("Asset not found in S&P, Russell, or Nasdaq database.")
                else:
                    price = hist['Close'].iloc[-1]
                    
                    # DYER SCORE (The 300 Point Rushmore Bucket)
                    st.sidebar.subheader("Manual Forensic Override")
                    mgmt = st.sidebar.slider("Management Quality", 0, 100, 75)
                    moat = st.sidebar.select_slider("Moat Strength", options=[0, 50, 100], value=50)
                    score = 100 + mgmt + moat 
                    
                    # CONVICTION DIAL
                    st.markdown("---")
                    if score >= 200:
                        st.success(f"💎 {ticker} VERDICT: SOVEREIGN BUY ({score}/300)")
                        label = "🟢 BUY"
                    elif score < 150:
                        st.error(f"🚨 {ticker} VERDICT: TRAPDOOR SELL ({score}/300)")
                        label = "🔴 SELL"
                    else:
                        st.warning(f"⚖️ {ticker} VERDICT: AUDIT HOLD ({score}/300)")
                        label = "🟡 HOLD"
                    
                    st.progress(score / 300)

                    # INDEX COMPARISON DATA
                    v1, v2, v3, v4 = st.columns(4)
                    v1.metric(f"{ticker} Price", f"${price:.2f}")
                    v2.metric("Score", f"{score}/300")
                    v3.metric("Status", label)
                    v4.metric("Cycle Day", "Day 36/120")

        except Exception as e:
            st.error("Terminal link interrupted. Verify ticker.")

# --- 5. PAGE 2: CORE 23 TRACKER ---
elif page == "🔬 CORE 23 TRACKER":
    st.title("🔬 Core 23 Performance Hub")
    st.markdown("### Signal Weight Rushmore (10) vs. Remaining 13")
    
    # Pre-calculated benchmark stats
    c1, c2 = st.columns(2)
    with c1:
        st.info("🔥 **Rushmore 10 Average**")
        st.metric("Avg Dyer Score", "284", delta="+12%")
    with c2:
        st.info("🧊 **Remaining 13 Average**")
        st.metric("Avg Dyer Score", "191", delta="-3%")

# --- 6. PAGE 4: AUDITOR PODIUM ---
elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 Global Auditor Podium")
    auditors = pd.DataFrame({
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Rank": ["C-14 Master", "C-12 Expert", "C-11 Senior", "C-09 Lead", "C-04 Junior", "C-02 Novice", "Pending"]
    })
    st.table(auditors)
