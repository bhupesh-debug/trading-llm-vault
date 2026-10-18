---
type: index
title: Trading Knowledge System Index
updated: 2026-10-18
---

# Trading Knowledge Base Index

Welcome to your compounding Trading Intelligence System. This catalog is maintained automatically by the LLM Agent upon every `ingest`, `query`, and `lint` operation.

---

## 🎯 Master Operational Synthesis
| Page | Description | Status |
|---|---|---|
| [[Rules_of_Engagement]] | Non-negotiable risk limits, daily execution routines, circuit breakers, and trade disqualification rules | `Active` |

---

## 📐 Strategies & Setup Playbooks (`wiki/strategies/`)
| Strategy | Description | Edge / Mechanism | Expected Win Rate |
|---|---|---|---|
| [[Opening_Range_Breakout]] | 15-minute opening range expansion capturing institutional morning momentum | Momentum Breakout | 45-55% |
| [[Support_Resistance_Liquidity_Sweep]] | Fading false breakouts at key levels where retail stop losses are clustered | Institutional Sweep | 55-65% |
| [[Minervini_Volatility_Contraction_Pattern_VCP]] | Progressive drying of floating supply across 2-4 contractions before explosive trend breakout | Supply Absorption (VCP) | ~50% (High R:R) |
| [[Classical_Chart_Pattern_Breakouts]] | Geometric pattern execution (Double Bottom, H&S, Rectangles) with measured price targets | Structural Breakout | 60-85% |
| [[Intraday_Options_Trend_Selling_Supertrend_Pivot]] | Directional intraday option writing with Supertrend(6,3), 9 EMA, daily pivots, and slippage-evasion entry | Quantitative Option Writing | 65-75% |
| [[ETF_Momentum_Rotation_Model]] | 54-ETF weighted multi-window momentum rotation into Top 6 with dual mid-month stops | Cross-Asset Momentum | 25-35% CAGR |
| [[Nifty500_Stock_Momentum_V3_Regime]] | Top 15 stock momentum filtered by 200 DMA + 50% constituent breadth circuit breaker | Equity Momentum & Breadth | 47% CAGR (<24% DD) |
| [[Sell_Today_Buy_Tomorrow_STBT_Breakout]] | Late afternoon range breakdown into overnight hold and morning auction exit | Overnight Continuation | ~26% CAGR (9.42 Calmar) |

---

## 🧠 Core Trading Concepts & Foundations (`wiki/concepts/`)
| Concept | Category | One-Line Summary |
|---|---|---|
| [[Risk_Management_and_R_Multiples]] | Math & Risk | Sizing formula, 1R definition, mathematical expectancy, and asymmetric loss recovery |
| [[Trading_Psychology_and_Tilt]] | Psychology | Identifying the 4 fears, tilt spectrum, circuit breaker protocols, and disciplined execution |
| [[Market_Regimes]] | Market Structure | The 4 market regimes (Trending, Range, High Vol, Low Vol) and how to match strategies |
| [[Top_Profitable_Chart_Patterns]] | Technical Edge | Statistical win rates (80-89%) and avg gains for high-probability chart patterns |
| [[Breakout_Execution_and_Confirmation_Filters]] | Execution Edge | The 5 confirmation filters, Stop-and-Reverse trap execution, throwbacks vs pullbacks |
| [[Institutional_Order_Flow_vs_Retail]] | Smart Money Flow | What institutions do (liquidity harvesting, dip accumulation) vs retail 100% invested trap |
| [[Algorithmic_Edge_and_Quantitative_Metrics]] | Quantitative Edge | CCD framework, Calmar ratio (> 10), multi-strategy diversification, avoiding curve-fitting |
| [[Psychological_Capital_Allocation_1X_Basket]] | Capital Architecture | 1X unit interface decoupling, 10% Cash, 45% ETF, 45% Equity, margin pledging for FNO |
| [[Execution_Slippage_and_Edge_Decay]] | Microstructure Edge | The 9:20 straddle autopsy: how ₹0.50–₹1.00 slippage turns gross green backtests all red |
| [[Automated_Market_Scanning_Chartink_Python]] | Pipeline Automation | Python Requests + CSRF handshake to scrape live Chartink scans into pandas in <1s |
| [[Rainbow_Moving_Average_Ribbons_and_Macro_Bands]] | Technical Edge | 8-Fibonacci EMA ribbon expansion/compression dynamics, bounce zones, and Pine Script |
| [[Fundamental_Rainbow_Valuation_and_Macro_Money_Multipliers]] | Valuation & Macro | Unified BVPS+DPS+CFPS+EPS intrinsic base with 0.2x-10x money multiplier bands & Pine Script |
| [[NIFTY_Futures_and_Options_FnO_Mechanics]] | Derivatives & Margins | NSE index contract specs, OI buildup matrix, PCR, India VIX regime matrix, 50:50 cash rule |

---

## 🏢 Entities, Tickers & Benchmarks (`wiki/entities/`)
| Entity | Type | Role in Trading System |
|---|---|---|
| [[SPY]] | Equity ETF | Core S&P 500 macro benchmark, VWAP trend barometer, and daily liquidity engine |
| [[QQQ]] | Equity ETF | Nasdaq-100 high-beta tech benchmark; key for momentum breakouts and earnings volatility |
| [[NIFTY50]] | Equity Index | NSE flagship benchmark; primary intraday options writing engine and V3 breadth regime filter |

---

## 📚 Source Distillations (`wiki/sources/`)
| Source | Author | Core Contribution | Date Ingested |
|---|---|---|---|
| [[Trading_in_the_Zone_Mark_Douglas]] | Mark Douglas | Probabilistic thinking, loss acceptance, invariant execution | 2026-10-18 |
| [[raw/market_notes/Top_Profitable_Chart_Patterns_Bulkowski_Study|Chart Pattern Reliability Study]] | Bulkowski / LiberatedStockTrader | Empirical win rates for top 10 patterns; identifies pennants as low reliability (~46%) | 2026-10-18 |
| [[Mark_Minervini_Setup_Study]] | Mark Minervini | Trend template, VCP calculation, 2x ATR stop loss, 5-6% monthly drawdown budget | 2026-10-18 |
| [[Fidelity_Identifying_Chart_Patterns_Kirkpatrick]] | Charles D. Kirkpatrick II, CMT | Confirmation filters, false/failed breakout traps, measured targets, NR4/inside bars | 2026-10-18 |
| [[Visual_Chart_Patterns_Reference]] | ForexBee & Community | High-resolution visual diagrams for reversal, continuation, and bilateral patterns | 2026-10-18 |
| [[Video_Transcript_Retail_vs_Institutions]] | Market Video Discussion | Bruce Lee karate paradox, intellectual humility, institutional liquidity harvesting | 2026-10-18 |
| [[Keshav_Systematic_Options_Algo_Framework]] | Keshav & Vivek Bajaj | Intraday options writing, MM stop evasion, Calmar metrics, 3-trade daily cap | 2026-10-18 |
| [[Marco_Hui_VCP_Algorithmic_Screener]] | Marco Hui | Python Finviz & yfinance scanner for Minervini Stage 2 Trend Template and VCP base detection | 2026-10-18 |
| [[Three_Practitioners_Systematic_Frameworks_NotebookLM]] | Shaik, Karunakar, Dsouza | 1X basket model, V3 breadth gates, ETF rotation, 9:20 straddle slippage autopsy, Second Brain | 2026-10-18 |
| [[Chartink_Python_Scraper_Automation]] | Trade Invest | Programmatic scraping of Chartink scanners via requests session, CSRF token, and scan_clause | 2026-10-18 |
| [[TradingView_Rainbow_Indicators]] | TradingView Community | Multi-MA ribbons, logarithmic cycle bands, and visual sentiment indicators | 2026-10-18 |
| [[TradingView_Rainbow_MA_Crossover_bestmentality2023]] | bestmentality2023 | 7-MA rainbow ribbon with multi-type kernels (EMA/HMA/VWMA), crossover signal dots, and alerts | 2026-10-18 |
| [[TradingView_Stock_Valuation_Rainbow_danny_peanuts]] | danny_peanuts | Fundamental valuation rainbow aggregating BVPS, DPS, CFPS, EPS, and Money Multipliers | 2026-10-18 |

---

## 📝 Trade Reviews & Post-Mortems (`wiki/reviews/`)
*(New trade post-mortems will be cataloged here automatically upon ingest)*
- *Awaiting first logged trade debrief.*

---

## 🛠️ System Tools & Governance
- [[AGENTS|AGENTS.md]]: Master LLM operating instructions, file schemas, and agent workflows.
- [[CLAUDE|CLAUDE.md]]: Claude Code quick reference.
- [[GEMINI|GEMINI.md]]: Gemini / Antigravity reference.
- [[log|log.md]]: Append-only chronological audit log.
- [[README|README.md]]: Trader's guide to using this vault with Obsidian.
