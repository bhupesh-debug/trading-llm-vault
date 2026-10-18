---
type: concept
title: Automated Market Scanning with Chartink & Python
category: market_microstructure
created: 2026-10-18
updated: 2026-10-18
status: foundational
tags:
  - automation
  - python
  - chartink
  - data-pipeline
  - screening
---

# Concept: Automated Market Scanning with Chartink & Python

> *"In today's video we are going to talk about how we can fetch screener data in Python... pass the CSRF token and scan clause to get live JSON data in 0.90 seconds."* — [[Chartink_Python_Scraper_Automation]]

To execute systematic breakout and momentum strategies (such as NR7 compressions or Minervini Stage 2 breakouts), traders require automated scanning pipelines that continuously filter thousands of market assets into actionable watchlists.

---

## 1. Technical Architecture & Communication Flow

```
[Python Script] ──(1) GET /screener/<name>──► [Chartink Web Server]
       │                                              │
       │ ◄──(2) HTML with CSRF Meta + Session Cookie──┘
       ▼
 [Extract CSRF & Cookie]
       │
       ├──(3) POST /screener/process with scan_clause ──► [Chartink Processing Engine]
       │                                                         │
       │ ◄──(4) JSON Response (Matched Tickers & Prices) ────────┘
       ▼
[Convert to pandas.DataFrame] ──► Feed to Broker Order API (Zerodha / Finvasia / ICICI)
```

---

## 2. Production-Ready Python Scraper Template

Save and run this script to automate any public or custom Chartink screener:

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def fetch_chartink_screener(screener_url: str) -> pd.DataFrame:
    """
    Automates live data extraction from any Chartink screener URL.
    Returns a clean pandas DataFrame with matched stocks.
    """
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    
    # Step 1: GET request to retrieve CSRF token and session cookies
    get_res = session.get(screener_url)
    if get_res.status_code != 200:
        raise ConnectionError(f"Failed to access screener page: {get_res.status_code}")
    
    soup = BeautifulSoup(get_res.text, 'html.parser')
    csrf_meta = soup.find('meta', {'name': 'csrf-token'})
    if not csrf_meta:
        raise ValueError("CSRF token not found in page metadata.")
    csrf_token = csrf_meta['content']
    
    # Step 2: Prepare POST headers
    process_url = 'https://chartink.com/screener/process'
    post_headers = {
        'x-csrf-token': csrf_token,
        'x-requested-with': 'XMLHttpRequest',
        'referer': screener_url
    }
    
    # Step 3: Extract scan_clause from page script or pass manually
    # Example below fetches default condition from the screener
    # In live usage, copy 'scan_clause' string from DevTools Network tab
    scan_clause = "( {33489} ( latest close > latest open and latest volume > 100000 ) )"
    
    payload = {'scan_clause': scan_clause}
    
    # Step 4: POST request to process the scan
    post_res = session.post(process_url, headers=post_headers, data=payload)
    if post_res.status_code != 200:
        raise ConnectionError(f"Screener process failed: {post_res.status_code}")
        
    data = post_res.json()
    if 'data' in data and len(data['data']) > 0:
        df = pd.DataFrame(data['data'])
        columns_to_keep = ['nsecode', 'name', 'close', 'per_chg', 'volume']
        existing_cols = [c for c in columns_to_keep if c in df.columns]
        return df[existing_cols]
    else:
        return pd.DataFrame()

# Example Execution
if __name__ == '__main__':
    url = "https://chartink.com/screener/nr7-current"
    stocks_df = fetch_chartink_screener(url)
    print(f"Total Matches: {len(stocks_df)}")
    print(stocks_df.head())
```

---

## 3. Integrating with Vault Playbooks

1. **NR4 / NR7 Breakouts**:
   - Screen for Narrow Range 7 contractions daily at 15:15.
   - Cross-reference with [[Breakout_Execution_and_Confirmation_Filters]] to trade morning breakouts.
2. **Minervini VCP Watchlist**:
   - Run daily scans for stocks trading within 25% of 52-week highs with volume contraction.
   - Feed candidate tickers into the Python VCP scanner ([[Marco_Hui_VCP_Algorithmic_Screener]], script at [[raw/market_notes/vcp_screener.py]]).
3. **Execution Safety**:
   - Ensure the daily execution frequency does not violate the **3-trade daily cap** from [[Rules_of_Engagement]].
