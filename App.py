import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# --- 1. LIVE ENGINE CONFIG ---
st.set_page_config(page_title="Dyer Global Sentinel", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; margin-bottom: 0px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. UNIVERSAL SEARCH FUNCTION ---
def find_ticker(query):
    if not query or len(query) < 2: return []
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        data = requests.get(url, headers=headers).json()
        return [f"{q['symbol']} - {q['shortname']}" for q in data.get('quotes', []) if 'symbol' in q and 'shortname' in q]
    except: return []

# --- 3. COMMAND NAVIGATION ---
page = st.sidebar.radio("COMMAND CENTER", ["📡 GLOBAL SCANNER", "🔬 CORE 23 HUB", "🧪 MODEL A/B LOGIC", "🏆 AUDITOR PODIUM"])

# --- 4. PAGE 1: THE SCANNER ---
if page == "📡 GLOBAL SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">LIVE UNIVERSAL INDEX SCAN | S&P 500 | NASDAQ | RUSSELL</p>', unsafe_allow_html=True)

    # AUTO-FILL SEARCH BAR
    user_query = st.text_input("ENTER COMPANY NAME OR TICKER", placeholder="e.g. Costco, Microsoft, Nvidia...")
    options = find_ticker(user_query)
    
    if options:
        selection = st.selectbox("SELECT ASSET FOR AUDIT:", options)
        ticker = selection.split(" - ")[0]
    else:
        ticker = user_query.upper()

    if st.button("CALCULATE DYER SCORE"):
        if ticker:
            try:
                with st.spinner(f"Initiating Live Forensic Audit for {ticker}..."):
                    asset = yf.Ticker(ticker)
                    price = asset.fast_info['last_price']
                    
                    # DYER SCORE BUCKETS (100pt each)
                    st.sidebar.subheader("Forensic Sliders")
                    stab = st.sidebar.slider("Stability (Asset Quality)", 0, 100, 85)
                    grow = st.sidebar.slider("Growth (Expansion)", 0, 100, 80)
                    prem = st.sidebar.slider("Premium (Management)", 0, 100, 90)
                    total = stab + grow + prem
                    
                    st.markdown("---")
                    if total >= 200: st.success(f"💎 {ticker} SCORE: {total}/300 | SOVEREIGN BUY")
                    elif total < 150: st.error(f"🚨 {ticker} SCORE: {total}/300 | TRAPDOOR SELL")
                    else: st.warning(f"⚖️ {ticker} SCORE: {total}/300 | AUDIT HOLD")
                    
                    st.progress(total / 300)

                    # LIVE DATA GRID
                    c1, c2, c3 = st.columns(3)
                    c1.metric(f"Live Price", f"${price:.2f}")
                    c2.metric("Rushmore Status", "Top 10" if ticker in ["AAPL", "COST", "MSFT"] else "Global Universe")
                    c3.metric("Audit Window", "Day 36 / 120")
            except:
                st.error("Terminal link interrupted. Select a valid company from the dropdown.")

# --- 5. PAGE 2: CORE 23 HUB ---
elif page == "🔬 CORE 23 HUB":
    st.title("🔬 Core 23 Tracking")
    st.write("Comparing the **Signal Weight Rushmore 10** against the **Remaining 13**.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🔥 **Rushmore 10**")
        st.write(["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "COST", "V", "MA"])
    with col2:
        st.warning("🧊 **Remaining 13**")
        st.write(["WMT", "JPM", "PG", "UNH", "HD", "DIS", "BAC", "VZ", "ADBE", "NFLX", "CRM", "INTC", "CMCSA"])

# --- 6. PAGE 4: PODIUM ---
elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 Global Auditor Leaderboard")
    auditors = pd.DataFrame({
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Rank": ["C-14", "C-12", "C-11", "C-09", "C-04", "C-02", "Pending"]
    })
    st.table(auditors)
