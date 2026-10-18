---
type: strategy
title: Nifty 500 Stock Momentum & V3 Market Breadth Regime Filter
asset_classes: Equities (Nifty 500 / Broad Market Equities)
timeframes: Monthly Rebalance
status: active
expected_cagr: 45-50%
target_max_drawdown: < 24%
tags:
  - strategy
  - equity-momentum
  - market-breadth
  - regime-filter
  - saddam-shaik
---

# Strategy: Nifty 500 Stock Momentum & V3 Market Breadth Regime Filter

Developed by Saddam Shaik ([[Three_Practitioners_Systematic_Frameworks_NotebookLM]]), this model captures high-momentum individual equities from the Nifty 500 while employing macro index-breadth circuit breakers that eliminate severe portfolio drawdowns during broad market bear markets.

---

## 1. Core Hypothesis & Edge
- Pure momentum investing generates outsized returns (often $> 60–100\%$ gross), but suffers catastrophic peak-to-trough drawdowns ($> 30–35\%$) during market sell-offs.
- By introducing **Macro Regime Filters** based on index trend and internal market breadth, new capital deployment is paused during market weakness, allowing existing positions to exit into cash and compressing maximum drawdown from **32% down to 24%** while preserving a **47% CAGR**.

---

## 2. Stock Screening Criteria & Rules

> [!CHECKLIST] Individual Stock Eligibility Filters
> - [ ] **Universe**: Nifty 500 constituents (eliminates illiquid micro-caps).
> - [ ] **Monthly RSI Momentum Sweet Spot**: Monthly Relative Strength Index (RSI) between **50 and 70**.
>   *(Avoids stocks with dead momentum $< 50$, and eliminates overextended exhaustion bubbles $> 70$)*.
> - [ ] **52-Week High Proximity**: Current price must be within **20% of its 52-week high**:
>   $$P_{\text{current}} \ge 0.80 \times P_{\text{52W High}}$$
> - [ ] **Trend Alignment**: Price must be trading strictly above its **200-day Simple Moving Average ($P > \text{SMA}_{200}$)**.

---

## 3. Portfolio Allocation & Rebalancing Rules

- **Position Count**: Select and hold the **Top 15 stocks** meeting all screening criteria, ranked by composite momentum score.
- **Rebalance Frequency**: Monthly review.
- **Rank Buffer Exit Rule**:
  - A stock is held as long as its momentum ranking remains within the **Top 30**.
  - If a stock's rank drops below **Rank 30**, exit 100% and replace it with the next qualified top-15 candidate.
  - This rank buffer prevents excessive turnover and churning from minor week-to-week rank fluctuations.

---

## 4. The V3 Market Breadth Regime Filter (Circuit Breaker)

Before executing monthly buys or deploying replacement capital, check the two master index-breadth health switches:

```
[Is Nifty 500 Index > 200 DMA?] ──► NO ──► [CIRCUIT BREAKER ACTIVATED: HALT ALL NEW BUYS]
               │ YES
               ▼
[Are > 50% of Constituents Positive?] ──► NO ──► [CIRCUIT BREAKER ACTIVATED: HALT ALL NEW BUYS]
               │ YES
               ▼
   [NORMAL BUY ALLOCATION PROCEEDS]
```

> [!DANGER] V3 Regime Rules
> 1. **Index Trend Rule**: If the broader **Nifty 500 Index** is trading **below its 200 DMA**, all new stock allocations are completely blocked.
> 2. **Index Breadth Rule**: If **$> 50\%$** of Nifty 500 constituent stocks are declining / in negative territory, all new stock entries are halted.
> 3. **Defensive Cash Conversion**: While new buys are blocked, existing positions that trigger trailing stops or rank drops ($> 30$) are closed and converted to **100% Cash**. The portfolio naturally rotates into defense until market health is restored.

---

## 5. Comparative Evolution: V1 vs. V2 vs. V3

| Version | Rules & Structure | CAGR | Max Drawdown | Verdict |
|---|---|---|---|---|
| **V1 Base** | 6 Stocks, No Regime Filter | **114%** | **~32%** | High return, but drawdowns break trader psychology |
| **V2 Top-15** | 15 Stocks, Exit when Rank > 30 | **63%** | **~30%** | Lower volatility, but still vulnerable to bear markets |
| **V3 Regime** | 15 Stocks + Index 200 DMA & Breadth Filter | **47%** | **24%** | **Optimal Institutional Risk-Adjusted Edge** |

---

## 6. Vault Cross-References
- Model Allocation: [[Psychological_Capital_Allocation_1X_Basket]] (45% equity tranche)
- Regime Theory: [[Market_Regimes]]
- Master Governance: [[Rules_of_Engagement]]
