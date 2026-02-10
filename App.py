import streamlit as st
import pandas as pd

# 1. THE RUSHMORE ENGINE (300 POINT MAX)
def get_rushmore_score(ticker):
    profiles = {
        "SOVEREIGN": ["COST", "WMT", "PG", "JPM", "V"],
        "GROWTH_LEADER": ["NVDA", "MSFT", "META", "AMZN"],
        "SPEC_TECH": ["RIVN", "GEVO", "PLTR", "TSLA"],
        "TRAPDOOR": ["NKLA", "AMC", "SAVE", "CVNA"]
    }
    h = sum(ord(c) for c in ticker)
    if ticker in profiles["SOVEREIGN"]:
        s, g, p = (85 + h%15), (70 + h%20), (88 + h%10)
    elif ticker in profiles["GROWTH_LEADER"]:
        s, g, p = (75 + h%15), (90 + h%10), (90 + h%10)
    elif ticker in profiles["SPEC_TECH"]:
        s, g, p = (20 + h%20), (60 + h%30), (30 + h%20)
    elif ticker in profiles["TRAPDOOR"]:
        s, g, p = (5 + h%10), (15 + h%20), (5 + h%15)
    else:
        # Unique universe generation
        s, g, p = (h % 60) + 30, (h % 70) + 20, (h % 50) + 10
    return {"S": s, "G": g, "P": p}

# 2. PERSISTENCE
if 'audit_db' not in st.session_state:
    st.session_state.audit_db = {}

# 3. NAVIGATION (Dyer Score Scanner is Landing Page)
st.sidebar.title("COMMAND")
page = st.sidebar.radio("GO TO", ["📡 DYER SCORE SCANNER", "🔬 5* MODELS HUB"])

# --- PAGE 1: SCANNER ---
if page == "📡 DYER SCORE SCANNER":
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🛡️ DYER SCORE</h1>', unsafe_allow_html=True)
    ticker = st.text_input("ENTER TICKER", "WMT").upper()
    current = st.session_state.audit_db.get(ticker, get_rushmore_score(ticker))

    st.subheader(f"300-Point Rushmore Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    s = c1.number_input("STABILITY", 0, 100, current["S"], key=f"{ticker}_s")
    g = c2.number_input("GROWTH", 0, 100, current["G"], key=f"{ticker}_g")
    p = c3.number_input("PREMIUM", 0, 100, current["P"], key=f"{ticker}_p")
    
    total = s + g + p
    if st.button("SYNC AUDIT"):
        st.session_state.audit_db[ticker] = {"S": s, "G": g, "P": p, "Total": total}
        st.success(f"Dyer Score for {ticker} locked at {total}")

    st.metric("Total Value", total)

# --- PAGE 2: 5* MODELS HUB ---
elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Performance")
    st.write("Current Audit Cycle: **Day 36 of 120**")
    
    perf_data = [
        {"Model": "Model A (Cull)", "Score": 268, "Perf": 14.2},
        {"Model": "Model B (Reset)", "Score": 242, "Perf": 8.1},
        {"Model": "Model C", "Score": 275, "Perf": 19.5},
        {"Model": "Model D", "Score": 255, "Perf": 4.3},
        {"Model": "Model E (Anti)", "Score": 118, "Perf": -22.8}
    ]
    
    for m in perf_data:
        # Green (10%+), Yellow (Positive), Red (Negative)
        color = "#00FF41" if m["Perf"] >= 10 else "#FFD700" if m["Perf"] > 0 else "#FF4B4B"
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.markdown(f'<p style="color:{color}; font-size:20px; font-weight:bold;">{m["Model"]}</p>', unsafe_allow_html=True)
        col2.write(f"Score: {m['Score']}")
        col3.write(f"Value: {m['Perf']}")
