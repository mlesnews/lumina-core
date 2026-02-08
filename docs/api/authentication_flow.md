# Authentication Flow Documentation

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

The JARVIS Master Agent API uses token-based authentication with JWT (JSON Web Tokens) and refresh tokens for secure access control.

### Authentication Architecture

- **Access Tokens**: Short-lived JWT tokens (1 hour expiration)
- **Refresh Tokens**: Long-lived tokens (30 days expiration) for token renewal
- **Token Storage**: Secure storage (never in localStorage for web apps)
- **Token Rotation**: Refresh tokens are rotated on each use
- **Revocation**: Tokens can be revoked immediately

---

## Authentication Flow

### 1. Initial Login

**Endpoint**: `POST /api/v1/auth/login`

**Request**:
```json
{
  "username": "user@example.com",
  "password": "secure_password",
  "device_id": "device-uuid-1234",
  "device_name": "Windows Desktop App"
}
```

**Response**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "refresh_token_string_here",
  "token_type": "Bearer",
  "expires_in": 3600,
  "user": {
    "id": "user-uuid",
    "username": "user@example.com",
    "email": "user@example.com",
    "permissions": ["workflows:read", "workflows:write", "chat:send"]
  }
}
```

**Process**:
1. Client sends username and password
2. Server validates credentials (from Azure Key Vault)
3. Server generates JWT access token (1 hour expiration)
4. Server generates refresh token (30 days expiration)
5. Server stores refresh token hash in database
6. Server returns both tokens to client

**Security**:
- Passwords are never stored in plain text
- Passwords validated against Azure Key Vault
- Failed login attempts are rate-limited
- Device tracking for security monitoring

---

### 2. Using Access Token

**Header Format**:
```
Authorization: Bearer {access_token}
```

**Example Request**:
```http
GET /api/v1/workflows HTTP/1.1
Host: api.jarvis.local
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json
```

**Token Validation**:
1. Extract token from Authorization header
2. Verify JWT signature
3. Check token expiration
4. Validate user permissions
5. Process request

**Token Expiration**:
- Access tokens expire after 1 hour
- When expired, client must use refresh token to get new access token
- Expired token returns `401 Unauthorized` with error code `AUTH_EXPIRED`

---

### 3. Refreshing Access Token

**Endpoint**: `POST /api/v1/auth/refresh`

**Request**:
```json
{
  "refresh_token": "refresh_token_string_here"
}
```

**Response**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Process**:
1. Client sends refresh token
2. Server validates refresh token
3. Server checks if refresh token is revoked
4. Server generates new access token
5. Server optionally rotates refresh token (security best practice)
6. Server returns new access token

**Refresh Token Rotation**:
- On each refresh, a new refresh token is generated
- Old refresh token is invalidated
- Client must store new refresh token
- Prevents token reuse if compromised

**Error Handling**:
- Invalid refresh token: `401 Unauthorized` with `AUTH_INVALID`
- Expired refresh token: `401 Unauthorized` with `AUTH_EXPIRED`
- Revoked refresh token: `401 Unauthorized` with `AUTH_REVOKED`

---

### 4. Logout

**Endpoint**: `POST /api/v1/auth/logout`

**Request Headers**:
```
Authorization: Bearer {access_token}
```

**Response**:
```json
{
  "message": "Logged out successfully"
}
```

**Process**:
1. Client sends access token in Authorization header
2. Server validates token
3. Server revokes access token (adds to blacklist)
4. Server revokes associated refresh token
5. Server clears session data
6. Server returns success

**Token Revocation**:
- Access token added to revocation list (checked on each request)
- Refresh token marked as revoked in database
- Tokens cannot be used after logout

---

### 5. Getting Current User

**Endpoint**: `GET /api/v1/auth/me`

**Request Headers**:
```
Authorization: Bearer {access_token}
```

**Response**:
```json
{
  "user": {
    "id": "user-uuid",
    "username": "user@example.com",
    "email": "user@example.com",
    "permissions": ["workflows:read", "workflows:write", "chat:send"],
    "preferences": {
      "theme": "dark",
      "notifications": true
    }
  }
}
```

**Use Cases**:
- Verify token is still valid
- Get current user information
- Check user permissions
- Load user preferences

---

## Token Structure

### Access Token (JWT)

**Header**:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload**:
```json
{
  "sub": "user-uuid",
  "username": "user@example.com",
  "permissions": ["workflows:read", "workflows:write"],
  "iat": 1705276800,
  "exp": 1705280400,
  "jti": "token-uuid"
}
```

**Claims**:
- `sub`: Subject (user ID)
- `username`: Username
- `permissions`: Array of permissions
- `iat`: Issued at timestamp
- `exp`: Expiration timestamp
- `jti`: JWT ID (unique token identifier)

### Refresh Token

**Format**: Cryptographically secure random string
**Storage**: Hashed in database
**Expiration**: 30 days
**Rotation**: Rotated on each use

---

## Security Best Practices

### Client-Side

1. **Token Storage**:
   - Web Apps: Use httpOnly cookies or secure storage (not localStorage)
   - Desktop Apps: Use secure keychain/credential store
   - Mobile Apps: Use secure keychain

2. **Token Transmission**:
   - Always use HTTPS
   - Never send tokens in URL parameters
   - Use Authorization header for all requests

3. **Token Refresh**:
   - Refresh token before expiration (e.g., at 50 minutes)
   - Handle refresh failures gracefully
   - Store new refresh token immediately

4. **Error Handling**:
   - Handle 401 errors by attempting token refresh
   - If refresh fails, redirect to login
   - Never retry with expired token

### Server-Side

1. **Token Validation**:
   - Verify JWT signature on every request
   - Check token expiration
   - Validate token against revocation list
   - Verify user permissions

2. **Token Generation**:
   - Use strong secret keys (from Azure Key Vault)
   - Set appropriate expiration times
   - Include necessary claims only

3. **Token Revocation**:
   - Maintain revocation list (Redis or database)
   - Check revocation on every request
   - Revoke on logout and security events

4. **Rate Limiting**:
   - Limit login attempts (5 per minute)
   - Limit refresh requests (10 per minute)
   - Prevent brute force attacks

---

## Error Codes

### AUTH_REQUIRED
**Status**: 401 Unauthorized
**Message**: "Authentication required"
**Cause**: Missing or invalid Authorization header

### AUTH_INVALID
**Status**: 401 Unauthorized
**Message**: "Invalid authentication credentials"
**Cause**: Invalid username/password or invalid token

### AUTH_EXPIRED
**Status**: 401 Unauthorized
**Message**: "Authentication token expired"
**Cause**: Access token or refresh token expired

### AUTH_REVOKED
**Status**: 401 Unauthorized
**Message**: "Authentication token revoked"
**Cause**: Token was revoked (logout, security event)

### PERMISSION_DENIED
**Status**: 403 Forbidden
**Message**: "Insufficient permissions"
**Cause**: User lacks required permissions for requested resource

---

## Implementation Examples

### JavaScript/TypeScript

```typescript
class JARVISAuth {
  private accessToken: string | null = null;
  private refreshToken: string | null = null;

  async login(username: string, password: string) {
    const response = await fetch('https://api.jarvis.local/api/v1/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });

    if (response.ok) {
      const data = await response.json();
      this.accessToken = data.access_token;
      this.refreshToken = data.refresh_token;
      // Store tokens securely
      this.storeTokens(data.access_token, data.refresh_token);
      return data;
    }
    throw new Error('Login failed');
  }

  async refreshAccessToken() {
    if (!this.refreshToken) throw new Error('No refresh token');

    const response = await fetch('https://api.jarvis.local/api/v1/auth/refresh', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh_token: this.refreshToken })
    });

    if (response.ok) {
      const data = await response.json();
      this.accessToken = data.access_token;
      this.storeTokens(data.access_token, this.refreshToken);
      return data.access_token;
    }
    throw new Error('Token refresh failed');
  }

  async makeRequest(url: string, options: RequestInit = {}) {
    if (!this.accessToken) throw new Error('Not authenticated');

    const response = await fetch(url, {
      ...options,
      headers: {
        ...options.headers,
        'Authorization': `Bearer ${this.accessToken}`
      }
    });

    if (response.status === 401) {
      // Token expired, try refresh
      await this.refreshAccessToken();
      // Retry request
      return this.makeRequest(url, options);
    }

    return response;
  }
}
```

### Python

```python
import requests
from datetime import datetime, timedelta

class JARVISAuth:
    def __init__(self):
        self.access_token = None
        self.refresh_token = None
        self.token_expires_at = None

    def login(self, username: str, password: str):
        response = requests.post(
            'https://api.jarvis.local/api/v1/auth/login',
            json={'username': username, 'password': password}
        )
        response.raise_for_status()
        data = response.json()
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
        self.token_expires_at = datetime.now() + timedelta(seconds=data['expires_in'])
        return data

    def refresh_access_token(self):
        if not self.refresh_token:
            raise Exception('No refresh token')

        response = requests.post(
            'https://api.jarvis.local/api/v1/auth/refresh',
            json={'refresh_token': self.refresh_token}
        )
        response.raise_for_status()
        data = response.json()
        self.access_token = data['access_token']
        self.token_expires_at = datetime.now() + timedelta(seconds=data['expires_in'])
        return data['access_token']

    def make_request(self, method: str, url: str, **kwargs):
        if not self.access_token:
            raise Exception('Not authenticated')

        # Check if token needs refresh
        if self.token_expires_at and datetime.now() >= self.token_expires_at - timedelta(minutes=10):
            self.refresh_access_token()

        headers = kwargs.get('headers', {})
        headers['Authorization'] = f'Bearer {self.access_token}'
        kwargs['headers'] = headers

        response = requests.request(method, url, **kwargs)

        if response.status_code == 401:
            # Token expired, try refresh
            self.refresh_access_token()
            headers['Authorization'] = f'Bearer {self.access_token}'
            response = requests.request(method, url, **kwargs)

        return response
```

---

## Multi-Device Support

### Device Management

- Each login can include `device_id` and `device_name`
- Server tracks active devices per user
- Users can view and revoke devices
- Maximum devices per user: 10 (configurable)

### Concurrent Sessions

- Multiple devices can be logged in simultaneously
- Each device has independent tokens
- Revoking one device doesn't affect others
- Device-specific rate limiting

---

## Troubleshooting

### Common Issues

1. **Token Expired Immediately**
   - Check system clock synchronization
   - Verify token expiration time in response
   - Check for token refresh logic

2. **Refresh Token Invalid**
   - Verify refresh token wasn't revoked
   - Check refresh token expiration (30 days)
   - Ensure refresh token is stored correctly

3. **401 Errors After Login**
   - Verify token is sent in Authorization header
   - Check token format: `Bearer {token}`
   - Verify token hasn't been revoked

4. **Permission Denied**
   - Check user permissions in token
   - Verify required permissions for endpoint
   - Check if user role has necessary permissions

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
