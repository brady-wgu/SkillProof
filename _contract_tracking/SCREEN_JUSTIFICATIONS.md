# Screen Justifications — Storyboard to Contract

> **Internal WGU tracker. Not product specification. JFT does not build from this file.**

**Direction:** Storyboard → Contract. For each storyboard screen, what binding contract requirement does it satisfy?

**Version:** v1.0 (initial baseline)
**Date:** 12 May 2026
**Author:** WGU Program Development
**Source:** brady-wgu/JFT_SDP at v4.34; signed JFT MSA / SOW (executed 2026)

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

## Student — Sally · 34 screens · `student/index.html`

> **The student portal is frozen as of v4.34.** WGU authorizes student-side changes individually. The classifications below document grounding for the existing screens; they do not authorize edits.

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `student-01` | 1.1 Welcome to Foundations of Programming (zyBooks LTI launch context) | SC-MVP-01 | — | A-8.1 LTI 1.3 launch (illustration) | Essential scaffolding | Keep | Reference design only; zyBooks page is not a JFT deliverable. Documented as such in `student/README.md`. |
| `student-02` | Coding Coach (welcome) | SC-MVP-01 | SOW-2.5 Student Web Experience · A-8.1 LTI 1.3 launch · A-7.3 WCAG 2.2 AA | A-7.1 responsive · A-7.2 mobile-first | Contract-required | Keep | First post-launch screen after SSO. |
| `student-03` | Basic Syntax & Data Types (diagnostic) | SC-MVP-01 | SOW-2.5 · A-6.1 multi-LLM · A-6.7 guardrails | A-7.3 accessibility | Contract-required | Keep | Diagnostic question 1. |
| `student-04` | Control Flow & Logic (diagnostic) | SC-MVP-01 | SOW-2.5 · A-6.1 · A-6.7 | A-7.3 | Contract-required | Keep | Diagnostic question 2. |
| `student-05` | We've established your starting point (diagnostic results) | SC-MVP-01 | SOW-2.5 · A-7.10 engagement tracking | A-7.13 visualizations | Contract-required | Keep | Diagnostic outcome summary. |
| `student-06` | Progress Map | SC-MVP-01 | SOW-2.5 · A-7.10 engagement · A-7.13 visualizations | A-7.3 accessibility | Contract-required | Keep | Visualizes Sally's position across 13 sub-sections. |
| `student-07` | Variables & Assignment (first coaching task) | SC-MVP-01 | SOW-2.5 · A-6.1 · A-6.7 | A-6.12 LaTeX (code blocks) | Contract-required | Keep | First adaptive coaching task. |
| `student-08` | Your progress has been saved | SC-MVP-01 | SOW-2.5 (session persistence) | A-10.4 audit (session timestamps) | Contract-required | Keep | Exit confirmation. |
| `student-09` | 1.1 Welcome to Foundations of Programming (SC-MVP-02 entry) | SC-MVP-02 | — | A-8.1 (illustration) | Essential scaffolding | Keep | Reference design. Same as `student-01`. |
| `student-10` | Coding Coach (SC-MVP-02 welcome) | SC-MVP-02 | SOW-2.5 · A-8.1 · A-7.3 | A-7.1 · A-7.2 | Contract-required | Keep | |
| `student-11` | Basic Syntax & Data Types | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | Diagnostic across multiple sub-sections. |
| `student-12` | Control Flow & Logic | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | Diagnostic. |
| `student-13` | Data Structures: Lists, Tuples, Sets, Dictionaries | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | Diagnostic. |
| `student-14` | Your Progress Map | SC-MVP-02 | SOW-2.5 · A-7.10 · A-7.13 | A-7.3 | Contract-required | Keep | Progress map after diagnostic. |
| `student-15` | List Operations (coaching task) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | Foundational difficulty. |
| `student-16` | Dictionary Iteration (incorrect answer + targeted feedback) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 (specific feedback) | — | Contract-required | Keep | Key feedback-specificity demonstration. |
| `student-17` | Dictionary Filtering (gap-resolution verification) | SC-MVP-02 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | |
| `student-18` | Gap resolved — difficulty advancing | SC-MVP-02 | SOW-2.5 · A-6.1 (adaptive difficulty) | A-7.10 engagement | Contract-required | Keep | |
| `student-19` | Your progress has been saved | SC-MVP-02 | SOW-2.5 · A-10.4 | — | Contract-required | Keep | |
| `student-20` | 1.1 Welcome to Foundations of Programming (SC-MVP-03 entry) | SC-MVP-03 | — | A-8.1 (illustration) | Essential scaffolding | Keep | Reference design. |
| `student-21` | Coding Coach (SC-MVP-03 welcome) | SC-MVP-03 | SOW-2.5 · A-8.1 · A-7.3 | — | Contract-required | Keep | |
| `student-22` | Basic Syntax & Data Types (fast-track diagnostic) | SC-MVP-03 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | |
| `student-23` | Control Flow & Logic | SC-MVP-03 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | |
| `student-24` | Advanced Data Handling | SC-MVP-03 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | |
| `student-25` | Data Structures: Lists, Tuples, Sets, Dictionaries | SC-MVP-03 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | |
| `student-26` | Strong baseline detected | SC-MVP-03 | SOW-2.5 (fast-track logic per Cicada v1) | A-7.10 | Contract-required | Keep | |
| `student-27` | Write a Python Module (verification task) | SC-MVP-03 | SOW-2.5 · A-6.1 (text-evaluated by LLM) | — | Contract-required | Keep | LLM-only evaluation; no code execution per v1 known limitations. |
| `student-28` | No coaching gaps identified | SC-MVP-03 | SOW-2.5 · A-7.10 | — | Contract-required | Keep | |
| `student-29` | 1.1 Welcome to Foundations of Programming (SC-MVP-04 entry) | SC-MVP-04 | — | A-8.1 (illustration) | Essential scaffolding | Keep | Reference design. |
| `student-30` | Welcome back, Sally (returning learner) | SC-MVP-04 | SOW-2.5 (session resume) · A-10.2 retention (3-year FERPA) | A-7.10 | Contract-required | Keep | Multi-week-break resume path. |
| `student-31` | Data Structures: Lists, Tuples, Sets, Dictionaries (resume) | SC-MVP-04 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | |
| `student-32` | Control Flow & Logic (adaptive difficulty drop) | SC-MVP-04 | SOW-2.5 · A-6.1 (regression handling per Cicada v1) | — | Contract-required | Keep | |
| `student-33` | Dictionary Operations | SC-MVP-04 | SOW-2.5 · A-6.1 · A-6.7 | — | Contract-required | Keep | |
| `student-34` | Your progress has been saved | SC-MVP-04 | SOW-2.5 · A-10.4 | — | Contract-required | Keep | |

Student totals: 30 Contract-required · 4 Essential scaffolding · 0 Discretionary.

---

## Content Creator / Tenant Admin — Alice · 23 screens · `tenant_admin/index.html`

> Persona UI label "Content Creator"; SOW deliverable name "Tenant Admin" (§§2.2, 2.5). Same role.

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `tenant-01` | Welcome to the Tenant Admin Portal (SSO landing) | SC-ADD-02 | SOW-2.5 Admin Portal · A-8.2 SAML SSO · A-10.8 RBAC | — | Contract-required | Keep | LRPS deep-link entry + Instructor LTI baseline + Tenant Admin elevation lookup (v4.29 framing). |
| `tenant-02` | Welcome back, Alice (portal home) | SC-ADD-02 | SOW-2.5 · A-8.6 multi-tenancy (read-only view of other tenants) · A-10.8 RBAC | A-9.1 monitoring summary | Contract-required | Keep | Multi-tenant scoping callout. |
| `tenant-03` | Create a new Subject | SC-ADD-02 | SOW-2.5 (Course-as-a-Service authoring) | A-10.4 audit on creation | Contract-required | Keep | |
| `tenant-04` | Topics & Learning Objectives | SC-ADD-02 | SOW-2.5 · A-10.4 audit on edit | A-7.13 data table viz | Contract-required | Keep | Per-LO threshold + weight integrated in table. |
| `tenant-05` | Add a Learning Objective | SC-ADD-02 | SOW-2.5 · A-10.4 audit | A-7.3 accessibility | Contract-required | Keep | Per-LO threshold + weight form. |
| `tenant-06` | Edit Learning Objective 1.3 | SC-ADD-02 | SOW-2.5 · A-10.4 audit | A-7.3 | Contract-required | Keep | |
| `tenant-07` | Remove Learning Objective 4.3? | SC-ADD-02 | SOW-2.5 · A-10.4 audit | A-7.3 | Contract-required | Keep | Confirmation flow with audit trail context. |
| `tenant-08` | Configure the AI Coaching Prompt | SC-ADD-02 | A-6.7 centralized prompt guardrails | A-7.3 | Contract-required | Keep | 4 short text-box guardrails; hallucination warning. |
| `tenant-09` | Choose the Preferred Model | SC-ADD-02 | A-6.1 multi-LLM · A-6.2 routing by use case | — | Contract-required | Keep | Per-Subject model picker. |
| `tenant-10` | Scoring style & coaching defaults | SC-ADD-02 | SOW-2.5 (coaching configuration) | A-6.7 | Contract-required | Keep | Socratic / Direct / Adaptive. |
| `tenant-11` | Deploy E135 to Production | SC-ADD-02 | A-6.24 automated CI/CD pipeline | A-10.4 audit on deploy | Contract-required | Keep | 5-step Stepper (Validate → Build → Test → Deploy → Verify). |
| `tenant-12` | E135 build succeeded (LRPS provisioning ticket) | SC-ADD-02 | A-6.24 · A-8.1 LTI 1.3 launch URL stability | LRPS coordination (illustrative; not a JFT build) | Contract-required | Keep | Manual handoff to WGU D&D team; JFT does not write to LRPS. |
| `tenant-13` | All systems operational | SC-ADD-06 | SOW-9.13 proactive monitoring · A-9.1 24/7 monitoring | — | Contract-required | Keep | SC-ADD-06 baseline. |
| `tenant-14` | Service degradation detected | SC-ADD-06 | SOW-9.13 · A-6.5 fallback mechanisms | — | Contract-required | Keep | |
| `tenant-15` | Service degradation: LLM provider unreachable | SC-ADD-06 | A-6.5 fallback engagement | A-6.6 token tracking (during fallback) | Contract-required | Keep | |
| `tenant-16` | Log a P1 incident in Jira | SC-ADD-06 | SOW-9.1 Jira ticketing · SOW-9.4 channel | A-9.5 SLAs | Contract-required | Keep | |
| `tenant-17` | JFT-SDP-2138 created | SC-ADD-06 | SOW-9.1 ticket confirmation · SOW-9.4 | — | Contract-required | Keep | |
| `tenant-18` | JFT-SDP-2138: Primary LLM unreachable (CSM chat thread) | SC-ADD-06 | SOW-9.7 CSM · SOW-9.5 P1 SLA <2hr · SOW-9.10 response | — | Contract-required | Keep | CSM Jordan as WGU-facing POC. |
| `tenant-19` | Service restored at 11:08:14 UTC | SC-ADD-06 | A-9.2 99.95% uptime · A-6.5 fallback success | — | Contract-required | Keep | |
| `tenant-20` | 99.95% Uptime SLA (dashboard) | SC-ADD-06 | A-9.2 99.95% uptime · SOW-9.5 SLA verification | A-7.13 visualizations | Contract-required | Keep | Uptime gauge + downtime budget remaining. |
| `tenant-21` | Branding & Customization | SC-ADD-02 (settings) | A-7.9 customizable interface per institution · A-7.6 multi-language · A-7.7 PWA | A-7.3 | Contract-required | Keep | |
| `tenant-22` | Instructor Roster & Course Assignment | SC-ADD-02 (settings) | SOW-2.5 · A-10.8 RBAC | A-10.4 audit | Contract-required | Keep | |
| `tenant-23` | Subject Lifecycle & Archival | SC-ADD-02 (settings) | SOW-2.5 · A-10.4 audit | A-10.2 data retention/deletion | Contract-required | Keep | |

Tenant Admin totals: 23 Contract-required · 0 Essential scaffolding · 0 Discretionary.

> Note: `tenant_admin/README.md` references a "Team & Role-Based Access" settings screen alongside Branding / Instructor Roster / Subject Lifecycle. Inventory shows three settings screens (21, 22, 23), not four. Either a Team & Roles screen exists in the HTML without an `id="sN-heading"` anchor (worth grep-confirming during D3a), or the README is stale. Flagged in `CONTRACT_TRACKER.md` row for A-10.8 RBAC.

---

## Instructor — Charlie · 8 screens · `instructor/index.html`

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

Instructor totals: 8 Contract-required · 0 Essential scaffolding · 0 Discretionary.

---

## Super Admin — Bob · 10 screens · `super_admin/index.html`

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
| `super-09` | User Management (4-tier role taxonomy) | SC-ADD-04 ext | A-10.8 RBAC · SOW-2.5 (instructors/admins management) | A-10.4 audit on elevation | Contract-required | Keep | v4.27 expanded to Student/Instructor/Tenant Admin/Global Admin; v4.29 LTI baseline annotations. |
| `super-10` | External Tooling & Integrations | SC-ADD-04 ext | SOW-5 Technology Stack · A-6.1 multi-LLM (provider dashboards) | — | Contract-required | Keep | v4.28 hub to AWS / OpenRouter / etc. Avoids duplicating provider UIs. |

Super Admin totals: 10 Contract-required · 0 Essential scaffolding · 0 Discretionary.

---

## LRPS Landing · 1 screen · `lrps/index.html`

| ID | Title | Scenario | Primary Grounding | Supporting Grounding | Classification | Action | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `lrps-01` | LRPS Landing (provider table + quick-launch) | LRPS handoff | — | A-8.1 LTI 1.3 launch URL stability (illustration) | Essential scaffolding | Keep | WGU's internal Learning Resource Provisioning System. JFT does not build LRPS; this screen makes the deep-link source feel authentic in the storyboard. Reviewed with JFT 06 Apr 2026 (LRPS team). |

LRPS totals: 0 Contract-required · 1 Essential scaffolding · 0 Discretionary.

---

## Totals across all surfaces

| Persona | Screens | Contract-required | Essential scaffolding | Discretionary |
|:---|:---:|:---:|:---:|:---:|
| Student (Sally) | 34 | 30 | 4 | 0 |
| Tenant Admin (Alice) | 23 | 23 | 0 | 0 |
| Instructor (Charlie) | 8 | 8 | 0 | 0 |
| Super Admin (Bob) | 10 | 10 | 0 | 0 |
| LRPS | 1 | 0 | 1 | 0 |
| **Total** | **76** | **71** | **5** | **0** |

**Zero Discretionary screens at v1.0 baseline.** Every screen is either Contract-required or Essential scaffolding with a written reason.

---

## Change log

| Version | Date | Status | Notes |
|:---|:---|:---|:---|
| 1.0 | 12 May 2026 | Current | Initial baseline. 76 screens cataloged. 71 Contract-required, 5 Essential scaffolding, 0 Discretionary. |

---

*WGU confidential. Author: WGU Program Development. Not for redistribution outside WGU.*
