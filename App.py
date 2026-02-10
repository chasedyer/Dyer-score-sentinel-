import streamlit as st
import pandas as pd

# 1. INDEPENDENT TICKER DATABASE (Memory Bank)
if 'audit_db' not in st.session_state:
    st.session_state.audit_db = {
        "COST": {"S": 95, "G": 85, "P": 98, "Total": 278},
        "WMT": {"S": 88, "G": 70, "P": 85, "Total": 243},
        "MSFT": {"S": 92, "G": 82, "P": 94, "Total": 268},
        "RIVN": {"S": 22, "G": 55, "P": 31, "Total": 108},
        "GEVO": {"S": 12, "G": 45, "P": 15, "Total": 72}
    }

# 2. UI NAVIGATION
st.sidebar.title("COMMAND CENTER")
page = st.sidebar.radio("NAVIGATE", ["📡 FORENSIC SCANNER", "🔬 5* MODELS HUB"])

# --- PAGE 1: FORENSIC SCANNER (LANDING PAGE) ---
if page == "📡 FORENSIC SCANNER":
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    ticker = st.text_input("ENTER TICKER", "WMT").upper()
    
    # Load specific data for WMT, COST, etc.
    defaults = st.session_state.audit_db.get(ticker, {"S": 50, "G": 50, "P": 50, "Total": 150})

    st.subheader(f"Raw Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    
    # Inputs with unique keys to ensure scores update per ticker
    s = c1.number_input("STABILITY", 0, 100, defaults["S"], key=f"{ticker}_s")
    g = c2.number_input("GROWTH", 0, 100, defaults["G"], key=f"{ticker}_g")
    p = c3.number_input("PREMIUM", 0, 100, defaults["P"], key=f"{ticker}_p")
    
    total = s + g + p
    
    if st.button("SYNC AUDIT"):
        st.session_state.audit_db[ticker] = {"S": s, "G": g, "P": p, "Total": total}
        st.success(f"Dyer Score for {ticker} locked at {total}")

    st.markdown(f"## TOTAL VALUE: {total}")

# --- PAGE 2: 5* MODELS PERFORMANCE ---
elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Performance")
    st.write("Current Audit Cycle: **Day 36 of 120**")
    
    # Model tracking data (Pro-rated for 2026 cycle)
    perf_data = [
        {"Model": "Model A (Cull)", "Score": 268, "Perf": 14.2},
        {"Model": "Model B (Reset)", "Score": 242, "Perf": 8.1},
        {"Model": "Model C", "Score": 275, "Perf": 19.5},
        {"Model": "Model D", "Score": 255, "Perf": 4.3},
        {"Model": "Model E (Anti)", "Score": 118, "Perf": 22.8} # Loss value shown as absolute
    ]
    
    # Color-coded performance grid
    for m in perf_data:
        # Green for 10%+, Yellow for positive, Red for fail
        color = "#00FF41" if m["Perf"] >= 10 else "#FFD700" if m["Perf"] > 0 else "#FF4B4B"
        if m["Model"] == "Model E (Anti)": color = "#FF4B4B" # Forced red for failure model
        
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.markdown(f'<p style="color:{color}; font-size:20px; font-weight:bold;">{m["Model"]}</p>', unsafe_allow_html=True)
        col2.write(f"Score: {m['Score']}")
        col3.write(f"Value: {m['Perf']}")
