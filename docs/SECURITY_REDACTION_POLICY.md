# Security Redaction Policy

## 🔒 Critical Security Principle

**ALL sensitive information MUST be redacted from files, logs, and documentation.**

## Scope of Redaction

Redact ALL sensitive information including:
- **Customer data** - Any customer information, PII, or business data
- **Personal data** - Names, emails, phone numbers, addresses
- **Six degrees of separation** - Any data that could be connected to customers, partners, or associates
- **Credentials** - Passwords, API keys, tokens, recovery codes
- **Account information** - Account numbers, IDs, usernames
- **Financial data** - Payment information, billing details

## Storage Policy

**Sensitive information MUST ONLY be stored in:**
- ✅ Azure Key Vault (`jarvis-lumina.vault.azure.net`)
- ✅ ProtonPass (where applicable)

**Sensitive information MUST NEVER be stored in:**
- ❌ Plain text files
- ❌ JSON configuration files
- ❌ Documentation files
- ❌ Log files (beyond minimal verification)
- ❌ Code comments
- ❌ Version control (Git)
- ❌ Environment variables in files

## Redaction Format

When documenting sensitive information, use:
```
[REDACTED - Stored in Azure Vault]
[REDACTED - Stored in Azure Vault: secret-name]
```

For verification in logs, use minimal prefixes:
```
Code verification: N5JJ****[REDACTED - Full code stored securely]
Phone: +1****[REDACTED - Stored in Azure Vault]
```

## Examples

### ✅ Correct
```json
{
  "phone_number": "[REDACTED - Stored in Azure Vault: matt-lesnewski-mobile]",
  "email": "[REDACTED - Stored in Azure Vault]"
}
```

### ❌ Incorrect
```json
{
  "phone_number": "+13023593913",
  "email": "mlesnewski@gmail.com"
}
```

## Azure Vault Secret Naming

Use descriptive but non-sensitive names:
- `matt-lesnewski-mobile` - Phone number
- `twillo-recovery-code` - Recovery codes
- `proton-bridge-mlesn-password` - Credentials
- `[service]-[purpose]-[identifier]` format

## Enforcement

- All scripts must check for and redact sensitive data before logging
- Documentation must use `[REDACTED]` placeholders
- Code reviews must verify no sensitive data in files
- Automated scanning for potential leaks (MARVIN Secret Leak Detector)

## Recovery

If sensitive data is accidentally committed:
1. Immediately rotate/revoke the exposed credentials
2. Remove from Git history if possible
3. Update Azure Vault with new values
4. Document the incident

---

**This policy applies to ALL files, scripts, and documentation in the LUMINA project.**
