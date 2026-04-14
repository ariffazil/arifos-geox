# GEOX Governed Agentic Apps — Roadmap

> **Status:** Wave 1 Trust Foundation  
> **Motto:** *Ditempa Bukan Diberi* — Forged, Not Given  
> **Constitutional Kernel:** arifOS F1–F13  
> **Ledger:** VAULT999

---

## 1. Executive Summary

This roadmap translates the Gemini strategic design spec into an implementable, governed trajectory for five GEOX applications. The work is phased by governance maturity, not merely feature count.

| App | Status | Target Phase | Governance Grade |
|---|---|---|---|
| **AC_Risk Console** | LIVE | Reference implementation | AAA |
| **Attribute Audit** | PREVIEW | Working prototype | AA |
| **Seismic Vision Review** | SCAFFOLD | Governed stub | A |
| **Georeference Map** | SCAFFOLD | Governed stub | A |
| **Analog Digitizer** | PLANNED | Design spike | B |

---

## 2. What Was Delivered in This Commit

### 2.1 AC_Risk Governance Hardening (Option A)
**Files:** `geox/core/ac_risk.py`, `geox/mcp/server.py`, `geox/core/tool_registry.py`

- **ClaimTag enum** added (`CLAIM`, `PLAUSIBLE`, `HYPOTHESIS`, `UNKNOWN`).
- **TEARFRAME dataclass** added (`truth`, `echo`, `amanah`, `rasa`).
- **Anti-Hantu screen** (`AntiHantuScreen`) with regex patterns to detect empathy/feeling claims. Fail-closed → `VOID`.
- **888_HOLD enforcement**:
  - Raw AC_Risk `HOLD`/`VOID` triggers `hold_enforced=True`.
  - `irreversible_action=True` forces `HOLD` regardless of score.
  - `amanah_locked=False` forces `HOLD` for `SEAL`/`QUALIFY`.
- **VAULT999 payload** embedded in every governed result.
- **MCP tool exposure:**
  - `compute_ac_risk` — backward-compatible basic tool.
  - `evaluate_ac_risk_governed` — canonical governance entrypoint.

### 2.2 MCP App Stubs + UI Bridge (Options B, C, D)
**Files:** `geox/apps/*/manifest.json`, `geox/apps/*/index.html`

Four new app directories created, each with:
- `manifest.json` aligned to the app-manifest schema.
- `index.html` with `ui_bridge` postMessage contract:
  - `app.initialize`
  - `ui.action`
  - `ui.state.sync`
  - `callServerTool`
- `ui://` resources exposed in `geox/mcp/server.py`.

### 2.3 Tool Registry Updates
**File:** `geox/core/tool_registry.py`

New metadata entries registered:
- `geox_evaluate_ac_risk_governed` (PROD)
- `geox_attribute_audit_stub` (PREVIEW)
- `geox_seismic_vision_review_stub` (SCAFFOLD)
- `geox_georeference_map_stub` (SCAFFOLD)
- `geox_analog_digitizer_stub` (SCAFFOLD)

---

## 3. Remaining Work — Acceptance Criteria

### 3.1 AC_Risk Console (AAA Grade)

| # | Task | Acceptance Criteria | Owner |
|---|---|---|---|
| A.1 | UI governance integration | `judge-console/index.html` displays ClaimTag, TEARFRAME bars, and Anti-Hantu pass/fail visually. | GEOX Frontend |
| A.2 | VAULT999 wiring | Every `evaluate_ac_risk_governed` call triggers an actual `VaultClient.seal()` invocation from the MCP server or AF-FORGE bridge. | Platform |
| A.3 | Host event contract | `ac_risk.calculated` and `ac_risk.reset` events are emitted and consumed by at least one MCP host (Claude Desktop / VS Code / arifOS surface). | Integration |
| A.4 | 888_HOLD escalation | When `hold_enforced=True`, the MCP server returns an `888_HOLD` structured response that pauses the host until `forge_approve` is called. | arifOS Kernel |

### 3.2 Attribute Audit (AA Grade)

| # | Task | Acceptance Criteria | Owner |
|---|---|---|---|
| B.1 | Real volume loader | `geox_attribute_audit_stub` replaced by `geox.attribute_audit.load_volume` that reads SEG-Y or ZGY headers. | GEOX Backend |
| B.2 | Attribute compute | `geox.attribute_audit.compute_attribute` supports RMS amplitude, spectral decomposition, and AVO intercept. | GEOX Backend |
| B.3 | Transform chain logger | Every filter/operator is logged with version, parameter hash, and provenance URI. | Platform |
| B.4 | Malay Basin analogs | Cross-check porosity/permeability proxies against Cycle V/VII turbidite analogs with RATLAS lookup. | Domain |
| B.5 | ClaimTag elevation | After local calibration, results can be promoted from `PLAUSIBLE` to `CLAIM` with TEARFRAME truth ≥0.85. | Governance |

### 3.3 Seismic Vision Review (A Grade)

| # | Task | Acceptance Criteria | Owner |
|---|---|---|---|
| C.1 | VLM backend integration | Replace mock fault picks with a real Vision-Language Model (e.g., GPT-4V/Claude 3.5 Sonnet) or a fine-tuned U-Net. | ML |
| C.2 | Physical Firewall (222_REFLECT) | Post-process VLM picks with a physics check: fault trends must align with regional tectonic stress fields. | Domain |
| C.3 | 7-day falsification probe | Host can upload human ground truth; system computes recall/precision and decides promotion to `PLAUSIBLE` or `CLAIM`. | QA |
| C.4 | MCP App rendering | `ui://seismic_vision_review` renders actual seismic slice with overlay picks in a sandboxed iframe. | Frontend |

### 3.4 Georeference Map (A Grade)

| # | Task | Acceptance Criteria | Owner |
|---|---|---|---|
| D.1 | Control point solver | Implement actual GCP → geotransform solving (GDAL/rasterio). | GEOX Backend |
| D.2 | CRS validation | Validate against EPSG registry; reject unsupported or ambiguous CRS strings. | Platform |
| D.3 | Git-backed reversibility | Every georeferencing action creates a commit in a tracked repo; rollback is one command. | DevOps |
| D.4 | F11 filesystem safety | Write operations are sandboxed; no overwrite of source TIFF/PDF permitted. | Governance |

### 3.5 Analog Digitizer (B Grade)

| # | Task | Acceptance Criteria | Owner |
|---|---|---|---|
| E.1 | Preprocessing pipeline | Image deskew, denoise, and grid isolation working on 10+ legacy Malay Basin scans. | ML |
| E.2 | Curve tracker | CNN/RNN tracks GR and RT curves with ≥90% pixel accuracy on test set. | ML |
| E.3 | LAS export | Vectorized curves export to LAS 2.0 with depth and scale validation. | GEOX Backend |
| E.4 | Truth ≥0.99 gate | Digitized output cannot be promoted to `CLAIM` until independently validated against digital source (where available). | Governance |

---

## 4. Governance Checklist for Every App

Before any app can be promoted to the next status (SCAFFOLD → PREVIEW → LIVE), the following must be verified:

- [ ] **F1 Amanah:** All side-effectful operations are reversible or protected by `888_HOLD`.
- [ ] **F2 Truth:** Every `CLAIM` carries TEARFRAME `truth ≥ 0.85` and a direct evidence link.
- [ ] **F4 Entropy:** Transform stacks are logged and risk-accumulated.
- [ ] **F7 Humility:** Confidence bands are explicit; overconfidence triggers `HOLD`.
- [ ] **F9 Anti-Hantu:** Model outputs are screened; empathy simulation is `VOID`.
- [ ] **F11 Coherence:** Output is internally consistent with registry skills and prior state.
- [ ] **F13 Sovereign:** Dangerous or irreversible actions require human approval.
- [ ] **VAULT999:** Terminal verdicts (`SEAL`, `HOLD`, `SABAR`, `VOID`) are hash-chained and persisted.

---

## 5. Architecture Decisions

### ADR-001: Mock-first, Govern-first
We intentionally ship SCAFFOLD apps with mock backends but *complete* governance wiring. This prevents premature "AI magic" while ensuring the host surface, event contract, and constitutional gates are stable.

### ADR-002: Two AC_Risk Entrypoints
We keep `compute_ac_risk` (legacy) and add `evaluate_ac_risk_governed` (canonical). This preserves backward compatibility for existing integrations while steering new development to the hardened path.

### ADR-003: ui:// Resource Pattern
Each GEOX app exposes its HTML via an MCP `ui://` resource. This aligns with the MCP Apps Extension direction and lets any host render the UI without host-side code changes.

---

## 6. Metrics of Success

| Metric | Target | Current |
|---|---|---|
| Governed tools in registry | 10 | 10 |
| Apps with `ui://` resource | 5 | 5 |
| AC_Risk verdicts with ClaimTag | 100% | 100% (governed path) |
| Anti-Hantu violation → VOID | 100% | 100% |
| 888_HOLD on irreversible action | 100% | 100% |

---

*Updated: 2026-04-13*  
*Seal: DITEMPA BUKAN DIBERI — 999 SEAL ALIVE*
