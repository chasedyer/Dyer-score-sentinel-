import streamlit as st
import pandas as pd

# --- 1. TICKER INTELLIGENCE LIBRARY ---
# This ensures that Rivian and Costco do NOT start with the same score.
TICKER_DATA = {
    "COST": {"s": 95, "g": 85, "p": 98, "name": "Costco Wholesale"},
    "RIVN": {"s": 20, "g": 60, "p": 30, "name": "Rivian Automotive"},
    "MSFT": {"s": 92, "g": 80, "p": 95, "name": "Microsoft Corp"},
    "NVDA": {"s": 85, "g": 98, "p": 90, "name": "Nvidia Corp"}
}

if 'audit_history' not in st.session_state:
    st.session_state.audit_history = {}

# --- 2. UI SETTINGS ---
st.set_page_config(page_title="Dyer Global Audit", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; }
    .metric-header { color: #00FF41; font-weight: bold; font-size: 22px; border-bottom: 2px solid #30363D; margin-bottom: 10px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. NAVIGATION ---
page = st.sidebar.radio("COMMAND CENTER", ["📡 DYER SCANNER", "🔬 5* MODELS HUB"])

if page == "📡 DYER SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    ticker = st.text_input("ENTER TICKER (e.g., COST, RIVN)", "COST").upper()
    
    # DYNAMIC SCORE LOADING
    # If the ticker is in our library, use those scores. Otherwise, use 50.
    defaults = TICKER_DATA.get(ticker, {"s": 50, "g": 50, "p": 50})

    st.markdown(f"### 📥 Forensic Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    # Using 'key' ensures Streamlit keeps these inputs unique to the ticker
    with c1: s = st.number_input("STABILITY", 0, 100, defaults['s'], key=f"{ticker}_s")
    with c2: g = st.number_input("GROWTH", 0, 100, defaults['g'], key=f"{ticker}_g")
    with c3: p = st.number_input("PREMIUM", 0, 100, defaults['p'], key=f"{ticker}_p")
    
    total = s + g + p

    if st.button("SYNC AUDIT TO MODELS"):
        st.session_state.audit_history[ticker] = {"Total": total, "S": s, "G": g, "P": p}
        st.success(f"Audit for {ticker} Synced. Total Dyer Score: {total}")

    # Sub-part display logic remains the same...

elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Performance")
    
    if st.session_state.audit_history:
        # CONVERT HISTORY TO TABLE
        df = pd.DataFrame.from_dict(st.session_state.audit_history, orient='index')
        st.table(df)
        
        # AGGREGATED CALCULATION
        avg_score = df['Total'].mean()
        st.metric("Aggregated Portfolio Dyer Score", f"{avg_score:.1f} / 300")
    else:
        st.warning("No data found. Please run audits in the Scanner first.")
