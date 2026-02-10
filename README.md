import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Dyer Score Sentinel", page_icon="🛡️")

# Initialize log
if 'query_log' not in st.session_state:
    st.session_state.query_log = []

st.sidebar.title("🛡️ Sentinel Access")
sovereign_id = st.sidebar.text_input("Enter Sovereign ID", value="SOVEREIGN-01")
is_admin = sovereign_id == "SOVEREIGN-00"

st.title("The Dyer Score™")
st.markdown("---")

ticker = st.text_input("Enter Ticker (e.g., WMT, COIN, COST)", value="WMT").upper()

if ticker:
    try:
        # Pulling Data
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # 1. Stability (Data-Driven)
        de_ratio = info.get('debtToEquity', 100)
        stability_score = max(0, 100 - (de_ratio / 5))
        
        st.subheader(f"Forensic Audit: {ticker}")
        col1, col2 = st.columns(2)
        
        with col1:
            # Added unique key tied to ticker
            management_trust = st.slider(
                "Management Quality", 0, 100, 85, 
                key=f"mgmt_{ticker}"
            )
        
        with col2:
            # Added unique key tied to ticker + default 'Stable'
            moat_status = st.select_slider(
                "Moat Capacity", 
                options=["Decaying", "Stable", "Expanding"],
                value="Stable",
                key=f"moat_{ticker}"
            )
        
        # Logic for Moat Points
        moat_points = {"Decaying": 0, "Stable": 50, "Expanding": 100}[moat_status]
        
        # FINAL SCORE
        dyer_score = int(stability_score + management_trust + moat_points)
        
        # Big Score Display
        st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>Dyer Score: {dyer_score} / 300</h1>", unsafe_allow_html=True)
        
        # Verdicts
        if dyer_score >= 240:
            st.success("🟢 SOVEREIGN STATUS")
        elif dyer_score >= 160:
            st.warning("🟡 MONITOR STATUS")
        else:
            st.error("🔴 TRAPDOOR ALERT")

    except Exception as e:
        st.error(f"Waiting for valid Ticker... (Error: {e})")

# Admin Log
if is_admin:
    st.sidebar.write("### Auditor Log", pd.DataFrame(st.session_state.query_log))
