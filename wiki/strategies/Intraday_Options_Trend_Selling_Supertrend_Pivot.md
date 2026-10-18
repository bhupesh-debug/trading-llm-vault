---
type: strategy
title: Intraday Options Trend Selling (Supertrend + Daily Pivots)
asset_classes: Index Options (Nifty / Bank Nifty / SPY / QQQ)
timeframes: 5m
status: active
expected_win_rate: 65-75%
target_reward_risk: 1.5:1 - 2:1
tags:
  - strategy
  - options-selling
  - intraday
  - trend-following
  - supertrend
---

# Strategy: Intraday Options Trend Selling (Supertrend + Daily Pivots)

Developed from the quantitative architecture of Keshav ([[Keshav_Systematic_Options_Algo_Framework]]), this strategy sells single-leg ATM/OTM options in the direction of strong intraday momentum, filtering out range-bound chop using Daily Pivot thresholds and front-running market-maker stop sweeps.

---

## 1. Technical Indicators & Parameters

| Indicator | Setting | Operational Purpose |
|---|---|---|
| **Supertrend** | Factor: `6`, Multiplier: `3` (5m timeframe) | Filters out noise; captures 30-minute institutional trend blocks |
| **9 EMA** | Exponential Moving Average (9-period) | Trend velocity check. Lows avoiding the 9 EMA confirms clean trend |
| **Daily Pivots** | Standard Pivot Points (Pivot, R1, S1, S2) | Chop filter. Zone between R1 and S1 is a designated dead zone |

---

## 2. Market Regime & Filter Pre-Conditions

> [!CHECKLIST] Daily Screening & Pre-Flight Checklist
> - [ ] **Trading Window**: Only take entries between **09:20 and 14:30**. No entries after 14:30.
> - [ ] **Expiry Day Exit**: Close all open positions by **15:00** strictly.
> - [ ] **Daily Frequency Limit**: Maximum **3 trades per day** (total calls + puts). If 3 trades fire, cease execution regardless of market action.
> - [ ] **Dead Zone Filter**: Do NOT initiate new positions if price is oscillating between Central Pivot and R1, or between Central Pivot and S1.

---

## 3. Setup Triggers & Entry Arithmetic

### Setup A: Bullish Momentum (Sell ATM Put)
1. **Pivot Break**: Price opens or breaks cleanly above **R1**.
2. **Re-test or Green Candle**: First 5-minute candle low dips to touch R1 and rejects upward, OR a clean green candle closes above R1.
3. **Supertrend & EMA Alignment**: Supertrend is Green (Bullish); candle low does not touch the 9 EMA.
4. **Proprietary Non-Swept Entry Trigger**:
   $$\text{Trigger Price} = \min(\text{Close} + 5 \text{ pts}, \text{High} + 2 \text{ pts})$$
   *(Bypasses retail stop clusters at candle highs where HFT algorithms induce maximum slippage).*
5. **Execution**: Sell At-The-Money (ATM) Put option.

### Setup B: Bearish Momentum (Sell ATM Call)
1. **Pivot Break**: Price opens or breaks cleanly below **S1**.
2. **Re-test**: Candle retests S1 from below and rejects.
3. **Supertrend & EMA Alignment**: Supertrend is Red (Bearish); candle highs do not penetrate above the 9 EMA.
4. **Execution**: Sell At-The-Money (ATM) Call option.

### Setup C: Short Covering Reversal (Sell ATM Put)
1. Price flushes down to **S2 low**, rejects, and fails to continue downward.
2. Supertrend flips from Red to Green.
3. Candle lows hold above 9 EMA.
4. **Execution**: Sell ATM Put option.

---

## 4. Volatility-Adjusted Strike Selection

> [!WARNING] The High-VIX Point-Risk Trap
> - When VIX is normal, ATM options trade at ₹80–₹120. A 20% stop loss = 16 to 24 points of risk.
> - When VIX spikes, ATM options trade at ₹250–₹300. A 20% stop loss = 50 to 60 points of risk ($60 \times \text{lot size}$)!
> - **The Filter Rule**: Only sell ATM strikes if the option premium is **$< \text{₹}120$**. If ATM premium exceeds ₹140, shift strike selection out-of-the-money (OTM) to select an option priced between ₹80–₹110.

---

## 5. Invalidation, Stop Loss & Exit Rules

1. **Indicator Invalidation**:
   - Exit immediately if Supertrend flips against the position.
   - Exit if underlying spot price breaks **10 points** past the Supertrend line.
2. **Premium Stop Loss**:
   - Hard stop loss set at **20%** above entry premium.
   - Max portfolio stop cap: ₹6,000 per lot / 1.0R maximum.
3. **Time-Based Exit**:
   - Daily squared-off at 15:10 (or 15:00 on expiry days).
   - Zero overnight risk.

---

## 6. Statistical Benchmarks & Performance Goals
- **Win Rate**: ~68–74%
- **Max Drawdown Target**: $< 2.5\%$
- **Calmar Ratio Target**: $> 10$
- **Average Trades Per Month**: ~20–25 trades (saving transaction costs and STT drag).
