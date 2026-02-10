import streamlit as st
import pandas as pd

# --- 1. EXPANDED TICKER LIBRARY ---
# Unique profiles to prevent the "Same Score" error.
PROFILES = {
    "COST": {"s": 95, "g": 85, "p": 98},
    "MSFT": {"s": 92, "g": 82, "p": 94},
    "RIVN": {"s": 22, "g": 55, "p": 31},
    "GEVO": {"s": 12, "g": 45, "p": 15}  # Lower stability/premium than RIVN
}

if 'audit_log' not in st.session_state:
    st.session_state.audit_log = {}

# --- 2. SCANNER (Simplified) ---
ticker = st.text_input("ENTER TICKER", "COST").upper()
data = PROFILES.get(ticker, {"s": 50, "g": 50, "p": 50})

st.write(f"### Raw Score Audit: {ticker}")
c1, c2, c3 = st.columns(3)
with c1: s = st.number_input("STABILITY", 0, 100, data['s'], key=f"{ticker}_s")
with c2: g = st.number_input("GROWTH", 0, 100, data['g'], key=f"{ticker}_g")
with c3: p = st.number_input("PREMIUM", 0, 100, data['p'], key=f"{ticker}_p")

total = s + g + p

if st.button("SYNC TO MODELS"):
    st.session_state.audit_log[ticker] = total
    st.success(f"{ticker} Total: {total}")

# --- 3. PERFORMANCE HUB ---
st.write("### 🔬 Model Performance Only")
if st.session_state.audit_log:
    # Just track the performance/score of the current audits
    st.dataframe(pd.DataFrame(st.session_state.audit_log.items(), columns=['Ticker', 'Dyer Score']))
