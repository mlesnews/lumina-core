# Copilot Money Integration

## Overview

Integration system for pulling data and information from **Copilot Money** (copilot.money), a personal finance budgeting app.

## Current Status

⚠️ **No Public API Available**: Copilot Money does not provide a public API for programmatic data access.

## Available Methods

### 1. CSV Export Parsing ✅

**Status**: Fully Implemented

Copilot Money allows manual export of all transactions as CSV from the app (iOS, iPadOS, macOS).

**CSV Fields Included**:
- `date` - Transaction date
- `name` - Transaction name/merchant
- `amount` - Transaction amount
- `pending/posted` - Status
- `category` - Transaction category
- `parent category` - Parent category
- `excluded` - Excluded flag
- `type` - Transaction type
- `account` - Account name
- `mask` - Account mask
- `notes` - Transaction notes
- `associated recurrings` - Recurring transaction info

**Usage**:
```bash
# Export CSV from Copilot Money app first, then:
python scripts/python/copilot_money_integration.py --import-csv <path_to_export.csv>
```

### 2. Browser Automation 🔄

**Status**: Planned (Not Yet Implemented)

If Copilot Money has a web interface, we can use MCP Browser tools to:
- Navigate to copilot.money
- Extract account balances
- Extract transactions
- Extract budgets and categories

**Implementation**: Would use `browser_navigate`, `browser_snapshot`, and data extraction from page elements.

### 3. Azure Direct Aggregator Integration ✅

**Status**: Fully Implemented - **RECOMMENDED**

Copilot Money uses these data aggregators:
- **Plaid** (primary)
- **Finicity** (Mastercard Open Banking)
- **MX**
- **Akoya**

**Azure Integration**: Direct integration with all aggregators using Azure services:
- ✅ **Azure Key Vault** - Secure credential storage
- ✅ **Azure Functions** - Webhook handling and API calls
- ✅ **API Management** - OAuth delegation and proxy
- ✅ **NAT Gateway** - Fixed IP for MX (if using MX)
- ✅ **Logic Apps** - Workflow automation

**Benefits over CSV Export**:
- ✅ Real-time data access (no manual export needed)
- ✅ Webhook support for live updates
- ✅ Same data sources Copilot Money uses
- ✅ Enterprise-grade Azure infrastructure
- ✅ Scalable and secure

**See**: `docs/azure_financial/README.md` for complete Azure integration guide.

**Direct OAuth Integrations** (also available):
- Apple Card
- Capital One
- Public
- Coinbase

## Limitations

1. **No API**: No programmatic access to live data
2. **Manual Export**: CSV export must be done manually in the app
3. **No Balances**: Account balances and holdings are NOT exportable via CSV
4. **No Automation**: No Zapier/Make/Shortcuts integration available

## Integration with LUMINA Financial System

The Copilot Money integration can be connected to:

1. **Financial Account Manager**: Add Copilot as a financial account source
2. **Financial Agent Daemon**: Include Copilot data in portfolio analysis
3. **Unified Dashboard**: Display Copilot transactions alongside other accounts

## Example Workflow

```python
from copilot_money_integration import CopilotMoneyIntegration

# Initialize
integration = CopilotMoneyIntegration()

# Import CSV export
result = integration.import_csv_export(Path("copilot_export.csv"))

# Access data
transactions = result["transactions"]
statistics = result["statistics"]

# Use in financial system
# ...
```

## Future Enhancements

1. **Automated CSV Processing**: Watch for new CSV exports
2. **Browser Automation**: Full web interface extraction
3. **Plaid Integration**: Direct access to underlying data
4. **Real-time Sync**: If Copilot adds API access

## Related Files

- `scripts/python/copilot_money_integration.py` - Main integration module
- `data/copilot_money/` - Imported data storage
- `docs/copilot_money/README.md` - This file

## References

- [Copilot Money Help: Exporting Data](https://help.copilot.money/en/articles/5944414-exporting-your-transaction-data)
- [Copilot Money: How We Get Your Data](https://help.copilot.money/en/articles/10768078-how-do-you-get-my-financial-data)
- [Copilot Money Privacy & Security](https://copilot.money/privacy-and-security/)
