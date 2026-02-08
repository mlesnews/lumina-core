# Cursor Internal Error – Workaround

When Cursor shows an **internal** or **serialization** error (e.g. agent loop crash), it often **does not** auto-retry. This doc is the **workaround**: use the Request ID to rerun the failed request.

## Error patterns (examples)

- `[internal] serialize binary: invalid int 32: 4294967295`
- `LTe: [internal] serialize binary: invalid int 32: 4294967295`
- Any message that includes **Request ID:** followed by a UUID and an internal/serialization stack

## Steps (workaround)

1. **Copy the Request ID** from the error (e.g. `e7484e66-20c0-4477-a83c-a0d7ae87981a`).
2. **Paste it in chat** and send (e.g. paste the UUID, or paste the full error and say "rerun" / "retry").
3. **Agent runs the rerun workflow** (see rule `request_id_internal_error_rerun.mdc`): runs `auto_fix_and_rerun_request_id.py <REQUEST_ID>` and, if the original @ask is found, tells you to rerun with the suggested `@bau [original ask]`.
4. **Rerun**: Use the suggested `@bau ...` command (or retry your last request manually).

## One-liner (manual)

From project root:

```bash
python scripts/python/auto_fix_and_rerun_request_id.py <REQUEST_ID>
```

Then follow the script output to rerun the @ask.

## Why Cursor didn’t retry

- Our **retry config** (`cursor.agent.retryAttempts` / `retryDelay` in `.vscode/settings.json`) is for **connection/timeout** only.
- **Internal/serialization** errors are not connection errors; Cursor often does not retry them. This workaround fills that gap.

## Related

- [Request ID Auto Fix and Rerun Workflow](REQUEST_ID_AUTO_FIX_RERUN_WORKFLOW.md)
- [Cursor Connection Stalled Quick Fix](CURSOR_CONNECTION_STALLED_QUICK_FIX.md) – retry scope note
- Rule: `.cursor/rules/request_id_internal_error_rerun.mdc`
