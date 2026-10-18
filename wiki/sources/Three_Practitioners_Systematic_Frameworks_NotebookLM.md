---
type: source
title: Three Practitioners Systematic Frameworks & Quantitative Synthesis
author: Saddam Shaik, Keshav Karunakar, Aniketh Dsouza
source_file: "[[raw/market_notes/NotebookLM_Executive_Summary_Systematic_Frameworks.md]]"
source_type: briefing_document
date_ingested: 2026-10-18
tags:
  - source-summary
  - etf-momentum
  - quantitative-frameworks
  - slippage
  - second-brain
---

# Source Summary: Three Practitioners Systematic Frameworks & Quantitative Synthesis

## Overview
A comprehensive briefing synthesizing institutional-grade trading systems, portfolio risk models, and knowledge infrastructure across three elite systematic practitioners:
- **Saddam Shaik**: Momentum rotation, index market breadth filters, capital isolation models.
- **Keshav Karunakar**: Intraday mechanical option underwriting, market-maker stop evasion.
- **Aniketh Dsouza**: Second-brain knowledge compounding via Obsidian, AI trade diagnostics, Minervini VCP growth.

---

## 1. Portfolio Architecture & Capital Allocation
1. **The "1X Basket" Allocation Model**:
   - Isolates trader psychology from multi-crore volatility.
   - Core unit (e.g. $1\text{X} = \text{₹}25\text{ Lakhs}$) is the only account viewed on mobile devices.
   - **Capital Split**: 10% Cash (churn & buffer), 45% ETF Momentum, 45% Equity Momentum.
   - **Margin Pledging**: Long ETF and stock positions are pledged as collateral margin to fund intraday FNO algorithms.
2. **The "V3" Market Breadth Regime Filter**:
   - Compresses Maximum Drawdown from 32% to 24% while delivering 47% CAGR.
   - **Circuit Breaker A**: Halt new buys if the benchmark index falls below its 200 DMA.
   - **Circuit Breaker B**: Halt new buys if $> 50\%$ of index constituents trade in negative territory.

---

## 2. Quantitative Strategy Specifications
1. **ETF Momentum Rotation Strategy**:
   - 54 liquid ETFs, filtered by $> 200\text{ DMA}$ and $\ge 262$ days trading history.
   - Ranked by weighted lookback: $\text{Score} = w_1(1\text{M}) + w_2(3\text{M}) + w_3(6\text{M}) + w_4(1\text{Y})$.
   - Top 6 ETFs held (~10% of universe).
   - Monthly rebalance, with mid-month hard stop at -15% and trailing peak stop at -20%.
2. **Nifty 500 Stock Momentum**:
   - Filtered by Monthly RSI (50–70), within 20% of 52-week high, and $> 200\text{ DMA}$. Top 15 stocks held.
3. **STBT Breakout Strategy**:
   - End-of-day breakout, overnight hold, early-morning exit.
   - Delivered 26% CAGR, 2.76% Max Drawdown, and Calmar ratio of 9.42 on Sensex.

---

## 3. Execution Friction & Edge Decay
- **The 9:20 AM Straddle Breakdown**:
  - Testing 1-minute increments with 10% to 100% stop losses on historical datasets.
  - Adding realistic execution slippage of just **₹0.50 to ₹1.00 (0.5%–1.0%)** turns historically gross profitable months completely net negative ("all red").
  - Superficial parameter tweaking cannot salvage a strategy whose underlying structural edge has eroded.

---

## 4. The "Second Brain" AI Knowledge Architecture
- **Tech Stack**: Obsidian (Local private markdown vault) + Claude Code / Antigravity Agent + Andrej Karpathy's LLM Wiki instructions.
- **Console Diagnostic Prompting**:
  - Ingest raw broker CSV trade statements (e.g. Zerodha statements).
  - Calculate win rate, profit factor, average win/loss in R.
  - Compute mathematical timeline to target capital goal (e.g. ₹1 Crore). This eliminates over-trading small setups and forces adoption of scalable systematic models.

---

## Direct Vault Integrations
- Strategies: [[ETF_Momentum_Rotation_Model]], [[Nifty500_Stock_Momentum_V3_Regime]], [[Sell_Today_Buy_Tomorrow_STBT_Breakout]]
- Concepts: [[Psychological_Capital_Allocation_1X_Basket]], [[Execution_Slippage_and_Edge_Decay]]
- Governance: [[Rules_of_Engagement]]
