import pandas as pd

# 1. Models Baseline
models = {
    "Model A": ["PLTR", "ARM", "PGR", "ANET", "VRT", "DKNG", "HIMS", "CELH", "MDB", "UBER"],
    "Model B": ["CDNS", "LRCX", "TMO", "INTU", "ACN", "ORCL", "SYK", "TJX", "LIN", "RS"],
    "Model C": ["MELI", "SHOP", "DDOG", "IOT", "AXON", "CRWD", "SNOW", "U", "PINS", "COIN", "DUOL", "BWXT", "NOW"],
    "Model D": ["MSFT", "COST", "V", "WM", "DE", "ASML", "LLY", "CP", "NEE", "BRK.B"],
    "Model F": ["MELI", "AXON", "IOT", "SHOP", "DDOG", "DUOL", "BWXT", "COIN", "PINS", "U"]
}

# 2. Share Calculation (1k Allocation + 0.5 Rule)
def get_stable_shares(prices):
    output = {}
    for model, tickers in models.items():
        allocation = 1000 if model != "Model C" else 769.23
        for t in tickers:
            px = prices.get(t, 100.0)
            raw = allocation / px
            # 0.5 Rounding Rule
            output[t] = int(raw + 0.5)
    return output

# 3. Sentinel Rules
rules = {"audit_cycle": 120, "target_growth": 0.10}
