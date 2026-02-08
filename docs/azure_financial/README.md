# Azure Financial Data Aggregation

## Overview

Azure-based integration with financial data aggregators (Plaid, Finicity, MX, Akoya) that Copilot Money uses. Since Copilot Money has no public API, this provides direct access to the same underlying data sources through Azure infrastructure.

## Why Azure Integration?

Copilot Money uses these aggregators but doesn't expose an API. By integrating directly with the aggregators via Azure services, you get:

- ✅ **Direct API Access** - Same data Copilot Money uses
- ✅ **Real-time Data** - No CSV export needed
- ✅ **Scalable Infrastructure** - Azure Functions, API Management
- ✅ **Secure Credential Management** - Azure Key Vault
- ✅ **Webhook Support** - Real-time updates
- ✅ **Enterprise-grade** - Production-ready architecture

## Supported Aggregators

### 1. Plaid (Primary)
- **Coverage**: Most US banks and financial institutions
- **Features**: Accounts, transactions, balances, identity verification
- **Azure Integration**: 
  - Key Vault for credentials
  - Functions for webhook handling
  - API Management for OAuth proxy

### 2. Finicity (Mastercard Open Banking)
- **Coverage**: US Open Banking network
- **Features**: Account aggregation, investments API
- **Azure Integration**:
  - Key Vault for partner credentials
  - API Management for OAuth flows

### 3. MX
- **Coverage**: Account aggregation with data cleansing
- **Features**: Enhanced merchant info, categorization
- **Azure Integration**:
  - **NAT Gateway required** for IP allowlisting
  - Functions Premium/Dedicated with VNet integration
  - Key Vault for credentials

### 4. Akoya
- **Coverage**: OAuth 2.0 + OIDC based aggregation
- **Features**: Tokenized, permissioned data access
- **Azure Integration**:
  - OAuth 2.0 + OIDC flow
  - Key Vault for client credentials
  - API Management for token management

## Azure Services Used

### Azure Key Vault
**Purpose**: Secure credential storage

**Secrets to Store**:
- `plaid-client-id`
- `plaid-secret`
- `finicity-partner-id`
- `finicity-partner-secret`
- `mx-client-id`
- `mx-api-key`
- `akoya-client-id`
- `akoya-client-secret`

**Best Practices**:
- Enable soft delete
- Enable purge protection
- Use managed identities
- Rotate secrets regularly

### Azure Functions
**Purpose**: Webhook handling and API calls

**Use Cases**:
- Plaid webhook receiver (JWT verification)
- Finicity webhook handler
- MX webhook handler
- Akoya webhook handler
- Scheduled account synchronization

**Configuration**:
- Runtime: Python 3.11+
- Authentication: Function keys or managed identity
- Retry policy: Exponential backoff
- Idempotency: Required for webhooks

### Azure API Management
**Purpose**: OAuth delegation and API proxy

**Features**:
- OAuth 2.0 between clients and aggregators
- Credential management
- Rate limiting
- Request/response transformation

### NAT Gateway
**Purpose**: Fixed egress IP for MX (IP allowlisting required)

**Requirements**:
- Functions Premium or Dedicated plan
- VNet integration
- NAT Gateway with static IP
- Register IP in MX dashboard

### Logic Apps
**Purpose**: Workflow automation

**Use Cases**:
- Scheduled account synchronization
- Data transformation pipelines
- Alert workflows

## Implementation Steps

1. **Store Credentials in Azure Key Vault**
   ```bash
   # Add aggregator credentials
   az keyvault secret set --vault-name jarvis-lumina --name plaid-client-id --value <value>
   az keyvault secret set --vault-name jarvis-lumina --name plaid-secret --value <value>
   ```

2. **Create Azure Functions for Webhooks**
   - HTTP trigger for webhook endpoints
   - JWT verification for Plaid
   - Idempotent processing

3. **Set Up API Management** (if needed)
   - OAuth 2.0 configuration
   - Backend API connections
   - Rate limiting policies

4. **Configure NAT Gateway** (if using MX)
   - Create NAT Gateway
   - Associate with Functions VNet
   - Register static IP in MX dashboard

5. **Register Redirect URIs**
   - Plaid: Register in Plaid Dashboard
   - Finicity: Register in Mastercard Developer Portal
   - Akoya: Register in Data Recipient Hub

6. **Implement OAuth Flows**
   - User authorization flows
   - Token exchange
   - Token refresh

7. **Store Access Tokens Securely**
   - Azure Key Vault or encrypted storage
   - Per-user token management

8. **Set Up Scheduled Sync**
   - Logic Apps or Functions Timer trigger
   - Regular account synchronization

9. **Implement Webhook Verification**
   - Plaid: JWT signature verification
   - Other aggregators: Per their documentation

10. **Test with Sandbox Environments**
    - Plaid Sandbox
    - MX MXCU test institutions
    - Akoya Sandbox Hub
    - Finicity Test Drive

## Integration with JARVIS Financial CLI

The Azure aggregation can be integrated with the JARVIS Financial CLI:

```python
from azure_financial_aggregation import AzureFinancialAggregation

# Initialize
aggregation = AzureFinancialAggregation()

# Get accounts from all aggregators
accounts = aggregation.get_all_accounts()

# Get accounts from specific aggregator
plaid_accounts = aggregation.get_all_accounts("plaid")
```

## Comparison: Copilot Money vs Azure Direct Integration

| Feature | Copilot Money | Azure Direct Integration |
|---------|---------------|-------------------------|
| **API Access** | ❌ No public API | ✅ Direct API access |
| **Real-time Data** | ❌ Manual CSV export | ✅ Real-time via API |
| **Webhooks** | ❌ Not available | ✅ Full webhook support |
| **Scalability** | ❌ Limited | ✅ Azure infrastructure |
| **Customization** | ❌ Limited | ✅ Full control |
| **Cost** | App subscription | Aggregator API costs |

## Security Considerations

1. **Credential Management**: All credentials in Azure Key Vault
2. **Token Storage**: Encrypted storage for access tokens
3. **Webhook Verification**: JWT verification for Plaid
4. **Network Security**: VNet integration, NAT Gateway for MX
5. **Access Control**: Managed identities, RBAC

## Testing

### Plaid Sandbox
```bash
# Create test public token
curl -X POST https://sandbox.plaid.com/sandbox/public_token/create \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "...",
    "secret": "...",
    "institution_id": "ins_109508",
    "initial_products": ["transactions"]
  }'
```

### MX Test Institutions
- Use MXCU OAuth test institutions
- Development environment: 100 user limit

### Akoya Sandbox
- Use Sandbox Hub
- Demo redirect URI for testing

## Related Files

- `scripts/python/azure_financial_aggregation.py` - Main integration module
- `config/azure/key_vault_config.json` - Key Vault configuration
- `docs/azure_financial/README.md` - This file

## References

- [Plaid API Documentation](https://plaid.com/docs/)
- [Finicity Developer Portal](https://www.finicity.com/developers/)
- [MX Platform API](https://docs.mx.com/)
- [Akoya Documentation](https://docs.akoya.com/)
- [Azure Key Vault Best Practices](https://learn.microsoft.com/azure/key-vault/secrets/secrets-best-practices)
- [Azure Functions HTTP Triggers](https://learn.microsoft.com/azure/azure-functions/functions-bindings-http-webhook-trigger)
