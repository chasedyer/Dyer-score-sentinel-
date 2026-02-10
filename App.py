import streamlit as st
import yfinance as yf

# --- UI CONFIG ---
st.set_page_config(page_title="Dyer Sentinel", layout="centered")

# --- CUSTOM THEME (TRAFFIC LIGHT LOGIC) ---
def apply_style(score):
    if score < 150:
        bg_color, text = "#721c24", "🚨 TRAPDOOR SELL" # Deep Red
    elif score >= 200:
        bg_color, text = "#155724", "💎 SOVEREIGN BUY" # Emerald Green
    else:
        bg_color, text = "#856404", "⚖️ AUDIT HOLD"    # Amber
    
    st.markdown(f"""
        <style>
        .stApp {{ background-color: #0E1117; }}
        .verdict-banner {{
            background-color: {bg_color};
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
        }}
        </style>
        <div class="verdict-banner">{text}</div>
    """, unsafe_allow_html=True)
    return text

# --- APP LOGIC ---
st.title("🛡️ Dyer Sentinel Terminal")
ticker = st.text_input("SCAN TICKER", value="COST").upper()

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # 1. CORE FORENSIC INPUTS
        st.subheader("Forensic Inputs")
        mgmt = st.slider("Management Quality", 0, 100, 85)
        moat = st.select_slider("Moat Strength", options=["Decaying", "Stable", "Expanding"], value="Stable")
        moat_pts = {"Decaying": 0, "Stable": 50, "Expanding": 100}[moat]
        
        # 2. THE DYER SCORE (Rushmore Metric)
        # Simplified for clarity: Stability + Management + Moat
        stability = 100 # Base asset quality proxy
        final_score = int(stability + mgmt + moat_pts)
        
        # 3. THE VERDICT BANNER
        verdict_text = apply_style(final_score)
        
        # 4. THE MASTER SCORE
        st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{final_score}</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray;'>Dyer Score (Max 300)</p>", unsafe_allow_html=True)

        # 5. CORE 5 VITALS (The Useful Stuff)
        st.markdown("---")
        v1, v2, v3 = st.columns(3)
        v1.metric("Profit Margin", f"{info.get('profitMargins', 0)*100:.1f}%")
        v2.metric("Rev Growth", f"{info.get('revenueGrowth', 0)*100:.1f}%")
        v3.metric("Debt/Equity", info.get('debtToEquity', 'N/A'))

        # 6. SHARING (Wordle Mode)
        st.markdown("---")
        if st.button("📤 Generate Share Report"):
            share_block = f"🛡️ Dyer Audit: ${ticker}\n🎯 Score: {final_score}/300\n{verdict_text}\n#DyerSentinel"
            st.code(share_block)
            st.success("Copied! Paste this into the family chat.")

    except Exception:
        st.warning("Please enter a valid ticker to scan.")

# Sidebar Leaderboard
st.sidebar.title("🏆 Leaderboard")
st.sidebar.write("1. YOU (SOV-00) - 150 pts")
st.sidebar.write("2. MOM (SOV-01) - 45 pts")
st.sidebar.write("3. DAD (SOV-02) - 30 pts")
