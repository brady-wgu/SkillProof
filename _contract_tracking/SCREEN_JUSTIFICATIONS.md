# Screen Justifications — Storyboard to Contract

> **Internal WGU tracker. Not product specification. JFT does not build from this file.**

**Direction:** Storyboard → Contract. For each storyboard screen, what binding contract requirement does it satisfy?

**Version:** v1.0 (initial baseline)
**Date:** 12 May 2026
**Author:** WGU Program Development
**Source:** brady-wgu/SkillProof at v4.45; signed JFT MSA / SOW (executed 2026)

## How to read this file

Every screen in every persona portal is listed exactly once. Each row carries:

- **Primary Grounding** — the contract requirement(s) the screen primarily exists to satisfy. References use IDs that match `CONTRACT_TRACKER.md` (e.g., `SOW-2.5`, `A-7.10`, `MSA-10`).
- **Supporting Grounding** — secondary requirements the screen also touches.
- **Classification** — Contract-required, Essential scaffolding, or Discretionary. The third class is not allowed to ship at release; every such row must be reclassified or removed.
- **Action** — Keep, Refactor, or Remove (with target release if non-Keep).
- **Anchor** — direct link into the storyboard HTML.

Classification policy:

| Class | Meaning |
|:---|:---|
| **Contract-required** | Screen satisfies a binding requirement from the MSA, SOW, or Appendix A. |
| **Essential scaffolding** | Screen is required for contract-required screens to make sense (navigation, transitions, role-bridging, illustrative LMS/LRPS context). Must have a written reason. |
| **Discretionary** | Nice-to-have without identified contract grounding. Must be reclassified or removed before next release tag. |

---

## Student — Sally · 18 screens · `student/index.html`

> **The student portal was rebuilt v4.58 from screenshots of the deployed JFT MVP at `https://wgu.teamjft.com/`.** The original 34-screen prototype is preserved at git tag `prototype-v4.57-frozen` + GitHub Release. The 18 screens below match the live MVP's distinct states; the SC-MVP-01 through SC-MVP-04 scenarios are now covered by a single unified flow because the deployed MVP runs one persistent flow for Sally rather than four scripted variants.

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `student-01` | Coding Coach Landing (Introduction to Python) | SC-MVP-01 | SOW-2.5 Student Web Experience · A-8.1 LTI 1.3 launch · A-7.3 WCAG 2.2 AA | A-7.1 responsive · A-7.2 mobile-first | Contract-required | Keep | Live entry point post-LTI launch. |
| `student-02` | Diagnostic Q1 empty (Basic Syntax & Data Types) | SC-MVP-01 | SOW-2.5 · A-6.1 multi-LLM · A-6.7 guardrails | A-7.3 | Contract-required | Keep | Diagnostic Q1 — empty answer state. |
| `student-03` | Diagnostic Q1 typed | SC-MVP-01 | SOW-2.5 · A-6.1 · A-6.7 | A-7.3 | Contract-required | Keep | Q1 with answer entered, Submit active. |
| `student-04` | Diagnostic Q1 evaluating | SC-MVP-01 | SOW-2.5 · A-6.1 (LLM evaluation in-flight) | — | Contract-required | Keep | Spinner / "Evaluating…" state. |
| `student-05` | Diagnostic Q1 feedback (5-row objective table) | SC-MVP-01 | SOW-2.5 · A-6.1 · A-6.7 (specific feedback) | A-7.13 visualizations | Contract-required | Keep | Demonstrates objective-by-objective AI feedback with summary + next focus. |
| `student-06` | Diagnostic Q13 final (Introduction to Machine Learning, insufficient) | SC-MVP-01 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | End-of-diagnostic with "Next: Results" CTA. |
| `student-07` | Diagnostic Results (We've established your starting point) | SC-MVP-01 | SOW-2.5 · A-7.10 engagement tracking · A-7.13 visualizations | — | Contract-required | Keep | Mastered Topics + Needs Practice columns + baseline %. |
| `student-08` | Progress Map (13 sub-sections grid) | SC-MVP-01 | SOW-2.5 · A-7.10 · A-7.13 | A-7.3 | Contract-required | Keep | Visualizes Sally's position across 13 sub-sections. |
| `student-09` | Coaching Task empty (Use logical operators) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | A-6.12 (code blocks) | Contract-required | Keep | 2-column adaptive coaching layout. |
| `student-10` | Coaching Task feedback (2-row table + Summary + Next focus) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 (specific feedback) | — | Contract-required | Keep | Demonstrates feedback specificity on practice work. |
| `student-11` | Welcome Back returning user (Sally, 3 weeks later) | SC-MVP-04 | SOW-2.5 (session resume) · A-10.2 retention (3-year FERPA) | A-7.10 | Contract-required | Keep | Multi-week-break resume path. |
| `student-12` | Re-Assessment (Verifying retention) | SC-MVP-04 | SOW-2.5 · A-6.1 (retention verification per Cicada v1) | A-7.10 | Contract-required | Keep | Welcome Back re-assessment with progress bar. |
| `student-13` | Session Saved | SC-MVP-01 | SOW-2.5 (session persistence) · A-10.4 audit (session timestamps) | — | Contract-required | Keep | Exit confirmation with session snapshot. |
| `student-14` | Verification Passed (Gap resolved — difficulty advancing) | SC-MVP-02 | SOW-2.5 · A-6.1 (adaptive difficulty) | A-7.10 engagement | Contract-required | Keep | Foundational → Intermediate → Advanced progression. |
| `student-15` | Adaptive Task Foundational (List Operations) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | Foundational-difficulty adaptive task. |
| `student-16` | Adaptive Feedback Correct (Sally's Answer + green Correct! panel) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | Correct-answer state with "Difficulty will increase" caption. |
| `student-17` | Adaptive Feedback Incorrect (red panel with correction code) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 (specific feedback) | — | Contract-required | Keep | Key feedback-specificity demonstration; same-difficulty retry. |
| `student-18` | Adaptive Verification Same Difficulty (Dictionary Filtering with TIP) | SC-MVP-02 | SOW-2.5 · A-6.1 (verification step per Cicada v1) | — | Contract-required | Keep | Verification step with contextual TIP card. |

Student totals: 18 Contract-required · 0 Essential scaffolding · 0 Discretionary.

---

## Content Creator / Tenant Admin — Alice · 20 screens · `tenant_admin/index.html`

> Persona UI label "Content Creator"; SOW deliverable name "Tenant Admin" (§§2.2, 2.5). Same role.

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `tenant-01` | Welcome to the Tenant Admin Portal (SSO landing) | SC-ADD-02 | SOW-2.5 Admin Portal · A-8.2 SAML SSO · A-10.8 RBAC | — | Contract-required | Keep | LRPS deep-link entry + Instructor LTI baseline + Tenant Admin elevation lookup (v4.29 framing). |
| `tenant-02` | Welcome back, Alice (portal home) | SC-ADD-02 | SOW-2.5 · A-8.6 multi-tenancy (read-only view of other tenants) · A-10.8 RBAC | A-9.1 monitoring summary | Contract-required | Keep | Multi-tenant scoping callout. |
| `tenant-03` | Create a new Subject | SC-ADD-02 | SOW-2.5 (Course-as-a-Service authoring) | A-10.4 audit on creation | Contract-required | Keep | |
| `tenant-04` | Topics & Learning Objectives | SC-ADD-02 | SOW-2.5 · A-10.4 audit on edit | A-7.13 data table viz · A-7.3 accessibility | Contract-required | Keep | v4.47 refactored to inline per-topic expanders with editable text + threshold inputs and inline add / remove (prior weight column was zero-contract-hits and was removed in v4.48). v4.55 added an Overall Skill passing threshold card above the topic expanders — per-objective threshold continues to drive each row; overall threshold is the Skill-level pass gate. Deploy review (screen 7) Step 2 summary updated to show both. |
| `tenant-05` | Model & Coaching (model picker + coaching style) | SC-ADD-02 | A-6.1 multi-LLM · A-6.2 routing by use case · SOW-2.5 (coaching configuration) | A-6.7 (prompt guardrails on the next step) | Contract-required | Keep | v4.48: absorbed prior tenant-10 (Scoring style — Socratic / Direct / Adaptive) and reordered ahead of tenant-06 so model + coaching basics are chosen before any custom prompt overrides. The assessment-pattern-per-objective table that briefly rode here was removed later in v4.48 as it duplicated screen-04 data with no editing affordance. |
| `tenant-06` | Configure the AI Coaching Prompt | SC-ADD-02 | A-6.7 centralized prompt guardrails | A-7.3 | Contract-required | Keep | 4 short text-box guardrails; hallucination warning. |
| `tenant-07` | Deploy E135 to Production | SC-ADD-02 | A-6.24 automated CI/CD pipeline | A-10.4 audit on deploy | Contract-required | Keep | 5-step Stepper (Validate → Build → Test → Deploy → Verify). |
| `tenant-06` | E135 build succeeded (LRPS provisioning ticket) | SC-ADD-02 | A-6.24 · A-8.1 LTI 1.3 launch URL stability | LRPS coordination (illustrative; not a JFT build) | Contract-required | Keep | Manual handoff to WGU D&D team; JFT does not write to LRPS. |
| `tenant-05` | All systems operational | SC-ADD-06 | SOW-9.13 proactive monitoring · A-9.1 24/7 monitoring | — | Contract-required | Keep | SC-ADD-06 baseline. |
| `tenant-10` | Service degradation detected | SC-ADD-06 | SOW-9.13 · A-6.5 fallback mechanisms | — | Contract-required | Keep | |
| `tenant-07` | Service degradation: LLM provider unreachable | SC-ADD-06 | A-6.5 fallback engagement | A-6.6 token tracking (during fallback) | Contract-required | Keep | |
| `tenant-08` | Log a P1 incident in Jira | SC-ADD-06 | SOW-9.1 Jira ticketing · SOW-9.4 channel | A-9.5 SLAs | Contract-required | Keep | |
| `tenant-09` | JFT-SkillProof-2138 created | SC-ADD-06 | SOW-9.1 ticket confirmation · SOW-9.4 | — | Contract-required | Keep | |
| `tenant-10` | JFT-SkillProof-2138: Primary LLM unreachable (CSM chat thread) | SC-ADD-06 | SOW-9.7 CSM · SOW-9.5 P1 SLA <2hr · SOW-9.10 response | — | Contract-required | Keep | CSM Jordan as WGU-facing POC. |
| `tenant-11` | Service restored at 11:08:14 UTC | SC-ADD-06 | A-9.2 99.95% uptime · A-6.5 fallback success | — | Contract-required | Keep | |
| `tenant-12` | 99.95% Uptime SLA (dashboard) | SC-ADD-06 | A-9.2 99.95% uptime · SOW-9.5 SLA verification | A-7.13 visualizations | Contract-required | Keep | Uptime gauge + downtime budget remaining. |
| `tenant-13` | Tenant Settings (identity + branding) | SC-ADD-02 (settings) | A-7.9 customizable interface per institution · A-8.6 multi-tenancy logical isolation · A-9.7 dedicated CSM | A-7.3 accessibility | Contract-required | Keep | v4.50: dual-card layout — left card = read-only Tenant identity (name, ID, parent org, LRPS launch URL, assigned JFT CSM); right card = Branding (light/dark logo uploads, accent color, custom domain). Footer preview not re-added (live footer renders on every page). |
| `tenant-14` | Subject Lifecycle & Archival | SC-ADD-02 (settings) | SOW-2.5 · A-10.4 audit | A-10.2 data retention/deletion | Contract-required | Keep | |
| `tenant-15` | Analytics & Reporting | SC-ADD-02 (analytics) | A-7.10 student engagement tracking · A-7.11 educator analytics · A-7.12 usage statistics & reporting · A-7.13 data visualization · A-7.14 report exports (CSV / PDF / JSON) | A-7.3 accessibility | Contract-required | Keep | v4.51: closes the analytics half of SOW §2.5 ("tenant-level controls for ... analytics") and the five §16.2 UX commitments that had no tenant_admin surface before this release. Three vertically-stacked sections (Engagement charts · Class Insights table with at-risk drill-down · Program Reports filter row + per-report export bar). FERPA-safe: no learner names, counts only. |
| `tenant-16` | Tenant Activity Log | SC-ADD-02 (audit) | A-10.4 audit logging (tenant-scoped view) | A-10.8 RBAC scope enforcement | Contract-required | Keep | v4.51: mirror of `super-08` cross-tenant audit log with implicit `tenant=pdev` filter and no tenant selector. Tenant Admin sees only their tenant's actions; cross-tenant audit remains Super Admin scope. |
| `tenant-21` | Access Denied (zero-trust deny path) | SC-ADD-02 (deny) | A-10.14 zero-trust · A-10.8 RBAC · A-10.4 audit (deny log) | RBAC doc v1.0 §4.2 Figure 6 | Contract-required | Keep | v4.57: Tenant Admin variant of the deny screen — Alice attempts a Super Admin link. Production UI strings only (heading, identity row, required row, two CTAs, log line). |

**SOW §2.5 deviation note** — The Admin Portal commitment in SOW §2.5 lists "Tenant-level controls for configuration, modules, **instructors**, and analytics." The `instructors` control was consciously consolidated under `super-12` (Super Admin) by WGU direction on 13 May 2026 in the v4.48 release, under the principle that Super Admin is the sole controller of platform access. Tenant Admin retains read-only visibility of instructor activity via the portal-home subject rows and the new `tenant-19` Class Insights table; no provisioning, removal, or reassignment affordance exists in tenant_admin. This deviation is intentional and documented; not a contract gap.

Tenant Admin totals: 21 Contract-required · 0 Essential scaffolding · 0 Discretionary.

> Note: `tenant_admin/README.md` references a "Team & Role-Based Access" settings screen alongside Branding / Instructor Roster / Subject Lifecycle. Inventory shows three settings screens (21, 22, 23), not four. Either a Team & Roles screen exists in the HTML without an `id="sN-heading"` anchor (worth grep-confirming during D3a), or the README is stale. Flagged in `CONTRACT_TRACKER.md` row for A-10.8 RBAC.

---

## Instructor — Charlie · 9 screens · `instructor/index.html`

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `instructor-01` | Welcome to the Instructor Dashboard (SSO landing) | SC-ADD-03 | A-8.2 SAML SSO · A-10.8 RBAC (Instructor baseline) | — | Contract-required | Keep | LTI baseline Instructor; no elevation needed (v4.29 framing). |
| `instructor-02` | Instructor Dashboard (course overview) | SC-ADD-03 | A-7.11 Learning analytics dashboard for educators | A-7.10 engagement · A-7.13 viz | Contract-required | Keep | 3 active courses, no traditional sections (rolling enrollment). |
| `instructor-03` | Class heatmap — competency mastery | SC-ADD-03 | A-7.13 visualizations · A-7.10 engagement | A-7.14 export (PDF/CSV CTAs) | Contract-required | Keep | 15 learners × 4 competencies, 9-step color scale. |
| `instructor-04` | 4 learners need attention (at-risk filter applied) | SC-ADD-03 | A-7.10 engagement (intervention) · A-7.11 | A-7.13 | Contract-required | Keep | |
| `instructor-05` | Sally (drill-down profile) | SC-ADD-03 | A-7.11 · A-7.10 | A-10.4 audit (last access) | Contract-required | Keep | v4.28 retargeted to struggle/intervention indicators. |
| `instructor-06` | Sally's coaching sessions (list) | SC-ADD-03 | A-10.4 audit (session log) · A-7.11 | — | Contract-required | Keep | v4.28 added Outcome column with semantic badges. |
| `instructor-07` | Conversation transcript (Session 09) | SC-ADD-03 | A-10.4 audit (full Q/R/feedback capture) · SOW-2.5 (transcript review) | A-6.7 guardrails (AI feedback visibility) | Contract-required | Keep | Charlie's intervention decision point. |
| `instructor-08` | All 47 messages logged (Audit Trail) | SC-ADD-03 | A-10.4 audit logging for all data access/modifications · SOW-9.13 monitoring | — | Contract-required | Keep | FERPA-aware capture-integrity stats. |
| `instructor-09` | Access Denied (zero-trust deny path) | SC-ADD-03 (deny) | A-10.14 zero-trust · A-10.8 RBAC · A-10.4 audit (deny log) | RBAC doc v1.0 §4.2 Figure 6 | Contract-required | Keep | v4.57: Instructor variant of the deny screen — Charlie attempts a School Admin link. Production UI strings only. |

Instructor totals: 9 Contract-required · 0 Essential scaffolding · 0 Discretionary.

---

## Super Admin — Bob · 14 screens · `super_admin/index.html`

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `super-01` | Welcome to the Super Admin Portal (SSO + MFA landing) | SC-ADD-04 | A-8.2 SAML SSO · A-10.18 MFA (TOTP/hardware key) | A-10.4 audit · A-10.14 zero-trust | Contract-required | Keep | Privileged session warning; all actions logged. |
| `super-02` | Super Admin Portal (home — KPIs, alerts, events, quick-links) | SC-ADD-04 | SOW-2.5 · A-9.1 24/7 monitoring · A-9.2 99.95% uptime | A-8.6 multi-tenancy (cross-tenant view) | Contract-required | Keep | 4 KPI gauges. |
| `super-03` | Token usage by tenant | SC-ADD-04 | A-6.6 token usage tracking · A-6.4 rate limiting per institution | A-7.12 usage stats | Contract-required | Keep | Per-tenant utilization meters; PDev flagged. |
| `super-04` | PDev — Foundations of Programming (Python) cost-spike drill-down | SC-ADD-04 | A-6.6 (cost telemetry) · A-6.4 | A-7.13 viz | Contract-required | Keep | 30-bar daily cost chart; top consumers; likely cause. |
| `super-05` | Tighten rate limits — PDev tenant | SC-ADD-04 | A-6.4 rate limiting/quota management | A-10.4 audit (pending entry preview) | Contract-required | Keep | Before/after projection. |
| `super-06` | Compliance report (TLS 1.3 + FERPA + expanded controls) | SC-ADD-04 | A-10.1 FERPA · A-10.7 TLS 1.3 · A-10.6 SOC 2 · A-10.13 ISO 27001 · A-10.14 zero-trust · A-10.12 GDPR · A-10.10 annual pentest · A-10.16 AES-256 at rest · A-10.18 MFA · A-10.15 SIEM · A-10.9 vuln scan · A-10.19 patch SLA · A-10.20 BC/DR | A-9.4 RTO 4hr · A-10.2 retention | Contract-required | Keep | Largest single-screen compliance surface; expanded in v4.18 sweep. |
| `super-07` | Cross-region resilience (geo-redundancy) | SC-ADD-04 | A-9.5 geographic redundancy · A-9.4 RTO < 4 hours · A-10.20 BC/DR | A-9.2 uptime | Contract-required | Keep | 3 region cards; replication lag; recent failover tests. |
| `super-08` | Cross-tenant audit log | SC-ADD-04 | A-10.4 audit logging (cross-tenant) | A-8.6 multi-tenancy | Contract-required | Keep | Surfaces events from Alice, Charlie, JFT CSM, system. |
| `super-09` | User Management (4-tier role taxonomy) | SC-ADD-04 ext | A-10.8 RBAC · SOW-2.5 (instructors/admins management) | A-10.4 audit on elevation | Contract-required | Keep | v4.27 expanded to Student/Instructor/Tenant Admin/Super Admin; v4.29 LTI baseline annotations. |
| `super-10` | External Tooling & Integrations | SC-ADD-04 ext | SOW-5 Technology Stack · A-6.1 multi-LLM (provider dashboards) | — | Contract-required | Keep | v4.28 hub to AWS / OpenRouter / etc. Avoids duplicating provider UIs. |
| `super-11` | Data & Integrations Hub (data export · webhooks · GraphQL · streaming) | SC-ADD-04 ext (proposed: SC-ADD-08 Data & Integrations) | A-6.28 GraphQL API · A-8.8 real-time/batch export · A-8.12 webhooks · A-8.13 GraphQL queries · A-8.14 data streaming | A-6.22 REST API · A-8.11 API docs (link card) | Contract-required | Keep | v4.45 closed the remaining 5 D3a true-gap items on this single new surface. Cross-tenant scope; consolidates data-export functions moved from tenant_admin in v4.22. |
| `super-12` | Instructor Roster & Course Assignment (cross-tenant) | SC-ADD-04 ext | SOW-2.5 · A-10.8 RBAC · A-10.4 audit | A-10.13 platform access governance | Contract-required | Keep | v4.48: moved from tenant_admin (prior `tenant-22`) under WGU direction that Super Admin is the sole controller of platform access. Cross-tenant scope; per-tenant filter at the top. v4.52: tenant labels normalized to WGU Schools; Skill-assignment authority callout added. |
| `super-13` | School / Tenant Management | SC-ADD-04 ext | A-8.6 multi-tenancy isolation · A-10.8 RBAC · SOW-2.5 Admin Portal | A-10.4 audit on School creation / deactivation | Contract-required | Keep | v4.52: Super Admin manages the 4 WGU Schools as tenants. List + per-row Manage + top-of-page `Create new School`. Grounding: Brady's RBAC doc v1.0 (13 May 2026) — "tenants = WGU Schools." |
| `super-14` | Access Denied (zero-trust deny path) | SC-ADD-04 (deny) | A-10.14 zero-trust · A-10.8 RBAC · A-10.4 audit (deny log) | RBAC doc v1.0 §4.2 Figure 6 | Contract-required | Keep | v4.57: Super Admin variant of the deny screen — expired/revoked provisioning. Production UI strings only. |

Super Admin totals: 14 Contract-required · 0 Essential scaffolding · 0 Discretionary.

---

## LRPS Landing (storyboard root) · 1 screen · `index.html`

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `lrps-01` | LRPS Landing (provider table + quick-launch) | LRPS handoff | — | A-8.1 LTI 1.3 launch URL stability (illustration) | Essential scaffolding | Keep | WGU's internal Learning Resource Provisioning System. JFT does not build LRPS; this screen makes the deep-link source feel authentic in the storyboard. Reviewed with JFT 06 Apr 2026 (LRPS team). **v4.59 (18 May 2026):** the LRPS surface was promoted to the storyboard root (`index.html`); the previous separate `/lrps/` URL retired. The portal-selector landing that previously sat at root was removed entirely. |

LRPS totals: 0 Contract-required · 1 Essential scaffolding · 0 Discretionary.

---

## Help & Resources · 1 screen · `help/index.html`

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `help-01` | Help & Resources (search, self-service cards, updates feed, role-filtered video gallery, Contact JFT Support FAB) | SC-ADD-07 (proposed for post-MVP support release) | A-9.14 Self-service support portal · A-9.15 Video training resources | A-9.1 24/7 monitoring (Contact JFT Support entry point) · A-9.4/§9.4 support channels · A-9.11 documentation/training materials | Contract-required | Keep | v4.45 introduced the shared surface. Persona: all admin roles (Tenant Admin / Instructor / Super Admin) plus LRPS admin. The student portal is frozen at v1.2 MVP and cannot link to Help & Resources yet; this is a post-MVP shared surface only. Closes the two true gaps from the v4.36 D3a re-audit for the Support & Training theme. |

Help & Resources totals: 1 Contract-required · 0 Essential scaffolding · 0 Discretionary.

---

## Totals across all surfaces

| Persona | Screens | Contract-required | Essential scaffolding | Discretionary |
|:---|:---:|:---:|:---:|:---:|
| Student (Sally) | 18 | 18 | 0 | 0 |
| Tenant Admin (Alice) | 21 | 21 | 0 | 0 |
| Instructor (Charlie) | 9 | 9 | 0 | 0 |
| Super Admin (Bob) | 14 | 14 | 0 | 0 |
| LRPS | 1 | 0 | 1 | 0 |
| Help & Resources (shared) | 1 | 1 | 0 | 0 |
| **Total** | **64** | **63** | **1** | **0** |

**Zero Discretionary screens at v4.58 baseline.** Every screen is either Contract-required or Essential scaffolding with a written reason.

---

## Change log

| Version | Date | Status | Notes |
|:---|:---|:---|:---|
| 1.0 | 12 May 2026 | Superseded | Initial baseline. 76 screens cataloged. 71 Contract-required, 5 Essential scaffolding, 0 Discretionary. |
| 1.1 | 18 May 2026 | Superseded | v4.57 RBAC pass added 3 Access Denied screens (tenant-21, super-14, instructor-09). v4.58 student rebuild reduced student count 34→18 to match live MVP (`https://wgu.teamjft.com/`). Original student section preserved at git tag `prototype-v4.57-frozen`. Total: 64 screens, 63 Contract-required, 1 Essential scaffolding, 0 Discretionary. |
| 1.2 | 18 May 2026 | Current | v4.59 entry-point consolidation. The LRPS surface was promoted to the storyboard root (`index.html`); the standalone `lrps/` folder was deleted and the separate portal-selector landing that previously sat at root was retired entirely. Surface and screen counts unchanged (LRPS-01 still cataloged; file path updated `lrps/index.html` → `index.html`). The 3 admin Access Denied "Open the correct LRPS link" CTAs now point at the storyboard root. |

---

*WGU confidential. Author: WGU Program Development. Not for redistribution outside WGU.*
