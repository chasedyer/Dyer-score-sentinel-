import streamlit as st
import pandas as pd
import requests

# 1. ATTEMPT DATA LINK
try:
    import yfinance as yf
    DATA_LINK = True
except ImportError:
    DATA_LINK = False

# 2. UI SETTINGS
st.set_page_config(page_title="Dyer Global Audit", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 48px; font-weight: bold; color: #00FF41; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. AUTOFILL ENGINE
def search_directory(query):
    if not query or len(query) < 2: return []
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}"
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
        return [f"{q['symbol']} - {q['shortname']}" for q in r.get('quotes', []) if 'symbol' in q]
    except: return []

# 4. MAIN INTERFACE
st.sidebar.title("🛡️ Dyer Command")
page = st.sidebar.selectbox("TASK", ["📡 AUDIT SCANNER", "🔬 CORE 23 HUB", "🧪 MODEL A/B LOGIC"])

if page == "📡 AUDIT SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    # LIVE SEARCH BAR
    search_q = st.text_input("TYPE COMPANY NAME (Autofills Ticker)", placeholder="e.g. Costco, Nvidia...")
    suggestions = search_directory(search_q)
    
    if suggestions:
        selected_stock = st.selectbox("MATCH FOUND:", suggestions)
        ticker = selected_stock.split(" - ")[0]
    else:
        ticker = search_q.upper()

    if st.button("CALCULATE DYER SCORE"):
        if ticker:
            with st.spinner(f"Auditing {ticker}..."):
                # DATA RETRIEVAL WITH BACKUP
                if DATA_LINK:
                    try:
                        stock = yf.Ticker(ticker)
                        info = stock.info
                        mgn = info.get('operatingMargins', 0) * 100
                        rev = info.get('revenueGrowth', 0) * 100
                        price = info.get('currentPrice', 0)
                        # ROIC Calculation
                        ebit = info.get('ebitda', 1) * 0.8
                        cap = (info.get('totalStockholderEquity', 1) + info.get('totalDebt', 0) - info.get('totalCash', 0))
                        roic = (ebit / cap) * 100 if cap > 0 else 0
                    except:
                        mgn, rev, roic, price = 0, 0, 0, 0
                else:
                    mgn, rev, roic, price = 0, 0, 0, 0 # Manual override mode

                # VITALS GRID
                st.markdown(f"### 📊 Forensic Vitals: {ticker}")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Op. Margin", f"{mgn:.1f}%" if mgn else "OFFLINE")
                c2.metric("Growth (YoY)", f"{rev:.1f}%" if rev else "OFFLINE")
                c3.metric("ROIC", f"{roic:.1f}%" if roic else "OFFLINE")
                c4.metric("Live Price", f"${price:.2f}" if price else "OFFLINE")

                # THE RUSHMORE BUCKETS
                st.sidebar.markdown("---")
                s1 = st.sidebar.slider("Stability (Asset Quality)", 0, 100, 80)
                s2 = st.sidebar.slider("Growth (Capacity)", 0, 100, 80)
                s3 = st.sidebar.slider("Premium (Management)", 0, 100, 80)
                total = s1 + s2 + s3
                
                st.markdown("---")
                if total >= 200: st.success(f"💎 SOVEREIGN BUY | SCORE: {total}/300")
                elif total < 150: st.error(f"🚨 TRAPDOOR SELL | SCORE: {total}/300")
                else: st.warning(f"⚖️ AUDIT HOLD | SCORE: {total}/300")

elif page == "🔬 CORE 23 HUB":
    st.title("🔬 Core 23 Audit Cycle")
    st.info("Rebalance every 120 days. Rule: 10% Dyer improvement or FAIL.")
    st.table(pd.DataFrame({
        "Ticker": ["COST", "MSFT", "V", "WM", "DE", "AAPL", "NVDA", "GOOGL", "AMZN", "META"],
        "Dyer Score": [285, 278, 270, 265, 260, 255, 288, 240, 245, 250],
        "120-Day Delta": ["+12%", "+5%", "+11%", "-2%", "+15%", "+8%", "+22%", "-1%", "+4%", "+9%"]
    }))
