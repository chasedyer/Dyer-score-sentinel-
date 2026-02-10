import streamlit as st
import pandas as pd
import yfinance as yf

# --- 1. CORE SETTINGS ---
st.set_page_config(page_title="Dyer Research Lab", layout="wide")

# Persistent CSS for the Terminal Look
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 48px; font-weight: bold; color: #00FF41; margin-top: 20px; }
    .stTextInput > div > div > input {
        background-color: #161B22; color: #00FF41; border: 2px solid #00FF41;
        border-radius: 50px; padding: 25px; font-size: 22px; text-align: center;
    }
    .model-card { background-color: #1C2128; border: 1px solid #30363D; padding: 20px; border-radius: 12px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("🛡️ LAB CONTROL")
page = st.sidebar.radio("NAVIGATE", ["📡 SCANNER (LANDING)", "🧪 THE 5 MODELS", "🏆 AUDITOR PODIUM"])

# --- 3. PAGE 1: SCANNER (THE LANDING PAGE) ---
if page == "📡 SCANNER (LANDING)":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">14 CHAPTER RESEARCH | 120-DAY AUDIT CYCLE</p>', unsafe_allow_html=True)
    
    # Large Search Bar
    ticker = st.text_input("", placeholder="TYPE TICKER (NVDA, COST, AMC)...").upper()
    
    if ticker:
        try:
            # Data Fetching
            stock = yf.Ticker(ticker)
            price = stock.fast_info['last_price']
            
            # Dyer Score Controls (Manual Sliders)
            st.sidebar.markdown("---")
            st.sidebar.subheader("Forensic Inputs")
            mgmt = st.sidebar.slider("Management Quality", 0, 100, 80)
            moat = st.sidebar.select_slider("Moat Strength", options=[0, 50, 100], value=50)
            score = 100 + mgmt + moat # Rushmore Metric Base
            
            # THE DIAL / GAUGE
            st.markdown("---")
            if score < 150:
                st.error(f"VERDICT: {score}/300 | 🚨 TRAPDOOR SELL")
                label = "🔴 SELL"
            elif score >= 200:
                st.success(f"VERDICT: {score}/300 | 💎 SOVEREIGN BUY")
                label = "🟢 BUY"
            else:
                st.warning(f"VERDICT: {score}/300 | ⚖️ AUDIT HOLD")
                label = "🟡 HOLD"
                
            st.progress(score / 300)
            
            # Forensic Vitals Grid
            st.markdown("### Forensic Vitals")
            c1, c2, c3 = st.columns(3)
            c1.metric("Current Price", f"${price:.2f}")
            c2.metric("Rushmore Score", f"{score}/300")
            c3.metric("Conviction", label)
            
        except Exception as e:
            st.info("Input ticker to begin forensic scan.")

# --- 4. PAGE 2: THE 5 MODELS ---
elif page == "🧪 THE 5 MODELS":
    st.title("🧪 The 5 Experimental Models")
    st.write("3-Year Strategy Cycle | Rebalance every 120 Days")
    
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
            st.markdown(f"""<div class="model-card">
                <h3>{name}</h3><p style='color:gray;'>{desc}</p><h1>{s}</h1><b>{status}</b>
            </div>""", unsafe_allow_html=True)

# --- 5. PAGE 3: PODIUM ---
elif page == "🏆 AUDITOR PODIUM":
    st.title("🏆 Auditor Podium")
    st.write("Tracking audit points for the 14-chapter study.")
    
    df = pd.DataFrame({
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Rank": ["C-14 Master", "C-12 Expert", "C-11 Senior", "C-09 Lead", "C-04 Junior", "C-02 Novice", "Trainee"]
    })
    st.table(df)
