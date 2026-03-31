# Changelog

All notable changes to the GEOX project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.2] — 2026-04-01

### Added

- **Constitutional Firewall**: Added `geox_feasibility_check` and `geox_verify_geospatial` tools for physical grounding of @RIF's inverse modeling.
- **Epistemic Mapping**: Incorporated the 'Forward vs Inverse Modeling' ontology into the core system documentation.
- **Multimodal Grounding**: Enhanced `geox_load_seismic_line` to prepare constraints for orchestrated @RIF reasoning.

### Fixed

- **MCP Tool Names**: Standardized on the `geox.*` namespace for all MCP-exposed tools.
- **Lint Cleanup**: Resolved multiple lint/formatting errors across the code and docs.

## [0.4.1] — 2026-03-31

### Added (v0.4.1)

- **Inverse Modelling Supervisor**: Hardened `SeismicSingleLineTool` to prevent narrative collapse using "Plausible Inverse Models."
- **Governed Verdicts**: Integrated `compute_contrast_verdict` for physical grounding at the tool boundary.

## [0.4.0] — 2026-03-31

### Added (v0.4.0)

- **Hardened Continuity**: Implemented `HardenedToolOutput` and `ContinuityRecord` across all MCP tool contracts.
- **Theory of Anomalous Contrast (ToAC)**: First-class integration of contrast-canon enforcement in visual pipelines.
- **FastMCP Transport**: Upgraded the local server to FastMCP for standard arifOS federation binding.

## [0.3.5] — 2026-03-31

### Added (v0.3.5)

- **Visual Ignition Engine**: Added `geox_load_seismic_line` with multi-contrast payload support.
- **Structural Candidate Generator**: Initial forge of the interpretation candidate tool.

---

**DITEMPA BUKAN DIBERI**
