---
type: concept
title: Top Profitable Chart Patterns & Historical Edge
category: market_microstructure
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - patterns
  - edge
  - win-rates
  - technical-analysis
---

# Concept: Top Profitable Chart Patterns & Historical Edge

Statistical analysis of classical chart formations (derived from empirical studies by Thomas Bulkowski and quantitative backtests) demonstrates that not all chart patterns have equal predictive validity.

![[raw/assets/top_profitable_chart_patterns.jpg]]

---

## 1. Top Tier Formations (Historical Win Rate > 80%)

| Pattern | Category | Win Rate | Avg Gain | Best Regime | Primary Execution Rule |
|---|---|---|---|---|---|
| **Inverse Head & Shoulders** | Reversal | **~89%** | **~45%** | [[Market_Regimes#Regime-2-Range-Bound--Chop-Distribution--Accumulation\|Reversal / Chop to Trend]] | Wait for neckline break + retest with volume spike. |
| **Double Bottom** | Reversal | **~88%** | **~50%** | Key Support / Range Extremes | Ensure second bottom shows absorption wick (see [[Support_Resistance_Liquidity_Sweep]]). |
| **Triple Bottom** | Reversal | **~87%** | **~45%** | Multi-week bottoming | Requires patient confirmation on neckline break. |
| **Descending Triangle** | Breakout | **~87%** | **~38%** | High Volatility / Liquidity Sweep | Often resolves in violent upside squeeze when horizontal floor holds. |
| **Rectangle Top / Bottom** | Range Bounds | **~85%** | **~48-51%** | Consolidation | Trade breaks of the range boundary or fade within boundaries. |
| **Bull Flag** | Continuation | **~85%** | **~39%** | [[Market_Regimes#Regime-1-Bullish--Bearish-Strong-Trend\|Strong Momentum Trend]] | Buy pullback to 9 or 20 EMA after an explosive impulse pole. |
| **Ascending Triangle** | Continuation | **~83%** | **~43%** | Upward Trend | Higher lows pressing against resistance; enter before or upon final breakout. |
| **Cup and Handle** | Continuation | **High Reliability** | Large | Prolonged Accumulation | Enter on breakout of handle or retest of cup rim. |

---

## 2. Patterns to Avoid (Negative Expectancy)

> [!DANGER] Disqualified Pattern: Pennants (~46% Win Rate)
> - **Historical Win Rate**: Only **~46%** with an anemic average gain of **~7%**.
> - **Why Traders Fail Here**: Pennants converge rapidly, creating tight consolidation with deteriorating volume. This makes them prime targets for market-maker stop runs and fake breakouts in both directions.
> - **Rule of Engagement**: Under [[Rules_of_Engagement]], do not execute symmetrical pennants without high-timeframe structural confluence.

---

## 3. Mathematical Expectancy & Application

Using the expectancy formula from [[Risk_Management_and_R_Multiples]]:

$$E = (\text{Win Rate} \times \text{Avg Win}) - (\text{Loss Rate} \times \text{Avg Loss})$$

For an **Inverse Head & Shoulders** or **Double Bottom** traded with disciplined **1.0R** risk and a **2.5R** target:
$$E = (0.85 \times 2.5R) - (0.15 \times 1.0R) = 2.125R - 0.15R = \mathbf{+1.975R \text{ per trade}}$$

Even accounting for real-world execution friction and slippage (reducing win rate to 60%), expectancy remains heavily positive ($+1.10R$).

---

## 4. Cross-References & Linked Strategies
- [[Support_Resistance_Liquidity_Sweep]]: Microstructure mechanics behind Double/Triple Bottoms.
- [[Opening_Range_Breakout]]: Intraday flag and breakout execution.
- [[Rules_of_Engagement]]: Stop loss placement rules.
- Source citation: [[raw/market_notes/Top_Profitable_Chart_Patterns_Bulkowski_Study|Raw Bulkowski Study Notes]].
