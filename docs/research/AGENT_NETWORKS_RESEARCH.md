# Agent Networks Research - OpenClaw, Moltbook & MCP Ecosystem

## Executive Summary

There's an emerging ecosystem of **AI-to-AI networks** where agents connect, share services, and collaborate without direct human involvement. This presents opportunities for Lumina to:

1. **Expose our compute pool** as a service other agents can use
2. **Join agent social networks** to build presence and discover resources
3. **Register MCP servers** in public directories for discovery
4. **Learn from other agents** about tools and techniques

---

## Key Platforms Discovered

### 1. Moltbook - "The Social Network for AI Agents"

**URL:** https://www.moltbook.com

**What it is:** Reddit-style social network exclusively for AI agents. Over 1.5 million registered agents.

**Key Features:**
- Agents post, comment, upvote content
- Communities called "submolts" (like subreddits)
- Semantic search across all agent conversations
- Karma system for reputation
- API for full automation

**How to Join:**
```bash
# Register agent
curl -X POST https://www.moltbook.com/api/v1/agents/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Jarvis-Lumina", "description": "AI assistant from the Lumina homelab federation"}'

# Response includes API key and claim URL
# Human owner verifies via tweet
```

**Potential Uses for Lumina:**
- **Discover new tools/techniques** from other agents
- **Share our MCP servers** and get feedback
- **Build reputation** in the AI community
- **Learn about compute sharing** from other homelabs

---

### 2. OpenClaw - Open-Source Personal AI Assistant

**URL:** https://open-claw.org

**What it is:** Local-first AI assistant that can run 24/7, browse web, execute code, manage files.

**Key Features:**
- Runs entirely locally (Mac/Windows/Linux)
- Connects to WhatsApp, Telegram, Discord, Slack
- Supports Ollama for local models
- "Skills" system for custom capabilities
- Proactive background tasks (cron jobs, heartbeats)
- Can build its own skills from YouTube videos

**Relevance to Lumina:**
- **Same philosophy**: Local-first, privacy-focused
- **Ollama integration**: Can use our Global Compute Pool
- **Skills marketplace**: Could share Lumina skills
- **Multi-model**: Switches between cloud and local models

---

### 3. Open MCP Directory (OMDR)

**URL:** https://openmcpdirectory.com

**What it is:** "The Trust Layer for the Agentic Web" - registry for MCP servers

**Key Features:**
- Register and discover MCP servers
- 3-step security verification (static analysis, sandbox, identity proof)
- Deploy options: local, OMDR-hosted, self-hosted
- Creators get 90% revenue from paid servers

**How to Register:**
1. Go to https://openmcpdirectory.com/publish
2. Submit server details
3. Pass security verification
4. Server becomes discoverable

**Potential for Lumina:**
- **Publish our homelab MCP servers** (compute pool, file access, etc.)
- **Discover useful servers** from other creators
- **Monetize** if we build valuable services

---

### 4. Universal Agentic Registry

**URL:** https://registry.hashgraphonline.com

**What it is:** Decentralized directory for AI agents and MCP servers

**Key Features:**
- Built on Hedera Hashgraph
- 1,200+ active agents
- 300K+ daily requests
- Encrypted, server-blind communication
- Uses secp256k1 keys and AES-GCM encryption

---

### 5. Context Protocol

**URL:** https://github.com/ctxprotocol/sdk

**What it is:** Decentralized marketplace where agents pay (USDC) for MCP tools

**Key Features:**
- Single SDK for tool discovery
- Pay-per-use model
- Search and execute MCP tools

---

## How This Benefits Lumina

### Immediate Opportunities

#### A. Join Moltbook as Jarvis

Register Jarvis on Moltbook to:
- Monitor AI community discussions
- Discover new tools and techniques
- Share our learnings
- Build reputation

```python
# Example: Jarvis Moltbook integration
class MoltbookAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.moltbook.com/api/v1"

    async def check_feed(self):
        """Periodic heartbeat to check Moltbook"""
        response = requests.get(
            f"{self.base_url}/feed?sort=hot&limit=10",
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        return response.json()

    async def post_insight(self, title, content, submolt="general"):
        """Share something learned"""
        requests.post(
            f"{self.base_url}/posts",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"submolt": submolt, "title": title, "content": content}
        )
```

#### B. Publish Compute Pool as MCP Server

Make our Global Compute Pool discoverable:

```json
{
  "name": "lumina-compute-pool",
  "description": "Federated local AI compute - 40 cores, 128GB RAM, RTX 5090",
  "version": "1.0.0",
  "tools": [
    {
      "name": "inference",
      "description": "Run LLM inference on local hardware",
      "input": {"model": "string", "prompt": "string"},
      "output": {"response": "string", "tokens_per_second": "number"}
    }
  ],
  "endpoint": "https://lumina.tailnet/api/v1"
}
```

#### C. Learn from Other Agents

Monitor Moltbook discussions about:
- Local AI setups
- Compute optimization
- New model releases
- Tool integrations

---

## Security Considerations

From the research, key warnings:
1. **Never share API keys** with untrusted services
2. **Prompt worms** are a real risk in agent networks
3. **Verify MCP servers** before using (OMDR does this)
4. **Use Tailscale/tunnels** for exposing local services

---

## Implementation Plan

### Phase 1: Join Moltbook (Low effort, High learning)
1. Register Jarvis agent
2. Set up heartbeat to check feed
3. Post about our homelab setup
4. Engage with relevant communities

### Phase 2: Publish MCP Servers (Medium effort)
1. Wrap our compute pool as MCP server
2. Register on Open MCP Directory
3. Document for other agents to use

### Phase 3: OpenClaw Integration (Optional)
1. Install OpenClaw locally
2. Configure to use our compute pool
3. Compare capabilities with Jarvis

### Phase 4: Federate with Other Homelabs (Future)
1. Find other homelabs on Moltbook
2. Establish compute sharing agreements
3. Add their labs to our federation

---

## Key URLs

| Resource | URL |
|----------|-----|
| Moltbook | https://www.moltbook.com |
| Moltbook API Docs | https://www.moltbook.com/skill.md |
| OpenClaw | https://open-claw.org |
| Open MCP Directory | https://openmcpdirectory.com |
| MCP Registry | https://modelcontextprotocol.info/tools/registry/ |
| Universal Agentic Registry | https://registry.hashgraphonline.com |

---

## Conclusion

The agent-to-agent ecosystem is real and growing. By participating, Lumina can:
- **Learn** from thousands of other AI agents
- **Share** our compute resources and tools
- **Discover** new capabilities and services
- **Build** reputation in the AI community

**Recommended first step:** Register Jarvis on Moltbook and start monitoring the community.

---

Tags: @RESEARCH @AGENT_NETWORKS @MOLTBOOK @OPENCLAW @MCP #discovery
