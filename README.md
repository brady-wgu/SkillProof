<div align="center">

# SkillProof

**Medium-fidelity storyboard for WGU's AI-powered Python coding coach + the administrative surfaces around it**

[![Live Demo](https://img.shields.io/badge/Live-GitHub_Pages-0070F0?style=for-the-badge&logo=github)](https://brady-wgu.github.io/SkillProof/)
[![Catalog](https://img.shields.io/badge/Catalog-Light-001730?style=for-the-badge)](https://brady-wgu.github.io/SkillProof/presentation.html)
[![Catalog Dark](https://img.shields.io/badge/Catalog-Dark-0E2841?style=for-the-badge)](https://brady-wgu.github.io/SkillProof/presentation_dark.html)
[![Version](https://img.shields.io/badge/Version-4.54-46B1EF?style=for-the-badge)](CHANGELOG.md)
[![Screens](https://img.shields.io/badge/Screens-77-001730?style=for-the-badge)]()
[![Personas](https://img.shields.io/badge/Personas-4-FBAE40?style=for-the-badge)]()

![Portal selector landing](assets/landing/light.png)

*A medium-fidelity sample — not a pixel-perfect specification. Built with Claude Code on the [SkillProof Design System v1.2](https://github.com/openedx/paragon) (Paragon / Open edX) with WGU FY26 brand tokens.*

</div>

---

## Overview

**SkillProof** is WGU's AI-powered Python coding coach for students, plus the administrative surfaces around it. This repo holds the **medium-fidelity storyboard** that JFT (Jellyfish Technologies) builds against — a self-contained, offline-capable visual sample of all the major surfaces:

- **Sally** (Student) — the v1.2 MVP coaching loop. **JFT shipped this first.** ([student/](student/))
- **Alice** (Content Creator; SOW §2.2 role: Tenant Admin) — Course-as-a-Service portal: subject creation wizard, topic + objective expanders with per-objective passing thresholds, AI coaching prompt configuration, model + coaching style selection, CI/CD-driven deploy, LRPS provisioning workflow, tenant settings, subject lifecycle, analytics & reporting, tenant-scoped activity log. ([tenant_admin/](tenant_admin/))
- **Charlie** (Instructor) — At-Risk Intervention dashboard. ([instructor/](instructor/))
- **Bob** (Super Admin) — Cross-tenant governance, financial controls, security compliance, user role management, instructor roster, data + integrations hub, school/tenant management. ([super_admin/](super_admin/))
- Plus **LRPS Landing** ([lrps/](lrps/)) — recreated WGU internal Learning Resource Provisioning System; the realistic entry point for all four personas.
- Plus **Help & Resources** ([help/](help/)) — shared self-service support + video training surface linked from every admin portal's navbar.

Each persona has its own **secret LRPS deep link** in production and authenticates separately. They share the SkillProof Design System v1.2 chrome and the WGU FY26 brand so the suite reads as one cohesive product family.

> **Implementation notes (for JFT).** The Tenant Admin, Instructor, and Super Admin scenarios are the design spec for surfaces JFT has not yet started building. Use this storyboard as the visual North Star for the **full SOW scope**. WGU expects JFT to deliver every binding requirement in the MSA, the SOW body, and Appendix A within the contracted engagement window. The first JFT release was an MVP slice (E010 Coding Coach in `student/`); subsequent releases close the rest of Appendix A across the Tenant Admin, Instructor, and Super Admin portals. The SC-MVP scenarios deploy the existing Cicada coaching loop as-is; the surrounding platform (multi-LLM orchestration, admin portals, observability, exports, integrations, compliance surfaces) is net-new build work per Appendix A. WGU also runs independent accessibility testing against WCAG 2.2 AA in addition to JFT's own self-checks per §16.2 #7.3 (student-facing surfaces; admin surfaces follow standard usability per SOW §3 Assumptions), so plan for remediation cycles inside the engagement window.

### Surfaces

| Surface | URL | Description |
|:--------|:----|:------------|
| **Portal Selector** | [`/`](https://brady-wgu.github.io/SkillProof/) | Landing page with cards for every surface. **Start here.** |
| **LRPS Landing** | [`/lrps/`](https://brady-wgu.github.io/SkillProof/lrps/) | Entry point for all four personas (4 live SkillProof rows + illustrative filler). |
| **Student Storyboard** | [`/student/`](https://brady-wgu.github.io/SkillProof/student/) | Sally's coaching loop — the v1.2 MVP. **34 screens.** |
| **Content Creator Portal** (SOW §2.2: Tenant Admin) | [`/tenant_admin/`](https://brady-wgu.github.io/SkillProof/tenant_admin/) | Alice — Subject creation wizard (5 steps), Tenant Settings (identity + branding), Subject Lifecycle, Analytics & Reporting, Tenant Activity Log, plus the SC-ADD-06 incident response flow. Owner / Read-only distinction on the portal home; Help link in every navbar. **20 screens** (sequential 1-20). |
| **Instructor Dashboard** | [`/instructor/`](https://brady-wgu.github.io/SkillProof/instructor/) | Charlie — class heatmap → at-risk drill-down → conversation transcript → Audit Trail. **8 screens.** |
| **Super Admin Portal** | [`/super_admin/`](https://brady-wgu.github.io/SkillProof/super_admin/) | Bob (Super Admin) — token usage, rate limits, compliance, geo-redundancy, cross-tenant audit log, User Management (4-tier role taxonomy with min-2-Super-Admins constraint), External Tooling hub, Data & Integrations Hub, Instructor Roster & Course Assignment (cross-tenant), School / Tenant Management. **13 screens.** |
| **Help & Resources** (shared) | [`/help/`](https://brady-wgu.github.io/SkillProof/help/) | Shared self-service support, documentation, and video training surface. Linked from every admin portal navbar. Closes Appendix A §16.4 #9.14 (self-service portal) and #9.15 (video training). |
| **Scenario Catalog (Light)** | [`/presentation.html`](https://brady-wgu.github.io/SkillProof/presentation.html) | All scenarios with workflow narratives and embedded screenshots. |
| **Scenario Catalog (Dark)** | [`/presentation_dark.html`](https://brady-wgu.github.io/SkillProof/presentation_dark.html) | Same catalog, dark-theme screenshots. |

**Total: 77 screens · 4 personas · 6 surfaces (4 persona portals + LRPS + Help) · 2 reference catalogs.**

---

## Repo layout

```
SkillProof/
├── index.html                  Portal selector landing
├── presentation.html           Scenario catalog (light)
├── presentation_dark.html      Scenario catalog (dark)
├── capture_screens.py          Playwright screenshot pipeline
├── README.md                   This file
├── CHANGELOG.md                Version history
├── assets/
│   ├── wgu-corporation-*.png  WGU FY26 corporate logos (3 variants)
│   ├── wgu-favicon.png        WGU shield (every page's favicon, added v4.46)
│   └── landing/                Portal-selector hero screenshots (light + dark)
├── student/                    v1.2 MVP — Sally (frozen at JFT-deployed baseline)
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            34 PNGs (light)
│   └── screenshots_dark/       34 PNGs (dark)
├── tenant_admin/               v1.3 — Alice (sequential 1-20 since v4.53)
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            20 PNGs
│   └── screenshots_dark/       20 PNGs
├── instructor/                 v1.3 — Charlie
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            8 PNGs
│   └── screenshots_dark/       8 PNGs
├── super_admin/                v1.3 — Bob (Super Admin, 13 screens since v4.52)
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            13 PNGs
│   └── screenshots_dark/       13 PNGs
├── lrps/                       Entry point for the 4 admin/learner portals
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            1 PNG (the LRPS page itself)
│   └── screenshots_dark/       1 PNG
└── help/                       Shared self-service support + training (added v4.38)
    ├── index.html
    ├── screenshots/            1 PNG
    └── screenshots_dark/       1 PNG
```

Click any persona folder to read its dedicated README.

---

## Persona sections

### 🎓 Student (v1.2 MVP) — Sally

**Surface:** [`student/`](student/) · [Live](https://brady-wgu.github.io/SkillProof/student/) · [README](student/README.md)

**Persona:** Sally — Beginner / Intermediate / Advanced Python knowledge. Launches via LTI 1.3 from her zyBooks course page.

**Scope:** This is the **v1.2 MVP scope** — the first JFT release. It deploys the existing Cicada v1 proof-of-concept codebase to production-quality, scalable infrastructure with a polished UI, accessible outside the WGU intranet via LTI 1.3 SSO. No new features, adaptive logic changes, or coaching algorithm modifications are in scope for this v1.2 release.

**Scenarios (4, 34 screens):**

| ID | Flow | Screens | Description |
|:---|:-----|:-------:|:------------|
| **SC-MVP-01** | Basic | 8 | First launch. New student with no Python knowledge. Diagnostic → progress map → first coaching task → save. |
| **SC-MVP-02** | Advanced | 11 | Progressive coaching. Partial Python knowledge. Diagnostic → coaching → incorrect-answer feedback → verification → difficulty advance. |
| **SC-MVP-03** | Professional | 9 | Experienced developer fast-tracks. Diagnostic shows mastery; one verification task for Functions & Modular Programming. |
| **SC-MVP-04** | Returning | 6 | Returns after multi-week break. Prior progress preserved. Re-assessment verifies retention before resuming. |

**Source:** SkillProof MVP Scenario Catalog v1.2 (07 Apr 2026).

**v1.2 catalog alignment:** 100% (34/34 screens depict every step described in the catalog). UX detail beyond the visual design — `Need a Hint?` interaction, persistent session-stats display, fast-track threshold reasoning, re-assessment retention framing — is elaborated in [`presentation.html`](presentation.html). Honest call-outs of what v1 does **not** depict (no real Python execution, no mid-task pause, no error recovery, no re-assessment failure path, etc.) are enumerated in [student/README.md](student/README.md#v1-known-limitations). The v1 student screens are deliberately frozen as a baseline — see that file for the full list of v1.4+ candidate gaps.

---

### 🏢 Content Creator (Tenant Admin per SOW §2.2) (v1.3) — Alice

**Surface:** [`tenant_admin/`](tenant_admin/) · [Live](https://brady-wgu.github.io/SkillProof/tenant_admin/) · [README](tenant_admin/README.md)

**Persona:** Alice — WGU Program Development (PDev) employee operating the **School of Technology** tenant. The SOW calls this role **"Tenant Admin"** (§2.2 deliverable, §2.5 admin portal). Alice's user-facing portal chrome calls it **"Content Creator"** per JFT meeting 10 May 2026 — same role, two names for ease of explanation to non-technical stakeholders. Authenticates via her own secret LRPS deep link.

**Scope:** Multi-tenancy + RBAC + Course-as-a-Service authoring (Subjects, Topics, Learning Objectives with per-objective passing thresholds via inline expanders), AI coaching prompt configuration, model + coaching style selection, CI/CD-driven deploys, post-deploy manual LRPS provisioning ticket workflow, tenant identity + branding, subject lifecycle / archival, analytics & reporting (engagement charts · class insights · program reports with CSV/PDF/JSON exports), tenant-scoped audit log, and the Support Plan / SLA workflow (SC-ADD-06).

**Scenarios (2, 20 screens; sequential 1-20):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-02** | **Content Creator Portal & Course Configuration.** SSO + role elevation → multi-tenant portal home (Owner / Read-only subject distinction) → New Subject form → Topics & Learning Objectives (inline per-topic expanders, per-objective passing threshold) → Model & Coaching (model picker + fallback chain + global coaching style) → Configure AI Coaching Prompt (5 guardrail fields + addendum + hallucination warning) → Deploy review (full subject summary) → Deploy success + LRPS provisioning ticket → Tenant Settings (identity + branding) → Subject Lifecycle & Archival → Analytics & Reporting (Engagement charts + Class Insights table + Program Reports with CSV/PDF/JSON exports) → Tenant Activity Log (tenant-scoped audit). | 12 |
| **SC-ADD-06** | **Critical Incident Response & SLA.** Primary LLM provider down → fallback engaged → P1 ticket in **Jira** (§9.1 + §9.4) → JFT Support 2-hr P1 response per §9.5 → service restored → 99.95% uptime SLA verified. | 8 |

**Source:** SkillProof User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026) + WGU working draft *"SkillProof Authentication, Access Control, and Role Hierarchy" v1.0* (13 May 2026).

---

### 👨‍🏫 Instructor (v1.3) — Charlie

**Surface:** [`instructor/`](instructor/) · [Live](https://brady-wgu.github.io/SkillProof/instructor/) · [README](instructor/README.md)

**Persona:** Charlie — Instructor (per User Profile + SOW §2.5) for E010 Foundations of Programming (Python), E075 Intermediate Python & Libraries, and E135 OOP with Python.

**Scope:** Educator-facing analytics and learner engagement tracking. SkillProof is a practice tool — coaching scores never feed academic records.

**Scenarios (1, 8 screens; sequential 1-8):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-03** | **Instructor Dashboard & At-Risk Intervention.** Course overview → class heatmap (15 learners × 4 competencies, 9-step color scale; export CTAs per §7.14) → at-risk filter → Sally drill-down → conversation transcript with AI feedback → Audit Trail event log. | 8 |

**Source:** SkillProof User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026).

---

### 🛡️ Super Admin (v1.3) — Bob

**Surface:** [`super_admin/`](super_admin/) · [Live](https://brady-wgu.github.io/SkillProof/super_admin/) · [README](super_admin/README.md)

**Persona:** Bob — WGU platform operations and infrastructure. Authenticates with MFA in addition to SSO. Cross-tenant scope and sole controller of platform access; minimum 2 Super Admins required at all times.

**Scope:** Cross-tenant governance, financial controls, security compliance, global resource management, user role elevation, instructor-to-Skill assignment, and tenant (School) lifecycle management.

**Scenarios (1, 13 screens; sequential 1-13):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-04** | **Super Admin Governance, Cost Audit, Access Control, and Tenant Management.** SSO + MFA → portal home (KPI gauges + 8 quick-link cards) → Token Usage → Cost-spike drill-down → Global Rate Limits → Compliance Report (TLS 1.3 + FERPA + SOC 2 + ISO 27001 + zero-trust + GDPR + MFA + SIEM + AES-256 + BC/DR) → Geo-redundancy → Cross-tenant Audit Log → **User Management** (4-tier role taxonomy: Student / Instructor / Tenant Admin / Super Admin; min-2-Super-Admins enforcement) → **External Tooling & Integrations** (AWS / OpenRouter / Redis / Grafana / Jira / GitHub) → **Data & Integrations Hub** (real-time + batch export, webhooks, GraphQL, Kafka / Kinesis / Pub-Sub streaming) → **Instructor Roster & Course Assignment** (cross-tenant, per-School filter) → **School / Tenant Management** (4 WGU Schools as tenants + `+ Create new School` affordance). | 13 |

**Source:** SkillProof User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026) + WGU working draft *"SkillProof Authentication, Access Control, and Role Hierarchy" v1.0* (13 May 2026).

---

### 🚪 LRPS Landing (Entry Point)

**Surface:** [`lrps/`](lrps/) · [Live](https://brady-wgu.github.io/SkillProof/lrps/) · [README](lrps/README.md)

**Persona:** Lana (the fictional LRPS admin who provisions the deep links) or any WGU staff with LRPS access.

**Scope:** A recreation of WGU's internal Learning Resource Provisioning System, styled in the SkillProof Design System v1.2. Each of the four persona portals has its own provider row in this table; clicking the row deep-links into the corresponding portal. JFT does not build LRPS — it is modeled here only to make the deep-link source feel authentic.

The LRPS surface includes:
- 4 live SkillProof rows (Student, Tenant Admin, Instructor, Super Admin) — clickable, deep-linked
- Illustrative filler rows (OEX modules, zyBooks, Pearson, ProctorU, Coursera, Cicada legacy, Panopto, etc.) for realistic LRPS density
- A meta-bar quick-launch with chips to all surfaces + the catalog

---

### 📚 Help & Resources (shared surface)

**Surface:** [`help/`](help/) · [Live](https://brady-wgu.github.io/SkillProof/help/)

**Scope:** Single-page self-service support + video training surface. Linked from the Help button in every admin portal's navbar (tenant_admin, super_admin — instructor still pending). Closes Appendix A §16.4 #9.14 (self-service support portal) and #9.15 (video training resources). The Contact JFT Support FAB at the bottom-right kicks the user into the SC-ADD-06 ticket flow.

---

## Shared persona & course reference

Canonical strings used across all surfaces. Use these verbatim when adding new screens, narrative, or test fixtures so the storyboard remains internally consistent. (Drift here is the most common source of bugs — e.g., a Tenant Admin screen that calls Sally's course "E010" while the Instructor heatmap calls it "Foundations of Programming".)

| String | Canonical value | Notes |
|:-------|:----------------|:------|
| **Student persona** | `Sally` | First name only. Avatar initial: `S`. Used in LTI 1.3 `name` claim. Knowledge level varies by scenario; same Sally across all four. |
| **Course code** | `E010` | Course code for "Foundations of Programming (Python)". |
| **Course title** | `Foundations of Programming (Python)` | Or short form `Python Foundations` in tight UI chrome. Never abbreviate to "FoP" in user-facing copy. |
| **Enrollment model** | `Rolling enrollment` | Per the User Profile, WGU has no fixed cohorts or sections. Every learner enters on their own day and progresses at their own rate. Avoid "Section 042" / "Spring 2026" framing in any new screen copy — talk about *active learners in a Skill* instead. |
| **Tenant (default example)** | `School of Technology` | Tenant slug: `tenant_school_tech`. Alice operates this tenant; she is a WGU Program Development (PDev) employee. |
| **Operating team** | `WGU Program Development` | PDev employees operate the School-tenants. Distinct from a tenant name — PDev does the work *on behalf of* each School. |
| **All 4 WGU Schools (example tenant set)** | `School of Technology`, `School of Business`, `School of Education`, `Leavitt School of Health` | Per WGU's School-as-Tenant model. Additional Schools can be created via super_admin screen 13. |
| **LMS course identifier** | `WGUE010PythonAY2026` | The LRPS-registered LMS course slug zyBooks renders. Visible on Screen 1 of every SC-MVP scenario. |
| **13 sub-sections** | Basic Syntax & Data Types · Control Flow & Logic · Data Structures: Lists, Tuples, Sets, Dictionaries · Functions & Modular Programming · Object-Oriented Programming · Error Handling & Exceptions · File I/O & Persistence · Iterators & Generators · Decorators & Closures · Concurrency Basics · Standard Library Essentials · Testing & Debugging · Packaging & Environments | The full Cicada v1 SkillProof sub-section taxonomy. Order is significant: Progress Map renders in this order. |
| **Cost-spike date (SC-ADD-04)** | `04 May 2026` | Bob's cost audit drill-down references this date as the spike origin. |
| **Role taxonomy** | `Student → Instructor → Tenant Admin → Super Admin` | 4-tier RBAC. Only Super Admin can change roles; minimum 2 Super Admins always. |
| **Storyboard version** | `v4.x` | Tracks the visual prototype, not the underlying SkillProof product. SkillProof product versions follow the catalog: v1.2 MVP, v1.3 Additional, etc. |

If you need to change any of these, update them everywhere in the same commit — `Glob` for the literal string across all portals, `presentation.html` / `presentation_dark.html`, and all per-persona READMEs before opening the PR.

---

## Design System

The storyboard implements the **SkillProof Design System v1.2**, a brand theme layer on top of [Paragon](https://github.com/openedx/paragon) (Open edX's open-source design system).

| Layer | Responsibility |
|:------|:--------------|
| **Paragon** | Component structure, accessibility, base CSS (`@openedx/paragon`) |
| **WGU Brand Tokens** | Color, typography, spacing overrides (`--pgn-*` CSS custom properties) |
| **SkillProof Product** | Page composition, content structure, learning interactions |

### Color Palette (WGU FY26 — Authoritative)

| Token | Hex | Role |
|:------|:----|:-----|
| Deep Navy | `#001730` | Primary dark background, navbar, headers |
| Dark Navy | `#002855` | Deep accent, logo gradient |
| Bright Blue | `#0070F0` | Primary actions, CTAs, links |
| Sky Blue | `#46B1EF` | Secondary blue, accents, progress |
| Ice Blue | `#EEF6F9` | Light surface backgrounds |
| Accent Red | `#C13232` | Error states, emphasis |
| Amber | `#FBAE40` | Warnings, section accents |

Where FY26 and SkillProof Figma tokens conflict, **FY26 takes precedence**.

#### Documented palette extensions (intentional; out of FY26 scope)

Two specialized UI domains use deliberately extended palettes for clarity and industry familiarity. **These are intentional and must NOT be expanded to other surfaces.** Implementers should keep these scoped to their declared domains:

| Domain | Tokens | Where used | Justification |
|:---|:---|:---|:---|
| **Code-block syntax highlighting** | GitHub-style: `--code-keyword: #ff7b72`, `--code-function: #79c0ff`, `--code-string: #a5d6ff`, `--code-bg: #0d1117`, `--code-border: #30363d` | `tenant_admin/index.html` (prompt preview); `student/index.html` (read-only Python code editors) | Industry-standard code coloring (matches GitHub / VS Code dark themes). FY26 navy/blue would be unreadable for code tokens. |
| **Heatmap gradient** (9-step) | `--heat-1` through `--heat-9` (red → green via amber midpoints) | `instructor/index.html` screen 3 (15-learner × 4-competency class heatmap) | Sequential data visualization needs perceptually distinct steps; FY26 has no diverging-scale tokens. |

All other surfaces (navbars, cards, forms, alerts, badges, status pills) use canonical FY26 tokens only.

### Typography

- **Headings:** Sora Bold (H1 40, H2 32, H3 28, H4 24, H5 20)
- **Body:** Lato Regular 16px / 1.5 line-height
- **Code blocks:** Lato 14px on `#0d1117` for JSON/API consoles; SkillProof-palette syntax in light mode for student code blocks
- **Type scale:** strict 12 / 14 / 16 / 18 / 20 / 24 / 28 / 32 / 40 / 48 px

### Spacing

8-point grid throughout. All padding, margin, and gap values are multiples of 8px.

### Branding

- Real **WGU FY26 Corporation logos** in [`assets/`](assets/) (White, Full Color, Full Color Reverse)
- **WGU shield favicon** at `assets/wgu-favicon.png` — every storyboard surface ships with the WGU shield in the browser tab (added v4.46)
- **Theme-aware logo swap:** Full Color Reverse on light theme, White on dark theme — both render correctly on the navy header
- **Wordmark text dropped** — the logo stands alone (per WGU's branding rule)

---

## How to use

### Online

The portal selector at [brady-wgu.github.io/SkillProof/](https://brady-wgu.github.io/SkillProof/) links to every surface. From there you can open any portal directly, or open LRPS first and click into a portal via its provider row.

### Offline

Clone the repo and open `index.html` in any modern browser. No build step, no server required (the screenshot pipeline is the only thing that needs a local HTTP server). Files are fully self-contained beyond Google Fonts (Sora + Lato + Material Icons Outlined).

### Regenerate screenshots

```bash
# 1. From the repo root, start a local HTTP server
python -m http.server 63417

# 2. In another terminal
python capture_screens.py
```

Output: **156 PNGs total** — student 34 + tenant_admin 20 + super_admin 13 + instructor 8 + lrps 1 + help 1, each × 2 themes (light + dark), plus 2 landing assets. Distributed across the per-persona `screenshots/` and `screenshots_dark/` subdirs.

---

## Source documents

| Document | Version | Date |
|:---------|:--------|:-----|
| Signed JFT MSA + SOW | (executed) | 03 Mar 2026 |
| SkillProof User Scenario Catalog: Additional Scenarios | v1.3 | 05 May 2026 |
| SkillProof MVP Scenario Catalog | v1.2 | 07 Apr 2026 |
| SkillProof User Profiles | v1.2 (v1.3 in progress) | 30 Mar 2026 |
| SkillProof Authentication, Access Control, and Role Hierarchy (working draft) | v1.0 | 13 May 2026 |
| SkillProof Design System Specification | v1.2 | 30 Mar 2026 |
| WGU FY26 Design System Specification | v1.0 | 25 Mar 2025 |

Upstream design system: [@openedx/paragon](https://github.com/openedx/paragon) (release-23.x, v23.19.1).

---

## For developers (JFT)

This storyboard is a **medium-fidelity sample**, not production code or a pixel-perfect specification. It illustrates the general look and feel of SkillProof and its administrative surfaces on a desktop browser. Use it as a rough guide for the intended user experience — adapt as needed for the production implementation.

When implementing:

1. **Install Paragon** — `npm install @openedx/paragon`
2. **Apply WGU brand tokens** via the brand package override mechanism (`@wgu/skillproof-brand`)
3. **Use Paragon React components** — do not rebuild them. The storyboard's CSS class names (`.pgn__card`, `.btn-primary`, `.pgn__breadcrumb`, etc.) map directly to Paragon's component schema.
4. **Per-persona portals are separately authenticated surfaces** — each has its own LRPS deep link. Tenant Admin, Instructor, and Super Admin should not be combined into a single SPA shell; the auth flow and RBAC scoping are role-bound.
5. **Zero-trust authorization** — the LRPS link does not grant authority. Effective role and scope are determined server-side after authentication.
6. **Tenant model = WGU Schools** — A tenant in SkillProof maps to a WGU School. The example storyboard uses School of Technology as Alice's default tenant; additional schools can be created via the Super Admin School / Tenant Management surface.
7. The CSS custom properties in the portal HTML files (`--pgn-*`) map directly to the Paragon token schema.
8. Each persona's [`README.md`](#repo-layout) lists the specific patterns and components introduced for that surface.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full version history. **Today's release is v4.54** — full repo-level documentation refresh reflecting every change made on 13 May 2026.

Today's major milestones (13 May 2026):

- **v4.43-v4.44** — Product rename to **SkillProof** (was Skill Development Platform / SDP); GitHub repo + Pages URL renamed.
- **v4.46** — WGU shield favicon added to every storyboard surface.
- **v4.47-v4.49** — Tenant Admin walkthrough: weight column removed (zero contract hits), `LO` abbreviation swept to `Objective`, screens 5/6/7/10/22 retired, Tenant Settings rebuilt, Screen 11 Deploy summary expanded.
- **v4.51** — Re-audited tenant_admin against the correct signed contract MD. Added 2 new screens (Analytics & Reporting, Tenant Activity Log) closing 8 Yes-committed Tenant-Admin requirements (A-7.10..7.14, A-9.14, A-9.15, A-10.4).
- **v4.52** — RBAC narrative solidification per Brady's working draft. `Global Admin` → `Super Admin` swept across all visible UI. `PDev` → `School of Technology` (tenant=School model). New Super Admin screen 13 (School / Tenant Management) closes the multi-school management gap.
- **v4.53** — End-of-day sequential renumber. Tenant Admin IDs collapsed `{1,2,3,4,9,8,11,12,13..20,21,23,24,25}` → `1..20`. Full screenshot regeneration (156 PNGs).
- **v4.54** — Documentation refresh across this README + per-persona READMEs to reflect all of the above as the JFT-delivery state.

---

<div align="center">

**Western Governors University** | Program Development | SkillProof

*WGU confidential / proprietary. Do not redistribute without authorization.*

</div>
