---
title: Marco Hui VCP Screener & Trend Template Implementation
date: 2026-10-18
source: https://github.com/marco-hui-95/vcp_screener.github.io
tags:
  - raw-source
  - vcp
  - minervini
  - python
  - screener
  - quant
---

# Raw Source: Marco Hui VCP Screener & Trend Template Implementation

- **Repository**: `https://github.com/marco-hui-95/vcp_screener.github.io`
- **Saved Script**: [[raw/market_notes/vcp_screener.py]]
- **Author**: Marco Hui
- **Foundational Texts**: Mark Minervini's *Trade Like a Stock Market Wizard* (2013) & *Think and Trade Like a Champion* (2017).

---

## 1. Finviz Pre-Screening Filters
- Market Cap: > $300 Million (`cap_smallover`)
- Average Volume: > 100K (`sh_avgvol_o100`)
- Price: > $2 (`sh_price_o2`)
- SMA 200 below SMA 50 (`ta_sma200_sb50`)
- SMA 50 below Price (`ta_sma50_pa`)

---

## 2. Programmatic Minervini Trend Template (Stage 2 Uptrend)
1. **Price > 150 SMA & Price > 200 SMA & Price > 50 SMA**
2. **150 SMA > 200 SMA & 50 SMA > 150 SMA**
3. **200 SMA Trending Up for ≥ 1 Month**: Evaluated via 20-day linear regression slope:
   $$\text{Slope} = \frac{N \sum(i \cdot P_i) - \sum P_i \sum i}{N \sum i^2 - (\sum i)^2} > 0$$
4. **Price ≥ 30% Above 52-Week Low**: $\text{Price} > \text{Low}_{52w} \times 1.30$
5. **Price Within 25% of 52-Week High**: $\text{Price} > \text{High}_{52w} \times 0.75$
6. **RS Line Outperforming S&P 500**: $\text{RS} = \frac{\text{Price}}{\text{SPX}}$, with 20-day linear slope $> 0$.
7. **RS Rating ≥ 70**: Stock's 52-week share performance in top 30% of entire market universe.

---

## 3. Algorithmic VCP Base Detection
- **Peak/Trough Detection**: `scipy.signal.argrelextrema(order=10)`
- **Alternating Extrema Filter**: Resolves consecutive highs or consecutive lows into monotonic peak-trough waves.
- **Contraction Formula**:
  $$\text{Contraction Depth} = \frac{\text{Local High} - \text{Local Low}}{\text{Local High}} \times 100$$
- **VCP Qualification Criteria**:
  - Number of contractions: $2 \le N \le 4$
  - Maximum contraction (first wave): $\le 50\%$
  - Minimum contraction (tightest final pivot): $\le 15\%$
  - Base duration: $\ge 2$ weeks (10 trading days)
  - Volume Contraction: 5-day average volume $<$ 30-day average volume ($\text{Vol}_5 < \text{Vol}_{30}$)
  - In Consolidation (not broken out yet): Current High $<$ Peak High.
