# JARVIS Financial CLI - API Reference

## Python API

The CLI can also be used as a Python module:

```python
from jarvis_financial_cli import JARVISFinancialCLI

# Initialize
cli = JARVISFinancialCLI()

# List accounts
accounts = cli.list_accounts()

# Get portfolio
portfolio = cli.get_portfolio_summary()

# Get balances
balances = cli.get_balances()

# Get status
status = cli.get_status()

# Generate report
report = cli.generate_report("full")
```

## Class Reference

### `JARVISFinancialCLI`

Main CLI class for all financial operations.

#### Methods

##### Account Management

- `list_accounts(status_filter: Optional[str] = None) -> List[Dict[str, Any]]`
  - List all financial accounts
  - Optional filter by status: 'connected', 'disconnected', 'error'

- `get_account(account_id: str) -> Optional[Dict[str, Any]]`
  - Get details for specific account

- `connect_account(account_id: str) -> Dict[str, Any]`
  - Connect to a financial account

- `disconnect_account(account_id: str) -> Dict[str, Any]`
  - Disconnect from a financial account

- `connect_all() -> Dict[str, Any]`
  - Connect to all registered accounts

- `register_account(account_type: str, name: str, **kwargs) -> Dict[str, Any]`
  - Register a new financial account

##### Portfolio & Balances

- `get_balances(account_id: Optional[str] = None) -> Dict[str, Any]`
  - Get account balances
  - If account_id provided, returns balance for that account
  - Otherwise returns all account balances with total

- `get_portfolio_summary() -> Dict[str, Any]`
  - Get comprehensive portfolio summary
  - Includes total balance, account breakdown, by-type summary

##### Monitoring

- `get_status() -> Dict[str, Any]`
  - Get comprehensive system status
  - Returns FinancialStatus dataclass as dict

- `monitor_accounts(interval: int = 60) -> Dict[str, Any]`
  - Monitor all accounts continuously
  - Returns current status (for use in loops)

- `check_alerts() -> List[str]`
  - Check for alerts and issues
  - Returns list of alert messages

##### Trading Operations

- `get_positions(account_id: Optional[str] = None) -> Dict[str, Any]`
  - Get trading positions
  - Returns positions for all accounts or specific account

- `get_orders(account_id: Optional[str] = None) -> Dict[str, Any]`
  - Get open orders
  - Returns orders for all accounts or specific account

##### Data Operations

- `sync_all() -> Dict[str, Any]`
  - Synchronize all account data
  - Returns sync results with success/failure counts

- `import_copilot_data(csv_file: Path) -> Dict[str, Any]`
  - Import Copilot Money CSV data
  - Returns import results with statistics

##### Administrative

- `export_account_map(output_file: Optional[Path] = None) -> Path`
  - Export complete account map
  - Returns path to exported file

- `generate_report(report_type: str = "full") -> Dict[str, Any]`
  - Generate financial report
  - Types: 'full', 'summary', 'status'
  - Returns report dict with file path

## Data Structures

### `FinancialStatus`

```python
@dataclass
class FinancialStatus:
    timestamp: str
    total_accounts: int
    connected_accounts: int
    total_balance: float
    accounts: List[Dict[str, Any]]
    alerts: List[str]
    last_sync: Optional[str] = None
```

### Account Dictionary

```python
{
    "id": "account_id",
    "name": "Account Name",
    "type": "CRYPTO_EXCHANGE",
    "status": "CONNECTED",
    "balance": 1234.56,
    "currency": "USD",
    "last_check": "2026-01-15T23:00:00"
}
```

### Portfolio Summary

```python
{
    "generated_at": "2026-01-15T23:00:00",
    "total_accounts": 5,
    "connected_accounts": 4,
    "total_balance": 50000.00,
    "accounts": [...],
    "by_type": {
        "CRYPTO_EXCHANGE": {
            "count": 2,
            "balance": 30000.00
        },
        "TRADING_BOT": {
            "count": 1,
            "balance": 10000.00
        }
    }
}
```

## Error Handling

All methods return dictionaries with success/error information:

```python
{
    "success": True/False,
    "error": "Error message if failed",
    "data": {...}
}
```

## Integration Examples

### With Financial Agent Daemon

```python
from jarvis_financial_cli import JARVISFinancialCLI

cli = JARVISFinancialCLI()

# Get current status for daemon
status = cli.get_status()

# Check for alerts
alerts = cli.check_alerts()

# Sync all accounts
sync_result = cli.sync_all()
```

### With Dashboard

```python
from jarvis_financial_cli import JARVISFinancialCLI

cli = JARVISFinancialCLI()

# Get portfolio for dashboard
portfolio = cli.get_portfolio_summary()

# Get positions
positions = cli.get_positions()

# Generate report
report = cli.generate_report("full")
```

### Automated Monitoring

```python
import time
from jarvis_financial_cli import JARVISFinancialCLI

cli = JARVISFinancialCLI()

while True:
    status = cli.get_status()
    alerts = cli.check_alerts()
    
    if alerts:
        # Send notifications
        send_notifications(alerts)
    
    time.sleep(300)  # Check every 5 minutes
```
