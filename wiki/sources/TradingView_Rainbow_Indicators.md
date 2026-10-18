---
type: source
title: TradingView Rainbow Indicators & Multi-Timeframe Clouds
author: TradingView Community Script Authors
source_file: "[[raw/market_notes/TradingView_Rainbow_Indicators_and_MA_Clouds.md]]"
source_type: technical_documentation
date_ingested: 2026-10-18
tags:
  - source-summary
  - indicators
  - moving-averages
  - rainbow-cloud
  - pine-script
---

# Source Summary: TradingView Rainbow Indicators & Multi-Timeframe Clouds

## Overview
Analysis of the "Rainbow" indicator family popular in the TradingView community scripts ecosystem, categorizing tools that use multi-layered moving average cascades and logarithmic sentiment channels.

---

## Key Frameworks & Technical Anatomy

### 1. The Rainbow Moving Average Ribbon / Cloud
- **Core Mechanism**: Layers 8 to 10 Exponential or Simple Moving Averages, typically using Fibonacci lookbacks:
  $$\text{Lookbacks} \in \{8, 13, 21, 34, 55, 89, 144, 233\}$$
- **Directional State Hierarchy**:
  - **Perfect Bullish Alignment**: $\text{MA}_8 > \text{MA}_{13} > \text{MA}_{21} > \dots > \text{MA}_{233}$. Confirms institutional accumulation and aggressive momentum.
  - **Perfect Bearish Alignment**: $\text{MA}_8 < \text{MA}_{13} < \text{MA}_{21} < \dots < \text{MA}_{233}$. Confirms institutional liquidation.
- **Volumetric Ribbon Spread**:
  - **Widening Ribbon (Expansion)**: The distance between short and long MAs expands, signaling acceleration and continuation of the active trend.
  - **Compressing / Entangled Ribbon (Contraction)**: Moving averages twist and overlap tightly, signaling a transition into [[Market_Regimes#Regime-2-Range-Bound--Chop-Distribution--Accumulation|Range-Bound Chop]] or an impending volatility breakout.

### 2. Macro Logarithmic Sentiment Rainbows
- **Application**: Applied primarily to secular cyclical assets like Bitcoin ($BTC) and Ethereum ($ETH).
- **Structure**: Uses historical non-linear logarithmic regression curves divided into color-coded sentiment bands:
  - Deep Blue / Violet: Fire-Sale / Heavy Accumulation.
  - Green / Yellow: Balanced Fair Value / HODL zone.
  - Orange / Dark Red: Parabolic Euphoria / Maximum Distribution Peak.

---

## Direct Vault Cross-References
- Concept: [[Rainbow_Moving_Average_Ribbons_and_Macro_Bands]]
- Regime Classification: [[Market_Regimes]]
- Breakout Confluence: [[Breakout_Execution_and_Confirmation_Filters]]
