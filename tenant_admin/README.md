# Tenant Admin — Alice · v1.3

[← Back to root README](../README.md) · [Live portal](https://brady-wgu.github.io/JFT_SDP/tenant_admin/) · [Catalog](../presentation.html#sc-add-02)

![Tenant Admin Portal hero](screenshots/sc-add-02_step02_screen02.png)

## Persona

**Alice** — WGU **Program Development (PDev) content owner**. Authenticates via her own secret LRPS deep link. Multi-tenant SaaS scoping limits her view to her assigned Program Subject (Foundations of Programming – Python).

## Scope

Multi-tenancy, RBAC, the Course-as-a-Service administrative UI, integration APIs and data export commitments, and the Support Plan / SLA workflow.

## Scenarios

This portal covers **three v1.3 scenarios** in one cohesive Alice experience, plus four supporting **Tenant Settings** screens accessible from the Portal home (Branding + Team & Roles + Instructor Roster + Subject Lifecycle):

| ID | Description | Screens | Screen IDs |
|:---|:------------|:-------:|:----------:|
| **SC-ADD-02** | **Tenant Admin Portal & Course Configuration.** Multi-tenant scoping → Subject creation → Topics & Learning Objectives → AI prompt config (toggles for profile data, domain limits, jailbreak guard, sandbox; custom system prompt addendum; right-pane compiled-prompt preview; one-line "Last edited" indicator with deferred diff/rollback) → preferred model picker (Claude / GPT / Gemini radio cards) → scoring rubric → Deploy to Production triggers automated CI/CD pipeline (5-step Stepper) → success panel with live-course link. **Plus four Tenant Settings:** Branding & Customization (§7.9), Team & Role-Based Access (§10.8 — internal Owner/Editor/Viewer for the Tenant Admin Portal itself), Instructor Roster & Course Assignment (§2.5 + §10.8 — 7-instructor table including Program Mentors with E010/E075/E135 course chips, active-learner counts, recent-assignment audit log, bulk import option; LRPS owns account provisioning, this screen owns course-level assignment), and Subject Lifecycle & Archival (§2.5 module lifecycle + §10.4 audit logging — active subjects table with deactivation flow, archived subjects with FERPA-aligned 7-year retention, deactivation-preview panel showing cutover date / retention policy / audit warning). | 13 | 1–9, 24–27 |
| **SC-ADD-05** | **Data Portability.** Data & APIs landing → REST API console (method + endpoint + query params, auth/scoping side panel, rate-limit display) → sample JSON response (syntax-highlighted code block) → one-click export wizard (engagement metrics dataset) → format picker (CSV / JSON tab switcher with 5-row preview) → download confirmation with file metadata + audit ID. | 6 | 10–15 |
| **SC-ADD-06** | **Critical Incident Response & SLA Verification.** All-systems-operational baseline → primary LLM provider down → Fallback engaged automatically → notification email / toast → P1 ticket creation form (prefilled from monitoring) → JFT-SDP-2138 confirmation → JFT CSM chat thread (within 2-hr SLA) → service-restored verification → SLA dashboard showing 99.97% uptime maintained. | 8 | 16–23 |

**Total: 3 scenarios · 27 screens.**

## Source

JFT SDP User Scenario Catalog: Additional Scenarios **v1.3** (05 May 2026). Authored by Brady Redfearn, WGU Program Development.

## SOW references

| Scenario | SOW refs | Where covered |
|:---------|:---------|:--------------|
| SC-ADD-02 | §8.6 (Multi-tenancy), §2.5 (Tenant Admin Portal — Course Configuration, modules, instructors, analytics), §6.24 (CI/CD), §10.8 (RBAC), §7.9 (Custom Branding), §10.4 (Audit Logging) | §8.6 → screen 2 (scoping callout); §2.5 (config) → whole portal; §6.24 → screen 8 (Stepper); §10.8 → screen 25 (internal Team & Roles) + screen 26 (instructor course assignment); §7.9 → screen 24 (Branding); §2.5 (modules lifecycle) + §10.4 → screen 27 (Subject Lifecycle); §2.5 (instructors) → screen 26 (Instructor Roster); §6.7 prompt guardrails → screen 5 inline G9 versions panel |
| SC-ADD-05 | §8.7 (API), §7.14 (Export Capability), §8.9 (Data Formats) |
| SC-ADD-06 | §6.5 (AI Fallback), §9.2 (Uptime), §9.5 (SLAs), §9.7 (CSM), §9.10 (Response time), §9.13 (Monitoring) |

## Files

- [`index.html`](index.html) — interactive storyboard (27 screens, 3 scenario flows + 4 supporting Tenant Settings screens)
- `screenshots/` — 27 light-theme PNGs at 1440×900
- `screenshots_dark/` — 27 dark-theme PNGs

## Components introduced in this portal

- 5-step **Stepper** for the CI/CD pipeline (Validate → Build → Test → Deploy → Verify)
- **REST API console** — method pill + endpoint input + query-param table + auth/scoping side panel
- **JSON code block** with syntax highlighting (`#0d1117` dark theme)
- **Tab switcher** (segmented control) for CSV / JSON format selection (per SOW §8.9)
- **File-meta card** for download confirmations
- **Uptime gauge** + **SLA dashboard** with downtime budget remaining
- **Chat-thread / chat-bubble / chat-avatar** for the JFT CSM response thread
- **Soft-tint feedback panels** (success / warning / danger) with left-edge accent stripe

## Notes

- The "Deploy to Production" CTA triggers the simulated CI/CD pipeline. The Stepper component models the live progression through Validate → Build → Test → Deploy → Verify with status badges per step.
- Tenant scoping is enforced at every layer: Subject creation locks the Program Subject field; the API console shows the bearer token last-4 + "Scoped to: pdev / Foundations…"; exports are logged to the cross-tenant audit trail.
- The CSM chat thread on screen 21 demonstrates within-2-hr SLA response (first reply at 6 minutes, full resolution at 1h 24m).
