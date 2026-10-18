---
type: concept
title: Market Regimes and Strategy Selection
category: market_microstructure
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - macro
  - market-structure
  - regimes
---

# Concept: Market Regimes and Strategy Selection

No trading strategy works in all market environments. A trader's edge depends on matching the active **Market Regime** to the appropriate playbook.

---

## 1. The Four Market Regimes

```
                      HIGH VOLATILITY (VIX > 25)
                                  │
         Breakout Traps           │         Violent Momentum
         Mean Reversion           │         Trend Following
       (Wide Stops / Small Size)  │         (Quick Scales / Runners)
                                  │
◄─────────────────────────────────┼─────────────────────────────────►
  RANGE-BOUND / CHOPPY            │             TRENDING
 (Price oscillating around VWAP)  │        (Higher Highs / 20 EMA slope)
                                  │
         Liquidity Sweeps         │         Moving Average Pullbacks
         Range Boundary Scalps    │         Opening Range Breakouts
         (Tight Targets)          │         (Trail Stops)
                                  │
                       LOW VOLATILITY (VIX < 15)
```

### Regime 1: Bullish / Bearish Strong Trend
- **Characteristics**: Price holds above/below 9 EMA and 20 EMA; high ADX (> 25); continuous one-directional volume.
- **Optimal Strategies**: [[Opening_Range_Breakout]], Trend Pullbacks, Continuation Flags.
- **Deadly Mistake**: Trying to pick the top or bottom with counter-trend mean reversion.

### Regime 2: Range-Bound / Chop (Distribution & Accumulation)
- **Characteristics**: Price repeatedly crosses VWAP back and forth; overlapping candles; declining volume.
- **Optimal Strategies**: [[Support_Resistance_Liquidity_Sweep]], Mean Reversion to VWAP.
- **Deadly Mistake**: Buying breakouts at range extremes (guaranteed trap).

### Regime 3: High Volatility Expansion (News / Earnings / Macro Shock)
- **Characteristics**: VIX spikes, huge candle wicks, wide bid-ask spreads, fast moves.
- **Execution Rule**: Cut normal position sizing in half (0.5R) to accommodate wider technical stop losses.

### Regime 4: Low Volatility Compression (Summer doldrums / Pre-holiday)
- **Characteristics**: Narrow daily ranges (low ATR), tight consolidation.
- **Execution Rule**: Reduce target expectations (take profits at 1.5R - 2R instead of waiting for 4R runners).

---

## 2. Daily Regime Filter Checklist

Before executing any trade on [[SPY]] or [[QQQ]]:
1. **Is price above or below Daily & 15m VWAP?**
2. **Where is price relative to Prior Day's High (PDH) and Low (PDL)?**
3. **What is the current VIX level and trend?**
4. **Is there an upcoming Fed announcement or major economic release today?**

---

## 3. Macro Market Breadth Circuit Breakers (The V3 Framework)

When executing equity momentum portfolios (see [[Nifty500_Stock_Momentum_V3_Regime]] and [[ETF_Momentum_Rotation_Model]]), individual stock filters are insufficient to stop bear market contagion. Professional systems enforce **Macro Index Breadth Gates**:

1. **Benchmark 200 DMA Gate**:
   - If the broad benchmark index (S&P 500 / Nifty 500) trades **below its 200 DMA**, all new risk allocations are frozen.
2. **Constituent Breadth Gate**:
   - If **$> 50\%$** of the index universe is trading in negative territory, freeze all new buys.
3. **The Drawdown Benefit**:
   - Applying these dual breadth filters compresses portfolio maximum drawdown from **~32% down to 24%** while preserving a **~47% CAGR** by systematically moving the portfolio to cash during prolonged distributions.
