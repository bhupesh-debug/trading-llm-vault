---
type: concept
title: Execution Slippage, Edge Decay, and The Straddle Autopsy
category: market_microstructure
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - slippage
  - edge-decay
  - straddles
  - execution-friction
  - backtesting-realism
---

# Concept: Execution Slippage, Edge Decay, and The Straddle Autopsy

> *"A granular simulation was executed testing 9:15 AM to 3:29 PM straddles across every 1-minute increment... Incorporating a conservative slippage of ₹0.50 to ₹1.00 (0.5% to 1.0%) turns historically profitable months entirely negative ('all red')."* — [[Three_Practitioners_Systematic_Frameworks_NotebookLM]]

A common pitfall in algorithmic and quantitative trading is confusing **theoretical backtest gross profit** with **real-world net alpha**. When execution friction is modeled honestly, many popular mechanical strategies collapse.

---

## 1. The Anatomy of Edge Decay: The 9:20 AM Straddle

For several years, selling mechanical 9:20 AM short straddles (selling ATM Call + ATM Put with 20–25% stop loss) was popular among retail option traders in India.

### The Backtest Illusion vs. Reality:
```
[ Idealized Zero-Slippage Backtest ] ──► Shows Consistent Green Months (Gross Profit)
                                                    │
                                                    ▼
                     + Add Realistic Slippage (₹0.50 - ₹1.00 per leg)
                                                    │
                                                    ▼
[ Real-World Net Backtest ] ────────────► Completely RED (Net Loss across all parameters)
```

1. **Crowded Alpha**: When thousands of retail algorithms fire market orders at the exact same minute (09:20:00), institutional market makers widen spreads and front-run the surge.
2. **Volatile Whipsaws**: Intraday index volatility regimes have shifted; stop-losses on both legs are triggered with increasing frequency.
3. **The Slippage Multiplier**: A ₹0.50–₹1.00 drag on entry and exit across 2 legs $\times$ 22 trading days completely consumes thin statistical margins.

---

## 2. The Fallacy of Parameter Optimization on Decayed Edges

When a mechanical strategy ceases to generate profit, traders instinctively attempt to salvage it by adding more indicators or fine-tuning parameters (e.g., shifting stop losses from 25% to 27%, or changing 9:20 to 9:24).

> [!DANGER] First Law of Strategy Robustness
> If a strategy's core structural edge is negative after accounting for conservative slippage and exchange fees, **no amount of superficial parameter tweaking, machine learning, or complex rules can produce sustainable alpha.** The strategy must be retired.

---

## 3. Mandatory Quantitative Stress-Testing Protocol

Before deploying real capital behind any backtested trading system, enforce the **Frictional Stress Test**:

1. **Add Base Slippage**: Apply at minimum **0.5% to 1.0% slippage** (or ₹0.75 per leg on index options) to every simulated fill.
2. **Model Latency Jumps**: Assume stop-loss orders are filled 1–2 ticks beyond the trigger price during fast-moving market cascades.
3. **Deduct Full Transaction Overhead**: Subtract brokerage, exchange fees, SEBI turnover charges, and capital gains / STT taxes.
4. **Viability Threshold**: The strategy must sustain a positive **Expectancy ($E > 0$)** and a **Calmar Ratio $> 2.0$** *after* full frictional deductions.

---

## 4. Vault Cross-References
- Algorithmic Longevity: [[Algorithmic_Edge_and_Quantitative_Metrics]]
- Institutional Order Flow: [[Institutional_Order_Flow_vs_Retail]]
- Alternative Option Edge: [[Intraday_Options_Trend_Selling_Supertrend_Pivot]]
- Master Risk Rules: [[Rules_of_Engagement]]
