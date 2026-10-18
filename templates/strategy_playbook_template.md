---
type: strategy
title: {{strategy_name}}
asset_classes: Equities | Futures | Forex | Crypto
timeframes: 1m | 5m | 15m | 1h | Daily
status: active | testing | retired
expected_win_rate: 0%
target_reward_risk: 0:1
tags:
  - strategy
---

# Strategy: {{strategy_name}}

## 1. Core Hypothesis & Edge
- **Why does this edge exist?** (e.g., trapped liquidity, institutional rebalancing, algorithmic momentum overshoot, mean reversion).
- **Favorable [[Market_Regimes|Market Regime]]**: (e.g. high relative volume, trending above 20 EMA, low volatility consolidation).

## 2. Invalidation & Entry Rules
> [!CHECKLIST] Entry Criteria
> - [ ] Pre-condition 1
> - [ ] Pre-condition 2
> - [ ] Trigger candle / order flow confirmation

> [!DANGER] Invalidation & Stop Loss
> - Stop loss placement rule: (e.g., below swing low, beyond consolidation bracket).
> - Never move stop loss away from price.

## 3. Position Sizing & Target Management
- **Risk per trade**: Sized via [[Risk_Management_and_R_Multiples]] (strict 1R limit).
- **Target 1 (Scale/De-risk)**:
- **Runner Target / Trailing Rule**:

## 4. Trade History & Cumulative Statistics
- **Sample Size**: 0 trades
- **Win Rate**: 0%
- **Average Win**: +0.0R
- **Average Loss**: -1.0R
- **Profit Factor / Expectancy**: 0.0

## 5. Linked Debriefs
- (Links to [[wiki/reviews/]] files where this setup was traded)
