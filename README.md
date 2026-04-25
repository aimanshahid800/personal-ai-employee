# 🤖 Personal AI Employee — Digital FTE

A local-first autonomous AI agent that manages personal and business affairs using Claude AI and a file-based vault system.

## 🎯 Tier
**Bronze** — Foundation (Minimum Viable Deliverable)

## 🏗️ Architecture

```
Inbox/              ← Drop any file here
    ↓
filesystem_watcher.py   ← Detects new files, creates task .md
    ↓
Needs_Action/       ← Structured task files queue up here
    ↓
orchestrator.py     ← Claude AI reads, reasons, plans
    ↓
Pending_Approval/   ← AI's plan waits for your review
    ↓
Done/               ← Approved & completed tasks archived
```

## 📁 Vault Structure

| Folder | Purpose |
|--------|---------|
| `Inbox/` | Drop files here to trigger processing |
| `Needs_Action/` | Auto-generated task files |
| `Pending_Approval/` | AI plans waiting for human approval |
| `Done/` | Completed and archived tasks |
| `Logs/` | Daily audit logs (JSON) |

## 📄 Key Files

- **Dashboard.md** — Live status updated by orchestrator
- **Company_Handbook.md** — Rules of engagement for the AI
- **filesystem_watcher.py** — Watches Inbox/ for new files
- **orchestrator.py** — Processes tasks using Claude AI

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/aimanshahid800/personal-ai-employee
cd personal-ai-employee
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Anthropic API key
```bash
export ANTHROPIC_API_KEY=your-api-key-here
```
Get your key at: https://console.anthropic.com

### 4. Run the Filesystem Watcher (Terminal 1)
```bash
python filesystem_watcher.py --vault .
```

### 5. Run the Orchestrator (Terminal 2)
```bash
python orchestrator.py --vault .
```

### 6. Test it!
Drop any file into the `Inbox/` folder and watch the magic:
```bash
echo "Process this invoice from Client A for $500" > Inbox/test_invoice.txt
```

Then check `Needs_Action/` → `Pending_Approval/` → `Done/`

## 🔒 Security

- All sensitive actions require human approval
- No credentials stored in vault — use environment variables
- Human-in-the-loop for all external actions
- Full audit log in `Logs/YYYY-MM-DD.json`

## 🛠️ Tech Stack

- **Claude AI** — Reasoning engine (claude-opus-4-5)
- **Python** — Watcher scripts & orchestrator
- **GitHub** — Vault and version control

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Your Claude API key (required) |

## 📋 How It Works

1. Drop a file into `Inbox/`
2. `filesystem_watcher.py` detects it and creates a structured task in `Needs_Action/`
3. `orchestrator.py` picks up the task, sends it to Claude AI with company rules
4. Claude analyzes and creates an action plan in `Pending_Approval/`
5. You review and approve — task moves to `Done/`
