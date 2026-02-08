# Financial Accounts Management System

Comprehensive system for mapping, connecting, and managing all financial accounts including 3commas.io, Binance.US, Fidelity Investments, and more.

## Overview

This system provides:
- **Account Registry**: Central registry for all financial accounts
- **API Connections**: Secure connections to financial services APIs
- **Credential Management**: Secure storage in Azure Key Vault
- **Account Mapping**: Visual mapping of all connected accounts
- **Dashboard**: Real-time dashboard showing account status and balances

## Quick Start

### 1. Discover Available Accounts

```bash
python scripts/python/financial_account_manager.py --discover
```

This will show you available accounts to register:
- 3Commas Trading Bot
- Binance.US Exchange
- Fidelity Investments

### 2. Register an Account

```bash
python scripts/python/financial_account_manager.py --register 3commas_main
python scripts/python/financial_account_manager.py --register binance_us
python scripts/python/financial_account_manager.py --register fidelity_investments
```

### 3. Store Credentials

```bash
# For 3Commas or Binance (API-based)
python scripts/python/add_financial_credentials.py --account 3commas_main --api-key YOUR_KEY --api-secret YOUR_SECRET

# For Fidelity (manual tracking)
python scripts/python/add_financial_credentials.py --account fidelity_investments --username YOUR_USERNAME --account-number YOUR_ACCOUNT_NUMBER
```

### 4. Connect to Accounts

```bash
# Connect to a specific account
python scripts/python/financial_account_manager.py --connect 3commas_main

# Connect to all accounts
python scripts/python/financial_account_manager.py --connect-all
```

### 5. View Dashboard

```bash
# Generate account map
python scripts/python/financial_account_manager.py --export data/financial_accounts/account_map.json

# Open dashboard
# Open web/financial_accounts_dashboard.html in your browser
```

## Components

### Financial Account Registry

**File**: `scripts/python/financial_account_registry.py`

Central registry that manages all financial accounts:
- Account registration and discovery
- Credential storage in Azure Key Vault
- Account status tracking
- Account mapping and relationships

**Usage**:
```bash
python scripts/python/financial_account_registry.py --list
python scripts/python/financial_account_registry.py --discover
python scripts/python/financial_account_registry.py --map
```

### Financial Account Manager

**File**: `scripts/python/financial_account_manager.py`

Unified manager for account operations:
- Discover and register accounts
- Connect/disconnect from accounts
- Generate account maps
- Dashboard reports

**Usage**:
```bash
python scripts/python/financial_account_manager.py --dashboard
python scripts/python/financial_account_manager.py --connect-all
```

### API Connections

**Directory**: `scripts/python/financial_connections/`

Individual connection modules for each financial service:

- **3Commas** (`threecommas_connection.py`): Trading bot platform
- **Binance.US** (`binance_connection.py`): Cryptocurrency exchange
- **Fidelity** (`fidelity_connection.py`): Traditional brokerage (manual tracking)

Each connection provides:
- `connect()`: Establish connection
- `disconnect()`: Close connection
- `get_balance()`: Retrieve account balance
- `get_account_info()`: Get account details
- Service-specific methods (e.g., `get_bots()` for 3Commas)

### Credential Management

**File**: `scripts/python/add_financial_credentials.py`

Securely stores credentials in Azure Key Vault:

```bash
# List stored credentials
python scripts/python/add_financial_credentials.py --list

# Store credentials
python scripts/python/add_financial_credentials.py --account binance_us --api-key KEY --api-secret SECRET
```

## Account Types

### 3Commas.io

- **Type**: Trading Bot Platform
- **API**: ✅ Available
- **Capabilities**: Spot trading, futures, grid trading, DCA, options
- **Credentials**: API Key, API Secret

### Binance.US

- **Type**: Cryptocurrency Exchange
- **API**: ✅ Available
- **Capabilities**: Spot trading, futures, staking, arbitrage
- **Credentials**: API Key, API Secret

### Fidelity Investments

- **Type**: Traditional Brokerage
- **API**: ❌ Not available (desktop app only)
- **Capabilities**: Stocks, ETFs, options, day trading
- **Credentials**: Username, Account Number (for tracking)
- **Note**: Use Fidelity Active Trader Pro desktop app for trading

## Integration with Financial Agent Daemon

The financial agent daemon (`financial_agent_daemon.py`) automatically integrates with the account management system:

- Loads accounts from registry
- Aggregates balances across all accounts
- Monitors market positions
- Updates account status

## Security

All credentials are stored securely in Azure Key Vault:
- No credentials in code or configuration files
- Encrypted storage
- Access controlled via Azure Key Vault policies

## Dashboard

The web dashboard (`web/financial_accounts_dashboard.html`) provides:
- Real-time account status
- Balance aggregation
- Account capabilities overview
- Connection status indicators

To use:
1. Generate account map: `python financial_account_manager.py --export data/financial_accounts/account_map.json`
2. Open `web/financial_accounts_dashboard.html` in browser
3. Dashboard auto-refreshes every 30 seconds

## Troubleshooting

### Account Not Connecting

1. Verify credentials are stored:
   ```bash
   python scripts/python/add_financial_credentials.py --list
   ```

2. Test connection manually:
   ```bash
   python scripts/python/financial_account_manager.py --connect ACCOUNT_ID
   ```

3. Check Azure Key Vault access:
   - Ensure Azure credentials are configured
   - Verify vault URL is correct

### Missing Account Map

Generate the account map:
```bash
python scripts/python/financial_account_manager.py --export data/financial_accounts/account_map.json
```

### API Errors

- Verify API keys are correct and have proper permissions
- Check API rate limits
- Review connection logs in financial agent daemon

## Next Steps

1. **Add More Accounts**: Extend `financial_account_registry.py` to discover additional accounts
2. **Custom Connections**: Create new connection classes in `financial_connections/`
3. **Enhanced Dashboard**: Add charts, graphs, and advanced visualizations
4. **Automated Trading**: Integrate with trading strategies using connected accounts

## Tags

`#FINANCIAL_ACCOUNTS` `#ACCOUNT_MAPPING` `#API_INTEGRATION` `@JARVIS` `@LUMINA`
