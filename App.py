import streamlit as st

# 1. PAGE CONFIG & NAVIGATION
st.set_page_config(page_title="Dyer Score", layout="wide")
tab1, tab2 = st.tabs(["📡 DYER SCORE SCANNER", "🔬 5* MODEL HUB"])

# --- TAB 1: SCANNER (LANDING PAGE) ---
with tab1:
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🛡️ DYER SCORE</h1>', unsafe_allow_html=True)
    ticker = st.text_input("ENTER TICKER", "WMT").upper()
    
    st.subheader(f"300-Point Rushmore Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    
    # Automated Logic (Example for WMT)
    s_score, g_score, p_score = 88, 70, 85
    c1.metric("STABILITY", s_score)
    c2.metric("GROWTH", g_score)
    c3.metric("PREMIUM", p_score)
    
    st.markdown(f"<h2 style='text-align: center;'>TOTAL VALUE: {s_score + g_score + p_score}</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("🔍 Automated Forensic Report")
    # (25-Metric green/red checklist logic displays here)
    st.write("Scroll for full audit details...")

# --- TAB 2: MODEL HUB ---
with tab2:
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🔬 5* MODEL HUB</h1>', unsafe_allow_html=True)
    st.write("**Cycle Status:** Day 36 of 120 | **Audit Rule:** +10% Dyer Score Threshold")
    
    models = [
        {"Name": "Model A (Quarterly Cull)", "Score": "2,480", "YTD": 14.2},
        {"Name": "Model B (90-Day Reset)", "Score": "2,310", "YTD": 8.1},
        {"Name": "Model C (Conviction Growth)", "Score": "2,750", "YTD": 19.5},
        {"Name": "Model D (Sovereign Vault)", "Score": "2,890", "YTD": 4.3},
        {"Name": "Model E (The Trapdoor)", "Score": "940", "YTD": 22.8}
    ]

    st.markdown("---")
    h1, h2, h3 = st.columns([2, 1, 1])
    h1.write("**MODEL NAME**")
    h2.write("**AGGREGATE DYER SCORE**")
    h3.write("**YTD PERFORMANCE**")
    st.markdown("---")

    for m in models:
        color = "#00FF41" if m["YTD"] >= 10 else "#FFD700" if m["YTD"] > 0 else "#FF4B4B"
        if m["Name"] == "Model E (The Trapdoor)": color = "#FF4B4B"
        
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.markdown(f'<p style="color:{color}; font-size:18px; font-weight:bold;">{m["Name"]}</p>', unsafe_allow_html=True)
        col2.markdown(f"**{m['Score']}**")
        col3.markdown(f'<p style="color:{color}; font-size:18px;">{abs(m["YTD"])}</p>', unsafe_allow_html=True)
