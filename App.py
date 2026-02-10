import streamlit as st
import pandas as pd

# --- UI CONFIG ---
st.set_page_config(page_title="Dyer Research Lab", layout="wide")

# --- CUSTOM CSS FOR CLEAN CARDS ---
st.markdown("""
    <style>
    .model-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    .status-pass { color: #238636; font-weight: bold; }
    .status-fail { color: #DA3633; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
nav = st.sidebar.radio("Lab Navigation", ["🏛️ Research Homepage", "📡 Asset Scanner"])

if nav == "🏛️ Research Homepage":
    st.title("🔬 The 14-Chapter Lab")
    st.subheader("120-Day Audit Cycle: **84 Days Remaining**")
    
    # 5-Model Simulation Data
    models = {
        "Model A (Cull Strategy)": {"Score": 245, "Delta": "+12%", "Status": "PASSING"},
        "Model B (90-Day Rebalance)": {"Score": 210, "Delta": "+4%", "Status": "AUDIT REQ"},
        "Model C (High Premium)": {"Score": 265, "Delta": "+15%", "Status": "PASSING"},
        "Model D (Value/Asset)": {"Score": 185, "Delta": "-2%", "Status": "FAILING"},
        "Model E (Anti-Model)": {"Score": 82, "Delta": "-20%", "Status": "TRAPDOOR"}
    }

    # Display 5 Models in a Grid
    cols = st.columns(5)
    for i, (name, data) in enumerate(models.items()):
        with cols[i]:
            status_class = "status-pass" if "PASSING" in data['Status'] else "status-fail"
            st.markdown(f"""
                <div class="model-card">
                    <h4>{name}</h4>
                    <h2 style="margin: 10px 0;">{data['Score']}</h2>
                    <p>Cycle Delta: <b>{data['Delta']}</b></p>
                    <p class="{status_class}">{data['Status']}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🏁 Auditor Leaderboard")
    st.table(pd.DataFrame({
        "Auditor": ["YOU (SOV-00)", "MOM (SOV-01)", "DAD (SOV-02)"],
        "Points": [150, 45, 30],
        "Chapter Rank": ["Chapter 14: Master", "Chapter 4: Apprentice", "Chapter 2: Novice"]
    }))

elif nav == "📡 Asset Scanner":
    # Scanner Code here
    st.title("📡 Asset Scanner")
    st.write("Scan a ticker to update the Dyer Score for the 120-day cycle.")
