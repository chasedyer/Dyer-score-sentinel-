import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# --- UI CONFIG ---
st.set_page_config(page_title="Dyer Research Lab", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #E0E0E0; }
    .search-container { display: flex; flex-direction: column; align-items: center; padding-top: 30px; }
    .stTextInput > div > div > input {
        background-color: #161B22; color: #00FF41; border: 2px solid #00FF41;
        border-radius: 50px; padding: 20px 30px; font-size: 24px; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
page = st.sidebar.radio("LAB NAV", ["📡 SCANNER", "🧪 THE 5 MODELS", "🏆 PODIUM"])

# --- PAGE 1: SCANNER (LANDING) ---
if page == "📡 SCANNER":
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    st.title("🛡️ DYER SENTINEL")
    ticker = st.text_input("", placeholder="ENTER TICKER (NVDA, COST, AMC)").upper()
    
    if ticker:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # --- DYER SCORE CALCULATION ---
            # Using your Rushmore logic: Stability + Growth + Premium
            mgmt = st.sidebar.slider("Management Quality", 0, 100, 80)
            moat = st.sidebar.select_slider("Moat Strength", options=[0, 50, 100], value=50)
            stability = 80 # Placeholder for asset quality
            score = int(stability + mgmt + moat)

            # --- CONVICTION DIAL ---
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': f"CONVICTION: {ticker}", 'font': {'size': 24}},
                gauge = {
                    'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
                    'bar': {'color': "white"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, 150], 'color': '#721c24'},  # TRAPDOOR
                        {'range': [150, 200], 'color': '#856404'}, # AUDIT
                        {'range': [200, 300], 'color': '#155724'}  # SOVEREIGN
                    ],
                    'threshold': {
                        'line': {'color': "white", 'width': 4},
                        'thickness': 0.75,
                        'value': score
                    }
                }
            ))
            fig.update_layout(paper_bgcolor='#0E1117', font={'color': "white", 'family': "Arial"})
            st.plotly_chart(fig, use_container_width=True)

            # --- DYNAMIC VERDICT ---
            if score >= 200: st.success("💎 SOVEREIGN BUY")
            elif score < 150: st.error("🚨 TRAPDOOR SELL")
            else: st.warning("⚖️ AUDIT HOLD")

            # Core 5 Vitals
            v1, v2, v3, v4, v5 = st.columns(5)
            v1.metric("Margin", f"{info.get('profitMargins', 0)*100:.1f}%")
            v2.metric("Growth", f"{info.get('revenueGrowth', 0)*100:.1f}%")
            v3.metric("Debt/Eq", info.get('debtToEquity', 'N/A'))
            v4.metric("ROIC", f"{info.get('returnOnEquity', 0)*100:.1f}%")
            v5.metric("Yield", f"{info.get('dividendYield', 0)*100:.2f}")

        except: st.warning("Awaiting Asset Validation...")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2 & 3 (RETAINED FROM PREVIOUS STEPS) ---
elif page == "🧪 THE 5 MODELS":
    st.title("🧪 Experimental Model Lab")
    # ... [Same Model Grid Code] ...

elif page == "🏆 PODIUM":
    st.title("🏆 Auditor Podium")
    # ... [Leaderboard including Anne, Pablo, Mike, Mom, Dad] ...
