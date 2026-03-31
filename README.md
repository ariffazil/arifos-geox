# GEOX: Earth Witness & Inverse Modelling Supervisor (v0.4.2)

> **DITEMPA BUKAN DIBERI**
>
> GEOX is the **Earth Witness** organ in the arifOS federation — the reality gatekeeper that ensures all reasoning and decision-making is physically possible, geospatially grounded, and consistent with world-state evidence.

---

## 🧭 Forward vs Inverse Modeling in arifOS

| Modeling Type | Description | Who Does It? | MCP Role |
| :--- | :--- | :--- | :--- |
| **Forward Modeling** | Simulate outcomes from known inputs | **GEOX tools** | Exposed as **MCP tools** under `geox.*` |
| **Inverse Modeling** | Infer model parameters from observed data | **@RIF** + GEOX | @RIF calls MCP tools to constrain hypotheses |

In this architecture:
- **GEOX tools** do **forward modeling** — simulate what the Earth would look like under a given model.
- **@RIF** does **inverse modeling** — proposes models and tests them against Earth evidence via GEOX.

---

## 🧠 What Is "AI" in This Stack?

In arifOS, **AI is not a monolithic model**, but a **federated organ system**:
- **@RIF**: Reasoning (Inverse modeling, hypothesis generation)
- **GEOX**: Earth Verification (Forward modeling, constraint enforcement)
- **@WEALTH**: Decision logic (Economic modeling)
- **@WELL**: Human energy modeling
- **@PROMPT**: Task shaping
- **@JUDGE**: Human veto

The AI is a **constitutional federation of organs**, each with a bounded role, runtime contracts, and floor enforcement.

---

## 🧬 GEOX as an MCP Agent

GEOX is embedded as a **governed MCP agent** with:
- **Tool Surface**: `geox.load_seismic_line`, `geox.feasibility_check`, `geox.verify_geospatial`, etc.
- **Resource Surface**: Terrain maps, climate data, logistics tables, and subsurface repositories.
- **System Prompt**: Defines its identity as the Earth Witness and its bounded role in the federation.
- **Telemetry Block**: Every output is sealed, calibrated, and audit-ready (v0.4.2).

It is not a plugin. It is a **Constitutional Firewall**.

---

## 🚀 Deployment (via FastMCP)

GEOX is now fully compatible with the **FastMCP** declarative deployment model.

### 1. Quick Start (Development)
```bash
# Run via FastMCP (Auto-detects fastmcp.json)
fastmcp run

# Or run with the inspector UI
fastmcp dev
```

### 2. Network Deployment (HTTP)
To deploy as a network-accessible service in the arifOS federation:
```bash
fastmcp run --transport http --port 8000
```

### 3. Manual Execution
```bash
# Default (STDIO)
python geox_mcp_server.py

# HTTP Mode
python geox_mcp_server.py --transport http --port 8000
```

---

## 🛠 Toolset Configuration (v0.4.2)

| Tool | Role | Protocol | Namespace |
| :--- | :--- | :--- | :--- |
| `geox_load_seismic_line` | **Visual Ignition** | FastMCP (Visual) | `geox.load_seismic_line` |
| `geox_build_structural_candidates` | **Constraint Provider** | Hardened Continuity | `geox.build_structural_candidates` |
| `geox_feasibility_check` | **Physical Firewall** | 222_REFLECT | `geox.feasibility_check` |
| `geox_verify_geospatial` | **Spatial Grounding** | Coordinate Validation | `geox.verify_geospatial` |
| `geox_evaluate_prospect` | **Governed Verdict** | SEALED Audit | `geox.evaluate_prospect` |

---

## 🛡 Theory of Anomalous Contrast (ToAC)

GEOX implements **ToAC** to prevent AI hallucinations in subsurface interpretation. This theory posits that "Anomalous Contrast" (display artifacts or processing biases) is the primary driver of geological misinterpretation.

By enforcing the **Contrast Canon**, GEOX mandates:
1. **Multi-Model Candidates**: Never collapse into a single inverse solution too early.
2. **Physical Attributes**: All visual interpretation must be anchored in deterministic physics (coherence, curvature).
3. **Bias Auditing**: Explicitly check for professional bias (Bond et al. 2007) before sealing a verdict.

---

## 🔐 System State: SEALED ✅

GEOX v0.4.2 is production-hardened and ready for integration into the `trinity-000-999-pipeline`.

**DITEMPA BUKAN DIBERI.**
