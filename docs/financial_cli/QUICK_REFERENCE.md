# JARVIS Financial CLI - Quick Reference

## 🚀 Quick Start

```bash
# List all accounts
jarvis-financial list

# Get portfolio overview
jarvis-financial portfolio

# Check system status
jarvis-financial status
```

## 📋 Command Reference

### Account Management

| Command | Description | Example |
|---------|-------------|---------|
| `list` | List all accounts | `jarvis-financial list` |
| `list --status connected` | Filter by status | `jarvis-financial list --status connected` |
| `connect --all` | Connect all accounts | `jarvis-financial connect --all` |
| `connect --account-id <id>` | Connect specific account | `jarvis-financial connect --account-id binance_001` |
| `disconnect <id>` | Disconnect account | `jarvis-financial disconnect binance_001` |
| `register` | Register new account | `jarvis-financial register --type CRYPTO_EXCHANGE --name "My Exchange"` |

### Portfolio & Balances

| Command | Description | Example |
|---------|-------------|---------|
| `portfolio` | Full portfolio summary | `jarvis-financial portfolio` |
| `balances` | All account balances | `jarvis-financial balances` |
| `balances --account-id <id>` | Specific account balance | `jarvis-financial balances --account-id binance_001` |

### Monitoring

| Command | Description | Example |
|---------|-------------|---------|
| `status` | System status | `jarvis-financial status` |
| `monitor` | Continuous monitoring | `jarvis-financial monitor --interval 60` |
| `alerts` | Check alerts | `jarvis-financial alerts` |

### Trading Operations

| Command | Description | Example |
|---------|-------------|---------|
| `positions` | All positions | `jarvis-financial positions` |
| `positions --account-id <id>` | Account positions | `jarvis-financial positions --account-id binance_001` |
| `orders` | Open orders | `jarvis-financial orders` |
| `orders --account-id <id>` | Account orders | `jarvis-financial orders --account-id binance_001` |

### Data Operations

| Command | Description | Example |
|---------|-------------|---------|
| `sync` | Sync all accounts | `jarvis-financial sync` |
| `import --copilot-csv <file>` | Import Copilot data | `jarvis-financial import --copilot-csv export.csv` |
| `export --output <file>` | Export account map | `jarvis-financial export --output map.json` |

### Reports

| Command | Description | Example |
|---------|-------------|---------|
| `report --type full` | Full report | `jarvis-financial report --type full` |
| `report --type summary` | Summary report | `jarvis-financial report --type summary` |
| `report --type status` | Status report | `jarvis-financial report --type status` |

## 🔄 Common Workflows

### Daily Check
```bash
jarvis-financial status
jarvis-financial portfolio
jarvis-financial alerts
```

### Account Setup
```bash
# 1. List discovered accounts
jarvis-financial list

# 2. Register new account
jarvis-financial register --type CRYPTO_EXCHANGE --name "Binance US"

# 3. Connect account
jarvis-financial connect --account-id <account_id>

# 4. Verify connection
jarvis-financial balances --account-id <account_id>
```

### Monitoring Setup
```bash
# Start continuous monitoring (every 5 minutes)
jarvis-financial monitor --interval 300
```

### Data Import
```bash
# Import Copilot Money CSV
jarvis-financial import --copilot-csv ~/Downloads/copilot_export.csv

# Sync all accounts
jarvis-financial sync
```

### Full Report Generation
```bash
# Generate comprehensive report
jarvis-financial report --type full
```

## 📊 Output Locations

- **Reports**: `data/financial_cli/financial_report_*.json`
- **Account Maps**: `data/financial_cli/account_map_*.json`
- **Copilot Data**: `data/copilot_money/copilot_transactions_*.json`

## 🎯 Account Types

- `CRYPTO_EXCHANGE` - Cryptocurrency exchanges
- `TRADING_BOT` - Trading bot platforms
- `TRADITIONAL_BROKERAGE` - Traditional brokerages
- `BUDGETING_APP` - Budgeting applications

## ⚡ Tips

1. **Use `--help`** for command-specific help:
   ```bash
   jarvis-financial connect --help
   ```

2. **Monitor in background**:
   ```bash
   nohup jarvis-financial monitor --interval 300 > monitor.log 2>&1 &
   ```

3. **Export for analysis**:
   ```bash
   jarvis-financial report --type full > report.json
   ```

4. **Check alerts regularly**:
   ```bash
   jarvis-financial alerts
   ```

## 🔗 Related Commands

- `financial-agent.ps1` - Financial agent daemon
- `add_financial_credentials.py` - Add account credentials
- `financial_account_manager.py` - Direct Python API
