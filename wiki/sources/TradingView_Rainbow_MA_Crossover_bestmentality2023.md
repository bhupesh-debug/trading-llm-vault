---
type: source
title: "TradingView: Rainbow Moving Average with Crossover Signals"
author: bestmentality2023
source_file: "[[raw/market_notes/TradingView_Rainbow_MA_Crossover_bestmentality2023.md]]"
source_type: tradingview_open_source_script
date_ingested: 2026-10-18
tags:
  - source-summary
  - tradingview
  - moving-averages
  - rainbow-cloud
  - crossover-signals
  - pine-script
---

# Source Summary: Rainbow Moving Average with Crossover Signals

## Overview
Analysis and distillation of the open-source TradingView script **"Rainbow Moving Average with Crossover Signals"** published by community author **bestmentality2023** ([TradingView Script 3JVIdB6i](https://www.tradingview.com/script/3JVIdB6i/)).

The script advances traditional rainbow ribbons by introducing:
1. **Multi-algorithm MA kernel flexibility**: Trader choice across 6 distinct moving average types (EMA, SMA, HMA, RMA, WMA, VWMA).
2. **Deterministic execution triggers**: Pinpointing fast MA crossover points (`MA1` $\times$ `MA2`) overlaid with visual chart markers (green/red signal dots) and webhook-ready alert conditions.

---

## Technical Specifications

### 1. Multi-MA Kernel Selection
Unlike standard ribbons locked into exponential smoothing, the architecture allows switching the base smoothing engine across the 7 layered bands:
- **EMA (Exponential)**: Balanced weighting for standard momentum.
- **SMA (Simple)**: Equal-weighted baseline, cleaner on macro horizons.
- **HMA (Hull)**: Ultra-responsive, reducing lag drastically while smoothing curve noise.
- **RMA (Running / Wilder's SMMA)**: Smoother, standard in RSI/ATR calculations.
- **WMA (Weighted)**: Linearly weighted toward recent volume/price bars.
- **VWMA (Volume-Weighted)**: Weights prices by traded volume, revealing institutional volume-backed moves.

### 2. Fast Crossover Signal Logic
- **Bullish Trigger**: `ta.crossover(MA1, MA2)`
  - Plots green signal dot directly below candle low.
  - Generates `alertcondition` for automated bot execution.
- **Bearish Trigger**: `ta.crossunder(MA1, MA2)`
  - Plots red signal dot directly above candle high.
  - Generates `alertcondition` for automated stop/short execution.

### 3. Structural Regime Identification
- **Trend Acceleration**: Parallel widening of the 7 bands confirms directional flow.
- **Compression / Squeeze**: Convergence of fast and slow bands warns of imminent breakout expansion.
- **Tangled Consolidation**: Overlapping bands trigger rule-based disqualification of trend trades (see [[Market_Regimes#Regime-2-Range-Bound--Chop-Distribution--Accumulation|Regime 2: Chop]]).

---

## Direct Vault Cross-References
- Core Concept & Pine Script: [[Rainbow_Moving_Average_Ribbons_and_Macro_Bands]]
- Broader Taxonomy: [[TradingView_Rainbow_Indicators]]
- Rule Disqualification & Regime Filters: [[Rules_of_Engagement]]
