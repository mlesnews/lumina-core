# JARVIS Financial API-CLI Suite

## Overview

Complete command-line interface for JARVIS to fully control, monitor, and administer all financial accounts. Provides unified access to all financial services through a single CLI tool.

## Features

### ✅ Account Management
- List all registered accounts
- Register new accounts
- Connect/disconnect accounts
- Account status monitoring

### ✅ Portfolio & Balances
- Real-time balance retrieval
- Portfolio summary
- Multi-account aggregation
- Currency conversion support

### ✅ Monitoring & Alerts
- Continuous account monitoring
- Alert system for issues
- Status checks
- Connection health monitoring

### ✅ Trading Operations
- Position tracking
- Order management
- Trade execution (via connections)
- Portfolio analysis

### ✅ Data Synchronization
- Sync all account data
- Import external data (Copilot Money, etc.)
- Export account maps
- Data backup and restore

### ✅ Reporting
- Full financial reports
- Summary reports
- Status reports
- Custom report generation

## Installation

The CLI is part of the LUMINA project. No additional installation needed.

## Usage

### Basic Commands

```bash
# List all accounts
python scripts/python/jarvis_financial_cli.py list

# Get portfolio summary
python scripts/python/jarvis_financial_cli.py portfolio

# Get account balances
python scripts/python/jarvis_financial_cli.py balances

# Get system status
python scripts/python/jarvis_financial_cli.py status
```

### Account Management

```bash
# Connect to all accounts
python scripts/python/jarvis_financial_cli.py connect --all

# Connect to specific account
python scripts/python/jarvis_financial_cli.py connect --account-id <account_id>

# Disconnect from account
python scripts/python/jarvis_financial_cli.py disconnect <account_id>

# Register new account
python scripts/python/jarvis_financial_cli.py register --type CRYPTO_EXCHANGE --name "My Binance"
```

### Monitoring

```bash
# Check for alerts
python scripts/python/jarvis_financial_cli.py alerts

# Monitor accounts continuously
python scripts/python/jarvis_financial_cli.py monitor --interval 60
```

### Trading Operations

```bash
# Get all positions
python scripts/python/jarvis_financial_cli.py positions

# Get positions for specific account
python scripts/python/jarvis_financial_cli.py positions --account-id <account_id>

# Get open orders
python scripts/python/jarvis_financial_cli.py orders
```

### Data Operations

```bash
# Synchronize all accounts
python scripts/python/jarvis_financial_cli.py sync

# Import Copilot Money CSV
python scripts/python/jarvis_financial_cli.py import --copilot-csv <path_to_csv>

# Export account map
python scripts/python/jarvis_financial_cli.py export --output <path>
```

### Reports

```bash
# Generate full report
python scripts/python/jarvis_financial_cli.py report --type full

# Generate summary report
python scripts/python/jarvis_financial_cli.py report --type summary

# Generate status report
python scripts/python/jarvis_financial_cli.py report --type status
```

## Supported Account Types

- **CRYPTO_EXCHANGE**: Cryptocurrency exchanges (Binance.US, etc.)
- **TRADING_BOT**: Trading bot platforms (3Commas.io)
- **TRADITIONAL_BROKERAGE**: Traditional brokerages (Fidelity Investments)
- **BUDGETING_APP**: Budgeting apps (Copilot Money - CSV import)

## Integration with Financial System

The CLI integrates with:

1. **Financial Account Registry**: Central account database
2. **Financial Account Manager**: Unified account operations
3. **Financial Connections**: API connections (3Commas, Binance, Fidelity)
4. **Copilot Money Integration**: CSV data import
5. **Financial Agent Daemon**: Background monitoring

## Output Format

Most commands output JSON-formatted data for programmatic use. Human-readable output is also provided for interactive use.

## Examples

### Complete Workflow

```bash
# 1. List all accounts
jarvis-financial list

# 2. Connect to all accounts
jarvis-financial connect --all

# 3. Get portfolio summary
jarvis-financial portfolio

# 4. Check for alerts
jarvis-financial alerts

# 5. Generate full report
jarvis-financial report --type full
```

### Daily Monitoring

```bash
# Monitor accounts every 5 minutes
jarvis-financial monitor --interval 300
```

### Data Import

```bash
# Import Copilot Money data
jarvis-financial import --copilot-csv ~/Downloads/copilot_export.csv

# Sync all accounts
jarvis-financial sync
```

## Configuration

Configuration is managed through:
- `config/azure/key_vault_config.json` - Azure Key Vault settings
- `data/financial_accounts/registry.json` - Account registry
- `data/financial_cli/` - CLI output and reports

## Security

- All credentials stored in Azure Key Vault
- No credentials in CLI output
- Secure API connections
- Encrypted data storage

## Troubleshooting

### Account Connection Issues

```bash
# Check account status
jarvis-financial status

# Check alerts
jarvis-financial alerts

# Reconnect account
jarvis-financial disconnect <account_id>
jarvis-financial connect --account-id <account_id>
```

### Data Sync Issues

```bash
# Force sync
jarvis-financial sync

# Check connection status
jarvis-financial status
```

## Related Files

- `scripts/python/jarvis_financial_cli.py` - Main CLI tool
- `scripts/python/financial_account_manager.py` - Account manager
- `scripts/python/financial_account_registry.py` - Account registry
- `scripts/python/financial_connections/` - API connections
- `docs/financial_cli/README.md` - This file

## Future Enhancements

1. **Interactive Mode**: TUI for easier navigation
2. **Webhook Support**: Real-time notifications
3. **Automated Trading**: Execute trades via CLI
4. **Advanced Analytics**: Portfolio optimization suggestions
5. **Multi-currency Support**: Automatic currency conversion
6. **Scheduled Tasks**: Automated monitoring and reporting
