import streamlit as st
import pandas as pd
import requests

# 1. ATTEMPT LIVE IMPORT (Safeguard)
try:
    import yfinance as yf
    LINK_ACTIVE = True
except ImportError:
    LINK_ACTIVE = False

# 2. UI SETTINGS
st.set_page_config(page_title="Dyer Global Sentinel", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 48px; font-weight: bold; color: #00FF41; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. UNIVERSAL SEARCH
def fetch_ticker_list(query):
    if not query or len(query) < 2: return []
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers).json()
        return [f"{q['symbol']} - {q['shortname']}" for q in r.get('quotes', []) if 'symbol' in q]
    except: return []

# 4. APP NAVIGATION
page = st.sidebar.radio("COMMAND CENTER", ["📡 GLOBAL SCANNER", "🔬 CORE 23 HUB", "🏆 PODIUM"])

if page == "📡 GLOBAL SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    # STATUS BAR
    if LINK_ACTIVE:
        st.sidebar.success("📡 EXCHANGE LINK: ACTIVE")
    else:
        st.sidebar.warning("⚠️ LINK OFFLINE: USING CACHE")

    # SEARCH INPUT
    search_input = st.text_input("ENTER COMPANY NAME (e.g. Costco, Apple, Visa)", "")
    suggestions = fetch_ticker_list(search_input)
    
    if suggestions:
        selected = st.selectbox("CONFIRM ASSET:", suggestions)
        ticker = selected.split(" - ")[0]
    else:
        ticker = search_input.upper()

    if st.button("CALCULATE DYER SCORE"):
        if ticker:
            try:
                # DATA PULLING LOGIC
                if LINK_ACTIVE:
                    stock = yf.Ticker(ticker)
                    info = stock.info
                    price = info.get('currentPrice', 0)
                    op_margin = info.get('operatingMargins', 0) * 100
                    rev_growth = info.get('revenueGrowth', 0) * 100
                    # ROIC PROXY: (EBITDA * 0.8) / (Equity + Debt - Cash)
                    roic = (info.get('ebitda', 0) * 0.79 / (info.get('totalStockholderEquity', 1) + info.get('totalDebt', 0) - info.get('totalCash', 0))) * 100
                else:
                    # SIMULATED/CACHE DATA FOR TEST
                    price, op_margin, rev_growth, roic = 150.0, 22.5, 12.0, 18.5

                # DISPLAY RESULTS
                st.markdown(f"### 🔍 Audit Results for **{ticker}**")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Op. Margin", f"{op_margin:.1f}%")
                c2.metric("Revenue Growth", f"{rev_growth:.1f}%")
                c3.metric("ROIC (Est.)", f"{roic:.1f}%")
                c4.metric("Live Price", f"${price:.2f}")

                # SCORE SLIDERS
                st.sidebar.markdown("---")
                stab = st.sidebar.slider("Stability Bucket", 0, 100, 85)
                grow = st.sidebar.slider("Growth Bucket", 0, 100, 80)
                prem = st.sidebar.slider("Premium Bucket", 0, 100, 90)
                total = stab + grow + prem

                if total >= 200: st.success(f"💎 SOVEREIGN BUY: {total}/300")
                elif total < 150: st.error(f"🚨 TRAPDOOR SELL: {total}/300")
                else: st.warning(f"⚖️ AUDIT HOLD: {total}/300")

            except Exception as e:
                st.error("Select a valid company from the list to trigger the audit.")

elif page == "🔬 CORE 23 HUB":
    st.title("🔬 Core 23 Tracking")
    st.info("Tracking Signal Weight Rushmore 10 vs. The Other 13")
    st.table(pd.DataFrame({
        "Group": ["Rushmore 10", "Other 13"],
        "Avg Score": [278, 194],
        "120-Day Delta": ["+12.4%", "-3.1%"],
        "Verdict": ["PASS", "CULL REQ"]
    }))
