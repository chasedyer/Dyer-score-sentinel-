import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Dyer Score Sentinel", page_icon="🛡️")

# --- Sovereign ID Logic ---
if 'query_log' not in st.session_state:
    st.session_state.query_log = []

st.sidebar.title("🛡️ Sentinel Access")
sovereign_id = st.sidebar.text_input("Enter Sovereign ID", value="SOVEREIGN-01")
is_admin = sovereign_id == "SOVEREIGN-00"

st.title("The Dyer Score™")
st.markdown("---")

ticker = st.text_input("Enter Ticker", value="COST").upper()

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # 1. Stability Bucket (100 Points)
        # We look at Debt-to-Equity. If it's over 200, the score drops.
        de_ratio = info.get('debtToEquity', 100)
        stability_score = max(0, 100 - (de_ratio / 5))
        
        # 2. Forensic Inputs (200 Points)
        st.subheader("Forensic Audit Inputs")
        col1, col2 = st.columns(2)
        
        with col1:
            management_trust = st.slider("Management Quality", 0, 100, 85)
        
        with col2:
            # Setting 'Stable' as the default so it doesn't start at 'Decaying'
            moat_status = st.select_slider(
                "Moat Capacity", 
                options=["Decaying", "Stable", "Expanding"],
                value="Stable" 
            )
        
        # Moat Logic: Expanding = 100, Stable = 50, Decaying = 0
        moat_points = {"Decaying": 0, "Stable": 50, "Expanding": 100}[moat_status]
        
        # --- FINAL DYER SCORE ---
        dyer_score = int(stability_score + management_trust + moat_points)
        
        # Visual Gauge
        st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{dyer_score} / 300</h1>", unsafe_allow_html=True)
        
        # The Dyer Verdict
        if dyer_score >= 240:
            st.success("🟢 SOVEREIGN STATUS: Strong Asset Quality & Moat.")
        elif dyer_score >= 160:
            st.warning("🟡 MONITOR: Average quality. No immediate Trapdoor.")
        else:
            st.error("🔴 TRAPDOOR: Asset is failing the Dyer Metric. High Decay Risk.")

    except Exception as e:
        st.error(f"Data Error: {e}")

if is_admin:
    st.sidebar.write("Admin View Active")
