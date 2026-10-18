---
type: strategy
title: ETF Momentum Rotation Strategy
asset_classes: Exchange Traded Funds (ETFs)
timeframes: Daily / Monthly Rebalance
status: active
expected_cagr: 25-35%
target_max_drawdown: < 15-18%
tags:
  - strategy
  - momentum
  - etf
  - systematic-investing
  - saddam-shaik
---

# Strategy: ETF Momentum Rotation Strategy

Developed by Saddam Shaik ([[Three_Practitioners_Systematic_Frameworks_NotebookLM]]), this strategy deploys cross-asset relative momentum across 54 diversified domestic and global ETFs, dynamically rebalancing into leading assets while enforcing dual stop-loss safeguards.

---

## 1. Core Hypothesis & Edge
- Sector, commodity, and international equity ETFs exhibit persistent medium-term trend continuation due to macro capital flows.
- By rotating monthly into the top 10% performers (> 200 DMA) and exiting lagging assets, the portfolio avoids prolonged bear markets while riding macroeconomic leadership cycles (e.g. tech, gold, defense, global indexes).

---

## 2. Universe & Eligibility Filters

> [!CHECKLIST] Screening & Pre-Conditions
> - [ ] **Universe**: 54 liquid domestic and international ETFs (e.g. NIFTYBEES, JUNIORBEES, GOLDBEES, SILVERBEES, MON100, MAFANG, Sectoral ETFs).
> - [ ] **Maturity Filter**: Minimum **262 trading days** (~1 full year) of trading history.
> - [ ] **Long-Term Trend Filter**: ETF current price must be strictly **above its 200-day Simple Moving Average ($P > \text{SMA}_{200}$)**.

---

## 3. Relative Momentum Ranking Formula

Rank all eligible ETFs based on a weighted multi-timeframe percentage price momentum score:

$$\text{Momentum Score} = w_1(\Delta 1\text{M}) + w_2(\Delta 3\text{M}) + w_3(\Delta 6\text{M}) + w_4(\Delta 1\text{Y})$$

Where lookback windows are calibrated in trading days:
- $\Delta 1\text{M} = 21 \text{ days}$
- $\Delta 3\text{M} = 63 \text{ days}$
- $\Delta 6\text{M} = 126 \text{ days}$
- $\Delta 1\text{Y} = 252 \text{ days}$

**Portfolio Selection**: Buy and hold the **Top 6 ranked ETFs** (~10% of the universe), allocated equally ($\approx 16.6\%$ per ETF).

---

## 4. Exit Rules & Stop Loss Protections

1. **Monthly Rebalance Exit**:
   - Rebalance on the 1st trading day of every month.
   - If an ETF drops out of the Top 6 rankings, exit 100% and rotate into the newly qualified leader.
2. **Mid-Month Hard Stop Loss**:
   - If an open ETF position declines **15% from its entry price**, exit immediately mid-month.
3. **Mid-Month Trailing Stop Loss**:
   - If an open ETF position gives back **20% from its highest peak price**, exit immediately mid-month.
4. **Cash Quarantine Rule**:
   - Capital freed from mid-month stop-outs remains strictly in **cash or liquid ETF / overnight funds** until the scheduled end-of-month rebalance. Never re-deploy mid-month impulsively.

---

## 5. Margin Synergy with the 1X Basket Model
Under the [[Psychological_Capital_Allocation_1X_Basket]] model, the ETF portfolio represents **45% of total account capital**. Long ETF holdings are pledged with brokers to generate collateral margin, funding low-risk intraday option selling systems like [[Intraday_Options_Trend_Selling_Supertrend_Pivot]].
