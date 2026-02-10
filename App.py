import streamlit as st
import pandas as pd

# 1. THE 5* MODELS PERFORMANCE (STATICS)
# Tracking performance pro-rated for Day 36 of the 120-Day Cycle
model_data = {
    "Model": ["Model A (Cull)", "Model B (Reset)", "Model C", "Model D", "Model E (Anti)"],
    "Aggregated Dyer Score": [268, 242, 275, 255, 118],
    "120-Day Performance %": [14.2, 8.1, 19.5, 4.3, -22.8]
}

# 2. TICKER-SPECIFIC FORENSIC PROFILES
# Hard-coded to prevent the "Same Score" error
PROFILES = {
    "COST": {"S": 95, "G": 85, "P": 98},
    "MSFT": {"S": 92, "G": 82, "P": 94},
    "RIVN": {"S": 22, "G": 55, "P": 31},
    "GEVO": {"S": 12, "G": 45, "P": 15}
}

st.title("🛡️ DYER GLOBAL TERMINAL")

# 3. 5* MODELS HUB (PERFORMANCE ONLY)
st.subheader("🔬 5* Models Performance")
st.table(pd.DataFrame(model_data))

st.markdown("---")

# 4. DYER SCANNER (SUB-PARTS)
st.subheader("📡 Dyer Forensic Scanner")
ticker = st.text_input("ENTER TICKER", "COST").upper()

# Pulling specific profile data
vals = PROFILES.get(ticker, {"S": 50, "G": 50, "P": 50})

col1, col2, col3 = st.columns(3)
with col1:
    s_val = st.number_input("Stability", 0, 100, vals["S"], key=f"{ticker}_s")
with col2:
    g_val = st.number_input("Growth", 0, 100, vals["G"], key=f"{ticker}_g")
with col3:
    p_val = st.number_input("Premium", 0, 100, vals["P"], key=f"{ticker}_p")

total = s_val + g_val + p_val

# DISPLAY RAW VALUE
st.markdown(f"### {ticker} Total Dyer Score: **{total}**")

# TOP 3 METRICS PER SCORE (SUB-PARTS)
f1, f2, f3 = st.columns(3)
with f1:
    st.info(f"**STABILITY: {s_val}**\n\n1. Op. Margin\n2. ROIC\n3. Debt/Equity")
with f2:
    st.info(f"**GROWTH: {g_val}**\n\n1. Rev Growth\n2. Market Share\n3. Capex")
with f3:
    st.info(f"**PREMIUM: {p_val}**\n\n1. Founder\n2. Pricing Power\n3. Moat")
