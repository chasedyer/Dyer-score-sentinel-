import streamlit as st
import pandas as pd

# 1. PERSISTENT STORAGE (Memory Bank)
if 'audit_db' not in st.session_state:
    st.session_state.audit_db = {
        "COST": {"S": 95, "G": 85, "P": 98, "Total": 278},
        "WMT": {"S": 88, "G": 70, "P": 85, "Total": 243}, # Fixed WMT Default
        "RIVN": {"S": 22, "G": 55, "P": 31, "Total": 108},
        "GEVO": {"S": 12, "G": 45, "P": 15, "Total": 72}
    }

# 2. NAVIGATION
st.sidebar.title("COMMAND")
page = st.sidebar.radio("GO TO", ["📡 SCANNER", "🔬 5* MODELS"])

# --- PAGE 1: SCANNER ---
if page == "📡 SCANNER":
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    ticker = st.text_input("ENTER TICKER", "WMT").upper()
    
    # Load from memory or use default
    if ticker in st.session_state.audit_db:
        defaults = st.session_state.audit_db[ticker]
    else:
        defaults = {"S": 50, "G": 50, "P": 50, "Total": 150}

    st.subheader(f"Forensic Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    
    # User inputs
    s = c1.number_input("STABILITY", 0, 100, defaults.get("S", 50), key=f"{ticker}_s")
    g = c2.number_input("GROWTH", 0, 100, defaults.get("G", 50), key=f"{ticker}_g")
    p = c3.number_input("PREMIUM", 0, 100, defaults.get("P", 50), key=f"{ticker}_p")
    
    total = s + g + p
    
    if st.button("SYNC TO GOLD LLC RECORDS"):
        st.session_state.audit_db[ticker] = {"S": s, "G": g, "P": p, "Total": total}
        st.success(f"Updated {ticker} to {total}")

    st.metric(f"{ticker} Dyer Score", total)

# --- PAGE 2: COLORED MODELS ---
elif page == "🔬 5* MODELS":
    st.title("🔬 5* Models Performance")
    
    # Define Model Performance Data
    perf_data = [
        {"Model": "Model A (Cull)", "Score": 268, "Perf": 14.2},
        {"Model": "Model B (Reset)", "Score": 242, "Perf": 8.1},
        {"Model": "Model C", "Score": 275, "Perf": 19.5},
        {"Model": "Model D", "Score": 255, "Perf": 4.3},
        {"Model": "Model E (Anti)", "Score": 118, "Perf": -22.8}
    ]
    
    # Display logic with color coding
    for m in perf_data:
        color = "#00FF41" if m["Perf"] > 10 else "#FFD700" if m["Perf"] > 0 else "#FF4B4B"
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.markdown(f'<p style="color:{color}; font-size:20px; font-weight:bold;">{m["Model"]}</p>', unsafe_allow_html=True)
        col2.write(f"Score: {m['Score']}")
        col3.write(f"Perf: {m['Perf']}")
