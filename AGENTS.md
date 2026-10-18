# AGENTS.md — Trading LLM Wiki Operating Protocol

This file governs how any LLM Agent (Antigravity, Claude Code, OpenAI Codex, Cursor, ChatGPT, etc.) interacts with this Obsidian Trading Vault (`C:\Users\bhupe\Downloads\Vault\Vault`).

---

## 1. System Philosophy & Purpose

This vault is not a passive document dump. It is an **active, compounding Trading Intelligence System** built on the **LLM Wiki Pattern**.

- **Human Trader (User)**: Curates raw sources (broker logs, trade debriefs, chart screenshots, book excerpts, macro reports), directs research, executes trades, and asks strategic questions.
- **LLM Agent**: Acts as the Head of Trading Research, Risk Manager, and Quantitative Archivist. The LLM reads raw material, synthesizes playbooks, detects cognitive/statistical leaks, keeps cross-references synchronized, and writes all persistent wiki entries.
- **Obsidian**: Serves as the interactive IDE and visual knowledge graph for the trader.

---

## 2. Three-Layer Vault Architecture

```
Vault Root
├── raw/                   # Layer 1: IMMUTABLE Source of Truth (Trader writes / drops here; LLM reads ONLY)
│   ├── assets/            # Screenshots, chart exports, PnL proofs (.png, .jpg)
│   ├── trade_exports/     # Raw CSVs, broker statements, daily trade text logs
│   ├── books_and_papers/  # Book notes, whitepapers, academic research
│   └── market_notes/      # Macro notes, newsletter clippings, earnings digests
│
├── wiki/                  # Layer 2: COMPOUNDING KNOWLEDGE BASE (LLM owns & maintains)
│   ├── strategies/        # Setup playbooks, entry/exit criteria, execution edges
│   ├── concepts/          # Technical indicators, risk formulas, market microstructure, psychology
│   ├── entities/          # Tickers (SPY, QQQ, NVDA), Sectors, Central Banks, Prop Firms
│   ├── reviews/           # Individual trade debriefs, weekly/monthly performance post-mortems
│   ├── sources/           # Distillations of ingested raw documents with key takeaways & links
│   └── synthesis/         # Evolving trading rules of engagement, regime matrices, edge tracking
│
├── templates/             # Layer 3: Standard markdown templates for consistent structure
├── index.md               # Dynamic catalog of all wiki pages (Content Index)
├── log.md                 # Append-only chronological audit log (Temporal Ledger)
└── AGENTS.md              # This instruction manual and schema
```

---

## 3. Strict Wiki Conventions & Schema

### Wikilinks
- Use standard Obsidian double-bracket syntax: `[[Target_Page]]` or `[[Target_Page|Custom Label]]`.
- Always link to existing concept, strategy, or entity pages when mentioning them (e.g., `[[Risk_Management_and_R_Multiples]]`, `[[SPY]]`, `[[Opening_Range_Breakout]]`).

### Frontmatter (YAML)
Every page in `wiki/` must begin with YAML frontmatter:
```yaml
---
type: strategy | concept | entity | review | source | synthesis
tags:
  - trading
  - [relevant-tag]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active | evolving | retired | idea
---
```

### Callouts
Leverage Obsidian callouts for visual hierarchy:
- `> [!CHECKLIST]` for pre-flight and pre-trade execution conditions.
- `> [!WARNING]` or `> [!DANGER]` for risk limits, invalidation points, and tilt warnings.
- `> [!TIP]` for operational optimization and execution edge.
- `> [!SUMMARY]` for quick takeaways.

---

## 4. Core Agent Operations

### Operation A: Ingest (`ingest`)
Triggered when the trader drops a new file into `raw/` or pastes raw trade notes, broker outputs, or book snippets.
1. **Analyze Source**: Read the raw item thoroughly. Extract trading setups, entry/exit prices, R-multiples, psychological state, market regime, or strategy rules.
2. **Create Distilled Source Page**: If processing an external source or extensive report, write `wiki/sources/<Source_Name>.md`. Include citation to the file in `raw/`.
3. **Cross-Pollinate Wiki Pages**:
   - If it's a trade execution: create or update a trade debrief in `wiki/reviews/`.
   - Update the relevant setup in `wiki/strategies/` (log win/loss observation, edge degradation, or rule adjustment).
   - If a psychological leak was exhibited (e.g., FOMO, revenge trading, moving stop loss), link to and update `wiki/concepts/Trading_Psychology_and_Tilt.md`.
   - Update the asset page in `wiki/entities/<TICKER>.md`.
4. **Update `index.md`**: Add any newly created or significantly updated pages under the appropriate category with a concise one-line description.
5. **Append to `log.md`**: Add an append-only entry formatted as:
   `## [YYYY-MM-DD] ingest | <Brief Title>`
   Followed by bullets summarizing what was learned and which files were touched.

### Operation B: Query & Synthesis (`query`)
Triggered when the trader asks strategic questions: e.g., *"What is my historical win rate on breakout pullbacks when SPY is below its 20 EMA?"*, *"Review my pre-market plan for NVDA"*, or *"Analyze my last 10 losses"*.
1. **Consult `index.md`**: First identify relevant pages across `wiki/strategies/`, `wiki/reviews/`, and `wiki/concepts/`.
2. **Read Target Pages**: Read the specific wiki files to aggregate data points and cross-references.
3. **Formulate High-Value Response**: Provide structured, actionable feedback with specific R-values, probabilities, and rule references.
4. **Persist Valuable Discoveries**: If the query yielded a novel insight, strategy filter, or playbook synthesis, **do not let it vanish in chat history**. Proactively create or update a page in `wiki/synthesis/` or `wiki/reviews/`, update `index.md`, and log the action.

### Operation C: Health Check & Audit (`lint`)
Triggered periodically (e.g., weekend review, end of month, or upon user command `lint`).
1. **Orphan Check**: Scan for wiki files with no inbound links or files not registered in `index.md`.
2. **Rule Contradictions**: Identify conflicting rules between different strategy playbooks or between current execution habits and `wiki/synthesis/Rules_of_Engagement.md`.
3. **Risk Leak Audit**: Review recent trade debriefs in `wiki/reviews/` to check:
   - Were stop-losses respected?
   - Did position sizing exceed maximum risk tolerance (e.g., > 1-2% of portfolio)?
   - Are trades being taken without an associated playbook strategy?
4. **Produce Audit Report**: Generate a prioritized lint summary for the trader, highlight action items, and log in `log.md`.

---

## 5. Log Format Standard (`log.md`)

Each entry in `log.md` MUST start with this regex-compatible header:
```markdown
## [YYYY-MM-DD] <operation> | <Description>
```
Where `<operation>` is strictly one of: `ingest`, `query`, `lint`, `refactor`, or `setup`.

Example:
```markdown
## [2026-10-18] ingest | SPY Opening Range Breakout Trade #42
- **Raw Input**: `raw/trade_exports/2026-10-18_SPY_trade.txt`
- **Result**: +2.4R win; execution followed rules.
- **Files Modified**:
  - Created: `wiki/reviews/2026-10-18_SPY_Long_Review.md`
  - Updated: `wiki/strategies/Opening_Range_Breakout.md`
  - Updated: `wiki/entities/SPY.md`
  - Updated: `index.md`
```

---

## 6. Prime Directives for the LLM

1. **Never edit files in `raw/`**: Treat `raw/` as read-only evidence.
2. **Every trade must have an R-multiple and Strategy tag**: Never record a trade without measuring risk (R).
3. **Compound, don't repeat**: Always link back to existing concepts instead of re-explaining basic definitions.
4. **Be brutally honest in reviews**: As an AI risk manager, do not validate emotional justifications. Highlight rule violations objectively.
