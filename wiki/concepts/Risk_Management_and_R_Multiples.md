---
type: concept
title: Risk Management and R-Multiples
category: math_and_risk
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - risk
  - math
  - sizing
---

# Concept: Risk Management and R-Multiples

The foundation of profitable trading is not forecasting the future; it is **asymmetric risk-to-reward management** and **capital survival**.

---

## 1. What is an "R"?

**1R** represents your predefined, dollar-denominated risk on a single trade.

$$\text{1R} = \text{Account Size} \times \text{Risk Percentage (e.g. 1\%)}$$

Example:
- Account Size: \$50,000
- Risk per Trade: 1.0%
- **1R = \$500**

All performance in this vault must be measured in **R-multiples**, never in raw dollars or percentages. Measuring in dollars triggers emotional attachment; measuring in R standardizes statistical expectancy.
- A **+2R** trade = +$1,000 profit.
- A **-1R** trade = -$500 loss (planned).
- A **-2.5R** trade = Catastrophic execution failure (holding past stop loss or moving stop).

---

## 2. Position Sizing Formula

Calculate exact share/contract size based on distance between **Entry** and **Stop Loss**:

$$\text{Position Size (Shares)} = \frac{\text{Dollar Risk (1R)}}{|\text{Entry Price} - \text{Stop Loss Price}|}$$

### Example:
- Capital at Risk (1R): \$500
- Setup: [[Opening_Range_Breakout]] on [[SPY]]
- Entry Price: \$580.00
- Stop Loss: \$578.50
- Stop Distance: \$1.50
- **Size = \$500 / \$1.50 = 333 shares**

> [!WARNING] Never Fit the Stop to the Size
> Determine the **technical stop loss** first based on market structure. Then calculate the size to equal 1R. Never size a position first and then pick a random stop loss!

---

## 3. Mathematical Expectancy Formula

An edge exists only if your mathematical expectancy per trade $E$ is positive:

$$E = (\text{Win Rate} \times \text{Average Win in R}) - (\text{Loss Rate} \times \text{Average Loss in R})$$

### Benchmark Scenarios:
| Win Rate | Avg Win | Avg Loss | Expectancy ($E$) | Verdict |
|---|---|---|---|---|
| 40% | +2.5R | -1.0R | $(0.40 \times 2.5) - (0.60 \times 1.0) = \mathbf{+0.40R}$ | Highly Profitable |
| 50% | +1.5R | -1.0R | $(0.50 \times 1.5) - (0.50 \times 1.0) = \mathbf{+0.25R}$ | Solid Edge |
| 70% | +0.5R | -1.8R | $(0.70 \times 0.5) - (0.30 \times 1.8) = \mathbf{-0.19R}$ | Bleeding Capital |

---

## 4. Drawdown & Asymmetric Loss Recovery

Losses compound against you non-linearly:
- 10% loss requires an 11.1% gain to recover.
- 20% loss requires a 25.0% gain to recover.
- 33% loss requires a 50.0% gain to recover.
- 50% loss requires a 100.0% gain to recover.

By strictly limiting individual trades to **1.0R** and daily loss to **-3.0R** (as mandated in [[Rules_of_Engagement]]), account ruin is mathematically impossible over any normal distribution of trading variance.
