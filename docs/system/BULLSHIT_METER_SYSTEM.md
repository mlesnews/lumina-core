# Bullshit Meter System - Reliability & Credibility Tracking

**Date**: 2025-01-27  
**Status**: ✅ **IMPLEMENTED**  
**Tag**: `#bullshitmeter`  
**Principle**: The Boy Who Cried Wolf

## Overview

The Bullshit Meter tracks claim accuracy and credibility over time. Based on "The Boy Who Cried Wolf" principle: credibility decreases with false claims, and repeated false alarms are filtered/hidden like spam in log files.

## Purpose

**Track when AI is bullshitting vs. telling the truth**

1. **Claim Tracking** - Record claims made by sources (AI, systems, etc.)
2. **Verification** - Track which claims were true/false
3. **Credibility Scoring** - Build reliability scores per source
4. **Spam Filtering** - Hide unreliable sources (like spam in log files)
5. **Prevent Fatigue** - Stop "crying wolf" from causing alert fatigue

## The Boy Who Cried Wolf Principle

From the fable:
- **First false alarm**: People still respond, but trust decreases
- **Multiple false alarms**: People stop responding (credibility lost)
- **Real emergency**: Nobody believes it (too late)

**Applied to Bullshit Meter**:
- Track false claims per source
- Decrease credibility score with each false claim
- Ignore/hide source after threshold (like spam)
- Exponential backoff for ignored sources

## Key Features

### 1. Claim Recording

Record claims with:
- Source (who made the claim)
- Claim text
- Claim type (statement, prediction, status, etc.)
- Initial confidence (based on source credibility)

### 2. Claim Verification

Verify claims as:
- **True** - Claim was accurate
- **False** - Claim was incorrect
- **Unverified** - Not yet checked

### 3. Credibility Scoring

Per-source credibility tracking:
- **Credibility Score** (0.0-1.0)
  - Starts at 0.5 (neutral)
  - Increases with true claims
  - Decreases with false claims (weighted by recency)
- **Accuracy Rate** - Percentage of verified claims that were true
- **Consecutive False Claims** - Counter for "crying wolf"

### 4. Spam Filtering (Like Log Files)

Sources that repeatedly make false claims:
- **Ignored** after threshold (default: 5 consecutive false claims)
- **Hidden** from results (like spam)
- **Exponential Backoff** - Ignore duration increases with violations
- **Auto-Recovery** - Can be trusted again after ignore period

### 5. Trust Decisions

`should_trust_source(source)` returns:
- **Should trust** (bool) - Whether to trust the source
- **Credibility score** (float) - Current reliability score

## Usage

### Record a Claim

```python
from bullshit_meter import BullshitMeter, ClaimType

meter = BullshitMeter()

claim_id = meter.record_claim(
    source="health_monitor",
    claim_text="All systems are healthy",
    claim_type=ClaimType.STATEMENT
)
```

### Verify a Claim

```python
# Later, verify the claim
meter.verify_claim(
    claim_id=claim_id,
    is_true=False,  # It was actually false!
    verified_by="user",
    notes="System was actually unhealthy"
)
```

### Check Source Credibility

```python
# Check if source should be trusted
should_trust, credibility = meter.should_trust_source("health_monitor")

if not should_trust:
    print(f"⚠️ Source ignored (like spam) - credibility: {credibility:.2f}")
else:
    print(f"✅ Source trusted - credibility: {credibility:.2f}")
```

### Filter Claims (Hide Unreliable)

```python
# Filter out unreliable sources (like spam filtering)
filtered_claims = meter.filter_claims(all_claims)
# Unreliable sources are marked as IGNORED and hidden
```

## Credibility Algorithm

### Score Calculation

1. **True Claim**: 
   - Increases credibility: `score += 0.1 / (total_claims / 10)`
   - Resets consecutive false claims counter

2. **False Claim**:
   - Decreases credibility: `score -= 0.2 * (1.0 + consecutive_false * 0.1)`
   - Increments consecutive false claims counter
   - Records timestamp of last false claim

3. **Ignore Threshold**:
   - After N consecutive false claims (default: 5), source is ignored
   - Ignore duration: `2^min(consecutive_false - threshold, 6)` hours
   - Source hidden from results (like spam)

## Data Persistence

- **Claims**: Stored in `data/bullshit_meter/claims.jsonl` (JSON Lines format)
- **Credibility**: Stored in `data/bullshit_meter/credibility.json`
- **State loaded** on initialization
- **State saved** after each verification

## Integration with Chat Metatagging

Tag: `#bullshitmeter`

Usage in chat:
- "Check #bullshitmeter for source credibility"
- "Track this claim in #bullshitmeter"
- "Filter unreliable claims using #bullshitmeter"

## Example Scenarios

### Scenario 1: AI Crying Wolf

```python
meter = BullshitMeter()

# AI makes 5 false health claims
for i in range(5):
    claim_id = meter.record_claim("health_ai", f"System healthy {i}")
    meter.verify_claim(claim_id, is_true=False)

# Check credibility
should_trust, cred = meter.should_trust_source("health_ai")
# should_trust = False (ignored like spam)
# cred < 0.3 (very low)
```

### Scenario 2: Reliable Source

```python
# Source makes mostly true claims
for i in range(10):
    claim_id = meter.record_claim("reliable_ai", f"Claim {i}")
    meter.verify_claim(claim_id, is_true=(i % 10 != 0))  # 90% true

# Check credibility
should_trust, cred = meter.should_trust_source("reliable_ai")
# should_trust = True
# cred > 0.7 (high credibility)
```

## Configuration

### Ignore Threshold

Default: 5 consecutive false claims before ignoring

Can be customized per source:
```python
source_cred = meter.get_source_credibility("source_name")
source_cred.ignore_threshold = 3  # Ignore after 3 false claims
```

### Trust Threshold

Default: 0.3 credibility score minimum to trust

## Benefits

1. **Prevent Alert Fatigue** - Filter out unreliable sources
2. **Build Trust** - Track which sources are reliable
3. **Improve Decision Making** - Know when to trust claims
4. **Spam-Like Filtering** - Hide unreliable sources automatically
5. **Self-Correction** - Sources can recover credibility over time

## The Boy Who Cried Wolf Lesson

**Applied to AI Systems**:
- **First false claim**: Still trust, but credibility decreases
- **Multiple false claims**: Stop trusting (ignore like spam)
- **Real claim from ignored source**: Might miss it (but source was unreliable)

**Solution**: Track credibility, filter unreliable sources, but allow recovery over time.

---

**Status**: ✅ Implemented  
**Location**: `scripts/python/bullshit_meter.py`  
**Tag**: `#bullshitmeter`  
**Principle**: The Boy Who Cried Wolf + Spam Filtering

