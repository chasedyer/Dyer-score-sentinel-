import streamlit as st
import pandas as pd
import yfinance as yf

# --- UI CONFIG ---
st.set_page_config(page_title="Dyer Research Lab", layout="wide")

# --- CLEAN TERMINAL STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; font-family: 'Helvetica', sans-serif; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; margin-bottom: 0px; color: #00FF41; }
    .stTextInput > div > div > input {
        background-color: #161B22; color: #00FF41; border: 2px solid #00FF41;
        border-radius: 50px; padding: 25px; font-size: 24px; text-align: center;
    }
    .model-card { background-color: #1C2128; border: 1px solid #30363D; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
page = st.sidebar.radio("LAB NAVIGATION", ["📡 SCANNER", "🧪 THE 5 MODELS", "🏆 AUDITOR PODIUM"])

# --- PAGE 1: SCANNER (LANDING) ---
if page == "📡 SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">14 CHAPTER RESEARCH | 120-DAY AUDIT CYCLE</p>', unsafe_allow_html=True)
    
    # The Main Search Bar
    ticker = st.text_input("", placeholder="TYPE TICKER (e.g. NVDA, COST, AMC)").upper()
    
    if ticker:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # DYER SCORE MATH (Rushmore Metric)
            # Stability (Fixed 100) + Management (Slider) + Moat (Select)
            st.sidebar.subheader("Forensic Controls")
            mgmt = st.sidebar.slider("Management Quality", 0, 100, 80)
            moat_opt = st.sidebar.select_slider("Moat Strength", options=["Decaying", "Stable", "Expanding"], value="Stable")
            moat_pts = {"Decaying": 0, "Stable": 50, "Expanding": 100}[moat_opt]
            score = 100 + mgmt + moat_pts

            # THE DIAL (Progress Bar Representation)
            st.markdown("---")
            st.write(f"### CONVICTION DIAL: {ticker}")
            
            # Visual logic for the "Dial"
            if score < 150:
                st.error(f"VERDICT: {score}/300 - 🚨 TRAPDOOR SELL")
                progress_color = "red"
            elif score >= 200:
                st.success(f"VERDICT: {score}/300 - 💎 SOVEREIGN BUY")
                progress_color = "green"
            else:
                st.warning(f"VERDICT: {score}/300 - ⚖️ AUDIT HOLD")
                progress_color = "orange"
            
            st.progress(score / 300)

            # THE CORE 5 VITALS
            st.markdown("#### Forensic Vitals")
            v1, v2, v3, v4, v5 = st.columns(5)
            v1.metric("Margin", f"{info.get('profitMargins', 0)*100:.1f}%")
            v2.metric("Growth", f"{info.get('revenueGrowth', 0)*100:.1f}%")
            v3.metric("Debt/Eq", info.get('debtToEquity', 'N/A'))
            v4.metric("ROIC", f"{info.get('returnOnEquity', 0)*100:.1f}%")
            v5.metric("Yield", f"{info.get('dividendYield', 0)*100:.2f}")

        except:
            st.info("Scanner calibrating... Please enter a valid ticker.")

# --- PAGE 2: THE 5 MODELS ---
elif page == "🧪 THE 5 MODELS":
    st.title("🧪 Experimental Model Lab")
    st.subheader("Quarterly Audit Status")
    
    m_cols = st.columns(5)
    model_data = [
        ("MODEL A", "Cull Strategy", 245, "PASS"),
        ("MODEL B", "90-Day Rebalance", 210, "AUDIT"),
        ("MODEL C", "High Premium", 265, "PASS"),
        ("MODEL D", "Value/Asset", 185, "FAIL"),
        ("MODEL E", "Anti-Model", 82, "TRAP")
    ]
    
    for i, (name, desc, s, status) in enumerate(model_data):
        with m_cols[i]:
            st.markdown(f"""<div class="model-card">
                <h3>{name}</h3><p>{desc}</p><h2>{s}</h2><b>{status}</b>
            </div>""", unsafe_allow_html=True)

# --- PAGE 3: PODIUM ---
elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 Auditor Podium")
    st.markdown("### Race to Chapter 14")
    
    podium_df = pd.DataFrame({
        "Rank": ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"],
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Chapter Rank": ["C-14", "C-12", "C-11", "C-09", "C-04", "C-02", "Pending"]
    })
    st.table(podium_df)
    st.success("🔥 Anne is on a 5-day audit streak!")
