# Master Workflow Orchestrator - JARVIS Master Agent Coordination

**Status**: ✅ **OPERATIONAL**  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24

---

## Overview

Master workflow orchestrator system where:
1. **User makes asks** in master agent chat session
2. **System matches asks** to appropriate workflows (does NOT execute directly)
3. **Manages from master session** - All coordination happens in master
4. **Spawns new sub-sessions** for each ask
5. **Sub-agents managed by JARVIS** from master session
6. **Coordinates and delegates** based on:
   - Balance
   - Resource consumption
   - ROI (Return on Investment)
   - Costs per second
   - Profits

---

## Architecture

### Master Session Flow

```
User Ask
    ↓
Master Session (JARVIS)
    ├─→ Match to Workflows (does NOT execute)
    ├─→ Spawn Sub-Session
    ├─→ Delegate to Sub-Agent
    ├─→ Track Resources/ROI/Costs
    └─→ Coordinate All Sub-Sessions
    ↓
Sub-Session Execution
    ├─→ Execute Workflow
    ├─→ Track Resources
    ├─→ Calculate ROI
    └─→ Return Results
    ↓
Master Session Consolidation
    └─→ Aggregate Results
```

---

## Features

### Master Session Management

- ✅ **Single master session** - JARVIS coordinates everything
- ✅ **User asks** - Receive and process user requests
- ✅ **Workflow matching** - Match asks to workflows (no execution)
- ✅ **Sub-session spawning** - Create sub-sessions for each ask
- ✅ **Sub-agent management** - Manage all sub-agents from master

### Resource & ROI Tracking

- ✅ **Resource consumption** - CPU, memory, API calls, tokens, time, cost
- ✅ **ROI calculation** - Return on investment metrics
- ✅ **Cost per second** - Real-time cost tracking
- ✅ **Profit tracking** - Track profits from workflows
- ✅ **Balance management** - Track overall balance

### Coordination & Delegation

- ✅ **Balance-based** - Coordinate based on current balance
- ✅ **Resource-based** - Consider resource consumption
- ✅ **ROI-based** - Prioritize high-ROI workflows
- ✅ **Cost-based** - Optimize costs per second
- ✅ **Profit-based** - Maximize profits

### Trading Platform Integrations

- ✅ **3Commas** - Crypto trading platform
- ✅ **TradingView** - Charting and analysis
- ✅ **Fidelity Investments** - Personal brokerage
- ✅ **Arbitrage System** - Cross-platform arbitrage

---

## Usage

### Basic Usage

```python
from master_workflow_orchestrator import MasterWorkflowOrchestrator

# Initialize orchestrator
orchestrator = MasterWorkflowOrchestrator()

# Receive user ask (does NOT execute)
ask_id = orchestrator.receive_user_ask(
    "Complete the Lumina extension",
    priority=8
)

# Get workflow matches
matches = orchestrator.get_workflow_matches_for_ask(ask_id)

# Spawn sub-session for best match
if matches:
    sub_session_id = orchestrator.spawn_sub_session(ask_id, matches[0])
    
    # Start sub-session
    orchestrator.start_sub_session(sub_session_id)
    
    # Execute workflow (in sub-session)
    # ... workflow execution ...
    
    # Complete sub-session
    orchestrator.complete_sub_session(
        sub_session_id,
        success=True,
        result={"value": 100.0}
    )

# Coordinate all sub-sessions
coordination = orchestrator.coordinate_sub_sessions()
```

---

## Sub-Session Management

### Sub-Session Lifecycle

1. **PENDING** - Created but not started
2. **RUNNING** - Currently executing
3. **COMPLETED** - Successfully completed
4. **FAILED** - Failed execution
5. **CANCELLED** - Cancelled by JARVIS

### Sub-Session Tracking

- Resource consumption
- ROI metrics
- Balance impact
- Profit calculation
- Cost per second

---

## Resource & ROI Tracking

### Resource Types

- **CPU** - CPU usage
- **Memory** - Memory consumption
- **API Calls** - API call count
- **Tokens** - AI token usage
- **Time** - Execution time
- **Cost** - Financial cost

### ROI Metrics

- **Investment Cost** - Cost to run workflow
- **Return Value** - Value returned
- **ROI Percentage** - (return - cost) / cost * 100
- **Profit** - return - cost
- **Cost Per Second** - cost / execution_time

---

## Trading Platform Integrations

### 3Commas Integration

**Purpose**: Crypto trading platform

**Features**:
- Get accounts
- Get market prices
- Place orders (crypto)

**Configuration**: `config/trading_accounts.json`

### TradingView Integration

**Purpose**: Charting and market analysis

**Features**:
- Get market prices
- Technical indicators
- Market analysis

**Configuration**: `config/trading_accounts.json`

### Fidelity Integration

**Purpose**: Personal brokerage

**Features**:
- Get accounts
- Get market prices
- Place orders (stocks, ETFs, etc.)

**Configuration**: `config/trading_accounts.json`

---

## Arbitrage System

### Arbitrage Opportunities

The system scans for arbitrage opportunities across:
- 3Commas (crypto)
- TradingView (analysis)
- Fidelity (traditional)

### Arbitrage Execution

1. **Scan opportunities** - Find price differences
2. **Calculate profit** - Estimate profit percentage
3. **Risk assessment** - Calculate risk score
4. **Execute trades** - Buy low, sell high
5. **Track results** - Monitor profit/loss

### Risk Management

- Risk score calculation (0-1, lower is riskier)
- Platform risk assessment
- Price spread analysis
- Execution risk mitigation

---

## Personal Hedge Fund/Bank

### Capabilities

- **Arbitrage Trading** - Cross-platform arbitrage
- **Portfolio Management** - Track assets across platforms
- **Risk Management** - Automated risk assessment
- **Profit Optimization** - Maximize ROI
- **Balance Tracking** - Real-time balance monitoring

### Integration Points

- Master Workflow Orchestrator
- Trading Platform Integrations
- Arbitrage System
- Resource/ROI Tracking

---

## Configuration

### Trading Accounts

**File**: `config/trading_accounts.json`

```json
{
  "accounts": [
    {
      "account_id": "3commas_main",
      "platform": "3commas",
      "api_key": "...",
      "api_secret": "...",
      "enabled": true
    }
  ]
}
```

---

## API Reference

### MasterWorkflowOrchestrator

#### Methods

- `receive_user_ask(ask_text: str, user_id: str, priority: int) -> str`
- `get_workflow_matches_for_ask(ask_id: str) -> List[WorkflowMatch]`
- `spawn_sub_session(ask_id: str, workflow_match: WorkflowMatch) -> str`
- `start_sub_session(sub_session_id: str) -> bool`
- `complete_sub_session(sub_session_id: str, success: bool, result: Dict) -> bool`
- `coordinate_sub_sessions() -> Dict[str, Any]`
- `get_sub_session_status(sub_session_id: str) -> Optional[Dict[str, Any]]`
- `get_orchestrator_summary() -> Dict[str, Any]`

---

## Examples

### Example 1: Receive Ask and Match Workflows

```python
# Receive user ask
ask_id = orchestrator.receive_user_ask(
    "Build a new feature",
    priority=7
)

# Get matches
matches = orchestrator.get_workflow_matches_for_ask(ask_id)

# Review matches
for match in matches:
    print(f"Workflow: {match.workflow_name}")
    print(f"Confidence: {match.confidence}")
    print(f"Estimated Cost: ${match.estimated_cost:.2f}")
    print(f"Estimated Time: {match.estimated_time:.2f}s")
```

### Example 2: Spawn and Execute Sub-Session

```python
# Spawn sub-session
sub_session_id = orchestrator.spawn_sub_session(ask_id, matches[0])

# Start execution
orchestrator.start_sub_session(sub_session_id)

# Execute workflow (in sub-session context)
# ... workflow code ...

# Complete with results
orchestrator.complete_sub_session(
    sub_session_id,
    success=True,
    result={"value": 500.0, "output": "Feature built"}
)
```

### Example 3: Coordinate Sub-Sessions

```python
# Coordinate all sub-sessions
coordination = orchestrator.coordinate_sub_sessions()

print(f"Balance: ${coordination['total_balance']:.2f}")
print(f"Profit: ${coordination['total_profit']:.2f}")
print(f"Cost: ${coordination['total_cost']:.2f}")

# Review recommendations
for rec in coordination['recommendations']:
    print(f"{rec['type']}: {rec['message']}")
    print(f"Action: {rec['action']}")
```

### Example 4: Arbitrage Trading

```python
# Initialize arbitrage system
arbitrage = ArbitrageSystem()

# Initialize platforms
accounts = [
    TradingAccount(
        account_id="3commas_1",
        platform=TradingPlatform.THREECOMMAS,
        api_key=os.getenv("3COMMAS_API_KEY"),
        api_secret=os.getenv("3COMMAS_API_SECRET"),
        enabled=True
    ),
    TradingAccount(
        account_id="fidelity_1",
        platform=TradingPlatform.FIDELITY,
        access_token=os.getenv("FIDELITY_ACCESS_TOKEN"),
        enabled=True
    )
]

arbitrage.initialize_platforms(accounts)

# Scan for opportunities
opportunities = arbitrage.scan_arbitrage_opportunities(
    symbols=["BTCUSDT", "ETHUSDT"],
    min_profit_percentage=0.5
)

# Execute best opportunity
if opportunities:
    result = arbitrage.execute_arbitrage(opportunities[0])
    print(f"Arbitrage executed: {result['success']}")
    print(f"Profit: ${result['estimated_profit']:.2f}")
```

---

## Best Practices

1. **Always use master session** - All coordination through master
2. **Match before executing** - Never execute directly from ask
3. **Track resources** - Monitor all resource consumption
4. **Calculate ROI** - Always track ROI for workflows
5. **Coordinate regularly** - Run coordination frequently
6. **Optimize costs** - Minimize costs per second
7. **Maximize profits** - Prioritize high-profit workflows

---

## Related Documentation

- [Master Session Manager](./MASTER_SESSION_MANAGER.md)
- [WOPR Workflow Pattern Mapping](./WOPR_CORE_WORKFLOW_PATTERN_MAPPING.md)
- [Trading Platform Integrations](./TRADING_PLATFORM_INTEGRATIONS.md)

---

**Status**: ✅ **OPERATIONAL**  
**Last Updated**: 2025-01-24

