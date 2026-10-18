---
type: concept
title: Rainbow Moving Average Ribbons and Macro Sentiment Bands
category: market_microstructure
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - indicators
  - moving-averages
  - rainbow-ribbon
  - trend-following
  - pine-script
---

# Concept: Rainbow Moving Average Ribbons and Macro Sentiment Bands

> *"Rainbow Moving Averages use a stack of 8 to 10 Moving Averages (often Fibonacci sequences like 8, 13, 21, 34, 55, 89, 144, 233)... Widening ribbon suggests trend acceleration, while an entangled ribbon points to consolidation."* — [[TradingView_Rainbow_Indicators]]

Multi-layered moving average cascades (commonly termed **Rainbow Ribbons** or Guppy Multiple Moving Averages) solve a core flaw of single moving averages: they separate short-term trader participation from long-term institutional capital commitments.

---

## 1. Anatomy of the Fibonacci Rainbow Ribbon

The classic Rainbow Ribbon utilizes 8 exponential moving averages (EMAs) grouped into two distinct psychological cohorts:

```
[Short-Term Speculators: 8, 13, 21 EMA] ──► Fast reaction, intraday momentum
                   │
[Medium-Term Swings: 34, 55 EMA]        ──► Dynamic pullback support zone
                   │
[Institutional Anchor: 89, 144, 233 EMA]──► Core trend direction & regime baseline
```

```
BULLISH ACCELERATION (EXPANSION)          CHOP / CONSOLIDATION (ENTANGLEMENT)
        EMA 8   ───────┐                         EMA 8  ───~-~-~-~
        EMA 13  ────────┐                        EMA 13 ──~-~-~-~
        EMA 21  ─────────┐                       EMA 21 ──~-~-~-~
        EMA 34  ──────────┐                      EMA 34 ──~-~-~-~
        EMA 55  ───────────┐                     EMA 55 ──~-~-~-~
        EMA 89  ────────────┐                    EMA 89 ──~-~-~-~
        EMA 144 ─────────────┐                   EMA 144──~-~-~-~
        EMA 233 ──────────────┘                  EMA 233──~-~-~-~
   (Wide spread, parallel order)             (MAs criss-crossing / overlapping)
```

---

## 2. The Three Ribbon States & Strategy Matching

| Ribbon State | Visual Appearance | Underlying Market Dynamic | Actionable Playbook Rule |
|---|---|---|---|
| **1. Clean Expansion** | MAs stacked in numerical order with widening distance | [[Market_Regimes#Regime-1-Bullish--Bearish-Strong-Trend\|Strong Momentum Trend]] | Execute trend-continuation pullbacks; hold runners |
| **2. Compression** | Outer MAs contract inward; ribbon thins | Volatility Contraction | Prepare for breakout (see [[Breakout_Execution_and_Confirmation_Filters]]) |
| **3. Entanglement** | Fast MAs weave through slow MAs; lines tangled | [[Market_Regimes#Regime-2-Range-Bound--Chop-Distribution--Accumulation\|Range-Bound Chop]] | **Stand Aside / No Trades**; avoid trend-following entries |

---

## 3. Multi-Kernel Smoothing Engines & Behavioral Differences

Following the framework in [[TradingView_Rainbow_MA_Crossover_bestmentality2023]], moving average ribbons can employ different algorithmic calculation kernels depending on asset volatility and time horizon:

| Kernel | Full Name | Lag vs. Smoothness | Best Used For |
|---|---|---|---|
| **EMA** | Exponential Moving Average | Balanced; weights recent bars higher | General equities, intraday indexes, standard momentum |
| **SMA** | Simple Moving Average | High lag, maximum smoothness | Macro horizons, institutional multi-month trendlines |
| **HMA** | Hull Moving Average | **Lowest lag**; highly responsive curvature | Fast scalping, volatile crypto pairs, early pivot inflection detection |
| **RMA** | Running Moving Average (Wilder's SMMA) | High smoothness; exponential decay $1/N$ | Trend filtration, indicator smoothing (RSI/ATR engines) |
| **WMA** | Weighted Moving Average | Linearly descending weights | Faster turn detection than SMA with linear weighting |
| **VWMA** | Volume-Weighted Moving Average | Dynamic responsiveness scaled by tick/bar volume | Identifies whether moves are institutionally funded with heavy volume |

---

## 4. Fast Crossover Execution Signals & Anti-Whipsaw Rule

While ribbon expansion determines macro regime, entry timing is often governed by **Fast Crossover Signals** (such as $\text{MA}_1 \times \text{MA}_2$):

1. **Bullish Signal (Green Marker)**:
   $$\text{Bullish Trigger} = \text{ta.crossover}(\text{MA}_1, \text{MA}_2)$$
   - *Visual*: Green dot plotted below the candle low.
   - *Execution Rule*: Take **ONLY** when intermediate and slow MAs ($\text{MA}_4, \text{MA}_5, \text{MA}_6, \text{MA}_7$) are already sloping upward or in bullish stack order.
2. **Bearish Signal (Red Marker)**:
   $$\text{Bearish Trigger} = \text{ta.crossunder}(\text{MA}_1, \text{MA}_2)$$
   - *Visual*: Red dot plotted above the candle high.
   - *Execution Rule*: Take for short entries or immediate long position stops when slow MAs confirm downward slope.
3. **The Anti-Whipsaw Filter**:
   - In [[Market_Regimes#Regime-2-Range-Bound--Chop-Distribution--Accumulation|Regime 2 (Chop / Tangled Ribbon)]], fast crossovers fire repeatedly in rapid succession.
   - **Non-Negotiable Rule**: Disqualify any $\text{MA}_1 \times \text{MA}_2$ crossover signal if the total spread between $\text{MA}_1$ and $\text{MA}_7$ is compressed below historical baseline ATR (see [[Rules_of_Engagement]]).

---

## 5. High-Probability Pullback Execution Protocol

When a market is in **Clean Bullish Expansion** (all MAs sloping up and ordered):
1. **The Bounce Zone**: Do NOT chase price when it is extended far above the 8 EMA. Wait for a pullback into the **21 EMA to 55 EMA dynamic cloud**.
2. **Candlestick Reversal Confirmation**: Look for a rejection wick or hammer candle testing the 34 or 55 EMA, followed by a fast MA recovery crossover.
3. **Invalidation / Stop Loss**: A 5-minute or daily close below the **89 EMA** (or $\text{MA}_6/\text{MA}_7$) invalidates the immediate pullback thesis and signals deeper trend breakdown.

---

## 6. Ready-to-Use TradingView Pine Script (v5)

This production-grade Pine Script v5 indicator integrates a **7-MA Rainbow Cascade**, multi-kernel algorithm selection (EMA, SMA, HMA, RMA, WMA, VWMA), dynamic cloud fills, fast crossover signal dots, and native TradingView alert conditions:

```pinescript
//@version=5
indicator(title="Vault Rainbow MA Ribbon with Signals", shorttitle="Rainbow_Ribbon_Signals", overlay=true)

// ========================
// 1. Inputs & Configuration
// ========================
src      = input.source(close, title="Source")
ma_type  = input.string("EMA", title="MA Type", options=["EMA", "SMA", "HMA", "RMA", "WMA", "VWMA"])

len1 = input.int(8,   title="MA 1 Length (Fastest)", minval=1)
len2 = input.int(13,  title="MA 2 Length", minval=1)
len3 = input.int(21,  title="MA 3 Length", minval=1)
len4 = input.int(34,  title="MA 4 Length (Cloud Top)", minval=1)
len5 = input.int(55,  title="MA 5 Length (Cloud Bottom)", minval=1)
len6 = input.int(89,  title="MA 6 Length (Anchor)", minval=1)
len7 = input.int(233, title="MA 7 Length (Macro Baseline)", minval=1)

show_signals = input.bool(true, title="Show Fast Crossover Signal Dots")

// ========================
// 2. Multi-Kernel MA Function
// ========================
calc_ma(type, source, length) =>
    switch type
        "EMA"  => ta.ema(source, length)
        "SMA"  => ta.sma(source, length)
        "HMA"  => ta.hma(source, length)
        "RMA"  => ta.rma(source, length)
        "WMA"  => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)
        => ta.ema(source, length)

// Calculate 7 Moving Averages
ma1 = calc_ma(ma_type, src, len1)
ma2 = calc_ma(ma_type, src, len2)
ma3 = calc_ma(ma_type, src, len3)
ma4 = calc_ma(ma_type, src, len4)
ma5 = calc_ma(ma_type, src, len5)
ma6 = calc_ma(ma_type, src, len6)
ma7 = calc_ma(ma_type, src, len7)

// ========================
// 3. Ribbon Plots & Colors
// ========================
c1 = color.new(#ff0055, 0)
c2 = color.new(#ff7700, 10)
c3 = color.new(#ffcc00, 20)
c4 = color.new(#33cc33, 30)
c5 = color.new(#00cccc, 40)
c6 = color.new(#0066ff, 50)
c7 = color.new(#990099, 60)

p1 = plot(ma1, color=c1, title="MA 1", linewidth=2)
p2 = plot(ma2, color=c2, title="MA 2", linewidth=1)
p3 = plot(ma3, color=c3, title="MA 3", linewidth=1)
p4 = plot(ma4, color=c4, title="MA 4", linewidth=1)
p5 = plot(ma5, color=c5, title="MA 5", linewidth=2)
p6 = plot(ma6, color=c6, title="MA 6", linewidth=2)
p7 = plot(ma7, color=c7, title="MA 7", linewidth=3)

// Dynamic Ribbon Fills
fill(p1, p3, color=ma1 > ma3 ? color.new(color.green, 85) : color.new(color.red, 85), title="Fast Cloud Fill")
fill(p4, p5, color=ma4 > ma5 ? color.new(color.teal, 88) : color.new(color.maroon, 88), title="Core Cloud Fill")

// ========================
// 4. Crossover Signal Dots
// ========================
bull_cross = ta.crossover(ma1, ma2)
bear_cross = ta.crossunder(ma1, ma2)

plotshape(show_signals and bull_cross, title="Bullish Cross Dot",
          style=shape.circle, location=location.belowbar,
          color=color.green, size=size.small, offset=0)

plotshape(show_signals and bear_cross, title="Bearish Cross Dot",
          style=shape.circle, location=location.abovebar,
          color=color.red, size=size.small, offset=0)

// ========================
// 5. Automated Alert Conditions
// ========================
alertcondition(bull_cross, title="Rainbow Bullish MA Crossover",
               message="Bullish Crossover: MA1 crossed above MA2 on {{ticker}} at {{close}}")
alertcondition(bear_cross, title="Rainbow Bearish MA Crossover",
               message="Bearish Crossover: MA1 crossed below MA2 on {{ticker}} at {{close}}")
```

---

## 7. Vault Integrations
- Trend Alignment: [[Market_Regimes]]
- Breakout Confirmation: [[Breakout_Execution_and_Confirmation_Filters]]
- Execution Rules & Circuit Breakers: [[Rules_of_Engagement]]
- Source Summaries: [[TradingView_Rainbow_Indicators]], [[TradingView_Rainbow_MA_Crossover_bestmentality2023]]

