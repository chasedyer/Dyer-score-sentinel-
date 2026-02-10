import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# --- 1. SETTINGS ---
st.set_page_config(page_title="Dyer Global Audit", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; margin-bottom: 5px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. COMPANY-TO-TICKER ENGINE ---
def get_ticker_suggestions(query):
    """Fetches stock suggestions from Yahoo Finance based on company name."""
    if not query or len(query) < 2:
        return []
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}&quotes_count=5"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers).json()
        # Returns a list of strings like "COST - Costco Wholesale Corporation"
        return [f"{q['symbol']} - {q['shortname']}" for q in response.get('quotes', []) if q.get('shortname')]
    except:
        return []

# --- 3. NAVIGATION ---
page = st.sidebar.radio("COMMAND CENTER", ["📡 GLOBAL SCANNER", "🔬 CORE 23 TRACKER", "🧪 MODEL A/B LOGIC", "🏆 AUDITOR PODIUM"])

# --- 4. PAGE 1: GLOBAL SCANNER (WITH AUTOFILL) ---
if page == "📡 GLOBAL SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">SEARCH BY NAME OR TICKER | UNIVERSAL AUDIT</p>', unsafe_allow_html=True)

    # SEARCH VAULT WITH DROPDOWN
    search_query = st.text_input("ENTER COMPANY NAME OR TICKER", placeholder="e.g. Costco, Nvidia, Microsoft...")
    
    suggestions = get_ticker_suggestions(search_query)
    
    if suggestions:
        selected_option = st.selectbox("DID YOU MEAN?", suggestions)
        final_ticker = selected_option.split(" - ")[0]
    else:
        final_ticker = search_query.upper()

    if st.button("CALCULATE DYER SCORE"):
        if final_ticker:
            try:
                with st.spinner(f"Auditing {final_ticker}..."):
                    asset = yf.Ticker(final_ticker)
                    price = asset.fast_info['last_price']
                    
                    # DYER SCORE (The 300 Point Rushmore Bucket)
                    st.sidebar.subheader("Forensic Parameters")
                    stability = st.sidebar.slider("Asset Quality (Stability)", 0, 100, 85)
                    growth = st.sidebar.slider("Expansion Capacity (Growth)", 0, 100, 80)
                    premium = st.sidebar.slider("Management/Moat (Premium)", 0, 100, 90)
                    total_score = stability + growth + premium
                    
                    # VERDICT DISPLAY
                    st.markdown("---")
                    if total_score >= 200:
                        st.success(f"💎 {final_ticker} SCORE: {total_score}/300 | SOVEREIGN BUY")
                    elif total_score < 150:
                        st.error(f"🚨 {final_ticker} SCORE: {total_score}/300 | TRAPDOOR SELL")
                    else:
                        st.warning(f"⚖️ {final_ticker} SCORE: {total_score}/300 | AUDIT HOLD")
                    
                    st.progress(total_score / 300)

                    # VITALS GRID
                    v1, v2, v3 = st.columns(3)
                    v1.metric("Live Price", f"${price:.2f}")
                    v2.metric("Rushmore Score", f"{total_score}/300")
                    v3.metric("Audit Status", "Day 36 / 120")
            except:
                st.error("Select a valid company from the dropdown to calculate.")

# --- 5. PAGE 2: CORE 23 TRACKER ---
elif page == "🔬 CORE 23 TRACKER":
    st.title("🔬 Core 23 Performance Hub")
    st.info("Tracking Rushmore 10 vs Remaining 13 as of today.")
    st.metric("Rushmore 10 Avg Score", "278", delta="+10% Threshold Met")
    st.metric("Remaining 13 Avg Score", "185", delta="-5% Audit Required")

# --- 6. PAGE 4: PODIUM ---
elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 Global Auditor Podium")
    df = pd.DataFrame({
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Rank": ["C-14", "C-12", "C-11", "C-09", "C-04", "C-02", "Pending"]
    })
    st.table(df)
