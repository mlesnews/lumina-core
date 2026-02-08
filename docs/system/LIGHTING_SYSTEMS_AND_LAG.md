# Lighting Systems Count & Why Typing Can Feel Laggy

## How Many Lighting “Systems” There Were (5+)

Different **entry points** that could affect lighting (before and after the merge):

| # | Entry point | What it does | Runs when |
|---|-------------|--------------|-----------|
| 1 | **JARVIS Smart Lighting Day/Night Sync** | Single source of truth: screen + keyboard + external (registry) | On demand, startup (headless), keyboard daemon |
| 2 | **MANUS time-based** (now delegates to JARVIS) | Used to run its own time logic; now just registry helper + CLI | CLI, toggle/force scripts |
| 3 | **Keyboard lighting auto-daemon** | Calls JARVIS when period changes | If run as daemon: loop every 15 min |
| 4 | **Smart Lighting Killer** | Kills lighting when dark + lid closed; we added “never kill in daytime” | **Scheduled task: every 5 min** (`smart_lighting_killer_task.xml`) |
| 5 | **Light profile startup** | Applies light profile on boot/logon and **every 15 min** | **Scheduled task: logon, boot, every 15 min** (`light_profile_startup_task.xml`) |
| 6 | **JARVIS continuous day/night monitor** | Calls JARVIS sync every N seconds (default **60 sec**) | If run as background process |
| 7 | **Keyboard lighting watchdog** | Health check + auto-fix every 15 min | If run as daemon |
| 8 | **Headless startup daemon** (phase 2) | Runs JARVIS setup_smart_lighting at login | Once at login |
| 9 | **External lighting fix / persistent killer** | Another killer task (legacy) | **Scheduled: every 5 min** if task exists (`external_lighting_fix/lighting_killer_task.xml`) |

So there were **5+ competing “systems”** (multiple scripts + multiple scheduled tasks). After the merge there is **one** decision-maker (JARVIS), but **several tasks/daemons** can still run on timers and cause load.

---

## Why Typing Can Feel Laggy

Likely contributors:

1. **Scheduled tasks every 5 min**  
   Smart lighting killer (and possibly the old persistent killer) run **every 5 minutes**. Each run starts Python + PowerShell (theme/lid checks). That can cause small, periodic CPU and I/O spikes.

2. **Light profile task every 15 min**  
   Another task runs every 15 min to apply a light profile. Again: Python (and possibly Armoury Crate / UI) running on a timer.

3. **Continuous day/night monitor at 60 sec**  
   If `jarvis_continuous_day_night_monitor` is running with default 60 s interval, it calls JARVIS sync every minute, which runs PowerShell (registry) and WMI (screen). That’s a lot of periodic work and can add to perceived lag.

4. **Armoury Crate / AacAmbientLighting**  
   ASUS services and processes (e.g. AacAmbientLighting) can hook or poll input/devices. That can add input latency regardless of our scripts.

5. **Multiple Python + PowerShell processes**  
   Several tasks (killer, light profile, maybe watchdog) each spawn processes. When they overlap or run close together, you get extra CPU and I/O, which can make typing feel less smooth.

6. **Watchdog health checks and fixes**  
   If the keyboard lighting watchdog is running, it does health checks and sometimes “attempt_fix” (more Python/PowerShell). That adds extra work and can coincide with typing.

---

## What To Do To Reduce Lag

- **Use one periodic lighting path**  
  Rely on **one** of: light profile task every 15 min **or** keyboard lighting auto-daemon every 15 min. Don’t run both if you care about lag.

- **Stop or slow the smart lighting killer task**  
  - Either **disable** the scheduled task that runs `jarvis_smart_lighting_killer_system_mode.py` every 5 min, or  
  - Change the trigger to run less often (e.g. every 30 min or once at logon only).  
  We already changed the script so it **never kills during daytime**; running it less often is safe and reduces spikes.

- **Don’t run the continuous day/night monitor at 60 s**  
  If you use it, run it with a long interval (e.g. 15 min) or only run JARVIS sync on logon + when period changes (e.g. via the keyboard auto-daemon), not every minute.

- **Don’t run the keyboard lighting watchdog** unless you need it; it adds another 15 min timer and extra work when it “fixes”.

- **Optional: disable or uninstall Armoury Crate / AacAmbientLighting**  
  If you don’t need RGB/lighting from ASUS, disabling those can reduce input-related lag (see `docs/external_lighting_bios_uefi_guide.md` for BIOS options).

---

## Summary

- There were **5+ lighting-related systems** (multiple scripts + scheduled tasks).
- **Typing lag** is likely from: tasks every 5 min (killer) and 15 min (light profile), possibly the 60 s day/night monitor, Armoury Crate, and overlapping Python/PowerShell.
- **Quick wins:** disable or slow the 5 min killer task, use only one 15 min lighting path, and avoid running the 60 s continuous monitor (or set a long interval).
