# @SCOTTY Shutdown / Startup & Focus Monitor

**Chief Engineer Scotty – Windows Architect monitoring.**

Use this when the cursor loses focus while you type (e.g. focus jumps to the editor or another pane), causing typos in docs and scripts.

---

## What it does

1. **Startup logging** – Records when the session started and (optionally) uptime, so you can correlate “after startup X, focus started stealing.”
2. **Focus-change logging** – Records every time the foreground window changes (which app/window stole focus). Logs: timestamp, previous window title/process, new window title/process.

Logs go to `data/scotty_monitor/`:

- `startup_YYYYMMDD_HHMMSS.json` – startup event
- `focus_YYYYMMDD_HHMMSS.jsonl` – one JSON object per focus change (one line each)

---

## Usage

### One-off: log startup only

```bash
python scripts/python/scotty_shutdown_startup_focus_monitor.py --startup
```

### One-off: monitor focus for N minutes (find what steals focus)

```bash
# Monitor for 15 minutes; then review the log
python scripts/python/scotty_shutdown_startup_focus_monitor.py --focus 15
```

Then open `data/scotty_monitor/focus_*.jsonl` and look for lines where `new_process` is something you didn’t click (e.g. `Cursor`, `Code`, a script, a notification).

### One-off: startup + focus monitor (typical after reboot)

```bash
python scripts/python/scotty_shutdown_startup_focus_monitor.py --both 10
```

Logs startup, then records focus changes for 10 minutes.

### Install: run at logon (startup + 10 min focus monitor, 2 min delay)

```bash
python scripts/python/scotty_shutdown_startup_focus_monitor.py --install
```

Creates a Task Scheduler task that runs 2 minutes after logon and monitors focus for 10 minutes. Use this to capture what steals focus right after boot.

---

## Reading the focus log

Each line in `focus_*.jsonl` is JSON, e.g.:

```json
{"ts": "2026-01-29T14:32:01.123456", "prev_title": "My Doc - Editor", "prev_process": "Cursor", "new_title": "Terminal", "new_process": "WindowsTerminal"}
```

- **prev_*** – window that had focus before the change  
- **new_*** – window that took focus (the “stealer”)  
- **ts** – time of the change  

Look for:

- **new_process** = `Cursor` or `Code` when you were typing in another app (browser, Word, etc.) – something is bringing the editor to front.
- **new_process** = a script or background tool – that process is stealing focus.
- Repeated **new_process** = same app – that app is aggressively taking focus (e.g. notifications, auto-refresh).

---

## Shutdown

Shutdown is not logged automatically (Windows doesn’t give a simple “about to shut down” hook from a normal script). To capture state *before* you shut down, run:

```bash
python scripts/python/scotty_shutdown_startup_focus_monitor.py --startup
```

before closing apps; that writes a startup-style event with current time (optional; mainly for consistency with “session start” if you use it that way).

---

## #automation

- **Manual:** `python scripts/python/scotty_shutdown_startup_focus_monitor.py --both 10`  
- **At logon:** `python scripts/python/scotty_shutdown_startup_focus_monitor.py --install` (then reboot or log off/on and wait 2 min; focus is monitored for 10 min).

---

## Related

- `scripts/python/scotty_engine_room.py` – Scotty master control
- `scripts/python/scotty_peak_reboot_optimization.py` – reboot optimization
- `docs/operations/SCOTTY_PEAK_REBOOT_OPTIMIZATION.md` – reboot flow
