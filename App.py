import streamlit as st
import pandas as pd
import yfinance as yf

# --- 1. SETTINGS & STYLING ---
st.set_page_config(page_title="Dyer Research Lab", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; height: 3em; }
    .model-card { background-color: #1C2128; border: 1px solid #30363D; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. NAVIGATION ---
page = st.sidebar.radio("LAB NAVIGATION", ["📡 SCANNER", "🧪 THE 5 MODELS", "🏆 AUDITOR PODIUM"])

# --- 3. PAGE 1: SCANNER (STABILIZED SEARCH) ---
if page == "📡 SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8B949E;">14 CHAPTER RESEARCH | 120-DAY AUDIT CYCLE</p>', unsafe_allow_html=True)

    # THE FORM PREVENTS STUTTERING / BLANK SCREENS
    with st.form("search_form"):
        col1, col2 = st.columns([3, 1])
        with col1:
            ticker_input = st.text_input("TICKER SYMBOL", value="COST").upper()
        with col2:
            st.write(" ") # Spacer
            submitted = st.form_submit_button("RUN FORENSIC SCAN")

    # Only executes once the button is clicked
    if submitted and ticker_input:
        try:
            with st.spinner(f'AUDITING {ticker_input}...'):
                stock = yf.Ticker(ticker_input)
                # Fetching price with basic error handling
                data = stock.history(period="1d")
                if data.empty:
                    st.error("Ticker not found. Try a common one like AAPL or NVDA.")
                else:
                    price = data['Close'].iloc[-1]
                    
                    # DYER SCORE LOGIC
                    st.sidebar.subheader("Manual Forensic Inputs")
                    mgmt = st.sidebar.slider("Management Quality", 0, 100, 85)
                    moat = st.sidebar.select_slider("Moat Strength", options=[0, 50, 100], value=50)
                    score = 100 + mgmt + moat
                    
                    # VERDICT DISPLAY
                    st.markdown("---")
                    if score >= 200:
                        st.success(f"💎 {ticker_input} SCORE: {score}/300 | SOVEREIGN BUY")
                        label = "🟢 BUY"
                    elif score < 150:
                        st.error(f"🚨 {ticker_input} SCORE: {score}/300 | TRAPDOOR SELL")
                        label = "🔴 SELL"
                    else:
                        st.warning(f"⚖️ {ticker_input} SCORE: {score}/300 | AUDIT HOLD")
                        label = "🟡 HOLD"
                    
                    st.progress(score / 300)

                    # VITALS GRID
                    v1, v2, v3 = st.columns(3)
                    v1.metric("Current Price", f"${price:.2f}")
                    v2.metric("Rushmore Score", f"{score}/300")
                    v3.metric("Verdict", label)
        except Exception as e:
            st.error("Exchange link failed. Check ticker symbol.")

# --- 4. PAGE 2: THE 5 MODELS ---
elif page == "🧪 THE 5 MODELS":
    st.title("🧪 Experimental Model Lab")
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
    df = pd.DataFrame({
        "Rank": ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"],
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD", "STEVE"],
        "Points": [1500, 1250, 1100, 950, 450, 300, 0],
        "Level": ["C-14", "C-12", "C-11", "C-09", "C-04", "C-02", "Pending"]
    })
    st.table(df)
