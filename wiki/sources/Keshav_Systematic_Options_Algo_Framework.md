---
type: source
title: Systematic Options & Algo Trading Framework
author: Keshav (IT Executive & Quantitative Algo Trader)
interviewer: Vivek Bajaj (Face2Face)
source_file: "[[raw/market_notes/Keshav_Face2Face_Algo_Options_Trading_Transcript.md]]"
source_type: video_transcript
date_ingested: 2026-10-18
tags:
  - source-summary
  - algo-trading
  - options-selling
  - quantitative-risk
  - market-makers
---

# Source Summary: Systematic Options & Algo Trading Framework (Keshav / Face2Face)

## Executive Summary
A comprehensive blueprint for quantitative, systematic options trading developed by Keshav, an IT entrepreneur with 20+ years in technology and 3+ years coding 100+ algorithms on Indian index derivatives (Nifty / Bank Nifty). The conversation addresses the structural realities of options selling, navigating predatory market makers, mathematical metrics for longevity (Calmar/Sharpe), and eliminating emotional leaks through automated execution.

---

## 1. Structural Market Realities: Cash vs. Options vs. The House
1. **Intraday Cash Equity is Nearly Impossible for Retail**: Stock-picking intraday against institutional algorithms and operators is a negative-sum game.
2. **Options as a Mathematical Business**: Selling options is structurally equivalent to selling insurance (like LIC). You collect premiums for underwriting statistical risk; it is an analytical skill game, not gambling.
3. **The 6 Opposing Forces in the Trading Arena**:
   - **Government**: Taxes (STT, capital gains up to 39%).
   - **Regulators (SEBI)**: Frequent rule shifts (increased lot sizes, margin limits, expiry days).
   - **Exchanges (NSE/BSE)**: Steep transaction fees.
   - **Market Makers & HFTs (e.g. Jane Street)**: Harvesting bid-ask spreads, sweeping obvious stops, dynamic inventory balancing.
   - **Social Media / Influencers**: Overfitted cherry-picked strategies with zero multi-year robustness.
   - **Social Circle**: Showing 2,000–4,000 profit screenshots while hiding devastating losses.

---

## 2. Why Intraday-Only? The Case Against Positional Options
- **Extreme Tail Risk (Gap Risk)**: A sudden overnight geopolitical event or trade deal announcement can cause massive overnight gap-ups/downs. Keshav experienced a 34% drawdown on a positional algo caught short on an unprecedented gap-up day.
- **Slippage & Stop-Jumps**: Commodity/overnight stop losses can jump (e.g., losing ₹1 lakh during family dinner on Crude).
- **Peace of Mind (Zero Overnight Exposure)**: Trading must serve life, not destroy sleep. Intraday execution guarantees zero overnight risk and complete mental detachment after market close.

---

## 3. The Core Nifty Trend-Following Algo Architecture
- **Underlying & Instrument**: Nifty Weekly Options (Liquid, hard to manipulate compared to narrow-breadth Bank Nifty).
- **Directional Core**:
  - **Supertrend**: Factor **6**, Multiplier **3** on the **5-minute timeframe** (captures 30-minute institutional flow blocks).
  - **9 EMA**: Trend confirmation. If candle lows touch the 9 EMA, the market is usually choppy; if lows stay clear of 9 EMA, a sustained directional trend is underway.
  - **Daily Pivot Points**: Filter out chop. The zone between **R1 and Pivot**, and between **Pivot and S1**, is a designated "no-trade" dead zone.
- **Rules of Engagement**:
  - **Long Bias (Sell ATM Put)**: Open above R1, first 5m candle low touches/retests R1 and rejects back up.
  - **Short Bias (Sell ATM Call)**: Close below S1, retest S1.
  - **Short Covering Reversal**: Price touches S2 low, fails to break down, Supertrend flips bullish, and lows stay above 9 EMA.
- **The Market-Maker Evasion Entry**:
  - Retail textbook enters at: $\text{High} + \text{buffer}$. Market makers sweep this exact level, inducing maximum slippage.
  - Keshav's Proprietary Entry: 
    $$\text{Entry Trigger} = \min(\text{Close} + 5 \text{ pts}, \text{High} + 2 \text{ pts})$$
  - Unpredictable arithmetic that front-runs the stop sweep.
- **Hard Execution Caps**:
  - **Max Trades Per Day**: Strictly capped at **3 trades** combined across calls and puts. Eliminates infinite loops, halts revenge overtrading, and preserves capital from transaction fees.
  - **Trading Window**: 09:20 to 14:30.
  - **Expiry Day Rule**: Exit at **15:00** (not 15:15) to avoid gamma explosions and order-book illiquidity.
- **VIX & Strike Selection Filter**:
  - High VIX inflates ATM options to ₹280–300. A 20% stop loss on a ₹300 option equals a 60-point loss ($60 \times \text{lot size}$)!
  - **The Filter**: Only sell ATM if premium is $< \text{₹}120$. If VIX is elevated and ATM is $> \text{₹}140$, shift strike selection to lower-premium strikes to cap absolute point-risk to ₹20–24.

---

## 4. Quantitative Metrics for Trading Longevity
- **The CCD Triad**: **Confidence, Courage, and Discipline** cannot be faked; they emerge solely from robust multi-year backtesting across bull, bear, and high/low VIX regimes.
- **Drawdown is King**: Retail traders chase returns; quants control drawdown. An intraday strategy must maintain a **drawdown under 2.5%** with a **Calmar Ratio $> 10$**.
  $$\text{Calmar Ratio} = \frac{\text{Annualized Return}}{\text{Maximum Drawdown}}$$
- **Multi-Strategy Portfolio**: Run a basket of uncorrelated algorithms (Keshav runs 7 live strategies and 2 paper tests) so that trend-following winners offset consolidation chop.
- **The Reality of Option Buying**: 100+ algorithms coded over 3 years yielded **zero** option-buying algorithms with $< 10\%$ drawdown and positive expectancy. Systematic option writing with tight stops remains the statistically superior edge.
- **Paper Trading Purpose**: Paper trading is an engineering check (order routing, API sync, strike assignment), not a psychological simulator.

---

## Direct Vault Integrations
- Strategy Playbook: [[Intraday_Options_Trend_Selling_Supertrend_Pivot]]
- Concept: [[Algorithmic_Edge_and_Quantitative_Metrics]]
- Microstructure: [[Institutional_Order_Flow_vs_Retail]]
- Rules: [[Rules_of_Engagement]]
