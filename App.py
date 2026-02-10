import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# --- 1. SETTINGS ---
st.set_page_config(page_title="Dyer Global Audit Terminal", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 48px; font-weight: bold; color: #00FF41; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; }
    .metric-card { background-color: #161B22; border: 1px solid #30363D; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LIVE SEARCH ENGINE ---
def find_ticker(query):
    if not query or len(query) < 2: return []
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers).json()
        return [f"{q['symbol']} - {q['shortname']}" for q in r.get('quotes', []) if 'symbol' in q]
    except: return []

# --- 3. PAGE LOGIC ---
st.sidebar.title("🛡️ LAB CONTROL")
page = st.sidebar.radio("NAVIGATE", ["📡 GLOBAL SCANNER", "🔬 CORE 23 TRACKER", "🏆 AUDITOR PODIUM"])

if page == "📡 GLOBAL SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    # SEARCH BAR
    search_query = st.text_input("ENTER COMPANY NAME (e.g. Costco, Apple, Tesla)", "")
    options = find_ticker(search_query)
    
    if options:
        selection = st.selectbox("SELECT MATCHING COMPANY:", options)
        ticker = selection.split(" - ")[0]
    else:
        ticker = search_query.upper()

    if st.button("CALCULATE DYER SCORE"):
        if ticker:
            try:
                with st.spinner(f"Pulling Forensic Vitals for {ticker}..."):
                    stock = yf.Ticker(ticker)
                    info = stock.info
                    
                    # RAW DATA PULL
                    price = info.get('currentPrice') or info.get('regularMarketPrice')
                    op_margin = info.get('operatingMargins', 0) * 100
                    rev_growth = info.get('revenueGrowth', 0) * 100
                    
                    # ROIC CALCULATION (Forensic Proxy)
                    ebitda = info.get('ebitda', 0)
                    tax_rate = 0.21
                    nopat = ebitda * (1 - tax_rate)
                    equity = info.get('totalStockholderEquity', 1)
                    debt = info.get('totalDebt', 0)
                    cash = info.get('totalCash', 0)
                    invested_capital = (equity + debt - cash)
                    roic = (nopat / invested_capital) * 100 if invested_capital > 0 else 0

                    # UI DISPLAY
                    st.markdown("### 📊 Forensic Vitals (Live Exchange Data)")
                    v1, v2, v3, v4 = st.columns(4)
                    v1.metric("Op. Margin", f"{op_margin:.2f}%")
                    v2.metric("Rev Growth (YoY)", f"{rev_growth:.2f}%")
                    v3.metric("ROIC (Est.)", f"{roic:.2f}%")
                    v4.metric("Live Price", f"${price:.2f}")

                    # DYER SCORE BUCKETS
                    st.sidebar.markdown("---")
                    st.sidebar.subheader("Adjust Rushmore Buckets")
                    stability = st.sidebar.slider("Stability (Asset Quality)", 0, 100, 85)
                    growth = st.sidebar.slider("Growth (Capacity)", 0, 100, 80)
                    premium = st.sidebar.slider("Premium (Moat)", 0, 100, 90)
                    
                    final_score = stability + growth + premium
                    
                    st.markdown("---")
                    if final_score >= 200:
                        st.success(f"💎 {ticker} VERDICT: SOVEREIGN BUY ({final_score}/300)")
                    elif final_score < 150:
                        st.error(f"🚨 {ticker} VERDICT: TRAPDOOR SELL ({final_score}/300)")
                    else:
                        st.warning(f"⚖️ {ticker} VERDICT: AUDIT HOLD ({final_score}/300)")
                    
                    st.progress(final_score / 300)

            except Exception as e:
                st.error(f"Data pull failed for {ticker}. Ensure you selected from the dropdown.")

elif page == "🔬 CORE 23 TRACKER":
    st.title("🔬 Core 23 Tracking")
    st.write("Current Audit Cycle: **Day 36 / 120**")
    st.table(pd.DataFrame({
        "Model": ["Rushmore 10 (Signal Weight)", "Remaining 13"],
        "Avg Score": [278, 191],
        "ROIC Avg": ["24.2%", "11.5%"],
        "Status": ["PASS", "AUDIT REQ"]
    }))

elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 Auditor Leaderboard")
    st.table(pd.DataFrame({
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD"],
        "Points": [1500, 1250, 1100, 950, 450, 300],
        "Level": ["Chapter 14", "Chapter 12", "Chapter 11", "Chapter 9", "Chapter 4", "Chapter 2"]
    }))
