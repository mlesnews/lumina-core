# Lumina Extensions: Core, Premium, and CE

**Date**: 2026-01-29  
**Tag**: @extension lumina

---

## Core, Premium, and CE: three-way relationship

**Are Core and Premium “layers of” CE?** No. **CE is a third layer** — a separate distribution.

| Layer | What it is | Where |
|-------|------------|--------|
| **Core** (lumina-oss) | Base product: Lumina Core extension + shared foundation (integration manager, attribution, capability router). Open-source, MIT. | **Public tree**: `.lumina/` (vscode-extensions/lumina-core, scripts, config, docs). |
| **Premium** | Paid add-on that **extends Core**. Same product line; depends on Core (VSIX `extensionDependencies`). | **Public tree**: `.lumina/vscode-extensions/lumina-premium/`. |
| **CE** (lumina-ce) | **Third distribution**: the **company fork**. Contains **proprietary data, information, logic, and intelligence** — not “Core + Premium in company mode.” | **Private tree**: `cedarbrook-financial-services_llc-env/`, etc. |

- **Core and Premium** = two layers of the **Lumina product** (both live in the public repo / ship from `.lumina/`). Premium sits *on top of* Core.
- **CE** = **third layer** in the sense of **third distribution**: the private company tree. It does *not* contain Core or Premium as subfolders; it contains company-specific code, config, data, and workspace tooling (e.g. cedarbrook_financial_services, roo-code-extension, JARVIS panel). When someone works in the CE workspace, they may *install* Core (and optionally Premium) in the IDE, but CE the *codebase* is just the proprietary layer.

**Summary:** Core and Premium are product layers in the public tree; CE is a separate, third layer (company fork) with proprietary data/logic/intelligence only.

---

## Consider rearranging? (Core ↔ Premium, and CE)

At this stage it’s worth periodically asking whether a feature is in the right place.

### Core vs Premium (both in `.lumina/`)

- **Move from Premium → Core** when a capability becomes **generic and non–revenue-critical**: e.g. a Premium feature is opened up for the community, or it’s clearly “foundation” (rules, MCP patterns, queue viewer) that everyone should have. Then Premium keeps only paid differentiators (advanced progress, analytics, license, SLA, branding).
- **Move from Core → Premium** when a capability is **paid-only by product decision**: e.g. advanced progress, priority queue, custom branding, or anything that must stay behind a license. Keep Core strictly OSS-safe (no secrets, no company names, generic config only).

**Current split (for review):**  
Core: GitHub/GitLens, NAS patterns, TODO status, unified queue, footer ticker, file auto-close, voice (pattern).  
Premium: Show Premium Features, LUMINA Progress, Ask Heap Stack, Show Notifications [IDE-QUEUE], license, analytics. If something in Premium is “everyone should have it,” consider moving to Core; if something in Core is “paid only,” consider moving to Premium.

### CE is not “Core + Premium + company”

CE is **only** the proprietary layer (data, logic, intelligence, company workspace config). It does **not** duplicate Core or Premium. So:

- **Don’t** put “generic Lumina features” in CE; they belong in Core (or Premium if paid). CE should hold only what is **company-specific** (company workflows, real data, internal APIs, roo-code config, etc.).
- **Do** use Core (and optionally Premium) *in the IDE* when working in the CE workspace; the CE tree itself stays company-only content.

**Summary:** Revisit Core↔Premium when features outgrow their tier; keep CE as the third layer (proprietary only), not a superset of Core+Premium.

---

## Do we need to rebuild Lumina Premium?

**Only if you use it and changed its code.**

- **Lumina Core** is the main extension. BDA: `.\vscode-extensions\lumina-core\build_and_install.ps1`. Rebuild Core whenever you change Core.
- **Lumina Premium** is a **private add-on that depends on Lumina Core** (`extensionDependencies: ["lumina.lumina-core"]`). It is **not** built or installed by the Core BDA script.
- Rebuild Premium only when:
  - You want to use Premium (Show Premium Features, LUMINA Progress, Ask Heap Stack, Notifications), and
  - You have changed `vscode-extensions/lumina-premium` code.
- Premium has no `build_and_install.ps1` today. To build it: from `vscode-extensions/lumina-premium`, run `npm install`, `npm run compile`, `npx vsce package`, then install the resulting `.vsix` with Cursor. Core must be installed and active first.

**Summary:** Rebuild Core for normal use. Rebuild Premium only when you use Premium and have edited it.

---

## Private company fork (lumina-ce)

The **private company fork** is the **lumina-ce** (Cedarbrook Enterprise) distribution. It lives in **private trees**, not in `.lumina/`:

- **Locations:** `cedarbrook-financial-services_llc-env/`, `cedarbrook-financial-services_llc-env_portable/`, `cfs-llc-env/`
- **Purpose:** Company operations, proprietary logic, real data — not published to any marketplace.
- **Extensions:** Company-specific builds (if any) stay in private trees. The **extension BDA in `.lumina/`** (lumina-core, lumina-premium) is for the **public/open-source tree** only. Do not publish lumina-ce or company builds from public; follow `docs/system/PUBLIC_PRIVATE_FORK_STRATEGY.md`.

**Summary:** Private company = lumina-ce in cedarbrook-* trees; separate from extension BDA in `.lumina/`.

---

## Roo Code extension (why in CE, not Premium?)

**Roo Code** (Roocode) is one of the CAs consolidated under JARVIS (see `docs/JARVIS_CA_IDE_CONSOLIDATION_PLAN.md`). The **roo-code-extension** folder in the CE tree (`cedarbrook-financial-services_llc-env/roo-code-extension/`) contains **workspace/extension configuration** (e.g. `roo-code-settings.json`, provider profiles, API configs, Iron Legion), not the Roo Code extension source.

- **Why it’s in CE today:** CE is the **company workspace** tree. Roo Code config there is **company-specific IDE setup** (how this workspace uses Roo Code with Anthropic, Ollama, Iron Legion, etc.). Per fork strategy, that kind of workspace/extension config lives in the private tree (CE), not in the public `.lumina/` or in the Lumina Premium VSIX.
- **Why it’s not in Premium:** **Lumina Premium** is a **Lumina-branded** paid add-on (VSIX) that extends Lumina Core (e.g. Show Premium Features, LUMINA Progress, Ask Heap Stack, Notifications). It’s not a bucket for “all paid/private IDE tooling” — it’s a specific Lumina product. Roo Code integration was never defined as a Premium *feature*; it was part of the company workspace setup, so it stayed in CE.
- **If you want it in Premium:** Treat Roo Code (or its presets/config) as a **Premium offering**: add Roo Code–related features or config templates to `vscode-extensions/lumina-premium` (or document them there), and ship with Premium. Then CE could reference Premium for that, or you move/copy the integration into Premium and keep CE minimal.

**Summary:** Roo Code extension config is in CE as company workspace tooling; Premium is Lumina’s paid add-on product. Moving it to Premium is a product decision (add to Premium, then optionally remove from CE).

---

## CA/IDE config: only Roo Code has a dedicated CE folder (inconsistency)

**Observation:** Roo Code is the **only** CA/IDE for which we have saved **CE proprietary** config in a dedicated folder (`cedarbrook-*/roo-code-extension/`). The other CAs in the JARVIS set do not have a parallel “company config” folder in CE:

| CA / IDE   | Where config / company-specific content lives today |
|------------|-----------------------------------------------------|
| **Continue** | **.lumina/.continue/** (public): config.yaml, agents, mcpServers. No CE-only Continue folder. |
| **Kilocode** | **.lumina/.kilocode/**, **.lumina/config/kilo_code_optimized_config.json** (public). No CE-only Kilocode folder. |
| **Cline**    | CE has **docs** (e.g. cline_terminal_management.md, cline_mcp_troubleshooting.md) but **no** dedicated `cline-extension` or saved Cline config folder in CE. |
| **Roo Code** | **CE only:** `cedarbrook-*/roo-code-extension/` with roo-code-settings.json, provider profiles, etc. |

So yes — it’s **odd** that only Roo Code has CE-proprietary saved config; the others either live in the public tree (Continue, Kilocode) or only have docs in CE (Cline).

**Options to fix the inconsistency:**

1. **Add parallel CE folders for the other CAs**  
   In CE, add company-specific config/presets for Continue, Kilocode, and Cline (e.g. `continue-extension/`, `kilocode-extension/`, `cline-extension/` or similar) so all four CAs are treated the same: generic/templates in `.lumina/`, company overrides/presets in CE.

2. **Document the current split**  
   Explicitly state that Continue and Kilocode are **public** (`.lumina/`) only, Cline has **docs** in CE and config elsewhere, and **only Roo Code** keeps company-specific config in CE (e.g. for historical or product reasons). Then decide whether that split is intentional or should be changed.

3. **Move Roo Code config to a shared pattern**  
   Put Roo Code templates in `.lumina/` (or Premium) and keep in CE only **overrides** (e.g. API keys refs, model names), so CE doesn’t hold the only copy of a full CA config.

**Recommendation:** Either (1) align all CAs with a CE company-config pattern, or (2) document the current split and the reason Roo Code alone has a CE folder, so the inconsistency is intentional and reviewable.

**Decision (documented):** The current split is **intentional and reviewable**. Continue and Kilocode config live in the **public** tree (`.lumina/.continue/`, `.lumina/.kilocode/`) because they are shared, generic, or workspace-default; no company-only secrets or endpoints are required there. Cline has **docs** in CE (troubleshooting, terminal management) and config in extension/UI storage. **Roo Code alone** has a dedicated CE folder (`cedarbrook-*/roo-code-extension/`) because its company config (Anthropic, VS Code LM, Iron Legion profiles, mode→API mapping) is **company-specific** and must not live in the public repo; Roo Code also supports auto-import from a path, so pointing at CE is natural. Optional CE folders for Continue, Kilocode, and Cline exist in CE for **demand-driven** company overrides (see `CA_OEM_AND_CE_CONFIG_DEEP_DIVE.md` §8 Optionals); add content when needed.

For **OEM state (Core) and custom configuration (CE)** for **CAs, PAs, and IDEs** — config locations, schema, and what belongs in Core vs CE — see **`docs/system/CA_OEM_AND_CE_CONFIG_DEEP_DIVE.md`**.

---

## Mobile fork (lumina-mobile)

The **mobile fork** is the **lumina-mobile** distribution — a **separate product**, not a VS Code extension:

- **Location:** `mobile-app/` (when present)
- **Purpose:** Remote monitoring & control (iOS/Android); PROPRIETARY.
- **Build:** Mobile has its **own build/release pipeline** (e.g. Xcode, Android Studio, app stores). It is **not** built or installed by the extension BDA script (`build_and_install.ps1`). Rebuild mobile only when you change mobile-app code and use the mobile project’s build process.

**Summary:** Mobile = lumina-mobile in `mobile-app/`; separate distribution and build, not part of extension BDA.

---

## Legacy / stale extension IDs

If the IDE shows a malformed or old extension (e.g. `undefined_publisher.lumina-ai`), clear workspace cache and use **Lumina Core** (`lumina.lumina-core`) only. See `docs/LUMINA_EXTENSION_FIX.md`.

---

## References

- Core BDA: `docs/system/LUMINA_EXTENSION_BDA.md`, `vscode-extensions/lumina-core/build_and_install.ps1`
- Fix guide (undefined_publisher.lumina-ai, activation): `docs/LUMINA_EXTENSION_FIX.md`
- Premium: `vscode-extensions/lumina-premium/README.md` (private add-on, requires Core)
- Fork strategy: `docs/system/PUBLIC_PRIVATE_FORK_STRATEGY.md`
- Multi-distribution: `docs/system/LUMINA_MULTI_DISTRIBUTION_ARCHITECTURE.md` (lumina-oss, lumina-premium, lumina-ce, lumina-mobile)
