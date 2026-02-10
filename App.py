import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Dyer Score Sentinel", layout="wide")

# --- Sovereign Admin Logic ---
if 'query_log' not in st.session_state:
    st.session_state.query_log = []

st.sidebar.title("🛡️ Sentinel Access")
sovereign_id = st.sidebar.text_input("Enter Sovereign ID", value="SOVEREIGN-01")
is_admin = sovereign_id == "SOVEREIGN-00"

# --- Main App ---
st.title("The Dyer Score™")
ticker = st.text_input("Enter Ticker", value="NVDA").upper()

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # 1. Forensic Metrics (The Top 5)
        # Pulling actual data from yfinance for the Top 5
        metrics = {
            "Profit Margin": info.get('profitMargins', 0) * 100,
            "Rev Growth": info.get('revenueGrowth', 0) * 100,
            "Debt-to-Equity": info.get('debtToEquity', 0),
            "ROIC": info.get('returnOnAssets', 0) * 100, # Proxy for ROIC
            "Cash Flow": info.get('freeCashflow', 0) / 1e9 # In Billions
        }

        # 2. Forensic Inputs (Manual Sliders)
        st.subheader("Forensic Audit Inputs")
        col_m, col_moat = st.columns(2)
        with col_m:
            mgmt = st.slider("Management Quality", 0, 100, 85, key=f"mgmt_{ticker}")
        with col_moat:
            moat = st.select_slider("Moat Capacity", options=["Decaying", "Stable", "Expanding"], value="Stable", key=f"moat_{ticker}")
        
        moat_pts = {"Decaying": 0, "Stable": 50, "Expanding": 100}[moat]
        
        # Final Score Calculation
        # Simple formula: (De-risked Stability) + Management + Moat
        de_risk = max(0, 100 - (metrics["Debt-to-Equity"] / 5))
        final_score = int(de_risk + mgmt + moat_pts)

        # --- THE THREE CLOCKS (Visual Status) ---
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        
        def get_status(score):
            if score < 150: return "🔴 SELL", "#FF4B4B"
            if score < 240: return "🟡 HOLD", "#FFAA00"
            return "🟢 BUY", "#00CC96"

        status, color = get_status(final_score)

        with c1:
            st.metric("3 MONTH OUTLOOK", status)
            st.caption("Short-term Asset Quality")
        with c2:
            st.metric("6 MONTH OUTLOOK", status)
            st.caption("Expansion Capacity")
        with c3:
            st.metric("12 MONTH OUTLOOK", status)
            st.caption("Sovereign Trajectory")

        # --- TOP 5 FORENSIC DATA ---
        st.markdown(f"### Top 5 Forensic Metrics for {ticker}")
        f_cols = st.columns(5)
        for i, (name, val) in enumerate(metrics.items()):
            f_cols[i].metric(name, f"{val:.1f}")

        # --- ADMIN LOGGING ---
        if st.button("Flag for Steve (Gold LLC)"):
            st.session_state.query_log.append({"ID": sovereign_id, "Ticker": ticker, "Score": final_score})
            st.success("Flagged for Audit Review.")

    except Exception as e:
        st.error(f"Search for a valid Ticker to begin. Error: {e}")

if is_admin:
    st.sidebar.markdown("---")
    st.sidebar.write("### Auditor Master Log")
    st.sidebar.dataframe(pd.DataFrame(st.session_state.query_log))
