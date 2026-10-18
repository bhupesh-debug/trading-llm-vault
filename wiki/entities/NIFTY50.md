---
type: entity
title: NIFTY 50 (^NSEI)
asset_class: Equity Benchmark Index
primary_exchange: National Stock Exchange of India (NSE)
liquidity: Ultra-High (Global Top Tier Derivative Volume)
typical_daily_range_atr: 250 - 350 points (~1.1% - 1.5%)
tags:
  - entity
  - ticker
  - benchmark
  - index
  - nse
  - fno
---

# Entity Profile: NIFTY 50 (`^NSEI` / `NIFTY`)

The flagship benchmark index representing the 50 largest and most liquid Indian equities listed on the National Stock Exchange (NSE). Nifty 50 futures and weekly options constitute one of the world's most heavily traded derivative contracts by volume.

---

## 1. Key Structural Characteristics

- **Trading Hours (IST)**:
  - Pre-Market: 09:00 - 09:08 IST
  - Regular Session: 09:15 - 15:30 IST
- **Key Sector Weights**:
  - Financial Services (~33%)
  - Information Technology (~14%)
  - Oil, Gas & Consumable Fuels (~12%)
  - Fast Moving Consumer Goods (~8%)
  - Automobile & Healthcare (~13%)
- **Major Anchor Heavyweights**: HDFC Bank, Reliance Industries, ICICI Bank, Infosys, TCS, Larsen & Toubro, Bharti Airtel.
- **Derivative Specifications & Mechanics**:
  - Detailed FnO Framework: [[NIFTY_Futures_and_Options_FnO_Mechanics]]
  - Expiry Cycle: Standard Weekly Thursday and Monthly Expiries (Cash Settled on 30-min VWAP).
  - Strike Increments: 50 points (ATM / near-month).
  - Margin Architecture: 100% upfront SPAN + Exposure; 50:50 cash-to-collateral rule for overnight positions.
- **Macro Drivers**:
  - RBI Monetary Policy Committee (MPC) repo rate decisions.
  - US 10-Year Yields & DXY (Dollar Index) foreign institutional investor (FII) flow dynamics.
  - Crude Oil prices (Brent) due to India's import sensitivity.

---

## 2. Intraday Personality & Execution Protocols

### A. The 09:15 – 09:30 AM Opening Volatility Shock
- Market open often absorbs overnight global cues (GIFT Nifty, Wall Street, Asian markets).
- Opening 15 minutes witness peak bid-ask spreads and market maker stop hunting.
- Per [[Rules_of_Engagement]] and [[Intraday_Options_Trend_Selling_Supertrend_Pivot]], avoid market orders before 09:30 AM to bypass the opening slippage trap (see [[Execution_Slippage_and_Edge_Decay]]).

### B. Daily Anchor Levels
For intraday trading, always map:
1. **Pivots**: Floor Daily Pivot, R1, R2, S1, S2 (calculated from prior session High, Low, Close).
2. **Prior Day High/Low (PDH / PDL)**: Prime zones for [[Support_Resistance_Liquidity_Sweep|Liquidity Sweeps]].
3. **Session VWAP**: Serves as the institutional demarcation between bullish and bearish control.

---

## 3. Systematic Strategy Mappings in Vault

| Strategy | Role of Nifty 50 | Execution Mechanism |
|---|---|---|
| [[Intraday_Options_Trend_Selling_Supertrend_Pivot]] | Primary Underlying | Directional writing on 5-min Supertrend (6, 3), 9 EMA, and daily pivot bounce/rejection |
| [[Nifty500_Stock_Momentum_V3_Regime]] | Macro Regime Filter | When Nifty 50 < 200 SMA or >50% constituents decline, fresh momentum equity buys are **halted** |
| [[Sell_Today_Buy_Tomorrow_STBT_Breakout]] | Overnight Futures/Options | Late-afternoon (03:15 PM) breakdown execution with 09:20 AM morning exit |
| [[Rainbow_Moving_Average_Ribbons_and_Macro_Bands]] | Trend & Pullback Filter | 8-Fibonacci EMA ribbon expansion/compression for swing and intraday trend bias |

---

## 4. Associated Trade Reviews & Debriefs
- Track logged executions in [[wiki/reviews/]].
