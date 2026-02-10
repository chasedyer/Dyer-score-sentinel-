import streamlit as st
import pandas as pd

# --- UI CONFIG ---
st.set_page_config(page_title="Dyer Research Lab", layout="wide")

# --- NEON TERMINAL STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #00FF41; }
    .search-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 100px;
    }
    .stTextInput > div > div > input {
        background-color: #161B22;
        color: #00FF41;
        border: 2px solid #00FF41;
        border-radius: 50px;
        padding: 20px 30px;
        font-size: 24px;
        text-align: center;
    }
    .audit-stat { color: #8B949E; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
page = st.sidebar.radio("LAB NAV", ["📡 SCANNER", "🧪 MODELS", "🏆 PODIUM"])

# --- PAGE 1: CATCHY SCANNER (LANDING) ---
if page == "📡 SCANNER":
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    st.title("🛡️ DYER SENTINEL")
    st.markdown('<p class="audit-stat">RESEARCHING 14 CHAPTERS | 120-DAY CYCLE</p>', unsafe_allow_html=True)
    
    # The Catchy Search Bar
    ticker = st.text_input("", placeholder="ENTER ASSET TICKER (e.g. NVDA, COST, AMC)").upper()
    
    if ticker:
        # Simulate real-time forensic loading
        with st.spinner(f"PERFORMING FORENSIC SCAN ON {ticker}..."):
            # (Insert scoring/verdict logic from previous step here)
            st.success(f"SCAN COMPLETE: {ticker} IS VALIDATED.")
            st.markdown("### DYER SCORE: **284**")
            st.markdown("---")
            # Traffic Light Banners and Core 5 Vitals go here
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: UPDATED PODIUM ---
elif page == "🏆 PODIUM":
    st.title("🏆 AUDITOR PODIUM")
    
    leaderboard_data = {
        "Rank": ["1st", "2nd", "3rd", "4th", "5th", "6th"],
        "Auditor": ["YOU (SOV-00)", "ANNE", "PABLO", "MIKE", "MOM", "DAD"],
        "Points": [1500, 1250, 950, 800, 450, 300],
        "Chapter": ["C-14", "C-12", "C-09", "C-08", "C-04", "C-02"]
    }
    
    # Display as a clean Podium Table
    st.table(pd.DataFrame(leaderboard_data))
    st.info("🎯 Mike is only 150 points away from passing Pablo!")
