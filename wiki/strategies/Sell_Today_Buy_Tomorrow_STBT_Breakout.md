---
type: strategy
title: Sell Today Buy Tomorrow (STBT) Breakout Strategy
asset_classes: Index Derivatives (Sensex / Nifty)
timeframes: Intraday Close to Next Day Open
status: active
expected_cagr: ~26%
target_max_drawdown: < 3%
tags:
  - strategy
  - stbt
  - breakout
  - overnight
  - quantitative
---

# Strategy: Sell Today Buy Tomorrow (STBT) Breakout Strategy

Extracted and backtested by Saddam Shaik using 3-year historical tick data ([[Three_Practitioners_Systematic_Frameworks_NotebookLM]]), this strategy captures afternoon institutional breakout continuation across the overnight cash session into the following morning's open.

---

## 1. Core Hypothesis & Edge
- Late-afternoon directional price discovery (14:30–15:20) frequently reflects institutional block orders establishing multi-day trend positions.
- When an afternoon range breaks out to new session extremes with expanding volume, overnight momentum exhibits strong continuation into the following morning's opening auction, allowing a rapid exit before intraday mean reversion begins.

---

## 2. Invalidation & Entry Rules

> [!CHECKLIST] Entry Setup Criteria
> - [ ] Time Window: 15:00 to 15:20 EST / IST (near regular trading session close).
> - [ ] Range Definition: Mark the afternoon session high and low range.
> - [ ] Downside Breakout Trigger: Underlying spot price breaches and closes below the defined session range floor.
> - [ ] Directional Execution: Sell Short Futures OR Sell At-The-Money / Out-Of-The-Money Call options (or buy put).

> [!DANGER] Invalidation & Stop Loss
> - Stop loss placed at the midpoint or opposite boundary of the late-afternoon breakout range.

---

## 3. Exit Rules & Target Management
- **Primary Exit**: Square off the entire position during the opening 5 to 15 minutes of the following morning's session (09:15–09:30).
- Do not hold into midday chop.

---

## 4. Multi-Year Backtest Performance (Sensex & Nifty Datasets)
- **CAGR**: **~26%**
- **Maximum Drawdown**: **2.76%** (Sensex dataset spanning June 2023 – May 2026)
- **Calmar Ratio**: **9.42**
- **Execution Warning**: Must incorporate realistic slippage and overnight margin requirements into live execution.
