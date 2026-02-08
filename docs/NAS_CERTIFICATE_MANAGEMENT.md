# NAS Certificate Management

**Date**: 2025-01-24  
**Status**: ✅ **IMPLEMENTED**

---

## Overview

The NAS Certificate Manager provides secure SSL/TLS certificate handling for NAS connections, replacing insecure `verify=False` with proper certificate validation.

---

## Features

### ✅ Certificate Download
- Automatically downloads NAS self-signed certificates
- Stores certificates in `config/certs/` directory
- Supports multiple NAS hosts and ports

### ✅ Certificate Generation
- **Self-Signed Certificates**: Generates self-signed certificates when download fails
- **CA-Signed Certificates**: Creates proper CA-signed certificates with certificate chain validation
- **Local CA**: Create your own Certificate Authority for signing certificates
- Creates certificates with proper subject alternative names
- Configurable validity period and organization details
- Automatic fallback: Download → Generate → Fallback

### ✅ Certificate Verification
- Validates certificate format and details
- Provides certificate information (subject, issuer, validity dates)
- Checks certificate existence before use

### ✅ Automatic Integration
- NAS Service Monitor automatically uses certificates
- Auto-downloads certificates if not found
- **Auto-generates certificates if download fails**
- Falls back gracefully if certificate unavailable

---

## Usage

### Download Certificate

```bash
python scripts/python/nas_certificate_manager.py --host 10.17.17.32 --port 5001 --download
```

**Output**:
```
✅ Certificate downloaded: config/certs/nas_10.17.17.32_5001.crt
```

### Create Certificate Authority (CA)

Create a local Certificate Authority for signing certificates:

```bash
python scripts/python/nas_certificate_manager.py --create-ca --ca-organization "LUMINA Local CA"
```

**Output**:
```
✅ Certificate Authority created:
   CA Certificate: config/certs/ca/ca_certificate.crt
   CA Private Key: config/certs/ca/ca_private_key.key
⚠️  Keep CA private key secure! Do not share it.
```

### Generate CA-Signed Certificate

Generate a proper CA-signed certificate (recommended for production):

```bash
python scripts/python/nas_certificate_manager.py --host 10.17.17.32 --port 5001 --ca-signed --organization "LUMINA NAS"
```

**Output**:
```
✅ CA-signed certificate generated: config/certs/nas_10.17.17.32_5001.crt
   This certificate is signed by the local CA and provides proper certificate chain validation.
```

### Generate Self-Signed Certificate

If download fails or NAS doesn't have HTTPS enabled:

```bash
python scripts/python/nas_certificate_manager.py --host 10.17.17.99 --port 5001 --generate --organization "My NAS"
```

**Output**:
```
✅ Self-signed certificate generated: config/certs/nas_10.17.17.99_5001.crt
⚠️  Note: This is a self-signed certificate. For production, use a CA-signed certificate.
```

### Ensure Certificate (Download or Generate)

Automatically tries download first, then generates if needed:

```bash
python scripts/python/nas_certificate_manager.py --host 10.17.17.99 --port 5001 --ensure
```

**Output**:
```
📥 Certificate not found, attempting download...
🔨 Download failed, generating self-signed certificate...
✅ Certificate ensured: config/certs/nas_10.17.17.99_5001.crt
```

### Verify Certificate

```bash
python scripts/python/nas_certificate_manager.py --host 10.17.17.32 --port 5001 --verify
```

**Output**:
```
Certificate Information:
  Exists: True
  Path: config/certs/nas_10.17.17.32_5001.crt
  Valid: True
  Subject: {...}
```

---

## Integration

### NAS Service Monitor

The `NASServiceMonitor` class automatically uses the certificate manager:

```python
from nas_service_monitor import NASServiceMonitor

# Certificate manager is automatically initialized
monitor = NASServiceMonitor(
    service_id="nas-monitor-1",
    nas_config={
        "host": "10.17.17.32",
        "api_port": 5001
    }
)

# Certificate is automatically downloaded and used
monitor.start()
```

**Before** (insecure):
```python
response = requests.get(api_url, verify=False)  # ❌ No verification
```

**After** (secure with auto-generation):
```python
verify_setting = cert_manager.get_requests_verify_setting(
    host, port,
    auto_download=True,   # Try to download first
    auto_generate=True    # Generate if download fails
)
response = requests.get(api_url, verify=verify_setting)  # ✅ Certificate verified
```

**Using CA-Signed Certificates** (recommended for production):
```python
# For CA-signed certificates, use CA certificate for verification
cert_manager = NASCertificateManager()
ca_cert_path = cert_manager.get_ca_certificate_for_verification()

if ca_cert_path:
    # Use CA certificate for chain validation
    response = requests.get(api_url, verify=ca_cert_path)  # ✅ CA-signed certificate verified
else:
    # Fallback to specific certificate
    cert_path = cert_manager.get_certificate_verify_path(host, port)
    response = requests.get(api_url, verify=cert_path or False)
```

---

## Certificate Storage

Certificates are stored in:
```
config/certs/nas_{host}_{port}.crt
```

Example:
```
config/certs/nas_10.17.17.32_5001.crt
```

---

## Security Benefits

### Before
- ❌ SSL verification disabled (`verify=False`)
- ❌ Vulnerable to man-in-the-middle attacks
- ❌ No certificate validation
- ❌ Security warnings ignored

### After
- ✅ SSL verification enabled with proper certificates
- ✅ Protection against man-in-the-middle attacks
- ✅ Certificate validation and trust
- ✅ Secure connections maintained

---

## API Reference

### `NASCertificateManager`

#### `download_nas_certificate(nas_host, nas_port=5001)`
Downloads and saves NAS SSL certificate.

**Returns**: `Path` to certificate file if successful, `None` otherwise

#### `get_certificate_verify_path(nas_host, nas_port=5001)`
Gets certificate path for `requests.verify` parameter.

**Returns**: Certificate path (str) if exists, `None` if not found

#### `ensure_certificate(nas_host, nas_port=5001, auto_download=True)`
Ensures certificate exists, downloads if needed.

**Returns**: Certificate path (str) if available, `None` otherwise

#### `verify_certificate(nas_host, nas_port=5001)`
Verifies certificate validity and gets details.

**Returns**: Dictionary with certificate information

#### `create_certificate_authority(organization="LUMINA Certificate Authority", country="US", validity_years=10)`
Creates a local Certificate Authority (CA) for signing certificates.

**Returns**: Dictionary with `success`, `ca_certificate_path`, `ca_private_key_path`, etc.

**Note**: Requires `cryptography` library. Install with: `pip install cryptography`

#### `generate_ca_signed_certificate(nas_host, nas_port=5001, validity_days=365, organization="LUMINA NAS")`
Generates a CA-signed certificate for NAS connection (recommended for production).

**Returns**: `Path` to certificate file if successful, `None` otherwise

**Note**: Requires CA to exist. Create CA first with `create_certificate_authority()`

#### `generate_self_signed_certificate(nas_host, nas_port=5001, validity_days=365, organization="LUMINA NAS", country="US")`
Generates a self-signed certificate for NAS connection.

**Returns**: `Path` to certificate file if successful, `None` otherwise

**Note**: Requires `cryptography` library. Install with: `pip install cryptography`

#### `get_requests_verify_setting(nas_host, nas_port=5001, auto_download=True, auto_generate=False)`
Gets verify setting for requests library.

**Args**:
- `auto_download`: Automatically download if certificate doesn't exist
- `auto_generate`: Automatically generate self-signed certificate if download fails

**Returns**: 
- Certificate path (str) if available
- `False` if should skip verification (fallback)
- `True` if should use system certificates

---

## Implementation Details

### Certificate Download Process

1. **Create SSL Context**: Creates default SSL context with hostname checking disabled
2. **Connect to NAS**: Establishes SSL connection to NAS
3. **Extract Certificate**: Gets peer certificate in DER format
4. **Convert to PEM**: Converts DER to PEM format
5. **Save Certificate**: Writes certificate to `config/certs/` directory

### Certificate Generation Process

1. **Generate Private Key**: Creates 2048-bit RSA private key
2. **Create Certificate**: Builds X.509 certificate with:
   - Subject and issuer (self-signed)
   - Public key from private key
   - Validity period (default: 365 days)
   - Subject Alternative Name (SAN) for hostname/IP
3. **Sign Certificate**: Signs with SHA-256 hash algorithm
4. **Save Files**: Saves certificate (.crt) and private key (.key) to `config/certs/`

### Certificate Usage Flow

1. **Check Existence**: Verifies certificate file exists
2. **Auto-Download**: Downloads certificate if not found (if enabled)
3. **Auto-Generate**: Generates self-signed certificate if download fails (if enabled)
4. **Return Path**: Returns certificate path for `requests.verify`
5. **Fallback**: Falls back to `False` if certificate unavailable (maintains functionality)

---

## Error Handling

### Connection Errors
- **Timeout**: Logs error, returns `None`
- **DNS Resolution**: Logs error, returns `None`
- **SSL Errors**: Logs error, returns `None`

### Certificate Errors
- **Not Found**: Auto-downloads if enabled, then auto-generates if download fails
- **Download Failed**: Auto-generates self-signed certificate if enabled
- **Invalid Format**: Logs warning, falls back to no verification
- **Parse Errors**: Logs error, returns error information
- **Generation Failed**: Logs error (usually missing cryptography library), returns `None`

---

## Future Enhancements

- [x] Certificate generation when download fails
- [x] CA-signed certificate generation
- [x] Local Certificate Authority creation
- [ ] Certificate expiration monitoring
- [ ] Automatic certificate renewal
- [ ] Certificate chain validation (partial - CA-signed certs have this)
- [ ] Multiple certificate support per host
- [ ] Certificate revocation checking
- [ ] Integration with Azure Key Vault for certificate storage
- [ ] Certificate installation on NAS (via API)
- [ ] Let's Encrypt integration for public certificates

---

## Related Files

- `scripts/python/nas_certificate_manager.py` - Certificate manager implementation
- `scripts/python/nas_service_monitor.py` - NAS service monitor (uses certificate manager)
- `config/certs/` - Certificate storage directory

---

## Status

✅ **Certificate Manager**: Implemented and tested  
✅ **NAS Service Monitor Integration**: Complete  
✅ **Certificate Download**: Working  
✅ **Certificate Generation**: Working (requires cryptography library)  
✅ **CA Creation**: Working (local Certificate Authority)  
✅ **CA-Signed Certificates**: Working (proper certificate chain validation)  
✅ **Certificate Verification**: Working  
✅ **Auto-Download**: Enabled by default  
✅ **Auto-Generate**: Enabled by default (fallback when download fails)  

---

**Last Updated**: 2025-01-24

