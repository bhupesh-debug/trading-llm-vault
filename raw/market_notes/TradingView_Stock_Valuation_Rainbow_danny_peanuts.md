---
title: "Stock Valuation based on Book Value, Dividends, Cashflow, Earnings and Estimates and Money Multiplier"
author: "danny_peanuts"
source_url: "https://www.tradingview.com/u/danny_peanuts/"
date: 2024-12-09
tags:
  - raw-source
  - tradingview-script
  - valuation
  - fundamental-analysis
  - money-multiplier
  - rainbow-bands
---

# Raw Record: Stock Valuation based on Book Value, Dividends, Cashflow, Earnings and Estimates and Money Multiplier

- **Author**: danny_peanuts
- **Published**: Dec 9, 2024
- **Platform**: TradingView Open-Source Community Scripts

## Verbatim Description
There are many ways to measure stock valuations: some methods are using book value, some are using dividends, some are using cashflow, some are using earnings and some using estimates data. Most of these valuation methods are based on multiplier effect which measure how many times the stock price could expand from their valuation base. This indicator attempts to unify all these measurements using just simple addition of all measurements such as: book value per share, dividend per share, cashflow per share, earning per share, and estimates of earning per share and then using multiplier effect to create beautiful rainbow to see how far the stock has growing up above or below their valuation base. The higher the stock price on rainbow spectrum means it is more expensive and the lower in the rainbow spectrum means it is cheaper.

### Valuation Formula Explanation:
```
SV = (BVPS + DPS + CFPS + EPS + EST) * MM

BVPS = Book Value Per Share (Asset - Liability)
DPS  = Dividends Per Share
CFPS = Free Cash Flow Per Share
EPS  = Earnings Per Share
EST  = Estimates of EPS
MM   = Money Multiplier (1x, 2x, ... ,10x)
```

- **Gray Line**: Represents the stock baseline value SV (1x multiplier).
- **Upper Rainbow Bands (above gray line)**: Multiplication expansion factors: 1x, 2x, 3x, ..., 10x.
- **Lower Rainbow Bands (below gray line)**: Division discount factors: 0.8x, 0.6x, ..., 0.2x.

### Related Valuation Scripts in Ecosystem:
- **Stock Value Rainbow**: Script to value stock based on book value, dividend, cash flow, earning and estimates.
- **Index Value Rainbow**: Script to value index based on Fed balance sheet and base/weighted money supply.
- **Gold Value Rainbow**: Script to value gold based on global money supply.
- **Crypto Value Rainbow**: Script to value crypto based on global money supply.
- **Regional Equity Scripts**: Stock Value US, Stock Value EU, Stock Value JP, Stock Value CN.
