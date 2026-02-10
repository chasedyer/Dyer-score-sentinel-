import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# --- 1. SETTINGS ---
st.set_page_config(page_title="Dyer Global Audit", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; margin-bottom: 0px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; }
    .metric-box { background: #161B22; border: 1px solid #30363D; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LIVE DATA ENGINE ---
def get_ticker_suggestions(query):
    if not query or len(query) < 2: return []
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers).json()
        return [f"{q['symbol']} - {q['shortname']}" for q in response.get('quotes', []) if 'symbol' in q]
    except: return []

# --- 3. DASHBOARD NAVIGATION ---
page = st.sidebar.radio("COMMAND CENTER", ["📡 GLOBAL SCANNER", "🔬 CORE 23 HUB", "🏆 AUDITOR PODIUM"])

if page == "📡 GLOBAL SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">LIVE FORENSIC AUDIT | MARGINS | GROWTH | ROIC</p>', unsafe_allow_html=True)

    # SEARCH
    search_query = st.text_input("ENTER COMPANY NAME", placeholder="Search for any S&P 500 / Russell / Nasdaq name...")
    suggestions = get_ticker_suggestions(search_query)
    
    if suggestions:
        selected = st.selectbox("CONFIRM ASSET:", suggestions)
        ticker = selected.split(" - ")[0]
    else:
        ticker = search_query.upper()

    if st.button("CALCULATE DYER SCORE"):
        if ticker:
            try:
                with st.spinner(f"Running Forensic Scan on {ticker}..."):
                    stock = yf.Ticker(ticker)
                    info = stock.info
                    
                    # --- VITAL EXTRACTION ---
                    # Margins
                    op_margin = info.get('operatingMargins', 0) * 100
                    net_margin = info.get('profitMargins', 0) * 100
                    
                    # Growth
                    rev_growth = info.get('revenueGrowth', 0) * 100
                    
                    # ROIC Calculation: NOPAT / (Equity + Debt - Cash)
                    ebit = info.get('ebitda', 1) * 0.8 # Rough NOPAT proxy if EBIT not available
                    equity = info.get('totalStockholderEquity', 1)
                    debt = info.get('totalDebt', 0)
                    cash = info.get('totalCash', 0)
                    roic = (ebit / (equity + debt - cash)) * 100 if (equity + debt - cash) != 0 else 0

                    # --- UI DISPLAY ---
                    st.markdown("### 📊 Live Forensic Vitals")
                    v1, v2, v3, v4 = st.columns(4)
                    v1.metric("Op. Margin", f"{op_margin:.1f}%")
                    v2.metric("Rev. Growth (YoY)", f"{rev_growth:.1f}%")
                    v3.metric("ROIC (Est.)", f"{roic:.1f}%")
                    v4.metric("Net Margin", f"{net_margin:.1f}%")

                    # --- DYER SCORE SECTION ---
                    st.sidebar.markdown("---")
                    st.sidebar.subheader("Adjust Rushmore Buckets")
                    stab = st.sidebar.slider("Stability (Asset Quality)", 0, 100, int(op_margin * 2 if op_margin < 50 else 90))
                    grow = st.sidebar.slider("Growth (Expansion)", 0, 100, int(rev_growth * 3 if rev_growth < 30 else 95))
                    prem = st.sidebar.slider("Premium (Management)", 0, 100, 85)
                    
                    total_score = stab + grow + prem
                    
                    st.markdown("---")
                    if total_score >= 200:
                        st.success(f"💎 {ticker} VERDICT: SOVEREIGN BUY ({total_score}/300)")
                    elif total_score < 150:
                        st.error(f"🚨 {ticker} VERDICT: TRAPDOOR SELL ({total_score}/300)")
                    else:
                        st.warning(f"⚖️ {ticker} VERDICT: AUDIT HOLD ({total_score}/300)")

            except Exception as e:
                st.error("Select a company from the dropdown to initialize the live data link.")

elif page == "🔬 CORE 23 HUB":
    st.title("🔬 Core 23 Tracking")
    st.write("Current Audit Cycle: **Day 36 / 120**")
    # Tracker for your specific 10 vs 13 setup
    st.table(pd.DataFrame({
        "Metric": ["Avg Dyer Score", "Avg ROIC", "Avg Margin"],
        "Rushmore 10": [278, "24.5%", "32.1%"],
        "Remaining 13": [191, "12.8%", "14.5%"]
    }))
