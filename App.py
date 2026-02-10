import pandas as pd

# Finalized 7 Portfolio Matrix
portfolios = {
    "Model A (Velocity)": ["PLTR", "ARM", "PGR", "ANET", "VRT", "DKNG", "HIMS", "CELH", "MDB", "UBER"],
    "Model B (Core)": ["CDNS", "LRCX", "TMO", "INTU", "ACN", "ORCL", "SYK", "TJX", "LIN", "RS"],
    "Model C (Excavation)": ["SBUX", "NKE", "PYPL", "LULU", "DIS", "TSLA", "UPS", "ENPH", "MMM", "BA"],
    "Model D (Sovereign)": ["MSFT", "COST", "V", "WM", "DE", "ASML", "LLY", "CP", "NEE", "BRK-B"],
    "Model E (Anti-Model)": ["NKLA", "SAVE", "AMC", "CVNA", "PTON", "BYND", "LCID", "RILY", "GME", "WBA"],
    "Model F (Rushmore)": ["MELI", "AXON", "IOT", "SHOP", "DDOG", "DUOL", "BWXT", "COIN", "PINS", "U"],
    "Model G (Spec Alpha)": ["PANW", "BKH", "BFLY", "NSA", "DUOT", "NBIS", "PUBM", "BKRRF", "INSG", "CLFD"]
}

# Dyer Score Tracking & Performance Logic
def update_tab_2_dashboard(price_data, current_dyer_scores):
    summary_table = []
    
    for model_name, tickers in portfolios.items():
        for ticker in tickers:
            # Calculate YTD Performance
            ytd_pct = (price_data[ticker]['current'] / price_data[ticker]['ytd_start'] - 1) * 100
            perf_color = "green" if ytd_pct >= 0 else "red"
            
            # Fetch Dyer Scores (Stability, Growth, Premium)
            scores = current_dyer_scores.get(ticker, {"S": 0, "G": 0, "P": 0})
            total_dyer = scores['S'] + scores['G'] + scores['P']
            
            summary_table.append({
                "Model": model_name,
                "Holding": ticker,
                "Dyer Score": f"{total_dyer}/300",
                "YTD %": f"{ytd_pct:.2f}%",
                "Color": perf_color,
                "Shares": 1000 // price_data[ticker]['ytd_start'] # 0.5 rounding rule applied at execution
            })
    
    return pd.DataFrame(summary_table)
