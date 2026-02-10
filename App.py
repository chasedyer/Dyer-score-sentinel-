import streamlit as st
import pandas as pd

# --- 1. PERSISTENT MEMORY (SESSION STATE) ---
if 'audit_log' not in st.session_state:
    # Initialize with some baseline data for the Core 23
    st.session_state.audit_log = pd.DataFrame(columns=['Ticker', 'Stability', 'Growth', 'Premium', 'Total'])

# --- 2. SYSTEM SETTINGS ---
st.set_page_config(page_title="Dyer Global Audit", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .search-title { text-align: center; font-size: 50px; font-weight: bold; color: #00FF41; margin-bottom: 0px; }
    .metric-header { color: #00FF41; font-weight: bold; font-size: 22px; border-bottom: 2px solid #30363D; margin-bottom: 10px; }
    .stButton>button { width: 100%; background-color: #00FF41; color: black; font-weight: bold; height: 3.5em; border-radius: 10px; font-size: 18px; }
    .aggregation-box { background-color: #161B22; border: 1px solid #30363D; padding: 20px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. NAVIGATION ---
page = st.sidebar.radio("COMMAND CENTER", ["📡 DYER SCANNER", "🔬 5* MODELS HUB", "🧪 STRATEGY LOGIC"])

# --- 4. PAGE 1: SCANNER & SUB-PARTS ---
if page == "📡 DYER SCANNER":
    st.markdown('<h1 class="search-title">🛡️ DYER SENTINEL</h1>', unsafe_allow_html=True)
    
    ticker_input = st.text_input("ENTER COMPANY NAME OR TICKER", "COSTCO").upper()
    
    st.markdown("### 📥 Input 300-Point Rushmore Buckets")
    c1, c2, c3 = st.columns(3)
    with c1: s_score = st.number_input("STABILITY", 0, 100, 85)
    with c2: g_score = st.number_input("GROWTH", 0, 100, 80)
    with c3: p_score = st.number_input("PREMIUM", 0, 100, 90)
    
    total = s_score + g_score + p_score

    if st.button("CALCULATE & SYNC TO HUB"):
        # SAVE TO SESSION STATE
        new_audit = pd.DataFrame([[ticker_input, s_score, g_score, p_score, total]], 
                                 columns=['Ticker', 'Stability', 'Growth', 'Premium', 'Total'])
        st.session_state.audit_log = pd.concat([st.session_state.audit_log, new_audit], ignore_index=True)
        
        st.markdown("---")
        if total >= 200: st.success(f"💎 {ticker_input} VERDICT: SOVEREIGN BUY ({total}/300)")
        elif total < 150: st.error(f"🚨 {ticker_input} VERDICT: TRAPDOOR SELL ({total}/300)")
        else: st.warning(f"⚖️ {ticker_input} VERDICT: AUDIT HOLD ({total}/300)")

        # SUB-PARTS
        f1, f2, f3 = st.columns(3)
        with f1:
            st.markdown('<div class="metric-header">STABILITY</div>', unsafe_allow_html=True)
            st.info("1. Op. Margin\n2. ROIC\n3. Debt/Equity")
        with f2:
            st.markdown('<div class="metric-header">GROWTH</div>', unsafe_allow_html=True)
            st.info("1. Rev Growth\n2. Market Share\n3. Capex")
        with f3:
            st.markdown('<div class="metric-header">PREMIUM</div>', unsafe_allow_html=True)
            st.info("1. Founder Alignment\n2. Pricing Power\n3. Moat")

# --- 5. PAGE 2: 5* MODELS HUB ---
elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Dashboard")
    
    # CALCULATE LIVE AGGREGATE
    if not st.session_state.audit_log.empty:
        live_avg = st.session_state.audit_log['Total'].mean()
        count = len(st.session_state.audit_log)
    else:
        live_avg = 0
        count = 0

    # SHOW AGGREGATION HEADER
    st.markdown(f"""
        <div class="aggregation-box">
            <h2 style="margin:0; color:#00FF41;">{live_avg:.1f} / 300</h2>
            <p style="margin:0; color:#8B949E;">AGGREGATED DYER SCORE ({count} ASSETS AUDITED)</p>
        </div>
    """, unsafe_allow_html=True)

    m_tab1, m_tab2, m_tab3, m_tab4, m_tab5 = st.tabs(["Model A (Cull)", "Model B (Reset)", "Model C", "Model D", "Model E (Anti)"])
    
    with m_tab1:
        st.subheader("Quarterly Cull Performance")
        if not st.session_state.audit_log.empty:
            st.table(st.session_state.audit_log.tail(10)) # Show last 10 audits
        else:
            st.write("No audits performed yet. Use the Scanner to update scores.")

    with m_tab5:
        st.subheader("Model E: Trapdoor Monitor")
        # Filter for anything under 150
        fails = st.session_state.audit_log[st.session_state.audit_log['Total'] < 150]
        st.error(f"Found {len(fails)} assets failing the Dyer threshold.")
        st.table(fails)
