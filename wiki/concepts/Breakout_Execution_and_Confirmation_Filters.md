---
type: concept
title: Breakout Execution, Traps, and Confirmation Filters
category: market_microstructure
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - breakouts
  - filters
  - traps
  - execution
---

# Concept: Breakout Execution, Traps, and Confirmation Filters

Breakouts represent points of acute imbalance between supply and demand. However, unconfirmed breakouts are prime hunting grounds for institutional liquidity sweeps.

---

## 1. The 5 Confirmation Filters (Charles Kirkpatrick)

To protect capital against false breakouts, professional traders employ one or more confirmation filters before declaring a breakout valid:

```
[Price Pierces Level] ──► Apply Filter ──► [Confirmed Breakout / Valid Entry]
                                 │
                                 └──► Fails Filter ──► [Potential Trap / Stand Aside]
```

1. **Intrabar Filter**: Price exceeds the boundary line by a predetermined tick amount during the candle.
2. **Multiple Closes Filter**: Requires at least **2 consecutive closes** above resistance / below support on the charting timeframe.
3. **Time Filter**: Price must hold beyond the level for a specific elapsed duration (e.g. 15–30 minutes) without reverting.
4. **Percentage / Point Filter**: Price must extend by at least **0.5% – 1.0%** (or 1 full ATR fraction) beyond the barrier.
5. **Volume / Turnover Filter**: Volume on the breakout bar must expand to at least **1.5x–2.0x** the 20-period moving average.

---

## 2. False Breakouts vs. Failed Breakout Traps

- **False Breakout**: Price exceeds the level, immediately loses momentum, and drifts back inside the range. (Result: Scratch or small loss).
- **Failed Breakout (The Institutional Trap)**: Price breaches the level, sweeps retail buy-stops, and violently cascades in the opposite direction.

### The "Stop and Reverse" Tactical Edge
When trading high-conviction breakout setups:
1. Place a **Buy Stop** order to enter on the breakout.
2. Place a **Protective Sell Stop** immediately on the opposite side of the breakout bar.
3. Attach a **Sell Short Entry Stop** at that same invalidation level.
4. If the breakout follows through: ride the trend to the calculated price target.
5. If the breakout fails: the position flips short automatically, monetizing the trapped buyers.

---

## 3. Retracement Dynamics: Pullback vs. Throwback

```
UPWARD BREAKOUT ─────────► Peak ───┐
                                   ▼
Resistance (Now Support) ◄────── Throwback Retest ────► Expansion Higher
```

- **Throwback**: A temporary retreat back to broken resistance (now acting as support) following an upside breakout.
- **Pullback**: A temporary bounce back to broken support (now acting as resistance) following a downside breakdown.
- **Execution Caveat**: Waiting for a throwback/pullback provides tighter stop placement, but risks missing the strongest, highest-momentum runaway breakouts that never retrace.

---

## 4. Short-Term Volatility Setups: Gaps & Narrow Ranges

### Explosion Gap Pivot
1. Stock gaps up on heavy volume.
2. Price enters a shallow consolidation without filling the gap (the lowest point of this pullback is the **Pivot Low**).
3. **Entry**: Place Buy Stop above the high of the initial gap candle.
4. **Stop Loss**: Placed strictly below the **Pivot Low**.

### Narrow Range 4 (NR4) & Inside Bars
- When a candle's high-low range is smaller than the prior 3 candles (NR4), volatility has compressed to an extreme.
- Enter on a break of the NR4 high or low, as volatility compression consistently precedes directional expansion.

---

## 5. Linked References
- Source: [[Fidelity_Identifying_Chart_Patterns_Kirkpatrick]]
- Setup Playbook: [[Classical_Chart_Pattern_Breakouts]]
- Sizing Protocol: [[Risk_Management_and_R_Multiples]]
