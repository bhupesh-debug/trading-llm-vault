---
type: strategy
title: Opening Range Breakout (ORB)
asset_classes: Equities | Index ETFs (SPY, QQQ)
timeframes: 5m | 15m
status: active
expected_win_rate: 45-55%
target_reward_risk: 2.5:1
tags:
  - strategy
  - momentum
  - breakout
  - intraday
---

# Strategy: Opening Range Breakout (ORB)

The Opening Range Breakout (ORB) captures the expansion of institutional order flow that establishes the dominant directional trend of the day during the first 15–30 minutes of the market session.

---

## 1. Core Hypothesis & Edge
- At 09:30 EST, accumulated overnight orders, earnings reactions, and institutional imbalances enter the market.
- By 09:45 or 10:00 EST, a high and low for the opening window is formed.
- A breakout of this initial bracket with above-average volume frequently results in trapped counter-trend traders and fuel for a multi-hour trend continuation.
- **Favorable [[Market_Regimes|Market Regime]]**: Trending Days, High Relative Volume (`RVOL > 1.5`), Catalyst days.

---

## 2. Invalidation & Entry Rules

> [!CHECKLIST] Long Entry Setup Criteria
> 1. Establish the **15-minute Opening Range** (High & Low between 09:30 - 09:45 EST).
> 2. Daily trend alignment: Asset is trading above Daily VWAP and above yesterday's close.
> 3. Trigger: A 5-minute candle closes **above** the 15-minute Opening Range High with volume expanding above the 20-period volume average.
> 4. Entry: Immediate market order on candle close or limit order on a 1-minute retest of the broken level.

> [!DANGER] Invalidation & Stop Loss
> - **Initial Stop Loss**: Placed strictly below the midpoint of the 15-minute opening range or below the breakout candle low (whichever is tighter).
> - **Catastrophic Invalidation**: If price immediately falls back inside the range and closes below the VWAP, exit manually without waiting for full stop.

---

## 3. Position Sizing & Target Management

- **Risk per trade**: Sized to strictly 1.0R using [[Risk_Management_and_R_Multiples]].
- **Target 1 (+1.5R)**: Scale out 50% of the position to secure the trade and move stop-loss to Breakeven.
- **Target 2 (+2.5R - 3.5R)**: Target next major daily pivot, Average True Range (ATR) extension, or round psychological level.
- **Runner (Trailing)**: Trail remaining 25% behind the 15-minute 9 EMA until a close below it.

---

## 4. Setup Disqualification
- Do NOT take ORB if the opening range is already larger than 80% of the asset's typical Daily ATR (overextended).
- Do NOT take ORB if major FOMC / Fed announcement occurs at 10:00 or 14:00 EST.

---

## 5. Linked Debriefs & Reviews
- *No trade debriefs logged yet. Run an `ingest` on your next ORB trade to populate statistical tracking.*
