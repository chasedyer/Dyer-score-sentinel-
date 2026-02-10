import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CORE LOGIC ---
# Cycle: 120 Days | Target: +10% Improvement
START_DATE = datetime(2026, 1, 1) # Start of the current cycle
CURRENT_DATE = datetime(2026, 2, 9)
DAYS_ELAPSED = (CURRENT_DATE - START_DATE).days

def calculate_dynamic_aggregate(base_score, growth_rate):
    # Logic: base_score + (pro-rated growth over the 120-day cycle)
    improvement_needed = base_score * 0.10
    current_boost = (DAYS_ELAPSED / 120) * improvement_needed
    return round(base_score + current_boost, 1)

# --- 2. UI SETTINGS ---
st.set_page_config(page_title="Dyer 5* Model Hub", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .status-pass { color: #00FF41; font-weight: bold; }
    .status-fail { color: #FF4B4B; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE 5* MODELS HUB ---
st.title("🔬 5* MODELS DYNAMIC HUB")
st.subheader(f"Cycle Audit: Day {DAYS_ELAPSED} / 120")

# DATA AGGREGATION
# Base Scores are from Day 0 of the cycle
m_data = {
    "Model": ["Model A (Cull)", "Model B (Reset)", "Model C (Growth)", "Model D (Yield)", "Model E (Anti)"],
    "Base Score (Day 0)": [260, 240, 270, 250, 110],
    "Growth Velocity": [1.2, 0.8, 1.5, 0.5, -0.2] # Multiplier for the 10% goal
}

# Calculate live aggregate scores
current_scores = []
for i in range(len(m_data["Model"])):
    base = m_data["Base Score (Day 0)"][i]
    vel = m_data["Growth Velocity"][i]
    # Current Score = Base + (Pro-rated 10% target * Velocity)
    score = base + ((DAYS_ELAPSED / 120) * (base * 0.10) * vel)
    current_scores.append(round(score, 1))

# 4. RENDER PERFORMANCE TABLE
df = pd.DataFrame({
    "Model": m_data["Model"],
    "Base Aggregate": m_data["Base Score (Day 0)"],
    "CURRENT AGGREGATE": current_scores,
    "120-Day Target": [round(b * 1.1, 1) for b in m_data["Base Score (Day 0)"]],
    "Status": ["ON TRACK" if s > b else "FAIL" for s, b in zip(current_scores, m_data["Base Score (Day 0)"])]
})

st.table(df)

# 5. FORENSIC DRILL-DOWN
st.markdown("---")
st.write("### 🔍 Model-Level Diagnostics")
c1, c2, c3 = st.columns(3)
c1.metric("Model A Score", current_scores[0], f"+{current_scores[0]-260:.1f} vs Day 0")
c2.metric("Model C Score", current_scores[2], f"+{current_scores[2]-270:.1f} vs Day 0")
c3.metric("Model E Score", current_scores[4], f"{current_scores[4]-110:.1f} vs Day 0", delta_color="inverse")
