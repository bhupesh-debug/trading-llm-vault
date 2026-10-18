import yfinance as yf
import pandas as pd
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def test_rainbow_valuation(ticker_symbol):
    print(f"\n{'='*60}")
    print(f"📊 TESTING FUNDAMENTAL RAINBOW VALUATION: {ticker_symbol}")
    print(f"{'='*60}")
    
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    
    current_price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
    bvps = info.get("bookValue", 0.0) or 0.0
    dps = info.get("dividendRate", 0.0) or 0.0
    eps = info.get("trailingEps", 0.0) or 0.0
    est = info.get("forwardEps", 0.0) or 0.0
    
    # Free Cash Flow Per Share
    fcf = info.get("freeCashflow")
    shares = info.get("sharesOutstanding")
    if fcf and shares and shares > 0:
        cfps = fcf / shares
    else:
        cfps = 0.0
        
    base_val = bvps + dps + cfps + eps + est
    
    print(f"  • Current Market Price: ${current_price:.2f}" if current_price else "  • Current Market Price: N/A")
    print(f"  • Book Value Per Share (BVPS): ${bvps:.2f}")
    print(f"  • Dividend Per Share (DPS):    ${dps:.2f}")
    print(f"  • Free Cashflow / Share(CFPS): ${cfps:.2f}")
    print(f"  • Trailing EPS (EPS):          ${eps:.2f}")
    print(f"  • Forward EPS Estimate (EST):  ${est:.2f}")
    print(f"  ---------------------------------------------")
    print(f"  🎯 UNIFIED INTRINSIC BASE:     ${base_val:.2f}")
    print(f"{'='*60}")
    
    if base_val <= 0:
        print("  ⚠️ Warning: Base valuation is zero or negative; multiplier model cannot be applied.")
        return
        
    multiplier = current_price / base_val if current_price else 0.0
    
    # Valuation Spectrum
    bands = {
        "0.2x (Deep Distress)": base_val * 0.2,
        "0.4x (Fire Sale)": base_val * 0.4,
        "0.6x (Undervalued)": base_val * 0.6,
        "0.8x (Margin of Safety)": base_val * 0.8,
        "1.0x (Intrinsic Base Anchor)": base_val * 1.0,
        "2.0x (Fair Accumulation)": base_val * 2.0,
        "3.0x (Stage 2 Growth Markup)": base_val * 3.0,
        "5.0x (Momentum Expansion)": base_val * 5.0,
        "7.0x (Extended Premium)": base_val * 7.0,
        "10.0x (Euphoric Bubble Climax)": base_val * 10.0,
    }
    
    print("\n🌈 MONEY MULTIPLIER SPECTRUM:")
    for label, val in bands.items():
        marker = " ◄ CURRENT PRICE" if current_price and abs(current_price - val) / val < 0.1 else ""
        print(f"  {label:<30} : ${val:>8.2f}{marker}")
        
    print(f"\n📈 CURRENT REALIZED MULTIPLIER: {multiplier:.2f}x")
    
    # Systematic Classification
    if multiplier < 0.8:
        regime = "DEEP VALUE / PANIC ACCUMULATION (High Margin of Safety)"
    elif multiplier <= 2.0:
        regime = "NEUTRAL FAIR VALUE (Institutional Accumulation / Base Building)"
    elif multiplier <= 5.0:
        regime = "MOMENTUM EXPANSION SWEET SPOT (Optimal for Minervini VCP / Breakouts)"
    elif multiplier <= 7.0:
        regime = "EXTENDED PREMIUM (Trail stops with 21 EMA; reduce fresh risk)"
    else:
        regime = "EUPHORIC BUBBLE EXHAUSTION (High distribution risk; disqualify new longs)"
        
    print(f"🏷️ SYSTEM REGIME: {regime}\n")

if __name__ == "__main__":
    tickers = ["AAPL", "NVDA", "MSFT"]
    if len(sys.argv) > 1:
        tickers = sys.argv[1:]
    for t in tickers:
        try:
            test_rainbow_valuation(t)
        except Exception as e:
            print(f"Error testing {t}: {e}")
