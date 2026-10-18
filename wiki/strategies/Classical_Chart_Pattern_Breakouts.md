---
type: strategy
title: Classical Chart Pattern Breakouts
asset_classes: Equities | Futures | Forex | Crypto
timeframes: 15m | 1h | 4h | Daily
status: active
expected_win_rate: 60-80% (Filtered by Top_Profitable_Chart_Patterns)
target_reward_risk: 2:1 - 3:1
tags:
  - strategy
  - chart-patterns
  - classical
  - breakouts
---

# Strategy: Classical Chart Pattern Breakouts

This playbook standardizes the execution of classical geometric price structures (Double Bottoms, Inverse Head & Shoulders, Rectangles, and Triangles) using calculated targets and strict confirmation filters.

---

## 1. Setup Selection & Filter Hierarchy
Prioritize patterns with empirically verified win rates from [[Top_Profitable_Chart_Patterns]]:
1. **Tier 1 (Win Rate 85–89%)**:
   - [[Top_Profitable_Chart_Patterns#1-top-tier-formations-historical-win-rate--80|Inverse Head & Shoulders]] (~89%)
   - [[Top_Profitable_Chart_Patterns#1-top-tier-formations-historical-win-rate--80|Double Bottom]] (~88%)
   - [[Top_Profitable_Chart_Patterns#1-top-tier-formations-historical-win-rate--80|Triple Bottom]] (~87%)
   - [[Top_Profitable_Chart_Patterns#1-top-tier-formations-historical-win-rate--80|Bull Flag & Rectangles]] (~85%)
2. **Disqualified (Negative Expectancy)**:
   - Symmetrical Pennants (~46% win rate, avoid under [[Rules_of_Engagement]]).

---

## 2. Invalidation & Entry Rules

> [!CHECKLIST] Entry Execution Criteria
> 1. **Pattern Completion**: The pattern is bounded by at least two clear trendlines with at least 2 distinct touches per boundary line.
> 2. **Breakout Trigger**: Price penetrates the boundary/neckline.
> 3. **Confirmation Filter**: Must satisfy at least one filter from [[Breakout_Execution_and_Confirmation_Filters]] (e.g. 2 consecutive candle closes outside the boundary or volume > 1.5x 20-period average).
> 4. **Entry Execution**: Buy on the breakout close OR enter on a throwback/pullback retest of the broken level.

> [!DANGER] Invalidation & Protective Stop
> - **Reversals (Double Bottom / H&S)**: Stop loss placed below the right shoulder or below the middle reaction pivot.
> - **Triangles / Rectangles**: Stop loss placed just inside the broken boundary line or below the breakout bar's opposite extreme.
> - **Catastrophic Exit**: If price falls back into the pattern and breaches the mid-line, exit immediately.

---

## 3. Position Sizing & Measured Targets

- **Risk Sizing**: 1.0R risk limit calculated via [[Risk_Management_and_R_Multiples]].
- **Measured Move Target ($T$)**:
  $$T = \text{Breakout Price} + \text{Pattern Height}$$
  *(Where Pattern Height is the distance from the extreme peak to the lowest trough in the pattern).*
- **Fibonacci Extensions**: For Cup & Handle formations, scale at 1.618 and 2.618 extensions.

---

## 4. Visual References
- Complete visual atlas: [[Visual_Chart_Patterns_Reference]]
- Study diagrams: `![[raw/assets/here_are_some_chart_patterns_to_keep_in_the_back.png]]`
