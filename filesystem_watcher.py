"""
filesystem_watcher.py — AI Employee Perception Layer (Bronze Tier)
Watches Inbox/ folder and creates structured task files in Needs_Action/
Run: python filesystem_watcher.py --vault .
"""

import time
import shutil
import logging
import argparse
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("watcher.log")],
)
logger = logging.getLogger("FileWatcher")


def create_task_file(source: Path, needs_action: Path) -> Path:
    """Create a structured .md task file in Needs_Action/"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    task_name = f"FILE_{timestamp}_{source.stem}.md"
    task_path = needs_action / task_name

    content = f"""---
type: file_drop
original_name: {source.name}
file_size: {source.stat().st_size} bytes
received: {datetime.now().isoformat()}
priority: medium
status: pending
---

## File Received

A new file has been dropped into the Inbox for processing.

**File:** `{source.name}`
**Size:** {source.stat().st_size} bytes
**Received:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Suggested Actions

- [ ] Review file contents
- [ ] Determine required action
- [ ] Draft response or process file
- [ ] Move to Done when complete
"""
    shutil.copy2(source, needs_action / source.name)
    task_path.write_text(content, encoding="utf-8")
    logger.info(f"✅ Task created: {task_name}")
    return task_path


def update_dashboard(vault: Path, task_count: int):
    """Update Dashboard.md with current watcher status"""
    dashboard = vault / "Dashboard.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""# 🤖 AI Employee Dashboard

## Status
- Last Updated: {now}
- Active Tasks: {task_count}
- Pending Approvals: 0

## Watcher Status
- File Watcher: ✅ ACTIVE
- Monitoring: Inbox/
- Last Check: {now}

## Today's Summary
Filesystem Watcher is running. Drop any file into `Inbox/` to trigger AI processing.
"""
    dashboard.write_text(content, encoding="utf-8")


def watch(vault_path: str, interval: int = 10):
    vault = Path(vault_path)
    inbox = vault / "Inbox"
    needs_action = vault / "Needs_Action"

    # Ensure all folders exist
    for folder in [inbox, needs_action, vault / "Done", vault / "Pending_Approval"]:
        folder.mkdir(parents=True, exist_ok=True)

    processed = set()
    task_count = 0

    logger.info(f"👁️  Watching: {inbox.resolve()}")
    logger.info(f"📁  Tasks going to: {needs_action.resolve()}")
    logger.info(f"⏱️  Checking every {interval} seconds")
    logger.info("Ready! Drop any file into Inbox/ to trigger processing...")

    while True:
        try:
            for file in inbox.iterdir():
                if file.name.startswith(".") or file.name == ".gitkeep":
                    continue
                if file.name in processed or not file.is_file():
                    continue

                logger.info(f"📥 New file detected: {file.name}")
                create_task_file(file, needs_action)
                processed.add(file.name)
                task_count += 1
                update_dashboard(vault, task_count)
                logger.info(f"📊 Total tasks queued today: {task_count}")

        except Exception as e:
            logger.error(f"Error in watch cycle: {e}")

        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Employee — Filesystem Watcher")
    parser.add_argument("--vault", default=".", help="Path to vault folder (default: current dir)")
    parser.add_argument("--interval", type=int, default=10, help="Check interval in seconds")
    args = parser.parse_args()

    try:
        watch(args.vault, args.interval)
    except KeyboardInterrupt:
        logger.info("👋 Watcher stopped by user.")
