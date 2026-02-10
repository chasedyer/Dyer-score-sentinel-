import pandas as pd

# Core Universe: The Core 13 + Waitlist
universe = ["MELI", "SHOP", "DDOG", "IOT", "AXON", "CRWD", "SNOW", "U", "PINS", "COIN", "DUOL", "BWXT", "NOW"]
waitlist = ["RDDT", "TTAN"]

# Allocation: $10,000 per Model ($1,000 per holding)
def get_shares_baseline(prices):
    # Focus: Model F (Rushmore 10)
    rushmore_10 = ["MELI", "AXON", "IOT", "SHOP", "DDOG", "DUOL", "BWXT", "COIN", "PINS", "U"]
    ledger = {}
    
    for ticker in rushmore_10:
        px = prices.get(ticker, 1.0)
        target_allocation = 1000
        raw_qty = target_allocation / px
        
        # Applying the 0.5 Rounding Rule
        if (raw_qty % 1) >= 0.5:
            qty = int(raw_qty) + 1
        else:
            qty = int(raw_qty)
        
        ledger[ticker] = qty
    return ledger

# Dyer Score Audit Protocol
audit_rules = {
    "cycle_days": 120,
    "target_improvement": 0.10, # 10% gain in score or fail
    "rebalance_model_b": 90    # 90-day equal weight reset
}
