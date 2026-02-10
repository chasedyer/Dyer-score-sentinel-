import streamlit as st
import pandas as pd

# 1. DATA AND STYLE LOGIC
model_data = {
    "Model": ["Model A (Cull)", "Model B (Reset)", "Model C", "Model D", "Model E (Anti)"],
    "Dyer Score": [268, 242, 275, 255, 118],
    "Performance": [14.2, 8.1, 19.5, 4.3, 22.8]
}

def color_performance(val):
    if val > 10: color = '#00FF41' # Green (Passed 10% threshold)
    elif val > 0: color = '#FFD700' # Yellow (Positive but under-target)
    else: color = '#FF4B4B' # Red (Failed/Loss)
    return f'color: {color}'

# 2. UI SETUP
st.set_page_config(page_title="Dyer Sentinel", layout="wide")
page = st.sidebar.radio("NAVIGATE", ["📡 DYER SCANNER (Home)", "🔬 5* MODELS HUB"])

# --- PAGE 1: SEARCH ---
if page == "📡 DYER SCANNER (Home)":
    st.markdown('<h1 style="text-align:center; color:#00FF41;">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    ticker = st.text_input("ENTER TICKER", "COST").upper()
    # (Scanner logic remains as previously established for RIVN/GEVO distinction)

# --- PAGE 2: COLORED MODELS HUB ---
elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Performance")
    st.write("Current Audit Cycle: **Day 36 of 120**")
    
    df = pd.DataFrame(model_data)
    
    # APPLYING COLORS TO THE DATAFRAME
    styled_df = df.style.applymap(color_performance, subset=['Performance'])
    
    st.table(styled_df)
    
    st.markdown("---")
    st.success("GREEN: Models exceeding the 10% Dyer Improvement target.")
    st.warning("YELLOW: Models trailing the target; requires 120-day audit review.")
    st.error("RED: Model E / Failing assets flagged for Gold LLC liquidation.")
