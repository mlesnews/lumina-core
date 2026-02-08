# Request ID Auto Fix and Rerun Workflow

## Permanent Workflow Entry

**CRITICAL**: This is a **PERMANENT WORKFLOW** that automatically triggers whenever a Request ID is pasted.

## Workflow Definition

**When**: A Request ID (UUID format) is detected in user input  
**Action**: Automatically execute the following workflow:

1. **Fix Connection Error** - Apply connection error fixes
2. **Find Original @ask/Job** - Search for the original request that caused the error
3. **Rerun the Job** - Automatically rerun the original @ask as @bau

## Implementation

**Script**: `scripts/python/auto_fix_and_rerun_request_id.py`

**Detection Pattern**: UUID format (e.g., `7f27bdec-ba62-4a86-bd20-0cf3df52b446`)

## Usage

### Automatic Detection

Simply paste a Request ID in chat:

```
7f27bdec-ba62-4a86-bd20-0cf3df52b446
```

The workflow will automatically:
- Detect the Request ID
- Fix the connection error
- Find the original @ask
- Prepare the job for rerun

### Manual Execution

```bash
python scripts/python/auto_fix_and_rerun_request_id.py <REQUEST_ID>
```

### From User Input

```bash
python scripts/python/auto_fix_and_rerun_request_id.py --input "Request ID: 7f27bdec-ba62-4a86-bd20-0cf3df52b446"
```

## Workflow Steps

### Step 1: Fix Connection Error

- Tracks the Request ID in diagnostics
- Investigates the connection error
- Applies retry manager fixes
- Verifies connection flow optimizations

**Script**: `fix_request_id_connection_error.py`

### Step 2: Find Original @ask/Job

- Searches recent chat histories (last 30 days)
- Extracts the original @ask directive
- Retrieves context and metadata

**Script**: `find_ask_by_request_id.py`

### Step 3: Rerun the Job

- Prepares the @ask for rerun as @bau
- Updates retry count
- Generates execution command

**Script**: `retry_ask_with_request_id.py`

## Output

### Success

When the original @ask is found:

```
✅ WORKFLOW COMPLETED
Request ID: 7f27bdec-ba62-4a86-bd20-0cf3df52b446
Status: Ready for rerun

📋 NEXT STEP: Execute the @ask as @bau:
   @bau [original ask text]
```

### Partial Success

When connection error is fixed but @ask not found:

```
⚠️  WORKFLOW COMPLETED WITH WARNINGS
Request ID: 7f27bdec-ba62-4a86-bd20-0cf3df52b446
Status: Connection fixed, but original @ask not found
```

## Integration with Cursor IDE

This workflow integrates with:

- **@JARVIS** - System coordination
- **@LUMINA** - Project ecosystem
- **#BAU** - Business As Usual workflows
- **#AIMLSEA** - Connection error handling
- **Connection Retry Manager** - Automatic retry logic
- **Request ID Tracking** - Diagnostic tracking

## Diagnostic Files

Workflow results are saved to:

```
data/diagnostics/auto_fix_rerun_{REQUEST_ID}_{TIMESTAMP}.json
```

## Tags

- `#BAU` - Business As Usual workflow
- `#AUTOMATION` - Automated workflow
- `#CONNECTION_ERROR` - Connection error handling
- `#RETRY` - Retry mechanism
- `#REQUEST_ID` - Request ID tracking
- `@JARVIS` - JARVIS system
- `@LUMINA` - LUMINA project

## Error Handling

The workflow handles:

- Connection errors (automatic fix)
- Missing @ask (graceful degradation)
- Retry failures (error reporting)
- Diagnostic tracking (always saved)

## Future Enhancements

- Automatic execution of @bau rerun (currently requires manual step)
- Extended search window for @ask (beyond 30 days)
- Integration with Cursor IDE retry button
- Cross-reference with helpdesk tickets

## Related Scripts

- `fix_request_id_connection_error.py` - Connection error fixes
- `find_ask_by_request_id.py` - @ask lookup
- `retry_ask_with_request_id.py` - Job rerun
- `track_request_id.py` - Request ID tracking
- `cursor_retry_with_request_id.py` - Cursor IDE retry integration

## Notes

- **PERMANENT ENTRY**: This workflow is permanently integrated into the system
- **AUTOMATIC TRIGGER**: No manual intervention required when Request ID is detected
- **GRACEFUL DEGRADATION**: Works even if original @ask is not found
- **COMPREHENSIVE TRACKING**: All steps are logged and tracked

---

**Last Updated**: 2026-01-16  
**Status**: Active  
**Version**: 1.0
