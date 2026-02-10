elif page == "🔬 5* MODELS HUB":
    st.title("🔬 5* Models Performance & Aggregation")
    st.write("Current Audit Cycle: **Day 36 / 120**")
    
    # AGGREGATED DATA TABLE
    model_stats = {
        "Model Name": ["Model A (Cull)", "Model B (Reset)", "Model C (Growth)", "Model D (Yield)", "Model E (Anti)"],
        "Avg Dyer Score": [268, 242, 275, 255, 118],
        "120-Day Return": ["+14.2%", "+8.1%", "+19.5%", "+4.3%", "-22.8%"],
        "10% Growth Goal": ["295", "266", "302", "280", "FAIL"],
        "Audit Status": ["ON TRACK", "STALLED", "ON TRACK", "MONITOR", "LIQUIDATE"]
    }
    
    st.table(pd.DataFrame(model_stats))
    
    st.markdown("---")
    st.subheader("Model A: Top 5 vs Bottom 5")
    st.info("Strategy: Quarterly Cull. Current focus: Sell bottom 5 by 25% on Day 90.")
