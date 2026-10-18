---
type: synthesis
title: Master Rules of Engagement
created: 2026-10-18
updated: 2026-10-18
status: active
tags:
  - rules
  - discipline
  - risk-management
---

# Master Rules of Engagement

These rules are non-negotiable. They protect capital first and extract edge second.

---

## 1. Capital Preservation & Risk Limits

> [!DANGER] Golden Sizing Law
> - **Max Risk per Trade**: 0.5% – 1.0% of total liquid account equity (1.0R). Never exceed 1.5R under any circumstance.
> - **Max Daily Loss Limit (Circuit Breaker)**: `-3.0R`. If hit, the trading terminal is closed immediately for the remainder of the session. No exceptions.
> - **Monthly Drawdown Budget**: Maximum **5% – 6% portfolio drawdown** per calendar month. If breached, liquidate all open positions and go to 100% cash for the rest of the month (Minervini Rule).
> - **Max Open Heat**: No more than 3 correlated positions open simultaneously (max total portfolio risk: `3.0R`).
> - **Invariant Stop Loss**: Stop loss is set immediately upon fill. **Never move a stop loss downward.**
> - **Cash is an Active Position**: Never be forced to trade or stay 100% invested. Big institutions and elite traders wait patiently for market falls to deploy dry powder (see [[Institutional_Order_Flow_vs_Retail]]).
> - **Daily Execution Cap**: Maximum **3 trades per day** combined across calls and puts. Eliminates software loop bugs, halts overtrading, and curtails transaction/STT drag (Keshav Rule).
> - **Zero Naked Overnight Risk (Peace of Mind)**: Never carry naked short options overnight. Gap risk from unexpected macroeconomic or geopolitical events destroys accounts. Intraday trading must grant complete peace of mind.
> - **Expiry Day Square-Off**: Close all intraday derivative positions strictly by **15:00** (avoiding late-session gamma illiquidity and execution spikes).

See detailed sizing mechanics in: [[Risk_Management_and_R_Multiples]].

---

## 2. Daily Execution Routine

### Phase 1: Pre-Market Preparation (08:30 - 09:25 EST)
1. Check Macro Economic Calendar (Fed speakers, CPI/PPI, Jobs reports).
2. Classify broad [[Market_Regimes|Market Regime]] on [[SPY]] and [[QQQ]] (Trend / Range / Volatile).
3. Identify 2-3 focus tickers with relative volume (`RVOL > 1.5`) and clear catalysts.
4. Define pre-calculated entry, stop, and target levels before the bell rings.

### Phase 2: Live Session Execution (09:30 - 11:30 EST & 14:00 - 16:00 EST)
1. **First 5 Minutes**: Observe only. Do not take reckless 09:30 market-open orders unless executing a backtested setup.
2. Verify all setup checklist criteria from [[Opening_Range_Breakout]] or [[Support_Resistance_Liquidity_Sweep]].
3. Set the hard stop-loss immediately upon fill in the broker software.
4. Walk away or step back if signs of emotional agitation occur (see [[Trading_Psychology_and_Tilt]]).

### Phase 3: Post-Market Debrief (16:30 EST)
1. Export trade executions or write bullet summary into `raw/trade_exports/`.
2. Instruct the LLM Agent: `"Ingest today's trades and update my reviews and stats."`
3. Score adherence to rules (1 to 10). A losing trade with 10/10 adherence is a victory. A winning trade with 2/10 adherence is a future account-killer.

---

## 3. Disqualification Criteria (Do NOT Trade If...)

- [ ] You are tired, distracted, hungover, or emotionally stressed.
- [ ] Major high-impact news (FOMC rate decision, CPI print) is releasing in less than 15 minutes.
- [ ] Spread is excessively wide or liquidity is sparse.
- [ ] Setup does not offer at least `2.0R` reward-to-risk ratio.
- [ ] **Unreliable Pattern**: Symmetrical Pennants (~46% win rate, see [[Top_Profitable_Chart_Patterns]]).
- [ ] **Time Stop Violation**: If holding a swing trade that fails to expand within 15–20 trading days, cut position and reallocate capital.
- [ ] **Unconfirmed Breakout**: Entering before an actual breakout or without a confirmation filter from [[Breakout_Execution_and_Confirmation_Filters]].
- [ ] **V3 Market Breadth Gate**: For equity momentum buys, do NOT enter if the benchmark index is below its 200 DMA or if >50% of constituents are declining (see [[Market_Regimes#3-macro-market-breadth-circuit-breakers-the-v3-framework|V3 Breadth Filter]]).
- [ ] **Un-modeled Slippage Trap**: Never trade an algorithmic strategy live without first stress-testing it with 0.5%–1.0% realistic slippage (see [[Execution_Slippage_and_Edge_Decay]]).

---

## 4. Quarterly Console Diagnostic Review (The Aniketh Dsouza Audit)
Every quarter, export broker trade statements (CSV) into `raw/trade_exports/` and run the diagnostic audit:
- Measure real win rate, profit factor, average win in R, average loss in R.
- Calculate the mathematical timeline (in trades and years) to reach your target capital goal (e.g. ₹1 Crore).
- If small, over-traded discretionary trades are delaying your financial timeline, eliminate them immediately and shift capital toward validated systematic models like [[ETF_Momentum_Rotation_Model]] and [[Intraday_Options_Trend_Selling_Supertrend_Pivot]].
