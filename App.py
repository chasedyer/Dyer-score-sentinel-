import streamlit as st
import yfinance as yf
import pandas as pd

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Dyer Research Lab", layout="wide")

# Custom CSS for the "Command Bar" look
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 45px; font-weight: bold; color: #00FF41; margin-top: 10px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #00FF41; color: black; font-weight: bold; }
    .model-card { background-color: #1C2128; border: 1px solid #30363D; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
page = st.sidebar.radio("LAB NAVIGATION", ["📡 SCANNER", "🧪 THE 5 MODELS", "🏆 AUDITOR PODIUM"])

# --- 3. PAGE 1: SCANNER (LANDING PAGE) ---
if page == "📡 SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">14 CHAPTER RESEARCH | 120-DAY AUDIT CYCLE</p>', unsafe_allow_html=True)
    
    # The Search UI
    col1, col2 = st.columns([4, 1])
    with col1:
        ticker_input = st.text_input("ENTER TICKER", value="COST", placeholder="e.g. NVDA, AMC, TSLA").upper()
    with col2:
        st.write(" ") # Padding
        st.write(" ") # Padding
        run_scan = st.button("RUN SCAN")

    if run_scan or ticker_input:
        try:
            with st.spinner('Accessing Exchange...'):
                stock = yf.Ticker(ticker_input)
                # Using fast_info for speed and stability
                price = stock.fast_info['last_price']
                
                # Dyer Score Logic (Rushmore Metric)
                st.sidebar.subheader("Forensic Controls")
                mgmt = st.sidebar.slider("Management Quality", 0, 100, 85)
                moat = st.sidebar.select_slider("Moat Strength", options=[0, 50, 100], value=50)
                score = 100 + mgmt + moat
                
                # THE VERDICT DIAL (Simplified to 3 Color Zones)
                st.markdown("---")
                if score < 150:
                    st.error(f"VERDICT: {score}/300 | 🚨 TRAPDOOR SELL")
                    verdict_icon = "🔴"
                elif score >= 200:
                    st.success(f"VERDICT: {score}/300 | 💎 SOVEREIGN BUY")
                    verdict_icon = "🟢"
                else:
                    st.warning(f"VERDICT: {score}/300 | ⚖️ AUDIT HOLD")
                    verdict_icon = "🟡"
                
                st.progress(score / 300)

                # Forensic Vitals Grid
                v1, v2, v3 = st.columns(3)
                v1.metric(f"Current {ticker_input}", f"${price:.2f}")
                v2.metric("Rushmore Score", f"{score}/300")
                v3.metric("Conviction Status", verdict_icon)
                
                # Information block
                st.markdown("---")
                if st.button("📤 GENERATE REPORT"):
                    st.code(f"🛡️ Dyer Audit: ${ticker_input}\n🎯 Score: {score}/300\nStatus: {verdict_icon}\n#DyerSentinel")

        except Exception as e:
            st.error("Connection Error. Ensure ticker is valid and internet is active.")

# --- 4. PAGE 2: THE 5 MODELS ---
elif page == "🧪 THE 5 MODELS":
    st.title("🧪 The 5 Experimental Models")
    m_cols = st.columns(5)
    model_data = [
        ("MODEL A", "Cull Strategy", 245, "PASSING"),
        ("MODEL B", "90-Day Rebalance", 210, "STABLE"),
        ("MODEL C", "High Premium", 265, "PASSING"),
        ("MODEL D", "Value/Asset", 185, "FAILING"),
        ("MODEL E", "Anti-Model", 82, "TRAPDOOR")
    ]
    for i, (name, desc, s, status) in enumerate(model_data):
        with m_cols[i]:
            st.markdown(f'<div class="model-card"><h3>{name}</h3><p>{desc}</p><h2>{s}</h2><b>{status}</b></div>', unsafe_allow_html=True)

# --- 5. PAGE 3: PODIUM ---
elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 Auditor Podium")
    podium_data = {
        "Rank": ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"],
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Chapter": ["C-14", "C-12", "C-11", "C-09", "C-04", "C-02", "Pending"]
    }
    st.table(pd.DataFrame(podium_data))
