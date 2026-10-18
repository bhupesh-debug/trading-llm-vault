---
type: strategy
title: Support and Resistance Liquidity Sweep
asset_classes: Equities | Futures | Crypto | Forex
timeframes: 5m | 15m | 1h
status: active
expected_win_rate: 55-65%
target_reward_risk: 2.0:1
tags:
  - strategy
  - smart-money
  - mean-reversion
  - liquidity
---

# Strategy: Support and Resistance Liquidity Sweep

The Liquidity Sweep (also known as a "turtle soup" or "stop hunt") capitalizes on institutional order matching: large players trigger resting retail stop-loss orders outside obvious key levels to build their own positions before driving price in the opposite direction.

---

## 1. Core Hypothesis & Edge
- Retail traders cluster stop-loss orders just beyond obvious technical levels: Prior Day High (PDH), Prior Day Low (PDL), Asian session highs/lows, or multi-day range limits.
- Market makers and algorithmic algorithms push price momentarily through these levels to absorb liquidity.
- Once the stops are triggered, buying/selling volume dries up, and the price sharply rejects back inside the range.
- **Favorable [[Market_Regimes|Market Regime]]**: Range-bound or choppy market regimes with low directional momentum.

---

## 2. Invalidation & Entry Rules

> [!CHECKLIST] Bullish Liquidity Sweep (Long) Setup
> 1. Identify a key support level (e.g., Prior Day Low or swing low on 15m / 1h chart).
> 2. Price pierces below support, triggering breakout shorts and resting stop-losses.
> 3. **The Sweep & Rejection**: A candle pierces below the level but leaves a prominent lower wick and closes back **above** the broken support level within 1-3 candles.
> 4. Delta / Volume: Heavy volume on the spike down followed by an immediate reversal (absorption).
> 5. **Entry**: Enter Long on the candle close back above the support line, or on a 1m retest of the reclaimed level.

> [!DANGER] Invalidation & Stop Loss
> - **Stop Loss**: Set just below the lowest wick of the sweep candle.
> - **Hard Invalidation**: If price closes below the sweep wick, the thesis is completely invalidated (it is a true breakdown, not a sweep). Cut immediately.

---

## 3. Position Sizing & Target Management

- Sized via [[Risk_Management_and_R_Multiples]] strictly to 1.0R.
- **Target 1 (+1.5R)**: Midpoint of the range or session VWAP.
- **Target 2 (+2.5R - 3.0R)**: Opposite boundary of the range (Prior Day High or session high).

---

## 4. Setup Disqualification
- Do NOT trade against a high-momentum catalyst trend day (e.g. gap and go on blowout earnings).
- Avoid if the sweep candle is too large (> 1.5x ATR), making the risk distance to the wick tip too wide for an attractive R-multiple.

---

## 5. Linked Debriefs & Reviews
- *Pending trade logs.*
