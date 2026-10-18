---
type: strategy
title: Minervini Volatility Contraction Pattern (VCP)
asset_classes: Equities (Mid & Large Cap Growth)
timeframes: Daily / Weekly
status: active
expected_win_rate: ~50%
target_reward_risk: 3:1 - 5:1
tags:
  - strategy
  - minervini
  - vcp
  - swing-trading
  - momentum
---

# Strategy: Minervini Volatility Contraction Pattern (VCP)

The Volatility Contraction Pattern (VCP) is an institutional accumulation setup developed by U.S. Investing Champion Mark Minervini. It exploits the progressive drying up of floating supply across multiple contractions before a high-velocity momentum breakout.

---

## 1. Core Hypothesis & Edge
- When an institutional stock pauses after an uptrend, retail sellers and impatient holders exit.
- Each successive wave of selling encounters stronger institutional absorption at higher support levels, resulting in progressively smaller price pullbacks and drying volume.
- Once overhead supply is completely absorbed, minimal buying pressure drives a powerful breakout.
- **Underlying Source**: [[Mark_Minervini_Setup_Study]] (extracted from `raw/document.pdf`).

---

## 2. Invalidation & Entry Rules

> [!CHECKLIST] Screening & Pre-Conditions (Trend Template)
> - [ ] Price > $30 (No penny stocks)
> - [ ] 200 SMA is rising for at least 3 months
> - [ ] 50 SMA is above 200 SMA
> - [ ] Current price is above 200 SMA and preferably 50 SMA
> - [ ] Current price is at least 100% off its 52-week low
> - [ ] Current price is within 25% of its 52-week high

> [!CHECKLIST] Pattern & Entry Criteria
> - [ ] **Base Duration**: Consolidating for 4 to 8 weeks.
> - [ ] **Contraction Waves**: Ideally 3 contractions (e.g., -16% drop, then -8% drop, then -4% drop). Each contraction decreases volatility by ~50%.
> - [ ] **Volume Confirmation**: Volume steadily contracts during the base and reaches extreme lows on the tightest final contraction.
> - [ ] **Buy Trigger**: Price crosses the previous swing pivot high with an expansion in daily volume (at least +50% above 50-day average volume).

> [!DANGER] Invalidation & Stop Loss
> - **Initial Stop Loss**: $2 \times \text{ATR}(20)$ below the buy point (Hard cap: Maximum 10%).
> - Never adjust stop loss lower.

---

## 3. Position Sizing & Pyramiding Execution

- **First Tranche**: 0.5% account capital at risk (1.0R).
- **Pyramiding Rule**:
  - Add to the position only if the stock gains **> 5%** from the initial entry.
  - Advance the stop loss on the initial tranche to **Breakeven**.
  - Risk on second tranche: 0.5% to 1.0% with stop loss placed at $2 \times \text{ATR}(20)$ from the addition level.

---

## 4. Exit Rules & Target Management

1. **ATR Trailing Stop**: Trail stop loss upward as ATR advances.
2. **Climax / Parabolic Take-Profit**: If the 10 DMA slope accelerates into an 80°–90° vertical angle, begin taking profits into strength.
3. **Distribution Warning**: Exit if the stock drops heavily on abnormally large volume or creates an unfilled exhaustion gap.
4. **Time Stop**: If the stock remains flat or fails to expand within 15–20 trading days, close the position to recycle capital.

---

## 5. Risk Controls & Drawdown Budget
- Respect the **5–6% monthly drawdown budget** from [[Rules_of_Engagement]]: if the portfolio declines 5–6% in a single calendar month, immediately go to 100% cash and halt trading until the next month.

---

## 6. Programmatic Screening & Python Scanner Implementation

Based on the quantitative scanner by Marco Hui ([[Marco_Hui_VCP_Algorithmic_Screener]], script at [[raw/market_notes/vcp_screener.py]]):

### Trend Template Algorithmic Rules:
1. **Moving Average Alignment**:
   $$\text{Price} > \text{SMA}_{150} > \text{SMA}_{200} \quad \text{and} \quad \text{Price} > \text{SMA}_{50} > \text{SMA}_{150}$$
2. **200 SMA Linear Slope**:
   Calculated across a 20-day rolling window:
   $$\text{Slope} = \frac{N \sum(i \cdot P_i) - \sum P_i \sum i}{N \sum i^2 - (\sum i)^2} > 0.0$$
3. **52-Week Price Anchors**:
   - $\text{Price} \ge 1.30 \times \text{Low}_{52w}$ (At least 30% off lows)
   - $\text{Price} \ge 0.75 \times \text{High}_{52w}$ (Within 25% of highs)
4. **Relative Strength Line vs. S&P 500**:
   $$\text{RS} = \frac{\text{Price}}{\text{SPX}}$$
   Must show a positive 20-day regression slope ($\text{Slope}_{\text{RS}} > 0$).
5. **VCP Base Constraints**:
   - Number of contractions: $2 \le N \le 4$
   - Maximum contraction (first swing): $\le 50\%$
   - Minimum contraction (final pivot): $\le 15\%$
   - Base duration: $\ge 2$ weeks (10 trading sessions)
   - Volume contraction: $\text{SMA}_5(\text{Volume}) < \text{SMA}_{30}(\text{Volume})$
   - Price Consolidation: $\text{High}_{\text{current}} < \text{Peak High}$ (Base is active, not broken out).
