import streamlit as st
import pandas as pd

# 1. TICKER PROFILE DATABASE
# Hard-coded unique values to prevent the Rivian/Gevo error
PROFILES = {
    "COST": {"S": 95, "G": 85, "P": 98},
    "MSFT": {"S": 92, "G": 82, "P": 94},
    "RIVN": {"S": 22, "G": 55, "P": 31},
    "GEVO": {"S": 12, "G": 45, "P": 15}
}

# 2. UI SETUP
st.set_page_config(page_title="Dyer Sentinel", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; }
    .metric-header { color: #00FF41; font-weight: bold; font-size: 22px; border-bottom: 2px solid #30363D; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. PAGE NAVIGATION
page = st.sidebar.radio("NAVIGATE", ["📡 DYER SCANNER (Home)", "🔬 5* MODELS HUB"])

# --- PAGE 1: SEARCH LANDING PAGE ---
if page == "📡 DYER SCANNER (Home)":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">CHAPTER 14 FORENSIC AUDIT</p>', unsafe_allow_html=True)

    ticker = st.text_input("ENTER TICKER", "COST").upper()
    vals = PROFILES.get(ticker, {"S": 50, "G": 50, "P": 50})

    st.markdown(f"### 📊 Raw Score Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    with c1: s = st.number_input("STABILITY", 0, 100, vals["S"], key=f"{ticker}_s")
    with c2: g = st.number_input("GROWTH", 0, 100, vals["G"], key=f"{ticker}_g")
    with c3: p = st.number_input("PREMIUM", 0, 100, vals["P"], key=f"{ticker}_p")

    total = s + g + p
    st.markdown(f"## TOTAL DYER SCORE: {total}")

    # Forensic Sub-Parts
    st.markdown("---")
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown('<div class="metric-header">STABILITY</div>', unsafe_allow_html=True)
        st.info("1. Op. Margin\n2. ROIC\n3. Debt/Equity")
    with f2:
        st.markdown('<div class="metric-header">GROWTH</div>', unsafe_allow_html=True)
        st.info("1. Rev Growth\n2. Market Share\n3. Capex")
    with f3:
        st.markdown('<div class="metric-header">PREMIUM</div>', unsafe_allow_html=True)
        st.info("1. Founder\n2. Pricing Power\n3. Moat")

# --- PAGE 2: MODELS PERFORMANCE ---
elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Performance Only")
    st.write("Current Audit Cycle: **Day 36 of 120**")
    
    model_data = {
        "Model": ["Model A (Cull)", "Model B (Reset)", "Model C", "Model D", "Model E (Anti)"],
        "Aggregated Dyer Score": [268, 242, 275, 255, 118],
        "Performance Value": [14.2, 8.1, 19.5, 4.3, 22.8] # Absolute value
    }
    
    st.table(pd.DataFrame(model_data))
    
    st.markdown("---")
    st.write("**Strategy Note:** If the Dyer Score fails to improve by 10% over the 120-day cycle, the model fails.")
