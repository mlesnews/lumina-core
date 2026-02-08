# Universal Hooks Framework — Every System Connected

**Vision:** A unified hook/event system where EVERY framework, service, and integration can trigger actions, receive events, and communicate.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         UNIVERSAL HOOKS HUB                                  │
│                    (Central Event Bus / Orchestrator)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐    │
│   │   IDE HOOKS      │    │  TRADING HOOKS   │    │  HOMELAB HOOKS   │    │
│   │                  │    │                  │    │                  │    │
│   │ • Cursor Agent   │    │ • 3Commas        │    │ • NAS Events     │    │
│   │ • VS Code        │    │ • Fidelity       │    │ • Docker         │    │
│   │ • JetBrains      │    │ • TradingView    │    │ • pfSense        │    │
│   │ • Neovim         │    │ • Robinhood?     │    │ • Tailscale      │    │
│   └──────────────────┘    └──────────────────┘    └──────────────────┘    │
│                                                                              │
│   ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐    │
│   │   AI HOOKS       │    │   COMMS HOOKS    │    │  PORTAL HOOKS    │    │
│   │                  │    │                  │    │                  │    │
│   │ • JARVIS Agent   │    │ • Twilio SMS     │    │ • RoamWise.AI    │    │
│   │ • Ollama/LLM     │    │ • ElevenLabs     │    │ • FISHBOWL       │    │
│   │ • MCP Servers    │    │ • Proton Mail    │    │ • GitHub         │    │
│   │ • n8n Workflows  │    │ • Discord        │    │ • Azure          │    │
│   └──────────────────┘    └──────────────────┘    └──────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Trading Hooks

### 3Commas.io (Crypto Trading)

**Status:** ✅ Configured

| Hook | Trigger | Action |
|------|---------|--------|
| `3commas.deal_started` | New deal opened | Log, notify, record in SYPHON |
| `3commas.deal_closed` | Deal closed | Log P/L, update dashboard |
| `3commas.bot_error` | Bot error | Alert, escalate to JARVIS |
| `3commas.signal_received` | TradingView signal | Start/close deal |

**Existing Integration:**
- n8n workflow: `config/n8n/3commas_tradingview_workflow.json`
- API keys: Azure Key Vault
- Webhook: `/3commas/tradingview`

**API Endpoints:**
```python
# 3Commas API Hooks
BASE_URL = "https://api.3commas.io"

HOOKS = {
    "start_deal": "/public/api/v2/bots/start_new_deal",
    "close_deal": "/public/api/v2/deals/close_by_pair",
    "get_bots": "/public/api/v2/bots",
    "get_deals": "/public/api/v2/deals",
    "account_balance": "/public/api/v2/accounts/balance_chart"
}
```

### Fidelity Investments (Stocks & Options)

**Status:** 🟡 Placeholder Ready (OAuth2 required)

| Hook | Trigger | Action |
|------|---------|--------|
| `fidelity.order_placed` | Order submitted | Log, confirm via SMS |
| `fidelity.order_filled` | Order executed | Update portfolio, notify |
| `fidelity.price_alert` | Price threshold hit | Trigger strategy evaluation |
| `fidelity.dividend_received` | Dividend posted | Log income, update tracking |
| `fidelity.option_expiring` | Option near expiration | Alert for action |

**Integration Approach:**

```python
# Fidelity requires OAuth2 authentication
# Option 1: Official API (if available)
# Option 2: Plaid for read-only account data
# Option 3: Manual webhook via broker notifications

FIDELITY_CONFIG = {
    "auth_type": "oauth2",
    "auth_url": "https://login.fidelity.com/ftgw/Fidelity/oauth2/authorize",
    "token_url": "https://login.fidelity.com/ftgw/Fidelity/oauth2/token",
    "scopes": ["accounts:read", "positions:read", "orders:read", "orders:write"],
    "redirect_uri": "http://localhost:5000/callback/fidelity"
}
```

**Alternative: Plaid Integration**
```python
# Plaid provides read-only access to Fidelity accounts
PLAID_CONFIG = {
    "client_id": "PLAID_CLIENT_ID",
    "secret": "PLAID_SECRET",
    "environment": "production",
    "products": ["investments"],
    "country_codes": ["US"]
}
```

### TradingView (Signals)

**Status:** ✅ Configured via n8n

| Hook | Trigger | Action |
|------|---------|--------|
| `tradingview.alert` | Pine Script alert | Route to 3Commas/Fidelity |
| `tradingview.strategy_signal` | Strategy buy/sell | Execute trade |

**Webhook Format:**
```json
{
  "action": "buy|sell|start_deal|close_deal",
  "ticker": "BTCUSDT",
  "bot_id": 12345678,
  "price": "{{close}}",
  "strategy": "DCA",
  "message": "{{strategy.order.comment}}"
}
```

---

## IDE Hooks (Already Configured)

### Cursor Agent Hooks

**Location:** `.cursor/hooks.json`

| Hook | Purpose |
|------|---------|
| `sessionStart` | Inject Lumina context |
| `sessionEnd` | Audit logging |
| `afterFileEdit` | Auto-format Python |
| `beforeShellExecution` | Security gate |
| `preCompact` | Context compaction notify |

---

## AI Agent Hooks

### JARVIS Orchestration Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| `jarvis.task_assigned` | New task for agent | Route to appropriate agent |
| `jarvis.task_completed` | Agent finished task | Log, notify, next action |
| `jarvis.escalation` | Agent can't handle | Escalate to human |
| `jarvis.error` | Agent error | Log, retry, or alert |

### n8n Workflow Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| `n8n.workflow_triggered` | Workflow started | Log execution |
| `n8n.workflow_completed` | Workflow finished | Log result, notify |
| `n8n.workflow_error` | Workflow failed | Alert, retry |

---

## Communication Hooks

### Twilio SMS

| Hook | Trigger | Action |
|------|---------|--------|
| `twilio.sms_received` | Incoming SMS | Parse, route to JARVIS |
| `twilio.sms_sent` | Outgoing SMS sent | Log communication |

### ElevenLabs Voice

| Hook | Trigger | Action |
|------|---------|--------|
| `elevenlabs.speech_generated` | TTS completed | Play audio |
| `elevenlabs.voice_cloned` | New voice ready | Update voice registry |

---

## Homelab Hooks

### NAS (Synology)

| Hook | Trigger | Action |
|------|---------|--------|
| `nas.disk_warning` | Disk space low | Alert, cleanup |
| `nas.container_stopped` | Docker container stopped | Restart or alert |
| `nas.backup_completed` | Backup finished | Log, verify |

### pfSense Firewall

| Hook | Trigger | Action |
|------|---------|--------|
| `pfsense.intrusion_detected` | IDS alert | Block, alert |
| `pfsense.vpn_connected` | VPN tunnel up | Log, notify |

---

## Implementation: Universal Hook Registry

### Config File: `config/universal_hooks_registry.json`

```json
{
  "version": "1.0.0",
  "description": "Universal hooks registry for all frameworks and services",
  "hooks": {
    "trading": {
      "3commas": {
        "enabled": true,
        "api_base": "https://api.3commas.io",
        "credentials": "azure_key_vault",
        "hooks": ["deal_started", "deal_closed", "bot_error", "signal_received"]
      },
      "fidelity": {
        "enabled": false,
        "auth_type": "oauth2",
        "credentials": "azure_key_vault",
        "hooks": ["order_placed", "order_filled", "price_alert", "dividend_received"]
      },
      "tradingview": {
        "enabled": true,
        "webhook_path": "/3commas/tradingview",
        "hooks": ["alert", "strategy_signal"]
      }
    },
    "ide": {
      "cursor": {
        "enabled": true,
        "config": ".cursor/hooks.json",
        "hooks": ["sessionStart", "sessionEnd", "afterFileEdit", "beforeShellExecution"]
      }
    },
    "ai": {
      "jarvis": {
        "enabled": true,
        "hooks": ["task_assigned", "task_completed", "escalation", "error"]
      },
      "n8n": {
        "enabled": true,
        "hooks": ["workflow_triggered", "workflow_completed", "workflow_error"]
      }
    },
    "communications": {
      "twilio": {
        "enabled": true,
        "hooks": ["sms_received", "sms_sent"]
      },
      "elevenlabs": {
        "enabled": true,
        "hooks": ["speech_generated", "voice_cloned"]
      }
    },
    "homelab": {
      "nas": {
        "enabled": true,
        "hooks": ["disk_warning", "container_stopped", "backup_completed"]
      },
      "pfsense": {
        "enabled": true,
        "hooks": ["intrusion_detected", "vpn_connected"]
      }
    },
    "portal": {
      "roamwise": {
        "enabled": true,
        "hooks": ["user_login", "navigation", "search_query"]
      }
    }
  }
}
```

---

## Central Event Bus

### Python Implementation

```python
#!/usr/bin/env python3
"""
Universal Hooks Event Bus — Central orchestrator for all hooks.

Tags: #hooks #events #orchestration @JARVIS
"""

import json
import asyncio
from dataclasses import dataclass
from typing import Callable, Dict, List, Any
from datetime import datetime


@dataclass
class HookEvent:
    source: str       # e.g., "3commas", "cursor", "fidelity"
    hook_name: str    # e.g., "deal_started", "sessionStart"
    payload: Dict[str, Any]
    timestamp: str = None

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class UniversalHooksHub:
    """Central event bus for all hooks."""

    def __init__(self):
        self.handlers: Dict[str, List[Callable]] = {}
        self.event_log: List[HookEvent] = []

    def register(self, event_pattern: str, handler: Callable):
        """Register a handler for an event pattern.

        Patterns:
        - "3commas.deal_started" - specific event
        - "3commas.*" - all 3commas events
        - "*" - all events
        """
        if event_pattern not in self.handlers:
            self.handlers[event_pattern] = []
        self.handlers[event_pattern].append(handler)

    async def emit(self, event: HookEvent):
        """Emit an event to all matching handlers."""
        self.event_log.append(event)

        # Find matching handlers
        event_key = f"{event.source}.{event.hook_name}"
        handlers_to_call = []

        # Exact match
        if event_key in self.handlers:
            handlers_to_call.extend(self.handlers[event_key])

        # Wildcard match (source.*)
        wildcard_key = f"{event.source}.*"
        if wildcard_key in self.handlers:
            handlers_to_call.extend(self.handlers[wildcard_key])

        # Global wildcard
        if "*" in self.handlers:
            handlers_to_call.extend(self.handlers["*"])

        # Call all handlers
        for handler in handlers_to_call:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(event)
                else:
                    handler(event)
            except Exception as e:
                print(f"Handler error for {event_key}: {e}")

    def get_recent_events(self, count: int = 100) -> List[HookEvent]:
        """Get recent events."""
        return self.event_log[-count:]


# Global hub instance
hub = UniversalHooksHub()


# Example handlers
def log_all_events(event: HookEvent):
    """Log all events to file."""
    print(f"[{event.timestamp}] {event.source}.{event.hook_name}: {event.payload}")


async def handle_trading_event(event: HookEvent):
    """Handle trading events specially."""
    if event.source in ["3commas", "fidelity", "tradingview"]:
        # Log to SYPHON
        # Notify if significant
        # Update dashboard
        pass


# Register handlers
hub.register("*", log_all_events)
hub.register("3commas.*", handle_trading_event)
hub.register("fidelity.*", handle_trading_event)
```

---

## Financial Hooks Deep Dive

### 3Commas API Hooks

```python
import hmac
import hashlib
import requests
from typing import Optional


class ThreeCommasHooks:
    """3Commas trading hooks."""

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.3commas.io"

    def _sign(self, path: str, body: str = "") -> str:
        message = path + body
        return hmac.new(
            self.api_secret.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()

    def _request(self, method: str, path: str, data: dict = None):
        body = json.dumps(data) if data else ""
        headers = {
            "APIKEY": self.api_key,
            "Signature": self._sign(path, body),
            "Content-Type": "application/json"
        }

        url = f"{self.base_url}{path}"
        resp = requests.request(method, url, headers=headers, data=body)
        return resp.json()

    # Hook implementations
    def on_deal_started(self, bot_id: int, pair: str):
        """Start a new deal."""
        return self._request("POST", "/public/api/v2/bots/start_new_deal", {
            "bot_id": bot_id,
            "pair": pair
        })

    def on_deal_closed(self, deal_id: int):
        """Close a deal."""
        return self._request("POST", f"/public/api/v2/deals/{deal_id}/close_by_pair")

    def get_active_deals(self) -> list:
        """Get all active deals."""
        return self._request("GET", "/public/api/v2/deals?scope=active")

    def get_bot_stats(self, bot_id: int) -> dict:
        """Get bot statistics."""
        return self._request("GET", f"/public/api/v2/bots/{bot_id}")
```

### Fidelity API Hooks (OAuth2 Flow)

```python
import requests
from urllib.parse import urlencode


class FidelityHooks:
    """Fidelity Investments trading hooks (OAuth2)."""

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.auth_url = "https://login.fidelity.com/ftgw/Fidelity/oauth2/authorize"
        self.token_url = "https://login.fidelity.com/ftgw/Fidelity/oauth2/token"
        self.api_base = "https://api.fidelity.com"
        self.access_token = None

    def get_auth_url(self) -> str:
        """Get OAuth2 authorization URL."""
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": "accounts:read positions:read orders:read orders:write"
        }
        return f"{self.auth_url}?{urlencode(params)}"

    def exchange_code(self, code: str) -> dict:
        """Exchange auth code for tokens."""
        resp = requests.post(self.token_url, data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri
        })
        tokens = resp.json()
        self.access_token = tokens.get("access_token")
        return tokens

    def _api_request(self, method: str, path: str, data: dict = None):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        url = f"{self.api_base}{path}"
        return requests.request(method, url, headers=headers, json=data).json()

    # Hook implementations
    def get_accounts(self) -> list:
        """Get all accounts."""
        return self._api_request("GET", "/v1/accounts")

    def get_positions(self, account_id: str) -> list:
        """Get positions for an account."""
        return self._api_request("GET", f"/v1/accounts/{account_id}/positions")

    def place_order(self, account_id: str, order: dict) -> dict:
        """Place an order."""
        return self._api_request("POST", f"/v1/accounts/{account_id}/orders", order)

    def get_order_status(self, account_id: str, order_id: str) -> dict:
        """Get order status."""
        return self._api_request("GET", f"/v1/accounts/{account_id}/orders/{order_id}")
```

---

## Next Steps

1. **Create registry file:** `config/universal_hooks_registry.json`
2. **Implement event bus:** `scripts/python/universal_hooks_hub.py`
3. **Fidelity OAuth2 setup:** Register app with Fidelity, complete OAuth flow
4. **Connect to n8n:** Create workflows for each hook type
5. **Dashboard:** RoamWise.AI hook monitoring dashboard

---

**Tags:** #hooks #trading #3commas #fidelity #universal #events @JARVIS @LUMINA
