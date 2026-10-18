---
type: source
title: Marco Hui Algorithmic VCP Screener
author: Marco Hui
source_file: "[[raw/market_notes/Marco_Hui_VCP_Screener_Study.md]]"
source_code: "[[raw/market_notes/vcp_screener.py]]"
source_type: github_repository
date_ingested: 2026-10-18
tags:
  - source-summary
  - vcp
  - minervini
  - algorithmic-screener
  - python
---

# Source Summary: Marco Hui Algorithmic VCP Screener

## Overview
- **Repository**: `https://github.com/marco-hui-95/vcp_screener.github.io`
- **Saved Script**: [[raw/market_notes/vcp_screener.py]]
- **Subject**: Automated Python implementation of Mark Minervini's Stage 2 Trend Template and Volatility Contraction Pattern (VCP) detection.

---

## Key Algorithmic Innovations

### 1. Mathematical 200 SMA & RS Line Slope Calculation
Rather than relying on visual inspection of the 200-day moving average, the script computes the exact linear regression slope across a rolling 20-day window:
$$\text{Numerator} = N \sum (i \cdot P_i) - \left(\sum P_i\right)\left(\sum i\right)$$
$$\text{Denominator} = N \sum i^2 - \left(\sum i\right)^2$$
A strictly positive slope ($\text{Slope} > 0$) mathematically guarantees the 200 SMA and Relative Strength line (vs. S&P 500) are trending upward for at least one month.

### 2. Peak-Valley Alternating Extrema Detection
Using `scipy.signal.argrelextrema(order=10)`, the script identifies candidate swing highs and lows, then iterates to eliminate consecutive highs without an intervening low and consecutive lows without an intervening high. This models genuine market swings.

### 3. Quantitative VCP Gate
A stock is mathematically confirmed as forming a valid VCP setup if and only if:
1. Contraction count $N \in [2, 4]$.
2. Primary contraction depth $\le 50\%$.
3. Final pivot contraction depth $\le 15\%$.
4. Duration across contractions $\ge 2$ weeks.
5. Volume dry-up: 5-day volume moving average $< 30$-day volume moving average ($\text{SMA}_5(\text{Vol}) < \text{SMA}_{30}(\text{Vol})$).
6. Unbroken pivot: The stock has not yet broken out past the base high.
7. Relative Strength rating $\ge 70$.

---

## Vault Cross-References
- Strategy Playbook: [[Minervini_Volatility_Contraction_Pattern_VCP]]
- Foundational Theory: [[Mark_Minervini_Setup_Study]]
- General Quantitative Edge: [[Algorithmic_Edge_and_Quantitative_Metrics]]
