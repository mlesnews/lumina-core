# SYPHON Financial Strategies with WOPR Pattern Matching

## Overview

The SYPHON Financial Strategies WOPR system extracts financial strategies from all sources using WOPR (WarGames) pattern matching and regex. It integrates with the Leroy Jenkins blacklist to prevent reckless trading behavior.

## Features

### 1. SYPHON Intelligence Extraction
- Scans all sources for financial strategies:
  - Documentation files
  - Code comments
  - Chat history
  - External sources (via SYPHON)
- Extracts actionable strategies with pattern matching

### 2. WOPR Pattern Matching
- Regex patterns for financial strategies:
  - DCA (Dollar Cost Averaging)
  - Swing Trading
  - Day Trading
  - Arbitrage
  - Staking/Yield
  - Options Trading
  - Dividend Stocks
  - ETFs
  - Risk Management (stop-loss, profit targets, position sizing)
  - Technical/Fundamental Analysis
  - Backtesting

### 3. Leroy Jenkins Blacklist
- Blacklist patterns:
  - All-in trades
  - YOLO moves
  - No stop-loss
  - Skip paper trading
  - Reckless behavior
- **Paper trading required before real money**

## Usage

### SYPHON All Sources

```python
from scripts.python.jarvis_syphon_financial_strategies_wopr import SyphonFinancialStrategiesWOPR

syphon = SyphonFinancialStrategiesWOPR()
results = syphon.syphon_all_sources()

# Results include:
# - Sources scanned
# - Strategies extracted
# - Patterns found
# - Blacklist checks
```

### WOPR Pattern Matching

```python
from scripts.python.jarvis_syphon_financial_strategies_wopr import WOPRPatternMatcher

wopr = WOPRPatternMatcher()
matches = wopr.match_patterns("DCA Bitcoin with stop-loss")
# Returns: {"dca": ["DCA"], "stop_loss": ["stop-loss"]}

strategy = wopr.extract_strategy("DCA Bitcoin with stop-loss")
# Returns: {
#   "strategy_type": "DCA",
#   "risk_level": "LOW",
#   "patterns_found": {...}
# }
```

### Blacklist Validation

```python
from scripts.python.jarvis_leroy_jenkins_blacklist import LeroyJenkinsBlacklist

blacklist = LeroyJenkinsBlacklist()

# Check text
result = blacklist.check_blacklist("YOLO all-in trade!")
# Returns: {"blacklisted": True, "action": "BLOCK"}

# Validate trade
trade_data = {
    "description": "DCA Bitcoin",
    "paper_trading": True,  # REQUIRED
    "stop_loss": True,
    "profit_target": True,
    "position_size_percent": 3
}

validation = blacklist.validate_trade(trade_data)
# Returns: {"valid": True, "action": "ALLOW"}
```

### Financial Execution with WOPR

```python
from scripts.python.jarvis_financial_execution_with_wopr_blacklist import JARVISFinancialExecutionWOPR

executor = JARVISFinancialExecutionWOPR()

trade_data = {
    "description": "DCA Bitcoin with stop-loss",
    "paper_trading": True,  # REQUIRED
    "stop_loss": True,
    "profit_target": True,
    "position_size_percent": 3
}

result = await executor.execute_with_wopr_validation(trade_data)
```

## Blacklist Rules

### Paper Trading Requirement
- **ALL trades must be paper traded first**
- Real money execution is blocked until paper trading is successful
- This prevents Leroy Jenkins behavior

### Blacklisted Content
- All-in trades
- YOLO moves
- No stop-loss
- Skip paper trading
- Reckless behavior
- Maximum leverage without risk management

### Position Size Limits
- Maximum 5% per trade
- Enforced by blacklist validation

## WOPR Patterns

### Strategy Patterns
- `dca`: Dollar Cost Averaging
- `swing_trading`: Swing Trading
- `day_trading`: Day Trading
- `arbitrage`: Arbitrage
- `staking`: Staking/Yield Farming
- `options`: Options Trading
- `dividend`: Dividend Stocks
- `etf`: Exchange Traded Funds

### Risk Management Patterns
- `stop_loss`: Stop Loss Orders
- `profit_target`: Profit Targets
- `position_sizing`: Position Sizing
- `risk_management`: Risk Management

### Analysis Patterns
- `technical_analysis`: Technical Analysis
- `fundamental_analysis`: Fundamental Analysis
- `backtesting`: Backtesting

## Integration

### With Financial Execution Plan
The WOPR system integrates with the calculated financial execution plan:
- Validates all trades against blacklist
- Matches patterns for strategy identification
- Enforces paper trading requirement
- Prevents Leroy Jenkins behavior

### With SYPHON System
- Uses SYPHON for intelligence extraction
- Extracts strategies from all sources
- Processes with WOPR pattern matching
- Stores results for future reference

## Output

Results are saved to:
```
data/syphon_financial_strategies/financial_strategies_YYYYMMDD_HHMMSS.json
```

Includes:
- Sources scanned
- Strategies extracted
- Patterns found
- Blacklist checks
- WOPR matches

## Example Output

```
Sources scanned: 3
Strategies extracted: 2,268
Patterns found: 10
Blacklist checks: 2,268
```

## Notes

- **Paper trading is MANDATORY** before real money
- Leroy Jenkins actions are **BLACKLISTED**
- WOPR pattern matching helps identify strategies
- All trades validated against blacklist
- Position size limits enforced (5% max)

## Tags

@JARVIS @SYPHON @FINANCIAL_STRATEGIES @WOPR @REGEX @PATTERN_MATCHING @BLACKLIST @PAPER_TRADING
