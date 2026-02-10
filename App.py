import streamlit as st
import yfinance as yf
import pandas as pd

# Page Config for professional look
st.set_page_config(page_title="Dyer Score Sentinel", page_icon="🛡️")

# --- Sovereign ID Logic ---
if 'query_log' not in st.session_state:
    st.session_state.query_log = []

st.sidebar.title("🛡️ Sentinel Access")
sovereign_id = st.sidebar.text_input("Enter Sovereign ID", value="SOVEREIGN-01")
is_admin = sovereign_id == "SOVEREIGN-00" # Your Admin ID

# --- The App Interface ---
st.title("The Dyer Score™")
st.markdown("---")

ticker = st.text_input("Enter Ticker for Audit", value="COST").upper()

if ticker:
    try:
        # Data Capture
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # 1. Stability (Asset Quality) - Auto-calculated
        current_ratio = info.get('currentRatio', 1.0)
        debt_to_equity = info.get('debtToEquity', 100)
        stability_base = 100 * (min(current_ratio, 2.0) / 2.0)
        
        # 2. Premium & Growth - Manual Forensic Inputs
        st.subheader("Forensic Inputs")
        col1, col2 = st.columns(2)
        with col1:
            management_trust = st.slider("Management Quality (0-100)", 0, 100, 80)
        with col2:
            moat_strength = st.select_slider("Moat Capacity", options=["Decaying", "Stable", "Expanding"])
        
        moat_bonus = {"Decaying": 0, "Stable": 50, "Expanding": 100}[moat_strength]
        
        # --- THE DYER SCORE CALCULATION ---
        # 300 Point Scale: 100 Stability + 100 Management + 100 Moat/Growth
        dyer_score = int(stability_base + (management_trust) + (moat_bonus * 0.5))
        
        # Display the Score
        st.markdown(f"<h1 style='text-align: center;'>{dyer_score} / 300</h1>", unsafe_allow_html=True)
        
        # Judgment logic
        if dyer_score >= 250:
            st.success("🟢 SOVEREIGN STATUS: Strong Expansion Capacity.")
        elif dyer_score >= 150:
            st.warning("🟡 MONITOR: Dyer Score shows neutral divergence.")
        else:
            st.error("🔴 TRAPDOOR: Asset is failing the Dyer Metric. Avoid.")

        # Log the Query
        st.session_state.query_log.append({"ID": sovereign_id, "Ticker": ticker, "Score": dyer_score})

    except Exception as e:
        st.error(f"Ticker not found or data unavailable: {e}")

# --- Admin View ---
if is_admin:
    st.sidebar.markdown("---")
    st.sidebar.subheader("Audit Log (Admin Only)")
    st.sidebar.write(pd.DataFrame(st.session_state.query_log))
