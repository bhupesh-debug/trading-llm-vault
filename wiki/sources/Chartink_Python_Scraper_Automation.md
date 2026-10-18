---
type: source
title: Chartink Python Automation & Screener Scraping Workflow
author: Trade Invest
source_file: "[[raw/market_notes/Chartink_Python_Screener_Automation_Transcript.md]]"
source_type: video_transcript
date_ingested: 2026-10-18
tags:
  - source-summary
  - chartink
  - python
  - web-scraping
  - data-pipeline
---

# Source Summary: Chartink Python Automation & Screener Scraping Workflow

## Overview
A technical walkthrough demonstrating how to programmatically extract live scanned stock lists from Chartink into Python without relying on manual browser monitoring.

---

## 1. Technical Reverse-Engineering of Chartink APIs
Chartink protects its scanning endpoints using CSRF verification and session tokens:

1. **Initial Handshake (GET Request)**:
   - Request the public screener page: `https://chartink.com/screener/<scanner_name>`.
   - Parse the raw HTML with `BeautifulSoup` to locate:
     `<meta name="csrf-token" content="...">`
   - Store the session cookies returned by the server.
2. **Execution Request (POST Request)**:
   - Target URL: `https://chartink.com/screener/process`
   - **Headers**:
     - `X-CSRF-TOKEN`: Extracted token string.
     - `X-Requested-With`: `XMLHttpRequest`
     - `Referer`: The original screener URL.
   - **Payload**:
     - `scan_clause`: The encoded scanning query string (found in DevTools Network tab).
3. **Response Handling**:
   - Status 200 returns a JSON object containing an array of matched stocks (`response.json()['data']`).
   - The dataset is converted into a structured `pandas.DataFrame` containing Ticker, NSE Code, Close Price, and Volume.

---

## 2. Speed Benchmarks: Requests vs. Selenium
- **Requests + Session**: Executes within **0.90 seconds**, ideal for low-latency intraday scanning.
- **Selenium / Headless Browser**: Takes 10+ seconds on initialization due to DOM rendering, but bypasses complex headers.

---

## 3. Practical Applications to Our System
- Automated screening for **Narrow Range 7 (NR7)** and **NR4** volatility compressions (see [[Breakout_Execution_and_Confirmation_Filters]]).
- Live intraday screening for Stage 2 breakouts (see [[Minervini_Volatility_Contraction_Pattern_VCP]]).
- Blueprint implementation: [[Automated_Market_Scanning_Chartink_Python]].
