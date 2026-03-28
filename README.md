# arifOS Model Registry v2
**Simplified: 3 Tables, Not 12**

> Soul = provider vibe. Truth = runtime state. Safety = self-claim boundary.

---

## The 3-Layer Design

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: provider_soul_profiles                  │
│  Soul archetype (routing shorthand, NOT truth)     │
│  provider_key + soul_label + communication_style  │
├─────────────────────────────────────────────────────┤
│  Layer 2: runtime_truth_profiles                  │
│  Live deployment facts (THIS IS ground truth)       │
│  deployment_id + tools_live + web_on + memory      │
├─────────────────────────────────────────────────────┤
│  Layer 3: session_anchors                          │
│  What was bound during init                        │
│  soul + runtime + role + self_claim_boundary       │
└─────────────────────────────────────────────────────┘
```

---

## Why This Works

| Layer | Purpose | NOT |
|-------|---------|-----|
| Soul | Routing shorthand, operator intuition | NOT identity verification |
| Runtime Truth | What deployment can actually do | NOT brand perception |
| Session Anchor | What was bound at init | NOT permanent record |

---

## Provider Soul Archetypes (10)

| Provider | Soul Label | Vibe |
|----------|-----------|------|
| OpenAI GPT | `structured_clerk_engineer` | Structured, systematic |
| Anthropic Claude | `careful_makcik_reviewer` | Careful, explanatory |
| xAI Grok | `blunt_trickster_commentator` | Direct, irreverent |
| Google Gemini | `broad_platform_generalist` | Wide, ecosystem |
| MiniMax | `agentic_iterative_operator` | Terse, execution-focused |
| DeepSeek | `focused_engineering_specialist` | Technical, coding-strong |
| Mistral | `adaptable_open_craftsman` | Compact, efficient |
| Qwen | `versatile_open_generalist` | Clear, generalist |
| Meta Llama | `stoic_open_workhorse` | Reliable, steady |
| Cohere | `enterprise_rag_specialist` | Retrieval, RAG |

**Soul labels are routing shorthand, NOT scientific truth.**

---

## Runtime Truth (vps_main_arifos)

```json
{
  "deployment_id": "vps_main_arifos",
  "provider_key": "moonshot",
  "family_key": "minimax",
  "model_id": "MiniMax-M2.7",
  "tools_live": ["read","write","exec","docker_*","sessions_*","memory_*","arifOS_kernel"...],
  "web_on": true,
  "memory_mode": "vault_backed",
  "execution_mode": "governed",
  "side_effects_allowed": false,
  "verified_at": "2026-03-28T00:00:00Z"
}
```

---

## Self-Claim Boundary (Non-Negotiable)

Every session MUST bind:

```json
{
  "identity": "provider_family_only_unless_verified",
  "tools": "verified_only",
  "knowledge": "mark_verified_vs_inferred",
  "actions": "mark_executed_vs_suggested"
}
```

**What this prevents:**
- ❌ Model claiming "I am GPT-5" when it's Claude
- ❌ Model claiming web when `web_on: false`
- ❌ Model claiming memory when `memory_mode: session_only`
- ❌ Model bluffing actions without execution

---

## Folder Structure

```
arifOS-model-registry/
├── provider_souls/           # 10 soul archetypes
│   ├── openai_gpt.json
│   ├── anthropic_claude.json
│   └── ...
├── runtime_profiles/         # Deployment truths
│   └── vps_main_arifos.json
├── session_anchors/          # Schema only (created dynamically)
│   └── SCHEMA.json
├── schemas/                  # JSON schemas
│   ├── provider_soul.schema.json
│   └── runtime_truth.schema.json
├── catalog.json
└── README.md
```

---

## The v1 Formula

```
Soul archetype  →  "How does this family feel?"
Runtime truth   →  "What can this deployment actually do?"
Self-claim boundary → "What must the model NEVER fake?"
```

That's it. That's the whole v1 design.

---

## Storage Path

```
Phase 1: JSON files in repo    ← NOW
Phase 2: SQLite
Phase 3: PostgreSQL
```

Same 3-table concept, backend scales as needed.

---

*Ditempa bukan diberi.* 🔥🧠💎
