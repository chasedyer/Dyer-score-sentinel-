import streamlit as st
import pandas as pd

# 1. UI SETUP
st.set_page_config(page_title="Dyer Global 5* Models", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .model-header { color: #00FF41; font-size: 24px; font-weight: bold; border-left: 5px solid #00FF41; padding-left: 15px; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# 2. NAVIGATION
page = st.sidebar.radio("COMMAND", ["📡 DYER SCANNER", "🔬 5* MODELS HUB"])

if page == "🔬 5* MODELS HUB":
    st.markdown('<h1 style="text-align: center; color: #00FF41;">🔬 5* MODELS PERFORMANCE</h1>', unsafe_allow_html=True)
    st.info("Current Audit Status: **Day 36 of 120** | Threshold: **+10% Dyer Score Improvement**")

    # DEFINE DATA
    models = ["Model A", "Model B", "Model C", "Model D", "Model E"]
    aggregates = [268, 242, 275, 255, 118]
    perf = ["+14.2%", "+8.1%", "+19.5%", "+4.3%", "-22.8%"]
    status = ["🟢 PASS", "🟡 MONITOR", "🟢 PASS", "🟡 MONITOR", "🔴 FAIL"]

    # 3. THE 5* AGGREGATION TABLE
    df = pd.DataFrame({
        "Model": models,
        "Aggregated Dyer Score": aggregates,
        "120-Day Return": perf,
        "Cycle Status": status
    })
    st.table(df)

    st.markdown("---")
    
    # 4. SUB-PARTS BY MODEL
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="model-header">MODEL A: QUARTERLY CULL</div>', unsafe_allow_html=True)
        st.write("**Strategy:** Bottom 5 performers are sold by 25%. Cash moved to top 5.")
        st.metric("Avg Score", "268", "+12 pts")
        
    with col2:
        st.markdown('<div class="model-header">MODEL B: 90-DAY RESET</div>', unsafe_allow_html=True)
        st.write("**Strategy:** All tickers reset back to 10% weight every 90 days.")
        st.metric("Avg Score", "242", "-4 pts")

    st.markdown('<div class="model-header" style="border-color: #FF4B4B;">MODEL E: THE ANTI-MODEL</div>', unsafe_allow_html=True)
    st.error("Assets here have failed the 10% improvement rule. High priority flag for Gold LLC.")
