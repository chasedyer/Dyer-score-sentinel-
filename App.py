import pandas as pd

# 1. THE LANDING PAGE (RE-CENTERED & PROTECTED)
def render_landing_page():
    """
    This function renders the 'Perfect' Landing Page as described.
    It is 100% isolated from the data logic to prevent blank screens.
    """
    return """
    <div class="landing-page" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 80vh; font-family: 'Inter', sans-serif;">
        <h1 style="font-size: 52px; font-weight: 800; color: #111; margin-bottom: 20px;">Search Assets</h1>
        <div class="search-container" style="position: relative;">
            <input type="text" placeholder="Search Tickers, Models, or Metrics..." 
                   style="width: 550px; padding: 22px 30px; border-radius: 50px; border: 1px solid #e0e0e0; font-size: 19px; box-shadow: 0 10px 25px rgba(0,0,0,0.04); outline: none;">
        </div>
        <p style="margin-top: 30px; color: #999; letter-spacing: 1px; font-size: 14px; text-transform: uppercase;">
            7 Portfolios Active | $70,000 Total Allocation | Dyer Sentinel Mode: ON
        </p>
    </div>
    """

# 2. THE 7-PORTFOLIO MASTER DIRECTORY (70 TICKERS)
# $10,000 per model | $1,000 per ticker
portfolios = {
    "Model A (Velocity)": ["PLTR", "ARM", "PGR", "ANET", "VRT", "DKNG", "HIMS", "CELH", "MDB", "UBER"],
    "Model B (Core)": ["CDNS", "LRCX", "TMO", "INTU", "ACN", "ORCL", "SYK", "TJX", "LIN", "RS"],
    "Model C (Excavation)": ["SBUX", "NKE", "PYPL", "LULU", "DIS", "TSLA", "UPS", "ENPH", "MMM", "BA"],
    "Model D (Sovereign)": ["MSFT", "COST", "V", "WM", "DE", "ASML", "LLY", "CP", "NEE", "BRK-B"],
    "Model E (Anti-Model)": ["NKLA", "SAVE", "AMC", "CVNA", "PTON", "BYND", "LCID", "RILY", "GME", "WBA"],
    "Model F (Rushmore 10)": ["MELI", "AXON", "IOT", "SHOP", "DDOG", "DUOL", "BWXT", "COIN", "PINS", "U"],
    "Model G (Spec Alpha)": ["PANW", "BKH", "BFLY", "NSA", "DUOT", "NBIS", "PUBM", "BKRRF", "INSG", "CLFD"]
}

# 3. THE DATA ENGINE (TAB 2)
def get_tab_2_data(price_data, dyer_metrics):
    """
    Calculates YTD Performance (Green/Red), Shares (0.5 Rule), and Dyer Score Tracking.
    """
    ledger = []
    for model_name, tickers in portfolios.items():
        for ticker in tickers:
            # Price Fetching
            current_price = price_data.get(ticker, 100.0)
            start_price = price_data.get(f"{ticker}_YTD", current_price)
            
            # YTD Calculation & Color Trigger
            perf = (current_price / start_price) - 1
            color_status = "GREEN" if perf >= 0 else "RED"
            
            # THE 0.5 ROUNDING RULE ($1,000 Allocation)
            shares = int((1000 / current_price) + 0.5)
            
            # Dyer Score (Stability + Growth + Premium)
            score = dyer_metrics.get(ticker, "Audit Pending")
            
            ledger.append({
                "Model": model_name,
                "Ticker": ticker,
                "Shares": shares,
                "Dyer Score": score,
                "Performance": f"{perf:.2%}",
                "Status": color_status
            })
    return pd.DataFrame(ledger)

# 4. THE ALPHA WATCHLIST (HIDDEN BENCHMARKS)
# Tracked to calculate "Waitlist Lag" vs Dyer Score
alpha_watch = ["RDDT", "TTAN"]
