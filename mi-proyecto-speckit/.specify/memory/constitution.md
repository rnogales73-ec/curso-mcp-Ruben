<!--
Sync Impact Report:
- Version change: Initial template -> 1.0.0
- Added sections: Core Principles (I-V), Technology Stack & Environment, Development Workflow & Quality Gates, Governance
- Modified principles: Replaced placeholders with project-aligned principles for Python / Spec-Kit development
- Removed sections: None
- Follow-up TODOs: None
-->

# curso-mcp-Ruben Constitution

## Core Principles

### I. Spec-First & Document-Driven Development
Every feature, module, or behavioral adjustment MUST begin with a specification (spec.md) and a plan (plan.md). Implementation code MUST NOT precede defined requirements and measurable acceptance criteria. Ambiguities must be resolved before tasks are generated and executed.

### II. Test-First (TDD Mandate)
Testing is non-negotiable. Unit and integration test suites MUST be authored against specifications before declaring feature implementation complete. All tests MUST pass via uv run pytest before any deliverable is integrated.

### III. Python Tooling & Dependency Hygiene via uv
All Python dependencies, virtual environments, and script executions MUST be managed exclusively using uv and declared in pyproject.toml. Direct global package installations (e.g. pip install without virtualenv management) are strictly prohibited.

### IV. Clean Architecture & CLI Explicability
Core business logic (such as temperature conversions or LLM client integrations) MUST remain decoupled from presentation or I/O layers. Scripts intended for user interaction MUST provide clear, resilient CLI interfaces with explicit error feedback on invalid inputs instead of unhandled exceptions.

### V. Defensive Boundary Handling & Input Validation
Functions and interfaces MUST validate inputs at public boundaries. Values outside domain bounds (e.g. temperatures below absolute zero or invalid non-numeric inputs) MUST fail fast with explicit, descriptive error messages.

## Technology Stack & Environment Constraints

- **Language & Runtime**: Python >= 3.13.
- **Package & Environment Manager**: uv.
- **Testing Framework**: pytest executed through uv run pytest.
- **Integrations**: Gemini API (google-genai), environment loading (python-dotenv), terminal formatting (ich).

## Development Workflow & Quality Gates

1. **Specification**: Establish requirements, user journeys, edge cases, and acceptance scenarios via Spec-Kit.
2. **Review Gate**: Verify the specification meets domain criteria and covers failure modes.
3. **Planning & Task Breakdown**: Decompose features into independent, verifiable tasks.
4. **Implementation & Verification**: Implement changes alongside automated tests. Run uv run pytest to ensure 100% test pass rate.
5. **No Regression**: Existing functionality and test suites must remain intact after each iteration.

## Governance

This Constitution represents the authoritative development guidelines for curso-mcp-Ruben. Any amendments to principles or workflow gates require documentation, rationale, and a version increment according to Semantic Versioning:
- **MAJOR**: Incompatible principle redefinitions or workflow overhaul.
- **MINOR**: Addition of new principles, tooling mandates, or quality gates.
- **PATCH**: Clarifications, formatting adjustments, or non-semantic refinements.

**Version**: 1.0.0 | **Ratified**: 2026-09-03 | **Last Amended**: 2026-09-03
