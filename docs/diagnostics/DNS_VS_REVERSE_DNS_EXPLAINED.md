# DNS vs Reverse DNS Explained

## Overview

**DNS (Forward DNS)** and **Reverse DNS (rDNS)** are related but serve different purposes:

### Forward DNS (What you're using now)
- **Purpose**: Resolves domain names → IP addresses
- **Example**: `google.com` → `142.251.45.206`
- **Query Type**: A records, AAAA records
- **Used by**: Browsers, applications, users

### Reverse DNS (rDNS)
- **Purpose**: Resolves IP addresses → domain names
- **Example**: `142.251.45.206` → `google.com`
- **Query Type**: PTR records
- **Used by**: Email servers (SPF/DKIM), security tools, logging

---

## Your Homelab Setup

### Current Configuration

**Primary DNS**: pfSense (10.17.17.1)
**Secondary DNS**: NAS (10.17.17.32)

### How It Works

When your computer needs to resolve a domain name:

1. **First**: Queries primary DNS (pfSense 10.17.17.1)
2. **If primary fails**: Queries secondary DNS (NAS 10.17.17.32)
3. **If both fail**: Falls back to system default (ProtonVPN 10.2.0.1)

### DNS Server Configuration

**Yes, you're correct**: If you run primary/secondary DNS locally on pfSense and NAS, you should use those as your DNS servers.

**Your current setup**:
- Wi-Fi adapter: Using `10.17.17.1` (pfSense) as DNS ✅ Correct
- The issue: DNS service on pfSense/NAS is not configured/working ❌

---

## Do You Need Reverse DNS?

### For Most Users: **No, not required**

Reverse DNS is typically needed for:
- **Email servers** (SPF/DKIM validation)
- **Security logging** (identifying sources)
- **Professional hosting** (some services require it)

### For Your Homelab: **Optional but recommended**

If you want to:
- Run email servers
- Have proper hostname resolution for internal IPs
- Professional setup

Then yes, set up reverse DNS.

### Reverse DNS Setup

**Same servers, different service**:
- Forward DNS and Reverse DNS can run on the same servers (pfSense/NAS)
- They're separate services but often bundled together
- pfSense DNS Resolver includes reverse DNS support
- NAS DNS service may or may not include reverse DNS

---

## Recommended Configuration

### Forward DNS (Required)
```
Primary DNS:   10.17.17.1  (pfSense)
Secondary DNS: 10.17.17.32 (NAS)
```

**Configuration needed**:
- Enable DNS service on both
- Configure upstream DNS (8.8.8.8, 1.1.1.1)
- Enable forwarding mode

### Reverse DNS (Optional)
```
Reverse DNS Zones:
- 10.17.17.0/24 → 17.17.10.in-addr.arpa
- Other internal subnets as needed
```

**Configuration needed**:
- Enable reverse DNS on pfSense DNS Resolver
- Configure PTR records for internal IPs
- Point reverse DNS queries to pfSense/NAS

---

## Current Issue

**Problem**: Your DNS servers (pfSense/NAS) are not responding to forward DNS queries.

**This affects**:
- ✅ Forward DNS (what you need for browsing)
- ❌ Reverse DNS (not the current issue, but would also fail if enabled)

**Fix**: Configure forward DNS first. Reverse DNS can be added later if needed.

---

## Summary

1. **Forward DNS (Primary/Secondary)**: 
   - ✅ Yes, use pfSense (10.17.17.1) and NAS (10.17.17.32) as your DNS servers
   - ✅ This is correct configuration
   - ❌ Currently not working - needs upstream DNS configured

2. **Reverse DNS**:
   - ⚠️ Optional - not required for basic browsing
   - ✅ Can run on same servers (pfSense/NAS)
   - ✅ Recommended for professional/email setups
   - ⚠️ Can be configured later after forward DNS is fixed

3. **Same "Server"**:
   - ✅ Yes, forward DNS and reverse DNS can run on the same physical servers
   - ✅ They're different services but often bundled together
   - ✅ pfSense DNS Resolver handles both

---

**Tags**: `#DNS` `#REVERSE_DNS` `#HOMELAB` `#PFSENSE` `#NAS` `#NETWORK`
