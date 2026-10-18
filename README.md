# Trading LLM Wiki — User Manual & Intelligence Portal

Welcome to your personal **Trading Intelligence System & Alpha Vault**, designed according to the **LLM Wiki Pattern**.

[![GitHub Pages](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-00f2fe?style=for-the-badge&logo=github)](https://bhupesh-debug.github.io/trading-llm-vault/)
[![Repository](https://img.shields.io/badge/GitHub-trading--llm--vault-8b5cf6?style=for-the-badge&logo=github)](https://github.com/bhupesh-debug/trading-llm-vault)

- **Live Interactive Web Portal**: [https://bhupesh-debug.github.io/trading-llm-vault/](https://bhupesh-debug.github.io/trading-llm-vault/)
- **GitHub Repository**: [https://github.com/bhupesh-debug/trading-llm-vault](https://github.com/bhupesh-debug/trading-llm-vault)

---

## 🚀 Quick Start: How to Use This System

### 1. Launch Live Interactive Web Portal
Open [https://bhupesh-debug.github.io/trading-llm-vault/](https://bhupesh-debug.github.io/trading-llm-vault/) in any browser (desktop or mobile) to access:
- **1R Position & Risk Sizer**: Instant mathematical share and dollar sizing.
- **Fundamental Rainbow Valuation Calculator**: Multiplier projections ($0.2\times$ to $10.0\times$) across BVPS, DPS, CFPS, EPS, and forward estimates.
- **NIFTY 50 FnO Strike Mapper**: Automatic ATM, OTM Call/Put strike zoning, and 1R stop calculation.
- **Copy-Paste Pine Script v5 Indicators**: Multi-MA rainbow cascades with real-time crossover signal dots.
- **Strategy & Rules Hub**: Complete operational rules of engagement and 8 quantitative playbooks.

### 2. Open Locally in Obsidian
1. Open **Obsidian**.
2. Click **Open folder as vault** and select this directory (`C:\Users\bhupe\Downloads\Vault\Vault`).
3. Open `index.md` as your home dashboard or press `Ctrl + G` to view your interactive **Graph View**.

### 2. The Golden Workflow: You Trade, the LLM Maintains
```
   [You] ➔ Trade in Broker ➔ Drop Raw Note/Export in raw/
                                     │
                                     ▼
               [LLM Agent] Reads, Cross-References & Synthesizes
                                     │
                                     ▼
               Updates [[wiki/]], [[index.md]], and [[log.md]]
                                     │
                                     ▼
   [You] ➔ Browse Compounded Wisdom in Obsidian (Graph View / Dashboards)
```

---

## ⚡ The Three Core Commands (Copy-Paste to your LLM)

### 1. Ingest a Trade or Source
When you close your trading day or finish reading an article/book:
> *"I just added my trade notes/export to `raw/trade_exports/`. Please **ingest** this: calculate R-multiples, check if I followed my [[Rules_of_Engagement]], create a post-trade review in `wiki/reviews/`, update the strategy stats in `wiki/strategies/`, update `index.md`, and log the entry in `log.md`."*

### 2. Query Your Trading Intelligence
Before taking a trade or during weekend review:
> *"Query the wiki: What has been my win rate and average R on [[Opening_Range_Breakout]] when trading [[QQQ]] vs [[SPY]]? What is my most frequent emotional leak according to [[Trading_Psychology_and_Tilt]]?"*

If the answer contains valuable insights, tell the LLM:
> *"File that analysis back into the wiki as a new page in `wiki/synthesis/` and update `index.md`."*

### 3. Lint (Weekly Risk & System Health Check)
Every Friday after market close:
> *"Run a **lint** check across all trade reviews and strategy playbooks. Check for broken links, missing trade debriefs, rule contradictions against [[Rules_of_Engagement]], and signs of recurring risk leaks (e.g. moving stops or oversized positions)."*

---

## 📂 Vault Structure at a Glance

| Directory | Purpose | Who Modifies It? |
|---|---|---|
| `raw/` | Immutable sources (broker statements, chart screenshots, book excerpts, macro reports) | **You** (Trader) |
| `wiki/` | Persistent knowledge base (strategies, concepts, entities, reviews, synthesis) | **LLM Agent** |
| `templates/` | Standardized layouts for trades, setups, and reviews | LLM & You |
| `index.md` | Master catalog with 1-line descriptions and links | LLM Agent |
| `log.md` | Append-only chronological audit log of all changes | LLM Agent |
| `AGENTS.md` | Master operating schema that instructs any AI how to behave | System |

---

## 💡 Recommended Obsidian Settings & Plugins

1. **Graph View**: Open `Ctrl + G`. Filter out `raw/` to see only your conceptual wiki connections. Watch how strategies, entities, and reviews cluster around your core risk rules!
2. **Attachments Folder**: In Obsidian *Settings → Files and links → Default location for new attachments*, choose `In the folder specified below` and set it to `raw/assets`.
3. **Dataview Plugin** (Optional): Install the community plugin `Dataview` to render automatic tables of trades, win rates, and tags across your vault.
4. **Obsidian Web Clipper**: Use the browser extension to clip articles directly into `raw/market_notes/`.
