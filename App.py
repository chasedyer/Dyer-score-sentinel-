# 🛡️ DYER SENTINEL: HARDENED AUDIT ENGINE
def calculate_dyer_score(ticker, margin, growth, roic, mgmt_quality):
    # 100pt Stability: Based on Margin + ROIC
    stability = (margin * 2) + (roic * 1.5)
    # 100pt Growth: Based on Rev Growth + Capacity
    expansion = growth * 4
    # 100pt Premium: Based on Management/Moat (Your Chapter 14 Forensic)
    premium = mgmt_quality
    
    total = min(stability, 100) + min(expansion, 100) + min(premium, 100)
    
    print(f"--- AUDIT FOR {ticker} ---")
    print(f"RUSHMORE SCORE: {total}/300")
    if total >= 200: print("VERDICT: SOVEREIGN BUY")
    elif total < 150: print("VERDICT: TRAPDOOR SELL")
    else: print("VERDICT: AUDIT HOLD")
