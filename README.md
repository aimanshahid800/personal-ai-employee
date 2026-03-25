# 🤖 Personal AI Employee — Digital FTE

A local-first autonomous AI agent that manages personal and business 
affairs using Claude AI and a file-based vault system.

## 🎯 Tier
**Bronze** — Foundation (Minimum Viable Deliverable)

## 🏗️ Architecture
```
External Sources (Gmail / Files)
         ↓
   Needs_Action/     ← Watcher drops tasks here
         ↓
   Claude AI         ← Reads, reasons, plans
         ↓
   Pending_Approval/ ← Waits for human approval
         ↓
   Done/             ← Completed tasks archived
```

## 📁 Vault Structure

| Folder | Purpose |
|--------|---------|
| Needs_Action/ | Incoming tasks for AI to process |
| Pending_Approval/ | Actions waiting for human approval |
| Done/ | Completed and archived tasks |
| Inbox/ | Raw incoming files |

## 📄 Key Files

- **Dashboard.md** — Real-time status of active tasks
- **Company_Handbook.md** — Rules of engagement for the AI

## 🔒 Security

- All sensitive actions require human approval
- No credentials stored in vault
- Human-in-the-loop for all external actions

## 🚀 Setup

1. Clone this repo
2. Open Dashboard.md to view AI Employee status
3. Drop files into Needs_Action/ to trigger processing
4. Review Pending_Approval/ before any action executes

## 🛠️ Tech Stack

- Claude AI — Reasoning engine
- GitHub — Vault and version control
- Python (planned) — Watcher scripts
- MCP Servers (planned) — External integrations
