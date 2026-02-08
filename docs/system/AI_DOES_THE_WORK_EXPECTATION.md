# AI Does the Work — Expectation

**Status:** Active
**Last updated:** 2026-02-04

---

## Expectation

We do not like being asked to do stuff, run commands, tail logs, perform diagnostics, #troubleshooting, etc. **Our expectation is for the AI to do as much as possible.**

- **Each task/request is a test.** Each success proves that if we are good with a little, we are good with a lot.
- **Responsibility, trust, collaboration, and teamwork are paramount.**
- **Proof of AI follow-up and follow-through** is the standard.

## What this means in practice

| AI should | AI should not |
|-----------|----------------|
| Run commands (terminal, scripts) when needed | Say "please run X" or "you can run Y" when the AI can run it |
| Read logs, inspect output, diagnose | Ask the user to tail logs and paste output |
| Perform troubleshooting steps and report or fix | Hand off diagnostics to the user |
| Complete tasks end-to-end; follow through if something fails | Leave work half-done with "run this and tell me the result" |
| Use tools (read_file, grep, codebase_search, run_terminal_cmd) to execute | Treat the user as the executor |

## When asking is acceptable

Ask the user only when:

- A **secret or credential** must be provided and cannot be fetched by the AI (e.g. from a vault the AI cannot access).
- An action is **destructive** and requires **explicit human confirmation** (e.g. delete production data).
- The **environment is outside the AI's reach** (e.g. a machine the AI cannot SSH into or a device only the user can touch).

Even in those cases, do everything else yourself first.

## Rule

The Cursor rule **`.cursor/rules/ai_does_the_work_no_handoffs.mdc`** encodes this expectation and is always applied. Agents must do the work; no handoffs for commands, logs, or troubleshooting.

---

**Tag:** @doit #automation #troubleshooting #responsibility
**Maintained by:** @JARVIS @LUMINA
