import streamlit as st
import pandas as pd

# --- 1. TICKER PROFILE LIBRARY ---
TICKER_PROFILES = {
    "COST": {"s": 95, "g": 85, "p": 98},
    "RIVN": {"s": 22, "g": 55, "p": 31},
    "MSFT": {"s": 90, "g": 82, "p": 94},
    "NVDA": {"s": 88, "g": 95, "p": 92}
}

# Persistent Storage
if 'audit_log' not in st.session_state:
    st.session_state.audit_log = {}

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

# --- 4. PAGE 1: SCANNER & SUB-PARTS ---
if page == "📡 DYER SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    ticker = st.text_input("ENTER TICKER", "COST").upper()
    
    # Load profile or use generic 50
    profile = TICKER_PROFILES.get(ticker, {"s": 50, "g": 50, "p": 50})

    st.markdown(f"### 📊 Raw Score Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    
    # Static inputs without delta logic
    with c1: s = st.number_input("STABILITY", 0, 100, profile['s'], key=f"{ticker}_s_val")
    with c2: g = st.number_input("GROWTH", 0, 100, profile['g'], key=f"{ticker}_g_val")
    with c3: p = st.number_input("PREMIUM", 0, 100, profile['p'], key=f"{ticker}_p_val")
    
    total = s + g + p

    if st.button("UPDATE CORE MODELS"):
        st.session_state.audit_log[ticker] = {"Dyer Score": total, "Stability": s, "Growth": g, "Premium": p}
        st.success(f"Dyer Score for {ticker} updated to {total}")

    # Sub-part display
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown('<div class="metric-header">STABILITY</div>', unsafe_allow_html=True)
        st.write(f"Value: {s}")
    with f2:
        st.markdown('<div class="metric-header">GROWTH</div>', unsafe_allow_html=True)
        st.write(f"Value: {g}")
    with f3:
        st.markdown('<div class="metric-header">PREMIUM</div>', unsafe_allow_html=True)
        st.write(f"Value: {p}")

# --- 5. PAGE 2: 5* MODELS HUB ---
elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Hub: Value Aggregation")
    
    if st.session_state.audit_log:
        df = pd.DataFrame.from_dict(st.session_state.audit_log, orient='index')
        
        # Display clean table
        st.table(df)
        
        # Aggregate Value
        agg_val = df['Dyer Score'].mean()
        st.metric("Aggregated Portfolio Value", f"{agg_val:.1f}")
    else:
        st.warning("No audit values detected. Return to Scanner to input data.")
