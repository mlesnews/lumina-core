# PR & Ticket Coordination System

## Overview

The PR & Ticket Coordination System automatically generates GitLens PR references and helpdesk tickets for all major/minor issues and changes, with full cross-referencing.

## Features

- **Automatic Detection**: Detects major/minor issues and changes
- **PR Generation**: Creates GitLens PR references (PR-XXX format)
- **Ticket Generation**: Creates helpdesk tickets (standardized 9-digit format: PM/CR/T prefix + 9 digits)
  - `PM` (Problem Management): `PM000000001`
  - `CR` (Change Request): `CR000000001`
  - `T` (Task): `T000000001`
  - See `docs/system/HELPDESK_TICKET_NUMBERING.md` for full standard
- **Cross-Referencing**: Links PR# and ticket numbers for tracking
- **GitLens Integration**: PR references work with GitLens autolinks
- **Helpdesk Integration**: Tickets routed to appropriate teams/droids

## Usage

### Manual Creation

```bash
# Create PR and ticket for an issue
python scripts/python/jarvis_pr_ticket_coordinator.py --create \
  --title "Fix: Invalid model reference" \
  --description "Fixed 'Iron Legion' model references in Cursor settings" \
  --type bug_fix \
  --severity major \
  --files ".cursor/settings.json" "scripts/python/jarvis_configure_ultron_cursor_chat.py"
```

### Auto-Detection

```bash
# Auto-detect changes and generate PRs/tickets
python scripts/python/jarvis_auto_pr_ticket_generator.py --auto
```

### Lookup Cross-Reference

```bash
# Lookup by PR number
python scripts/python/jarvis_pr_ticket_coordinator.py --lookup PR-123

# Lookup by ticket number
python scripts/python/jarvis_pr_ticket_coordinator.py --lookup PM000000001
python scripts/python/jarvis_pr_ticket_coordinator.py --lookup CR000000001
```

## Cross-Reference Format

When PRs and tickets are created, they are automatically cross-referenced:

- **PR Entry**: Contains `ticket_number` field
- **Ticket Entry**: Contains `pr_number` field
- **Mapping File**: `data/pr_tickets/pr_ticket_map.json` maintains bidirectional mapping

### Example Cross-Reference

```json
{
  "pr_number": "PR-123",
  "ticket_number": "PM000000001",
  "change_request_number": "CR000000001",
  "cross_reference": {
    "pr_to_ticket": "PR-123 → PM000000001",
    "ticket_to_pr": "PM000000001 → PR-123"
  }
}
```

**Note**: Ticket numbers use standardized 9-digit format:
- `PM` prefix for Problem Management tickets
- `CR` prefix for Change Requests
- `T` prefix for Tasks

## GitLens Integration

PR references use the `PR-XXX` format which works with GitLens autolinks configured in `.cursor/settings.json`:

```json
{
  "prefix": "PR-",
  "url": "https://github.com/mlesnews/lumina-ai/pull/${num}",
  "title": "Pull Request #${num}"
}
```

In commit messages or code comments, reference PRs as:
- `PR-123` - Automatically links to GitHub PR #123

## Helpdesk Integration

Tickets are automatically routed to appropriate helpdesk teams based on issue type:

- **Security issues** → `@k2so`
- **Health/system issues** → `@2-1b`
- **Technical issues** → `@r2d2`
- **Knowledge/context** → `@r5`
- **Analysis** → `@marvin`
- **Default** → `@c3po` (coordinator)

## File Structure

```
data/pr_tickets/
├── pr_ticket_map.json          # Cross-reference mapping
├── ticket_counter.json          # Ticket number counter
├── pr_counter.json              # PR number counter
├── prs/
│   └── PR-123.json              # Individual PR entries
└── tickets/
    └── PM000000001.json         # Individual ticket entries (PM/CR/T prefix + 9 digits)
```

## Change Types

- `bug_fix`: Bug fixes and error corrections
- `feature`: New features
- `enhancement`: Improvements to existing features
- `refactor`: Code refactoring
- `config`: Configuration changes
- `docs`: Documentation updates
- `security`: Security-related changes
- `performance`: Performance optimizations

## Severity Levels

- `critical`: Critical issues requiring immediate attention
- `major`: Major issues affecting functionality
- `minor`: Minor issues or improvements
- `trivial`: Trivial changes (typos, formatting)

## Integration with Workflows

The system can be integrated into:

- **Git Hooks**: Pre-commit hooks to auto-generate PRs/tickets
- **CI/CD**: Automated PR/ticket generation in pipelines
- **Monitoring**: Integration with system monitoring for issue detection
- **@DOIT**: Automatic PR/ticket generation for autonomous tasks

## Annotations

When creating PRs/tickets, use the annotation helper:

```python
coordinator = PRTicketCoordinator(project_root)
annotated_text = coordinator.annotate_with_references(
    text="Original description",
    pr_number="PR-123",
    ticket_number="PM000000001"
)
```

This adds cross-reference annotations to the text.

## Commit Messages

Generate commit messages with PR and ticket references:

```python
commit_msg = coordinator.generate_commit_message(
    pr_number="PR-123",
    ticket_number="PM000000001",
    title="Fix: Invalid model reference"
)
# Result: "[PR-123] Fix: Invalid model reference\n\nRelated: PM000000001"
```

## Best Practices

1. **Always create PRs/tickets for major/minor changes**
2. **Use descriptive titles and descriptions**
3. **Include file lists for change tracking**
4. **Reference related issues when applicable**
5. **Update status when issues are resolved**
6. **Use cross-references for tracking**

## Status Tracking

PRs and tickets have status fields:
- `open`: Newly created
- `in_progress`: Work in progress
- `review`: Under review
- `resolved`: Issue resolved
- `closed`: Closed/completed

Update status in the JSON files or through the coordinator API.
