# Leroy Jenkins Blacklist & Paper Trading Requirement

## Overview

The Leroy Jenkins Blacklist system prevents reckless trading behavior by enforcing strict rules:
- **Paper trading is MANDATORY before real money**
- All-in trades are BLACKLISTED
- YOLO moves are BLACKLISTED
- No risk management is BLACKLISTED

## Blacklist Rules

### Paper Trading Requirement
- **ALL trades must be paper traded first**
- Real money execution is **BLOCKED** until paper trading is successful
- This prevents Leroy Jenkins behavior

### Blacklisted Content
The following patterns are automatically blocked:
- All-in trades
- YOLO moves
- No stop-loss
- Skip paper trading
- Reckless behavior
- Maximum leverage without risk management
- "Fuck it, send it" mentality
- "Let it ride" without risk management

### Position Size Limits
- Maximum 5% per trade
- Enforced by blacklist validation
- Prevents over-leveraging

## Usage

### Validate Trade

```python
from scripts.python.jarvis_leroy_jenkins_blacklist import LeroyJenkinsBlacklist

blacklist = LeroyJenkinsBlacklist()

trade_data = {
    "description": "DCA Bitcoin with stop-loss",
    "paper_trading": True,  # REQUIRED
    "stop_loss": True,
    "profit_target": True,
    "position_size_percent": 3
}

validation = blacklist.validate_trade(trade_data)
# Returns: {"valid": True, "action": "ALLOW"}
```

### Check Blacklist

```python
# Check if text contains blacklisted content
result = blacklist.check_blacklist("YOLO all-in trade!")
# Returns: {"blacklisted": True, "action": "BLOCK"}
```

## Integration

### With Financial Execution
All trades are validated against the blacklist before execution:
- Paper trading check
- Blacklist content check
- Risk management check
- Position size check

### With WOPR Pattern Matching
The blacklist works with WOPR to identify risky patterns:
- Detects Leroy Jenkins behavior
- Blocks reckless trades
- Enforces paper trading

## Blacklist Storage

Blacklisted content is stored in:
```
data/leroy_jenkins_blacklist.json
```

Includes:
- Blacklisted content
- Blacklisted actions
- Paper trading requirement flag
- Last updated timestamp

## Example Validation

### ✅ ALLOWED Trade
```python
{
    "description": "DCA Bitcoin with stop-loss",
    "paper_trading": True,  # ✅ Paper trading enabled
    "stop_loss": True,      # ✅ Risk management
    "profit_target": True,  # ✅ Profit target
    "position_size_percent": 3  # ✅ Within 5% limit
}
```
**Result**: `{"valid": True, "action": "ALLOW"}`

### ❌ BLOCKED Trade (No Paper Trading)
```python
{
    "description": "DCA Bitcoin",
    "paper_trading": False,  # ❌ Paper trading required
    "stop_loss": True,
    "profit_target": True,
    "position_size_percent": 3
}
```
**Result**: `{"valid": False, "reason": "Paper trading required before real money", "action": "BLOCK"}`

### ❌ BLOCKED Trade (Leroy Jenkins)
```python
{
    "description": "YOLO all-in Bitcoin!",
    "paper_trading": True,
    "stop_loss": False,  # ❌ No risk management
    "position_size_percent": 10  # ❌ Exceeds 5% limit
}
```
**Result**: `{"valid": False, "reason": "Leroy Jenkins behavior detected", "action": "BLOCK"}`

## Notes

- **Paper trading is MANDATORY** - No exceptions
- Leroy Jenkins actions are **BLACKLISTED** - No exceptions
- Position size limits enforced (5% max)
- Risk management required (stop-loss, profit target)
- All trades validated before execution

## Tags

@JARVIS @BLACKLIST @LEROY_JENKINS @PAPER_TRADING @REAL_MONEY @RISK_MANAGEMENT
