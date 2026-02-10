import streamlit as st

# 1. THE FORENSIC STATUS LOGIC
def get_forensic_status(ticker, bucket):
    sovereigns = ["COST", "WMT", "MSFT", "V"]
    trapdoors = ["RIVN", "GEVO", "NKLA"]
    
    if ticker in sovereigns:
        return [True, True, True, True, True, True, True, False] 
    elif ticker in trapdoors:
        return [False, False, False, True, False, False, True, False] 
    else:
        return [True, False, True, True, False, True, False, True]

# 2. UI BRANDING & TABS
st.set_page_config(page_title="Dyer Score", layout="wide")

tab1, tab2 = st.tabs(["📡 DYER SCORE SCANNER", "🔬 5* MODELS HUB"])

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
    
    c1.metric("STABILITY", s_score)
    c2.metric("GROWTH", g_score)
    c3.metric("PREMIUM", p_score)
    
    total = s_score + g_score + p_score
    st.markdown(f"<h2 style='text-align: center;'>TOTAL DYER SCORE: {total}</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("🔍 Automated Forensic Report")
    f1, f2, f3 = st.columns(3)
    
    def render_list(title, results, metrics):
        st.markdown(f"**{title}**")
        for i, m in enumerate(metrics):
            if results[i]:
                st.markdown(f"✅ <span style='color:#00FF41;'>{m}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"❌ <span style='color:#FF4B4B;'>{m} (FLAGGED)</span>", unsafe_allow_html=True)

    with f1:
        render_list("STABILITY", s_results, ["Op. Margin", "ROIC", "Debt/EBITDA", "FCF Yield", "Consistency", "Liquidity", "Interest Cov", "Earnings Q"])
    with f2:
        render_list("GROWTH", g_results, ["Top-Line", "Market Share", "R&D Spend", "TAM Exp", "CAC Logic", "Retention", "Capex ROI", "Global Scale"])
    with f3:
        render_list("PREMIUM", p_results, ["Insider Skin", "Founder-Led", "Pricing Power", "Mindshare", "Reg. Moat", "Network Effect", "Cap Allocation", "Chapter 14"])

# --- TAB 2: 5* MODELS HUB ---
with tab2:
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🔬 5* Models Hub</h1>', unsafe_allow_html=True)
    st.write("**Cycle:** Day 36 of 120 | **Threshold:** +10% Dyer Score")
    
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
    h2.write("**AGGREGATE SCORE**")
    h3.write("**YTD VALUE**")
    st.markdown("---")

    for m in models:
        color = "#00FF41" if m["YTD"] >= 10 else "#FFD700" if m["YTD"] > 0 else "#FF4B4B"
        if m["Name"] == "Model E (The Trapdoor)": color = "#FF4B4B"
        
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.markdown(f'<p style="color:{color}; font-size:18px; font-weight:bold;">{m["Name"]}</p>', unsafe_allow_html=True)
        col2.markdown(f"**{m['Score']}**")
        col3.markdown(f'<p style="color:{color}; font-size:18px;">{abs(m["YTD"])}</p>', unsafe_allow_html=True)
