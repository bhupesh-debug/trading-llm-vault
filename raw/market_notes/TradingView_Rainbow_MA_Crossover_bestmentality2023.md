---
title: "TradingView: Rainbow Moving Average with Crossover Signals"
author: "bestmentality2023"
source_url: "https://www.tradingview.com/script/3JVIdB6i/"
date: 2026-10-18
tags:
  - raw-source
  - tradingview-script
  - indicators
  - rainbow-ma
  - crossover-signals
  - pinescript
---

# Raw Record: Rainbow Moving Average with Crossover Signals

- **Script Link**: https://www.tradingview.com/script/3JVIdB6i/
- **Author**: bestmentality2023
- **Script Type**: Open-source TradingView Pine Script Indicator
- **Updated**: May 30

## Overview
Rainbow Moving Average is a trend-following indicator designed to visualize market structure, momentum shifts, and moving average alignment through a layered MA system.
This version combines multiple moving averages into a dynamic “rainbow” structure while adding automatic crossover signal detection for improved trend confirmation and timing.

## Features
* 7 configurable Moving Averages
* Supports multiple MA types:
  - EMA (Exponential Moving Average)
  - SMA (Simple Moving Average)
  - HMA (Hull Moving Average)
  - RMA / SMMA (Running Moving Average)
  - WMA (Weighted Moving Average)
  - VWMA (Volume Weighted Moving Average)
* Colored rainbow visualization for trend clarity
* Bullish crossover detection
* Bearish crossover detection
* Visual signal dots directly on the chart:
  - Green dot = bullish crossover (MA1 crosses above MA2)
  - Red dot = bearish crossover (MA1 crosses below MA2)
* Built-in TradingView alert conditions

## How It Works
The indicator monitors the crossover between the fast moving average (MA1) and the slower moving average (MA2).
* When MA1 crosses above MA2:
  - A green dot appears below the candle
  - Indicates potential bullish momentum
* When MA1 crosses below MA2:
  - A red dot appears above the candle
  - Indicates potential bearish momentum

The rainbow structure helps traders quickly identify:
* Trend direction
* Momentum acceleration
* Compression and expansion phases
* Potential reversals

## Best Use Cases
This indicator can be used for:
* Trend following
* Intraday trading
* Swing trading
* Momentum analysis
* Market structure confirmation
Works effectively on Forex, Indices, Crypto, Stocks, and Futures.

## Alerts
TradingView alert conditions are included for both bullish and bearish crossover events, allowing full automation compatibility.
