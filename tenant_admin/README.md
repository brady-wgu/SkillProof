# Content Creator (Tenant Admin) — Alice · v1.3

[← Back to root README](../README.md) · [Live portal](https://brady-wgu.github.io/SkillProof/tenant_admin/) · [Catalog](../presentation.html#sc-add-02)

![Content Creator Portal hero](screenshots/sc-add-02_step02_screen02.png)

## Persona

**Alice** — WGU **Program Development (PDev)** employee, operating the **School of Technology** tenant. The SOW (§2.2 deliverable list, §2.5 admin portal sub-area) refers to this role as **"Tenant Admin"** — Alice's user-facing portal chrome calls it **"Content Creator"** (per JFT meeting 10 May 2026) for ease of explanation to non-technical stakeholders. The two terms refer to the same role. Authenticates via her own secret LRPS deep link. Per WGU's School-as-Tenant model, tenants map to WGU's 4 Schools; Alice is scoped to School of Technology where she manages Skills like Foundations of Programming (Python).

## Scope

Multi-tenancy + RBAC, Course-as-a-Service authoring (Subjects, Topics, Learning Objectives with per-objective passing thresholds), AI coaching prompt configuration, model selection + coaching style, CI/CD-driven deploys, post-deploy LRPS provisioning ticket workflow, the Support Plan / SLA workflow (SC-ADD-06), tenant identity + branding, subject lifecycle / archival, analytics + reporting, and tenant-scoped audit log.

## Scenarios

This portal covers **two v1.3 scenarios** in one cohesive Alice experience:

| ID | Description | Screens | Screen IDs |
|:---|:------------|:-------:|:----------:|
| **SC-ADD-02** | **Content Creator Portal & Course Configuration.** SSO + role elevation (1) → multi-tenant portal home with Owner / Read-only subject distinction (2) → New Subject form (3) → Topics & Learning Objectives with inline per-topic expanders carrying editable text + per-objective passing threshold + inline Add / Remove (4) → Model & Coaching (model picker + fallback chain + coaching style) (5) → Configure AI Coaching Prompt with five 200-char guardrail fields and a 600-char addendum + hallucination warning (6) → Deploy review with full subject summary (7) → Deploy success + LRPS provisioning ticket (8) → Tenant Settings (identity card + branding card) (17) → Subject Lifecycle & Archival (18) → Analytics & Reporting (Engagement + Class Insights + Program Reports with CSV/PDF/JSON exports) (19) → Tenant Activity Log (tenant-scoped audit) (20). | 12 | 1-8, 17-20 |
| **SC-ADD-06** | **Critical Incident Response & SLA Verification.** All-systems-operational baseline (9) → service degradation detected (10) → email + toast notification (11) → P1 ticket creation in Jira (12) → JFT-SkillProof-2138 confirmation (13) → JFT CSM Jordan response thread, 2-hr P1 SLA per §9.5 (14) → service restored (15) → 99.95% Uptime SLA dashboard (16). | 8 | 9-16 |

**Total: 2 scenarios · 20 screens (sequential 1-20).**

## Source

- SkillProof User Scenario Catalog: Additional Scenarios **v1.3** (05 May 2026)
- WGU working draft **"SkillProof Authentication, Access Control, and Role Hierarchy" v1.0** (13 May 2026) — drives the RBAC narrative on the SSO landing, the Owner / Read-only badges on the portal home, the Tenant identity card fields on Tenant Settings, and the role-elevation audit row on the Activity Log.
- Storyboard rev: **v4.53** (13 May 2026 — end-of-day sequential renumber).

## SOW references

| Scenario | SOW refs | Where covered |
|:---------|:---------|:--------------|
| SC-ADD-02 | §2.2 ("Tenant Admin" deliverable name), §2.5 (Admin Portal — Course Configuration, modules, analytics; **instructors** consciously consolidated under Super Admin per v4.48 deviation), §16.1 #6.7 (guardrails), #6.8 (A/B testing — badge), #6.12 (LaTeX — badge), §16.2 #7.9 (Custom Branding), #7.10 (engagement tracking), #7.11 (educator analytics), #7.12 (usage stats), #7.13 (visualization), #7.14 (report exports), §16.3 #8.6 (Multi-tenancy), §16.4 #9.7 (CSM), #9.14 (self-service support — Help nav link), #9.15 (video training — Help nav link), §16.5 #10.4 (Audit logging — tenant-scoped view on screen 20), #10.8 (RBAC), #10.14 (zero-trust — SSO landing line) | Multi-tenant scoping callout + Owner/Read-only on screen 2; topic + objective expanders with passing thresholds on screen 4; Model & Coaching radio cards on screen 5; AI Coaching Prompt (5 guardrail fields + LaTeX/A-B-test badges) on screen 6; deploy step summary on screen 7; LRPS provisioning ticket on screen 8; Tenant Settings (identity + branding) on screen 17; Subject Lifecycle on screen 18; Analytics & Reporting (engagement charts · class insights table · program reports with CSV/PDF/JSON exports) on screen 19; Tenant Activity Log on screen 20; Help link in every navbar. |
| SC-ADD-06 | §6.5 (AI Fallback), §9.1 (Jira ticketing), §9.4 (channel), §9.2 (Uptime), §9.5 (SLAs), §9.7 (CSM), §9.10 (Response time), §9.13 (Monitoring) | All systems baseline → fallback → Jira ticket → CSM response thread → service restored → SLA dashboard across screens 9-16. |

## Files

- [`index.html`](index.html) — interactive storyboard (20 screens, sequential 1-20)
- `screenshots/` — 20 light-theme PNGs at 1440×900
- `screenshots_dark/` — 20 dark-theme PNGs

## Components introduced in this portal

- 5-step **Stepper** for the CI/CD pipeline (Validate → Build → Test → Deploy → Verify)
- **Topic expanders** (`<details>` / `<summary>` with caret rotation) carrying inline editable objective text + per-objective passing threshold + inline Add / Remove
- **Owner / Read-only badges** on the portal-home subject list distinguishing write scope from read scope within the same tenant
- **Tenant identity card** with read-only key/value rows (Tenant ID, parent org, Operated by, LRPS launch URL, assigned JFT CSM, Your role scope)
- **Branding card** with light-theme + dark-theme logo upload swatches and accent-color picker
- **Analytics SVG charts** (time-on-task line chart + submissions bar chart, both with `role="img"` + accessible `aria-label`)
- **Class Insights table** with at-risk badges and per-row "Open in Instructor portal" drill-down
- **Program Reports** filter row + per-row CSV / PDF / JSON export buttons
- **Tenant-scoped audit log** mirroring `super-08` with implicit `tenant=pdev` filter
- **JSON code block** with syntax highlighting (`#0d1117` dark theme) — retained for prompt preview on Configure AI Coaching Prompt
- **Radio cards** for Model picker + global Coaching Style selector
- **File-meta card** for LRPS ticket destination URL display
- **Uptime gauge** + **SLA dashboard** with downtime budget remaining
- **Chat-thread / chat-bubble / chat-avatar** for the JFT Support P1 response thread
- **Soft-tint feedback panels** (success / warning / danger) with left-edge accent stripe

## Notes

- The "Deploy to Production" CTA triggers the simulated CI/CD pipeline. The Stepper component models the live progression through Validate → Build → Test → Deploy → Verify with status badges per step.
- After deploy, the **LRPS provisioning ticket** workflow on screen 8 is a manual handoff: JFT does not write to LRPS; the WGU D&D team owns provisioning. The screen shows the production URL + auto-filled ticket justification for Alice to submit.
- Tenant scoping is enforced at every layer: Subject creation locks the Program Subject field; deploys are audit-logged per SOW §10.4; the Tenant Activity Log on screen 20 only shows actions for Alice's School of Technology tenant (cross-tenant audit is Super Admin scope).
- The chat thread on screen 14 demonstrates the JFT Support P1 response SLA (§9.5, <2-hr target). CSM Jordan is shown as the WGU-facing POC; the SLA itself is owned by JFT Support, not the CSM. First reply at 6 minutes, full resolution at 1h 24m.
- The wizard's Step 3 (Model & Coaching, screen 5) is intentionally before Step 4 (AI Coaching Prompt, screen 6) — model + coaching basics are chosen before any custom prompt overrides.
- Instructor management is **not** a tenant-level affordance in this portal. SOW §2.5 lists "instructors" as a tenant-level control, but WGU consolidated that under Super Admin (`super-12` Instructor Roster) in v4.48 because Super Admin is the sole controller of platform access. Tenant Admin retains read-only visibility of instructor activity via the portal-home subject rows and the Class Insights table on screen 19.

## Device context

Desktop-primary. Course authoring, AI prompt configuration, and deploy workflows are not well-suited to mobile screens. The mobile-first commitment in Appendix A §16.2 #7.2 applies universally, so the portal renders responsively, but the optimized workflow assumes a desktop session.

## Tenant Admin portal as the configuration path for the full SOW

The Content Creator / Tenant Admin portal **is** the production configuration mechanism for SkillProof across all WGU Schools. The v1.2 student-only MVP was bootstrapped by JFT engineers via Git-versioned config for E010; once SC-ADD-02 ships, all subsequent Skill onboarding (E075 Intermediate Python & Libraries, E135 OOP with Python, and any future courses across the other 3 WGU Schools) flows through this portal. The portal is not optional MVP-extension scope — it is part of the binding Appendix A §16.3 #8.6 multi-tenancy commitment and the §2.5 Admin Portal deliverable.

## LRPS provisioning is a manual WGU-side handoff

The LRPS provisioning ticket workflow on screen 8 is intentionally a manual handoff — JFT does not write to LRPS. WGU's distributed LMS architecture (the LRPS provider table on `lrps/index.html` illustrates this) means generic "LTI 1.3 compliance" alone is not sufficient for end-to-end course launch; the WGU D&D team registers and provisions LRPS deep links separately. JFT's responsibility is to expose a stable launch URL that does not change when courses are reorganized.

## Deep link management is an LTI Advantage post-MVP capability

The Tenant Admin / Content Creator persona definition (in the WGU User Profile Catalog) describes "creating, testing, and updating deep link URLs that target specific sub-sections of the platform, then placing those links in the LMS as LRPS resources within the appropriate course modules." That per-sub-section deep linking is an **LTI Advantage Deep Linking 2.0** capability, in scope for post-MVP per Appendix A §16.3 #8.1 ("Full LTI 1.3 (including Advantage services)"). The deployed MVP uses basic LTI 1.3 with a single stable launch URL per course — no per-sub-section deep linking — so the deep link management workflow described in Alice's profile is a post-MVP design target, not an immediate MVP feature. The LRPS provisioning ticket workflow on screen 8 anticipates both cases: in the MVP it provisions one stable launch URL per course; in post-MVP it can provision multiple LTI Advantage deep links per course.
