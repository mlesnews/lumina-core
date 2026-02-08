# Friend or Foe Identification System
**Friendly/Green vs Enemy/Red Classification**

**Status:** ✅ **IFF SYSTEM ACTIVE**

## The System

**IFF (Identify Friend or Foe):**
- 🟢 **Green (FRIENDLY):** Safe, trusted, authorized
- 🔴 **Red (FOE):** Threat, malicious, unauthorized
- 🟡 **Yellow (UNKNOWN):** Unidentified, needs analysis
- ⚪ **Gray (NEUTRAL):** Neither friend nor foe

## Classification

### 🟢 Friendly (Green) - Trusted Entities

**Default Friendly List:**
- ✅ **JARVIS** - Trusted system, authorized operations
- ✅ **MARVIN** - Validation system, reality checks
- ✅ **@SECTEAM** - Authorized security operations
- ✅ **@SYPHON** - Authorized intelligence extraction

**Characteristics:**
- Safe, trusted, authorized
- Green classification
- High confidence
- On friendly list

### 🔴 Foe (Red) - Threat Entities

**Default Foe List:**
- ❌ **hardcoded_secrets** - Critical security threat
- ❌ **sql_injection** - Critical security threat
- ❌ **command_injection** - Critical security threat

**Characteristics:**
- Threat, malicious, unauthorized
- Red classification
- High confidence
- On foe list

## Integration

### With Pentest Violation Scanner

**Violation Classification:**
- Critical violations → 🔴 FOE (Red)
- High violations → 🔴 FOE (Red)
- Medium violations → 🟡 UNKNOWN (Yellow)
- Low violations → 🟢 FRIENDLY (Green) - if benign

### With @SECTEAM

**Entity Classification:**
- All tools classified as 🟢 FRIENDLY
- Security violations classified as 🔴 FOE
- Unknown entities → 🟡 UNKNOWN (needs analysis)

### With JARVIS/MARVIN

**System Classification:**
- JARVIS → 🟢 FRIENDLY (Green)
- MARVIN → 🟢 FRIENDLY (Green)
- Working hand in hand → 🟢 FRIENDLY (Green)

## Usage

### Identify Entity

```bash
python scripts/python/friend_foe_identification_system.py --identify "JARVIS"
```

**Output:**
- 🟢 FRIENDLY (green) - JARVIS
- 🔴 FOE (red) - sql_injection
- 🟡 UNKNOWN (yellow) - unknown_entity

### Add to Friendly List

```bash
python scripts/python/friend_foe_identification_system.py --add-friendly "ACE" --type "virtual_assistant" --reason "Combat assistant, authorized"
```

### Add to Foe List

```bash
python scripts/python/friend_foe_identification_system.py --add-foe "xss_vulnerability" --type "security_violation" --reason "High security threat"
```

### View Summary

```bash
python scripts/python/friend_foe_identification_system.py --summary
```

## Classification Rules

**Friendly Indicators:**
- authorized
- trusted
- validated
- safe
- approved

**Foe Indicators:**
- malicious
- unauthorized
- threat
- vulnerability
- exploit

## Context Analysis

**If entity not in lists:**
- Analyzes context for friendly/foe indicators
- Counts indicators to determine classification
- Medium confidence if context-based
- Low confidence if unknown

## The Color System

**🟢 Green (FRIENDLY):**
- Safe, trusted, authorized
- Positive classification
- High confidence
- On friendly list

**🔴 Red (FOE):**
- Threat, malicious, unauthorized
- Negative classification
- High confidence
- On foe list

**🟡 Yellow (UNKNOWN):**
- Unidentified, needs analysis
- Neutral classification
- Low confidence
- Not in lists

**⚪ Gray (NEUTRAL):**
- Neither friend nor foe
- Neutral classification
- Medium confidence
- Context-dependent

---

**Status:** ✅ **IFF SYSTEM ACTIVE**
**Green (FRIENDLY):** Safe, trusted, authorized
**Red (FOE):** Threat, malicious, unauthorized
**System:** Integrated with @SECTEAM, JARVIS, MARVIN, Pentest Scanner

**Friend or Foe identified. Green for friends. Red for foes. IFF system active. @BAL @DOIT @PEAK. @<3**
