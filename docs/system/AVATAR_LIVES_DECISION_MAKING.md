# Avatar Lives & Decision-Making System

## Overview

Each avatar has **x3 lives** and during duels, their overall losses determine the victors of any debates escalated to combat **#decisioning**. Avatars dynamically react to problems or areas of interest related to particular alerts, **@triage**, and **@bau**.

## Avatar Lives System

### Lives Per Avatar
- **Maximum Lives**: 3 per avatar
- **Lives Tracking**: Each persona (JARVIS, FRIDAY, EDITH, ULTIMATE) has independent lives
- **Life Loss**: When avatar health reaches 0 in combat
- **Elimination**: When lives reach 0, avatar is eliminated

### Life Management
- **Initialization**: All avatars start with 3 lives
- **Defeat**: Lose 1 life when health reaches 0
- **Resurrection**: Automatically resurrected with full health after defeat
- **Elimination**: When lives reach 0, avatar cannot continue

## Win/Loss Tracking

### Victory Conditions
- **Defeat Entity**: When player defeats any entity (monster, elite, champion, boss)
- **Win Count**: Incremented for each victory
- **Duel Record**: Stored with timestamp, opponent, outcome

### Defeat Conditions
- **Health Depletion**: When player health reaches 0
- **Loss Count**: Incremented for each defeat
- **Life Loss**: One life deducted per defeat

### Statistics
- **Wins**: Total victories per avatar
- **Losses**: Total defeats per avatar
- **Win Rate**: Wins / (Wins + Losses) * 100%
- **Lives Remaining**: Current lives / Maximum lives

## Decision-Making System (#decisioning)

### Combat Escalation
- **Debates**: Can escalate to combat mode
- **Combat Outcomes**: Determine decision victors
- **Overall Losses**: Primary factor in determining victor

### Decision Logic
1. **Track Duels**: All combat encounters recorded
2. **Calculate Stats**: Win/loss ratios per avatar
3. **Determine Victor**: Lowest losses + highest win rate
4. **Decision Trigger**: After every 5 duels, recalculate victor

### Victor Determination
```python
victor = min(persona_stats.items(), 
           key=lambda x: (x[1]["losses"], -x[1]["win_rate"]))
```

**Criteria** (in order):
1. **Lowest Losses**: Avatar with fewest defeats
2. **Highest Win Rate**: Avatar with best win/loss ratio
3. **Most Lives**: Avatar with most lives remaining

### Decision Announcements
- **Victory Declaration**: "🏆 DECISION: [Avatar] is VICTOR"
- **Statistics**: W/L ratio and lives remaining
- **Logging**: All decisions logged with #decisioning tag

## Dynamic Alert/Triage/BAU Reaction System

### Alert Monitoring
- **Unified Queue Connection**: Connects to UnifiedQueueAdapter
- **Real-time Updates**: Checks every 60 frames (~1 second)
- **Alert Types**: ALERT, PROBLEM, TASK, NOTIFICATION

### Alert Categories

#### 🚨 Critical Alerts
- **Priority**: ≤ 3
- **Reaction**: Immediate combat mode activation
- **Message**: "🚨 ALERT: [title]..."
- **Action**: Triggers combat mode if not already active

#### ⚠️ High-Priority Problems
- **Priority**: ≤ 4
- **Reaction**: Display problem with severity
- **Message**: "⚠️ PROBLEM: [title]... [severity]"
- **Action**: Logs problem for avatar awareness

#### 🔴 Triage Items
- **Priority**: Critical triage
- **Reaction**: Critical attention notification
- **Message**: "🔴 TRIAGE: Critical item requires attention"
- **Action**: Highlights critical triage items

#### 📋 BAU Items
- **Priority**: ≥ 7 (low priority)
- **Reaction**: Batch notification when > 5 items
- **Message**: "📋 BAU: [count] items pending"
- **Action**: Notes BAU items for later processing

### Reaction Logic
1. **Update Queue**: Fetch latest alerts/problems/BAU items
2. **Filter by Priority**: Categorize by priority level
3. **React Dynamically**: Avatar responds based on alert type
4. **Combat Escalation**: Critical alerts trigger combat mode

## Integration Points

### With Unified Queue Adapter
- **Connection**: Automatic connection on initialization
- **Queue Items**: Monitors all queue item types
- **Status Updates**: Tracks item status changes
- **Metadata**: Extracts triage priorities from metadata

### With Combat System
- **Combat Mode**: Triggered by critical alerts
- **Entity Defeat**: Tracks wins for decision-making
- **Avatar Defeat**: Tracks losses and life loss
- **Duel Records**: All combat outcomes stored

### With Triage System
- **Triage Priorities**: Extracted from queue item metadata
- **Critical Triage**: Triggers immediate reactions
- **BAU Items**: Monitored but lower priority

## Visual Display

### Lives Indicator
- **Location**: Bottom left of screen
- **Color Coding**:
  - Green: > 1 life remaining
  - Yellow: 1 life remaining
  - Red: 0 lives (eliminated)
- **Format**: "Lives: X/3"

### Win/Loss Display
- **Location**: Below lives indicator
- **Format**: "W:X L:Y"
- **Color**: White text

### Alert Messages
- **Chatbot Display**: Alerts shown in chatbot-style messages
- **Color Coding**: Based on alert type (red for critical, yellow for warnings)
- **Attention**: Sound and VFX alerts for critical items

## Controls

### Stats Display
- **S Key**: Show avatar stats (lives, wins, losses, win rate)

### Automatic Reactions
- **No Manual Control**: Reactions are automatic based on alerts
- **Combat Mode**: Auto-activated for critical alerts

## Decision-Making Flow

1. **Combat Occurs**: Avatar engages in combat
2. **Outcome Recorded**: Win or loss tracked
3. **Life Management**: Lives adjusted on defeat
4. **Duel History**: All duels stored with metadata
5. **Decision Check**: After every 5 duels, calculate victor
6. **Victor Declared**: Avatar with best record declared victor
7. **Decision Logged**: All decisions logged with #decisioning tag

## Example Scenarios

### Scenario 1: Critical Alert
```
Alert: "System Overload Detected" (Priority: 2)
→ Avatar: "🚨 ALERT: System Overload Detected..."
→ Action: Combat mode activated
→ Avatar engages in combat to resolve issue
```

### Scenario 2: Debate Escalation
```
Debate: JARVIS vs FRIDAY on system architecture
→ Escalated to combat
→ JARVIS: 2 wins, 1 loss, 2 lives
→ FRIDAY: 1 win, 2 losses, 1 life
→ Decision: JARVIS declared victor (lower losses)
```

### Scenario 3: Triage Item
```
Triage: "Database Connection Critical" (Priority: critical)
→ Avatar: "🔴 TRIAGE: Critical item requires attention"
→ Action: Avatar focuses on triage item
```

### Scenario 4: BAU Accumulation
```
BAU Items: 8 pending items (Priority: 7-10)
→ Avatar: "📋 BAU: 8 items pending"
→ Action: Avatar notes for later processing
```

## Status

✅ **COMPLETE** - Full avatar lives and decision-making system

Features:
- ✅ x3 lives per avatar
- ✅ Win/loss tracking
- ✅ Decision-making based on combat outcomes
- ✅ Dynamic reactions to alerts/triage/BAU
- ✅ Unified queue integration
- ✅ Visual lives/wins/losses display
- ✅ Automatic combat escalation for critical alerts

---

**Tags**: @LIVES @DECISIONING @TRIAGE @BAU @ALERTS @COMBAT @AVATARS @DUELS
