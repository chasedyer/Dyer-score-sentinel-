import pandas as pd

# The 7 Portfolio Architecture
portfolios = {
    "Model A": ["PLTR", "ARM", "PGR", "ANET", "VRT", "DKNG", "HIMS", "CELH", "MDB", "UBER"],
    "Model B": ["CDNS", "LRCX", "TMO", "INTU", "ACN", "ORCL", "SYK", "TJX", "LIN", "RS"],
    "Model C": ["SBUX", "NKE", "PYPL", "LULU", "DIS", "TSLA", "UPS", "ENPH", "MMM", "BA"],
    "Model D": ["MSFT", "COST", "V", "WM", "DE", "ASML", "LLY", "CP", "NEE", "BRK.B"],
    "Model E": ["NKLA", "SAVE", "AMC", "CVNA", "PTON", "BYND", "LCID", "RILY", "GME", "WBA"],
    "Model F": ["MELI", "AXON", "IOT", "SHOP", "DDOG", "DUOL", "BWXT", "COIN", "PINS", "U"],
    "Model G": ["PANW", "BKH", "BFLY", "NSA", "DUOT", "NBIS", "PUBM", "BKRRF", "INSG", "CFLD"]
}

def render_tab_2(ticker_data, dyer_scores):
    summary = []
    for model, tickers in portfolios.items():
        for t in tickers:
            # 1. Performance Logic
            ytd_change = (ticker_data[t]['price'] / ticker_data[t]['open'] - 1)
            color = "green" if ytd_change >= 0 else "red"
            
            # 2. Allocation ($1k per stock) + 0.5 Rounding
            raw_shares = 1000 / ticker_data[t]['price']
            final_shares = int(raw_shares + 0.5)
            
            # 3. Dyer Score Tracking (S + G + P)
            score = dyer_scores.get(t, 0)
            
            summary.append({
                "Portfolio": model,
                "Ticker": t,
                "Shares": final_shares,
                "Dyer Score": score,
                "YTD": f"{ytd_change:.2%}",
                "Status": color
            })
    return pd.DataFrame(summary)

# Waitlist (Manual Tracking Only - Does not affect site code)
# Alpha Watch: RDDT, TTAN
