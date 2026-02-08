# Memory Plus Rating System

**Date**: 2026-01-02  
**Status**: ✅ ACTIVE  
**Priority**: +++++ (CRITICAL - Always Use)

## Overview

The Plus Rating System (+, ++, +++, ++++, +++++) is used to indicate importance, urgency, and warning levels for memory items, alerts, and system priorities.

## Rating Scale

### + (One Plus) - LOW
- **Importance**: Low priority
- **Urgency**: Non-urgent
- **Warning Level**: Info/Notice
- **Use Case**: General information, nice-to-have features, optional enhancements
- **Example**: "Consider optimizing X in the future"

### ++ (Two Plus) - MEDIUM-LOW  
- **Importance**: Medium-low priority
- **Urgency**: Low urgency
- **Warning Level**: Minor notice
- **Use Case**: Minor improvements, low-impact items
- **Example**: "Feature Y could be enhanced"

### +++ (Three Plus) - MEDIUM
- **Importance**: Medium priority
- **Urgency**: Moderate urgency
- **Warning Level**: Attention recommended
- **Use Case**: Important features, should be addressed
- **Example**: "Feature Z should be implemented"

### ++++ (Four Plus) - HIGH
- **Importance**: High priority
- **Urgency**: High urgency
- **Warning Level**: ⚠️ WARNING - Action Required
- **Use Case**: Critical features, must be addressed soon
- **Example**: "Security issue needs immediate attention"

### +++++ (Five Plus) - CRITICAL/URGENT
- **Importance**: CRITICAL priority
- **Urgency**: URGENT - Immediate action required
- **Warning Level**: 🔴 RED FLAG - Critical Alert
- **Use Case**: Critical issues, security vulnerabilities, system failures
- **Example**: "ALWAYS use Azure Key Vault credentials - NEVER hardcode passwords"

## Warning System Integration

The number of pluses serves as a **red flag warning system**:

- **+ to ++**: Informational, no immediate action needed
- **+++**: Attention recommended, plan to address
- **++++**: ⚠️ WARNING - Action required, prioritize
- **+++++**: 🔴 RED FLAG - Critical/Urgent, immediate action required

## Usage Guidelines

### When to Use Each Level

**+ (One Plus)**:
- Documentation notes
- Future enhancements
- Optional features
- General reminders

**++ (Two Plus)**:
- Minor improvements
- Low-priority bugs
- Nice-to-have features

**+++ (Three Plus)**:
- Standard priority items
- Features to implement
- Issues to address

**++++ (Four Plus)**:
- High-priority bugs
- Important security items
- Critical features
- System optimizations

**+++++ (Five Plus)**:
- Security vulnerabilities
- System-critical issues
- Always/Never rules
- Credential management
- Data protection rules

### Examples in Context

```markdown
# ALWAYS use Azure Key Vault credentials +++++
# Never hardcode passwords +++++
# Security: Always validate inputs ++++
# Performance: Consider optimizing X ++
# Enhancement: Feature Y could be improved +
```

## Memory Integration

When creating memories or documentation:

1. **Use pluses to indicate priority**: Add appropriate pluses to memory titles/content
2. **Red flag system**: More pluses = higher warning level
3. **Actionable items**: Items with ++++ or +++++ require action
4. **Always rules**: Critical rules should be +++++

## Current Critical Rules (+++++)

1. **ALWAYS use Azure Key Vault credentials** +++++
   - Never hardcode passwords
   - Always retrieve from Azure Key Vault
   - Applies to all scripts and integrations

2. **NAS credentials** +++++
   - Always use Azure Key Vault for NAS credentials
   - Never store passwords in code or config files
   - Use `NASAzureVaultIntegration` class

3. **Security best practices** +++++
   - Never commit secrets to git
   - Always use environment variables or Azure Key Vault
   - Validate all inputs

---

**Last Updated**: 2026-01-02  
**Maintained By**: JARVIS System
