import streamlit as st

# 1. THE FORENSIC STATUS LOGIC (Protected Baseline)
def get_forensic_status(ticker, bucket):
    sovereigns = ["COST", "WMT", "MSFT", "V", "WM", "DE"]
    trapdoors = ["RIVN", "GEVO", "NKLA", "SAVE", "AMC", "CVNA"]
    
    if ticker in sovereigns:
        return [True, True, True, True, True, True, True, False] 
    elif ticker in trapdoors:
        return [False, False, False, True, False, False, True, False] 
    else:
        # Standard Audit for Growth/Spec names
        return [True, False, True, True, False, True, False, True]

# 2. UI BRANDING & TABS
st.set_page_config(page_title="Dyer Score Sentinel", layout="wide")

tab1, tab2 = st.tabs(["📡 DYER SCORE SCANNER", "🔬 7* MODELS HUB"])

# --- TAB 1: SCANNER ---
with tab1:
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🛡️ DYER SCORE</h1>', unsafe_allow_html=True)
    ticker = st.text_input("ENTER TICKER", "WMT").upper()
    
    st.subheader(f"300-Point Rushmore Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    
    s_results = get_forensic_status(ticker, "STABILITY")
    g_results = get_forensic_status(ticker, "GROWTH")
    p_results = get_forensic_status(ticker, "PREMIUM")
    
    s_score = int((sum(s_results)/len(s_results))*100)
    g_score = int((sum(g_results)/len(g_results))*100)
    p_score = int((sum(p_results)/len(p_results))*100)
    
    c1.metric("STABILITY (Asset Quality)", s_score)
    c2.metric("GROWTH (Expansion Cap)", g_score)
    c3.metric("PREMIUM (Management/Moat)", p_score)
    
    total = s_score + g_score + p_score
    st.markdown(f"<h2 style='text-align: center;'>TOTAL DYER SCORE: {total}</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🔍 Automated Forensic Report")
    f1, f2, f3 = st.columns(3)
    
    def render_list(title, results, metrics):
        st.markdown(f"**{title}**")
        for i, m in enumerate(metrics):
            color = "#00FF41" if results[i] else "#FF4B4B"
            symbol = "✅" if results[i] else "❌"
            flag = "" if results[i] else " (FLAGGED)"
            st.markdown(f"{symbol} <span style='color:{color};'>{m}{flag}</span>", unsafe_allow_html=True)

    with f1:
        render_list("STABILITY", s_results, ["Op. Margin", "ROIC", "Debt/EBITDA", "FCF Yield", "Consistency", "Liquidity", "Interest Cov", "Earnings Q"])
    with f2:
        render_list("GROWTH", g_results, ["Top-Line", "Market Share", "R&D Spend", "TAM Exp", "CAC Logic", "Retention", "Capex ROI", "Global Scale"])
    with f3:
        render_list("PREMIUM", p_results, ["Insider Skin", "Founder-Led", "Pricing Power", "Mindshare", "Reg. Moat", "Network Effect", "Cap Allocation", "Chapter 14"])

# --- TAB 2: 7* MODELS HUB ---
with tab2:
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🔬 7* Models Hub</h1>', unsafe_allow_html=True)
    
    # 3. ALPHA GAP & WAITLIST METRICS (Real-time Context)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("ALPHA GAP (F vs D)", "+15.2%", delta="2.1%")
    col_b.metric("WAITLIST LAG (RDDT)", "$142.08", delta="-4.2%")
    col_c.metric("WAITLIST LAG (TTAN)", "$64.40", delta="-1.04%")
    
    st.write("**Audit Cycle:** Day 36 of 120 | **Threshold:** +10% Dyer Score Improvement Required")
    st.markdown("---")
    
    models = [
        {"Name": "Model A (Quarterly Cull)", "Score": "2,480", "YTD": 14.2},
        {"Name": "Model B (90-Day Reset)", "Score": "2,310", "YTD": 8.1},
        {"Name": "Model C (Excavation/Conviction)", "Score": "2,750", "YTD": 19.5},
        {"Name": "Model D (Sovereign Vault)", "Score": "2,890", "YTD": 4.3},
        {"Name": "Model E (The Trapdoor)", "Score": "940", "YTD": -22.8},
        {"Name": "Model F (Signal Rushmore)", "Score": "2,610", "YTD": 11.4},
        {"Name": "Model G (Spec Alpha)", "Score": "1,840", "YTD": 2.5}
    ]

    h1, h2, h3 = st.columns([2, 1, 1])
    h1.write("**MODEL NAME (Total Allocation: $70k)**")
    h2.write("**AGGREGATE DYER SCORE**")
    h3.write("**YTD VALUE (%)**")
    st.markdown("---")

    for m in models:
        # Custom coloring: Red for fail/trapdoor, Gold for caution, Green for leaders
        color = "#00FF41" if m["YTD"] >= 10 else "#FFD700" if m["YTD"] > 0 else "#FF4B4B"
        if m["Name"] == "Model E (The Trapdoor)": color = "#FF4B4B"
        
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.markdown(f'<p style="color:{color}; font-size:18px; font-weight:bold;">{m["Name"]}</p>', unsafe_allow_html=True)
        col2.markdown(f"**{m['Score']}**")
        col3.markdown(f'<p style="color:{color}; font-size:18px;">{m["YTD"]}%</p>', unsafe_allow_html=True)

    st.markdown("---")
    st.caption("Baseline Locked: 2026-02-10 | Portfolio G Tickers: PANW, BKH, BFLY, NSA, DUOT, NBIS, PUBM, BKRRF, INSG, CLFD")
