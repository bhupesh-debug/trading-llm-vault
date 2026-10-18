---
type: concept
title: Fundamental Rainbow Valuation and Macro Money Multipliers
category: valuation_and_macro
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - valuation
  - fundamental-analysis
  - money-multiplier
  - rainbow-bands
  - macro-liquidity
  - pine-script
---

# Concept: Fundamental Rainbow Valuation & Macro Money Multipliers

> *"Most valuation methods are based on a multiplier effect measuring how many times price expands from its valuation base. Unifying Book Value, Dividends, Cash Flow, Earnings, and Forward Estimates creates a fundamental rainbow spectrum showing exactly where an asset sits in its valuation lifecycle."* — [[TradingView_Stock_Valuation_Rainbow_danny_peanuts]]

While technical moving average ribbons (see [[Rainbow_Moving_Average_Ribbons_and_Macro_Bands]]) track intraday and multi-week trend momentum, **Fundamental Rainbow Valuation** anchors market prices to cash-generating reality. It answers the critical institutional question: *Is this momentum driven by organic balance-sheet expansion, or is it pure speculative multiple inflation?*

---

## 1. Unified Fundamental Valuation Formula

Traditional finance isolates single ratios ($P/E$, $P/B$, $P/CF$, Dividend Yield). The unified model aggregates per-share tangible value components into a single **Intrinsic Per-Share Base**:

$$\text{Base Valuation} = \text{BVPS} + \text{DPS} + \text{CFPS} + \text{EPS} + \text{EST}$$

$$\text{Stock Value Band } (\text{SV}_k) = \text{Base Valuation} \times \text{MM}_k$$

```
┌────────────────────────────────────────────────────────────────────────┐
│                      THE FUNDAMENTAL BASE COMPONENTS                    │
├───────────────────┬────────────────────────────────────────────────────┤
│ BVPS (Book Value) │ (Total Assets - Total Liabilities) / Shares        │
│ DPS (Dividends)   │ Annual Cash Dividends Paid / Shares                │
│ CFPS (Cash Flow)  │ Free Cash Flow (Operating Cash Flow - CapEx) / Shs │
│ EPS (Earnings)    │ Trailing 12-Month Net Income / Diluted Shares      │
│ EST (Estimates)   │ Forward 1-Year Consensus EPS Forecast              │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 2. The Money Multiplier Spectrum & Strategic Playbooks

By applying multiplier coefficients ($\text{MM}_k$) from $0.2\times$ up to $10.0\times$, price action is partitioned into five distinct strategic phases:

```
  10.0x ─── [PARABOLIC EUPHORIA / BUBBLE] ──────────► Tighten stops; fade climaxes
   7.0x ─── [OVEREXTENDED SPECULATION]    ──────────► Profit-taking; trail 21 EMA
   5.0x ─── [RAPID MULTIPLE EXPANSION]    ──────────► Sweet spot for Stage 2 Trend
   3.0x ─── [HEALTHY GROWTH MARKUP]       ──────────► VCP & Chart Pattern Breakouts
   1.0x ─── [NEUTRAL VALUATION ANCHOR]    ──────────► Gray Line (Base intrinsic value)
   0.6x ─── [DISCOUNT / ACCUMULATION]     ──────────► Long-term institutional buying
   0.2x ─── [DEEP CRISIS DISTRESS]        ──────────► Fire-sale / Maximum asymmetry
```

| Zone | Multiplier Range | Market Psychology | Systematic Playbook Rule |
|---|---|---|---|
| **Deep Discount** | $0.2\times - 0.8\times$ | Panic, insolvency fears, market crash | Macro accumulation; asymmetric long-horizon buying |
| **Neutral Fair Value** | $1.0\times - 2.0\times$ | Balance sheet parity; steady compounding | Position accumulation; swing breakout base building |
| **Momentum Expansion** | $3.0\times - 5.0\times$ | Institutional earnings growth, Stage 2 | **Prime setup zone**: Execute [[Minervini_Volatility_Contraction_Pattern_VCP\|VCP Breakouts]] & [[Classical_Chart_Pattern_Breakouts\|Chart Patterns]] |
| **Extended Premium** | $6.0\times - 8.0\times$ | Widespread retail optimism, narrative surge | Move stops to trailing; reduce fresh position sizing to 0.5R |
| **Euphoric Climax** | $9.0\times - 10.0\times+$ | Valuation decoupling, liquidity bubble | **Disqualify fresh momentum buys**; anticipate mean reversion |

---

## 3. Macro Multipliers: Global Liquidity & Central Bank Anchors

In addition to single-stock fundamental accounting, macro benchmarks and commodities derive their multiple expansion directly from central bank liquidity:

1. **Equities ($SPY, $QQQ) vs. Fed Balance Sheet (`WALCL`) + M2 Supply**:
   - Stock index price expansions mirror the expansion of central bank reserve assets and broad money supply ($M_2$).
   - When central bank balance sheets contract (Quantitative Tightening), equity multiples compress back toward the $1.0\times - 2.0\times$ base.
2. **Gold ($XAUUSD) vs. Global Money Supply**:
   - Gold serves as a neutral monetary anchor against aggregate global fiat debasement.
   - Gold price / Global M2 ribbons identify secular accumulation channels during currency expansion regimes.
3. **Cryptocurrency ($BTC) vs. Global Liquidity Waves**:
   - High-beta crypto cycles track global M2 liquidity pulses with ~60–90 day lead/lag dynamics.

---

## 4. Synergy with Existing Vault Strategies

Integrating Fundamental Valuation Rainbows prevents classic momentum traps:
- **Avoiding Late-Stage VCP Failures**: If a stock shows a tight Minervini VCP but its price is already trading at the $10\times$ valuation band, the probability of institutional distribution or failed breakout climbs significantly.
- **High-Conviction Breakout Filtering**: A breakout from a Stage 2 base at the $2.0\times - 3.0\times$ multiplier band has massive structural runway for multiple expansion compared to one at $8.0\times$.
- **Macro Hedging**: When benchmark indices hit the upper valuation rainbow bands, trigger the [[Rules_of_Engagement]] circuit breaker to protect trailing profits.

---

## 5. Ready-to-Use TradingView Pine Script (v5)

This script pulls company financials via Pine Script's native `request.financial()` functions to calculate the unified fundamental base and project the Multiplier Rainbow bands across historical price charts:

```pinescript
//@version=5
indicator("Vault Fundamental Stock Value Rainbow", shorttitle="Fund_Rainbow", overlay=true)

// ==========================================
// 1. Fetch Fundamental Per-Share Metrics
// ==========================================
// Book Value Per Share (Annual)
bvps = request.financial(syminfo.tickerid, "BOOK_VALUE_PER_SHARE", "FY")
// Dividends Per Share (Annual)
dps  = request.financial(syminfo.tickerid, "DIVIDENDS_PER_SHARE", "FY")
// Free Cash Flow Per Share (TTM)
cfps = request.financial(syminfo.tickerid, "FREE_CASH_FLOW_PER_SHARE", "TTM")
// Diluted Earnings Per Share (TTM)
eps  = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_DILUTED", "TTM")

// Handle null values with clean fallback
f_clean(val) => na(val) ? 0.0 : val

clean_bvps = f_clean(bvps)
clean_dps  = f_clean(dps)
clean_cfps = f_clean(cfps)
clean_eps  = f_clean(eps)

// ==========================================
// 2. Calculate Unified Intrinsic Valuation Base
// ==========================================
// Base = BVPS + DPS + CFPS + EPS
fund_base = clean_bvps + clean_dps + clean_cfps + clean_eps
valid_base = fund_base > 0 ? fund_base : na

// ==========================================
// 3. Project Multiplier Rainbow Bands
// ==========================================
// Discount Bands (< 1x)
band_02 = valid_base * 0.2
band_04 = valid_base * 0.4
band_06 = valid_base * 0.6
band_08 = valid_base * 0.8

// Baseline Anchor (1x)
band_10 = valid_base * 1.0

// Expansion Multiplier Bands (> 1x)
band_20 = valid_base * 2.0
band_30 = valid_base * 3.0
band_50 = valid_base * 5.0
band_70 = valid_base * 7.0
band_100= valid_base * 10.0

// ==========================================
// 4. Plots & Color Palette
// ==========================================
// Plot Gray Intrinsic Baseline
plot(band_10, "Base (1.0x)", color=color.gray, linewidth=2)

// Discount Bands (Cold / Accumulation)
plot(band_02, "0.2x Deep Discount", color=color.new(#000080, 20), linewidth=1)
plot(band_04, "0.4x Discount",      color=color.new(#0000ff, 30), linewidth=1)
plot(band_06, "0.6x Undervalued",   color=color.new(#00bfff, 40), linewidth=1)
plot(band_08, "0.8x Fair Value",    color=color.new(#00ffcc, 50), linewidth=1)

// Premium Expansion Bands (Warm / Distribution)
plot(band_20, "2.0x Markup",       color=color.new(#32cd32, 40), linewidth=1)
plot(band_30, "3.0x Growth",       color=color.new(#ffd700, 30), linewidth=1)
plot(band_50, "5.0x Expansion",    color=color.new(#ff8c00, 20), linewidth=2)
plot(band_70, "7.0x Extended",     color=color.new(#ff4500, 10), linewidth=2)
plot(band_100,"10.0x Bubble Climax",color=color.new(#ff0000, 0), linewidth=3)
```

---

## 6. Vault Integrations
- Trend Lifecycle & Sizing: [[Minervini_Volatility_Contraction_Pattern_VCP]]
- Macro Cycles: [[Market_Regimes]], [[ETF_Momentum_Rotation_Model]]
- Technical Ribbon Counterpart: [[Rainbow_Moving_Average_Ribbons_and_Macro_Bands]]
- Risk Controls & Sizing: [[Risk_Management_and_R_Multiples]], [[Rules_of_Engagement]]
- Source Distillation: [[TradingView_Stock_Valuation_Rainbow_danny_peanuts]]
