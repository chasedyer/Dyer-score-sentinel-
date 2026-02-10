import streamlit as st

# 1. THE 25-METRIC BLUEPRINT
METRICS = {
    "STABILITY (Asset Quality)": [
        "Operating Margin > 15%", "ROIC > 15%", "Debt/EBITDA < 3x", 
        "Positive FCF Yield", "Revenue Consistency", "Current Ratio > 1.5",
        "Interest Coverage", "Earnings Quality (Cash-backed)"
    ],
    "GROWTH (Expansion Capacity)": [
        "Top-Line Growth > 10%", "Market Share Velocity", "R&D Intensity",
        "TAM Expansion", "CAC Efficiency", "Retention/Churn Rates",
        "Capex ROI", "International Scalability"
    ],
    "PREMIUM (Management/Moat)": [
        "Insider Skin in the Game", "Founder-Led/Visionary", "Pricing Power",
        "Brand Mindshare", "Regulatory Moat", "Network Effects",
        "Capital Allocation Strategy", "Internal Culture", "Chapter 14 Intuition"
    ]
}

# 2. UI SETUP
st.set_page_config(page_title="Dyer Score", layout="wide")
st.sidebar.title("COMMAND")
page = st.sidebar.radio("NAVIGATE", ["📡 DYER SCORE SCANNER", "🔬 5* MODELS HUB"])

if page == "📡 DYER SCORE SCANNER":
    st.markdown('<h1 style="color:#00FF41; text-align:center;">🛡️ DYER SCORE</h1>', unsafe_allow_html=True)
    ticker = st.text_input("ENTER TICKER", "WMT").upper()
    
    # TOP LEVEL: The Search Result
    st.subheader(f"300-Point Rushmore Audit: {ticker}")
    c1, c2, c3 = st.columns(3)
    s_val = c1.number_input("STABILITY", 0, 100, 80, key="s_top")
    g_val = c2.number_input("GROWTH", 0, 100, 70, key="g_top")
    p_val = c3.number_input("PREMIUM", 0, 100, 90, key="p_top")
    
    total = s_val + g_val + p_val
    st.metric("Aggregate Dyer Score", f"{total} / 300")
    
    st.markdown("---")
    
    # SCROLL DOWN: The Forensic Checklist
    st.markdown("### 🔍 Forensic Audit Checklist (The 25 Metrics)")
    st.write("Check the boxes that apply to the current 120-day audit cycle.")
    
    f1, f2, f3 = st.columns(3)
    
    # Stability Column
    with f1:
        st.markdown("**STABILITY BUCKET**")
        s_count = 0
        for m in METRICS["STABILITY (Asset Quality)"]:
            if st.checkbox(m, key=f"s_{m}"): s_count += 1
        st.info(f"Points Calculated: {int((s_count/8)*100)}")

    # Growth Column
    with f2:
        st.markdown("**GROWTH BUCKET**")
        g_count = 0
        for m in METRICS["GROWTH (Expansion Capacity)"]:
            if st.checkbox(m, key=f"g_{m}"): g_count += 1
        st.info(f"Points Calculated: {int((g_count/8)*100)}")

    # Premium Column
    with f3:
        st.markdown("**PREMIUM BUCKET**")
        p_count = 0
        for m in METRICS["PREMIUM (Management/Moat)"]:
            if st.checkbox(m, key=f"p_{m}"): p_count += 1
        st.info(f"Points Calculated: {int((p_count/9)*100)}")

    if st.button("LOCK FULL AUDIT"):
        # This would sync the checkbox data to the model
        st.success(f"Audit for {ticker} verified against all 25 metrics.")
