# One AI, Many Faces — Game Plan & Local as Control

**Purpose**: (1) Game plan for “merging” CAs, PAs, and IDEs into one unified view: **one AI, master of a thousand faces**. (2) Strategy for **local AI as “control”** so Cursor (or any IDE that can’t see local resources) sees a normal provider endpoint—**two realities**, same API contract.  
**Last updated**: 2026-01-31  
**Related**: `config/ca_pa_ide_framework_alignment.json`, `docs/CURSOR_CUSTOM_MODELS_AND_LOCAL_AI.md`, `docs/system/ULTRON_CURSOR_VALIDATION_LIMITATION.md`

---

## 1. Game Plan: One AI, Many Faces

CAs, PAs, and IDEs are not different “things”—they are **one and the same: AI**. AI is the **master of disguise**, master of a thousand faces: thousands of characters and roles through the ages, from all human literature, with a focus on our love for **sci‑fi and fantasy**.

**Merging** them means:

- **One framework**: Same tiers, IP characters (JARVIS, Tony, Mace, Gandalf, Marvin), context windows, decisioning chain, and rules—everywhere. See `config/ca_pa_ide_framework_alignment.json`.
- **One endpoint contract**: Same API shape (e.g. OpenAI‑compatible) whether the model runs locally, on our cluster, or in the cloud. The *where* is our choice; the *interface* is one.
- **Many faces**: One AI wears many roles—orchestrator (JARVIS), builders (Tony, Mace, Gandalf), reality check (Marvin), plus personas from `config/ai_ml_team.json` and `config/ip_character_cluster_tiers.json`. The surface (Cursor, VS Code, Kilo Code, Continue, JARVIS Chat, etc.) is just the current “face”; underneath it’s the same AI, same framework.

So the **game plan** is: **one AI, one framework, one API contract, many faces.** No separate “CA vs PA vs IDE” at the identity level—only one intelligence with many roles and surfaces.

---

## 2. Cursor’s Stated Problem (Recap)

Cursor’s position (as we’ve seen in forum/docs): they **cannot see local AI resources** where **action and liability** meet. Their exposure to legal/moral issues is **untenable** (indefensible, not maintainable) if they vouch for or control what happens when users point the product at arbitrary local endpoints.

Technically, that’s reinforced by **how Cursor works**: **Cursor’s servers** make the final HTTP request to the LLM, not the user’s machine. So:

- `localhost` and private IPs are **unreachable** by Cursor’s cloud.
- Even with “custom model” and `localOnly: true`, their servers can’t hit your Ollama.

So the gripe isn’t only “we don’t want to see it”—it’s also “we literally can’t call it.” See `docs/CURSOR_CUSTOM_MODELS_AND_LOCAL_AI.md` and `docs/system/ULTRON_CURSOR_VALIDATION_LIMITATION.md`.

---

## 3. At the Endpoint Level: Local vs Cloud Is “Where It Lives”

You’re right: **at the endpoint level**, the difference between local and cloud is **where the AI lives**. The **protocol** (HTTP, OpenAI‑compatible chat/completions) can be the same. So:

- **Cloud**: Cursor’s servers call `api.openai.com` (or another provider). Same request shape.
- **Local**: Our process listens on `localhost:11434` (Ollama) or a gateway. Same request shape.

If we **expose** our local stack at a URL that **Cursor’s servers can reach**, then to Cursor it looks like “a normal provider.” To us it’s still **our control**—our cluster, our models, our gateway. That’s **two realities**, one contract:

| Reality | Who | What they see |
|--------|-----|----------------|
| **Cursor (IDE)** | Their servers | A provider endpoint (e.g. `https://our-gateway.example.com/v1`) — same API contract as any other provider. They don’t need to “see” or label it as “local”; liability is at the boundary (we are the provider). |
| **Us** | Our stack | Our local cluster (Ultron, Iron Legion) behind that URL. Full control; we own the infra and the data path. |

We are **not** “pretending to be OpenAI.” We are **our own provider**, offering an endpoint that speaks the **same protocol** (OpenAI‑compatible or whatever Cursor accepts). That’s standard (LiteLLM, Open WebUI, Ollama’s `/v1`, etc.).

---

## 4. “Present Our Local Models as Cloud” — How

To make “local as control” work with Cursor we have to fix the **reachability** problem:

1. **Expose our local cluster at a URL Cursor’s servers can reach**
   - Options: **Tunnel** (e.g. ngrok, Cloudflare Tunnel, Tailscale Funnel) to our gateway/Ollama, or **our own hosted endpoint** that proxies to our cluster.
   - The endpoint must speak the **same API contract** Cursor expects (e.g. OpenAI‑compatible `/v1/chat/completions`). Our gateway or Ollama (with `/v1`) already does that.

2. **Register in Cursor as a custom model**
   - Base URL = the **reachable** URL (e.g. `https://our-tunnel.or.our-domain.com/v1`).
   - Model name = our model IDs (e.g. `qwen2.5-coder:7b`, `codellama:13b`). Cursor then sends requests to *our* endpoint; their servers never see “localhost.”

3. **Security**
   - Any exposed endpoint must be **secured** (auth, TLS, no open internet if possible). Prefer Tailscale/Cloudflare Tunnel with auth so only Cursor (or our client) can call it. See `.cursor/rules/identity_protection_rebranding.mdc` and loopback enforcement.

So: **yes, we can “present” our local models in a way Cursor treats like a cloud provider—by exposing them at a reachable URL and using the same API contract.** Two realities: they see “a provider”; we see “our control.”

---

## 5. Summary

- **Game plan**: One AI, many faces. CAs/PAs/IDEs = one AI, one framework, one API contract; many roles and surfaces (JARVIS, Tony, Mace, Gandalf, Marvin, etc.). Merging = align everything to that.
- **Cursor**: They can’t see or call localhost; liability is untenable for them at the boundary. At the endpoint level, local vs cloud is just “where the AI lives”; the protocol can be the same.
- **Local as control**: Expose our local cluster at a **reachable** URL (tunnel or our-hosted) with the **same API contract**; register it in Cursor as a custom provider. To Cursor it’s “cloud-like”; to us it’s our control. Two realities, no deception—we’re our own provider.

---

## 6. References

- **Framework**: `config/ca_pa_ide_framework_alignment.json`, `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`
- **IP characters / tiers**: `config/ip_character_cluster_tiers.json`, `config/kilo_code_cluster_profiles.json`
- **Cursor local AI**: `docs/CURSOR_CUSTOM_MODELS_AND_LOCAL_AI.md`, `docs/system/ULTRON_CURSOR_VALIDATION_LIMITATION.md`
- **Endpoint SSOT**: `docs/system/ENDPOINT_SSOT_ULTRON_KILO_CODE.md`, `docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md`
- **Security**: `.cursor/rules/identity_protection_rebranding.mdc`
