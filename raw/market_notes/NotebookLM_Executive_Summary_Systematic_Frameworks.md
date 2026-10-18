---
title: Executive Summary & Systematic Frameworks - Three Practitioners
source: NotebookLM Briefing Document
date: 2026-10-18
tags:
  - raw-source
  - systematic-investing
  - etf-momentum
  - algo-trading
  - slippage-decay
  - second-brain
---

# Executive Summary & Systematic Frameworks: Three Market Practitioners

Briefing document synthesizing quantitative strategies, technical workflows, and risk-management methodologies from:
1. **Saddam Shaik**: Bank Manager, Quantitative Algo Trader (ETF/Equity Momentum, "1X Basket", V3 Regime Filter, 100-idea AI prompting).
2. **Keshav Karunakar**: IT/AI Executive, Systems Option Trader (Intraday Mechanical Option Selling, SuperTrend + Pivot + 9 EMA, High-VIX strike caps, Calmar > 10).
3. **Aniketh Dsouza**: Marketing Agency Owner, Systematic Trader (Minervini VCP Growth, Karpathy LLM Wiki, Obsidian Second Brain, Console trade diagnostics).

---

## Complete Report Content
*(Ingested verbatim from practitioner briefing)*

### Key Takeaways
1. **Democratization of Quant Development via AI**: Writing 2,000–3,000 lines of robust Python backtesting code per day via LLMs like Claude ($20/mo).
2. **Data Accessibility & Verification**: 1-minute OHLC & tick data via broker APIs (ICICI Direct, Firstock) across 336,000+ rows (3+ years).
3. **Execution Edge vs. Friction in Option Strategies**: Mechanical option selling edge vs. cash intraday impossibility. Edge decay in static 9:20 AM straddles when adding 0.50–1.00 INR slippage.
4. **Regime-Filtered Momentum Portfolios**: Halting new stock/ETF entries when index < 200 DMA or >50% constituents decline cuts max drawdown from 32% to 24% while sustaining 47% CAGR.
5. **The "Second Brain" Knowledge Management Architecture**: Local offline Markdown vaults (Obsidian) + AI reasoning engines (Claude Code) guided by Andrej Karpathy's LLM Wiki instructions.

### Detailed Frameworks Included
- **Data Acquisition**: ICICI Direct / Firstock API automation, session tokens, NoteGPT YouTube strategy extraction, STBT breakout strategy (Sensex 26% CAGR, 2.76% Max DD, 9.42 Calmar).
- **Option Edge Decay**: 9:20 AM straddle sensitivity test showing complete net loss with realistic 0.5–1.0% slippage.
- **1X Basket Model**: 1X unit (e.g. ₹25 Lakhs) mobile interface isolation; 10% Cash, 45% ETF Momentum, 45% Equity Momentum, margin pledging for intraday FNO.
- **ETF Momentum Strategy**: 54 ETF universe, >200 DMA, 262 days history, weighted growth score $w_1(1M) + w_2(3M) + w_3(6M) + w_4(1Y)$, Top 6 selection, 15% hard SL, 20% peak trailing SL.
- **Nifty 500 Momentum (V1 to V3)**: Monthly RSI 50-70, within 20% of 52W high, >200 DMA, Top 15 stocks. V3 Regime Filter: halt buys if Nifty 500 < 200 DMA or >50% constituents declining.
- **100-Idea Framework**: Systematic prompting to discover drawdown reduction ideas without overfitting.
- **Second Brain Workflow**: Local Obsidian vault + Claude Code CLI + Karpathy LLM Wiki prompts + console trade diagnostics to measure years to target capital.
