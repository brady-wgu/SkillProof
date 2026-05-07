<div align="center">

# JFT SDP — Skills Development Platform

**Medium-fidelity storyboard for WGU's AI-powered Python coding coach + the administrative surfaces around it**

[![Live Demo](https://img.shields.io/badge/Live-GitHub_Pages-0070F0?style=for-the-badge&logo=github)](https://brady-wgu.github.io/JFT_SDP/)
[![Catalog](https://img.shields.io/badge/Catalog-Light-001730?style=for-the-badge)](https://brady-wgu.github.io/JFT_SDP/presentation.html)
[![Catalog Dark](https://img.shields.io/badge/Catalog-Dark-0E2841?style=for-the-badge)](https://brady-wgu.github.io/JFT_SDP/presentation_dark.html)
[![Version](https://img.shields.io/badge/Version-4.0-46B1EF?style=for-the-badge)](CHANGELOG.md)
[![Screens](https://img.shields.io/badge/Screens-73-001730?style=for-the-badge)]()
[![Personas](https://img.shields.io/badge/Personas-4-FBAE40?style=for-the-badge)]()

![Portal selector landing](assets/landing/light.png)

*A medium-fidelity sample — not a pixel-perfect specification. Built with Claude Code on the [SDP Design System v1.2](https://github.com/openedx/paragon) (Paragon / Open edX) with WGU FY26 brand tokens.*

</div>

---

## Overview

The **JFT Skills Development Platform (SDP)** is WGU's AI-powered Python coding coach for students, plus the administrative surfaces around it. This repo holds the **medium-fidelity storyboard** that JFT (Jellyfish Technologies) builds against — a self-contained, offline-capable visual sample of all the major surfaces:

- **Sally** (Student) — the v1.2 MVP coaching loop. **JFT shipped this first.** ([student/](student/))
- **Alice** (Tenant Admin / PDev content owner) — Course-as-a-Service portal, Data Portability, Critical Incident Response. ([tenant_admin/](tenant_admin/))
- **Charlie** (Instructor) — At-Risk Intervention dashboard. ([instructor/](instructor/))
- **Bob** (Super Admin / Platform Operations) — Governance & Cost Audit. ([super_admin/](super_admin/))
- Plus **LRPS Landing** ([lrps/](lrps/)) — recreated WGU internal Learning Resource Provisioning System; the realistic entry point for all three admin portals.

Each persona has its own **secret LRPS deep link** in production and authenticates separately. They share the SDP Design System v1.2 chrome and the WGU FY26 brand so the suite reads as one cohesive product family.

> **Note for JFT:** The Tenant Admin, Instructor, and Super Admin scenarios are the design spec for surfaces JFT has not yet started building. Use this storyboard as the visual North Star, not a frozen contract. The first JFT release was an MVP and will be iterated on several times during the contract.

### Surfaces

| Surface | URL | Description |
|:--------|:----|:------------|
| **Portal Selector** | [`/`](https://brady-wgu.github.io/JFT_SDP/) | Landing page with cards for every surface. **Start here.** |
| **LRPS Landing** | [`/lrps/`](https://brady-wgu.github.io/JFT_SDP/lrps/) | Entry point for the three admin portals (3 live SDP rows, 17 illustrative). |
| **Student Storyboard** | [`/student/`](https://brady-wgu.github.io/JFT_SDP/student/) | Sally's coaching loop — the v1.2 MVP. 34 screens. |
| **Tenant Admin Portal** | [`/tenant_admin/`](https://brady-wgu.github.io/JFT_SDP/tenant_admin/) | Alice — course config, data exports, incident response. 23 screens. |
| **Instructor Dashboard** | [`/instructor/`](https://brady-wgu.github.io/JFT_SDP/instructor/) | Charlie — class heatmap → Sally drill-down → Audit Trail. 8 screens. |
| **Super Admin Portal** | [`/super_admin/`](https://brady-wgu.github.io/JFT_SDP/super_admin/) | Bob — token usage, rate limits, compliance, geo-redundancy. 8 screens. |
| **Scenario Catalog (Light)** | [`/presentation.html`](https://brady-wgu.github.io/JFT_SDP/presentation.html) | All 9 scenarios with workflow narratives and embedded screenshots. |
| **Scenario Catalog (Dark)** | [`/presentation_dark.html`](https://brady-wgu.github.io/JFT_SDP/presentation_dark.html) | Same catalog, dark-theme screenshots. |

**Total: 73 screens · 4 personas · 5 admin/learner surfaces · 1 LRPS entry · 2 reference catalogs.**

---

## Repo layout

```
JFT_SDP/
├── index.html                  Portal selector landing
├── presentation.html           Scenario catalog (light)
├── presentation_dark.html      Scenario catalog (dark)
├── capture_screens.py          Playwright screenshot pipeline
├── README.md                   This file
├── CHANGELOG.md                Version history
├── assets/
│   ├── wgu-corporation-*.png  WGU FY26 corporate logos (3 variants)
│   └── landing/                Portal-selector hero screenshots
├── student/                    v1.2 MVP — Sally
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            34 PNGs (light)
│   └── screenshots_dark/       34 PNGs (dark)
├── tenant_admin/               v1.3 — Alice
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            23 PNGs
│   └── screenshots_dark/       23 PNGs
├── instructor/                 v1.3 — Charlie
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            8 PNGs
│   └── screenshots_dark/       8 PNGs
├── super_admin/                v1.3 — Bob
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            8 PNGs
│   └── screenshots_dark/       8 PNGs
└── lrps/                       Entry point for the 3 admin portals
    ├── index.html
    ├── README.md
    ├── screenshots/            1 PNG (the LRPS page itself)
    └── screenshots_dark/       1 PNG
```

Click any persona folder to read its dedicated README.

---

## Persona sections

### 🎓 Student (v1.2 MVP) — Sally

**Surface:** [`student/`](student/) · [Live](https://brady-wgu.github.io/JFT_SDP/student/) · [README](student/README.md)

**Persona:** Sally — Beginner / Intermediate / Advanced Python knowledge. Launches via LTI 1.3 from her zyBooks course page.

**Scope:** This is the **v1.2 MVP scope** — the first JFT release. It deploys the existing Cicada v1 proof-of-concept codebase to production-quality, scalable infrastructure with a polished UI, accessible outside the WGU intranet via LTI 1.3 SSO. No new features, adaptive logic changes, or coaching algorithm modifications are in scope for this v1.2 release.

**Scenarios (4, 34 screens):**

| ID | Flow | Screens | Description |
|:---|:-----|:-------:|:------------|
| **SC-MVP-01** | Basic | 8 | First launch. New student with no Python knowledge. Diagnostic → progress map → first coaching task → save. |
| **SC-MVP-02** | Advanced | 11 | Progressive coaching. Partial Python knowledge. Diagnostic → coaching → incorrect-answer feedback → verification → difficulty advance. |
| **SC-MVP-03** | Professional | 9 | Experienced developer fast-tracks. Diagnostic shows mastery; one verification task for Functions & Modular Programming. |
| **SC-MVP-04** | Returning | 6 | Returns after multi-week break. Prior progress preserved. Re-assessment verifies retention before resuming. |

**Source:** JFT SDP MVP Scenario Catalog v1.2 (07 Apr 2026).

---

### 🏢 Tenant Admin (v1.3) — Alice

**Surface:** [`tenant_admin/`](tenant_admin/) · [Live](https://brady-wgu.github.io/JFT_SDP/tenant_admin/) · [README](tenant_admin/README.md)

**Persona:** Alice — WGU Program Development (PDev) content owner. Authenticates via her own secret LRPS deep link.

**Scope:** Multi-tenancy, RBAC, the Course-as-a-Service administrative UI, integration APIs and data export commitments, and the Support Plan / SLA workflow.

**Scenarios (3, 23 screens):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-02** | **Tenant Admin Portal & Course Configuration.** Multi-tenant scoping, Subject creation, Topics & Learning Objectives, AI prompt config, model picker, rubric, deploy via CI/CD. | 9 |
| **SC-ADD-05** | **Data Portability.** REST API console (query learner scores), one-click export wizard (CSV / JSON / Parquet) with audit trail. | 6 |
| **SC-ADD-06** | **Critical Incident Response & SLA.** Primary LLM provider down → fallback engaged → P1 ticket → JFT CSM 2-hr response → service restored → 99.95% uptime SLA verified. | 8 |

**Source:** JFT SDP User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026).

---

### 👨‍🏫 Instructor (v1.3) — Charlie

**Surface:** [`instructor/`](instructor/) · [Live](https://brady-wgu.github.io/JFT_SDP/instructor/) · [README](instructor/README.md)

**Persona:** Charlie — course instructor for E010 Foundations of Programming (Python).

**Scope:** Educator-facing analytics and student engagement tracking.

**Scenarios (1, 8 screens):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-03** | **Instructor Dashboard & At-Risk Intervention.** Section overview → class heatmap (15 learners × 4 competencies, 9-step color scale) → at-risk filter → Sally drill-down → conversation transcript with AI feedback → Audit Trail event log. | 8 |

**Source:** JFT SDP User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026).

---

### 🛡️ Super Admin (v1.3) — Bob

**Surface:** [`super_admin/`](super_admin/) · [Live](https://brady-wgu.github.io/JFT_SDP/super_admin/) · [README](super_admin/README.md)

**Persona:** Bob — WGU platform operations and infrastructure. Authenticates with MFA in addition to SSO.

**Scope:** Cross-tenant governance, financial controls, security compliance, global resource management.

**Scenarios (1, 8 screens):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-04** | **Super Admin Governance & Cost Audit.** Cross-tenant overview → token usage tracking → cost-spike drill-down → global rate limits → TLS 1.3 compliance report → geo-redundancy status → cross-tenant audit log. | 8 |

**Source:** JFT SDP User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026).

---

### 🚪 LRPS Landing (Entry Point)

**Surface:** [`lrps/`](lrps/) · [Live](https://brady-wgu.github.io/JFT_SDP/lrps/) · [README](lrps/README.md)

**Persona:** Brady (the LRPS admin who provisions the deep links) or any WGU staff with LRPS access.

**Scope:** A recreation of WGU's internal Learning Resource Provisioning System, styled in the SDP Design System v1.2. Each of the three admin portals has its own provider row in this table; clicking the row deep-links into the corresponding portal. JFT does not build LRPS — it is modeled here only to make the deep-link source feel authentic.

The LRPS surface includes:
- 3 live SDP rows (Tenant Admin, Instructor, Super Admin) — clickable, deep-linked
- 17 illustrative filler rows (OEX modules, zyBooks, Pearson, ProctorU, Cicada legacy, Panopto, etc.) for realistic LRPS density
- A meta-bar quick-launch with chips to all 5 surfaces + the catalog

---

## Design System

The storyboard implements the **SDP Design System v1.2**, a brand theme layer on top of [Paragon](https://github.com/openedx/paragon) (Open edX's open-source design system).

| Layer | Responsibility |
|:------|:--------------|
| **Paragon** | Component structure, accessibility, base CSS (`@openedx/paragon`) |
| **WGU Brand Tokens** | Color, typography, spacing overrides (`--pgn-*` CSS custom properties) |
| **SDP Product** | Page composition, content structure, learning interactions |

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

Where FY26 and SDP Figma tokens conflict, **FY26 takes precedence**.

### Typography

- **Headings:** Sora Bold (H1 40, H2 32, H3 28, H4 24, H5 20)
- **Body:** Lato Regular 16px / 1.5 line-height
- **Code blocks:** Lato 14px on `#0d1117` for JSON/API consoles; SDP-palette syntax in light mode for student code blocks
- **Type scale:** strict 12 / 14 / 16 / 18 / 20 / 24 / 28 / 32 / 40 / 48 px

### Spacing

8-point grid throughout. All padding, margin, and gap values are multiples of 8px.

### Branding

- Real **WGU FY26 Corporation logos** in [`assets/`](assets/) (White, Full Color, Full Color Reverse)
- **Theme-aware logo swap:** Full Color Reverse on light theme, White on dark theme — both render correctly on the navy header
- **Wordmark text dropped** — the logo stands alone (per Brady's branding rule)

---

## How to use

### Online

The portal selector at [brady-wgu.github.io/JFT_SDP/](https://brady-wgu.github.io/JFT_SDP/) links to every surface. From there you can open any portal directly, or open LRPS first and click into a portal via its provider row.

### Offline

Clone the repo and open `index.html` in any modern browser. No build step, no server required (the screenshot pipeline is the only thing that needs a local HTTP server). Files are fully self-contained beyond Google Fonts (Sora + Lato + Material Icons Outlined).

### Regenerate screenshots

```bash
# 1. From the repo root, start a local HTTP server
python -m http.server 63417

# 2. In another terminal
python capture_screens.py
```

Output: 148 PNGs total — 74 per theme, distributed across the 5 per-persona `screenshots/` and `screenshots_dark/` subdirs.

---

## Source documents

| Document | Version | Date |
|:---------|:--------|:-----|
| JFT SDP User Scenario Catalog: Additional Scenarios | v1.3 | 05 May 2026 |
| JFT SDP MVP Scenario Catalog | v1.2 | 07 Apr 2026 |
| JFT SDP User Profiles | v1.2 | 30 Mar 2026 |
| SDP Design System Specification | v1.2 | 30 Mar 2026 |
| WGU FY26 Design System Specification | v1.0 | 25 Mar 2025 |
| WGU Design Systems Differential Analysis | v2.0 | 16 Apr 2026 |

Upstream design system: [@openedx/paragon](https://github.com/openedx/paragon) (release-23.x, v23.19.1).

---

## For developers (JFT)

This storyboard is a **medium-fidelity sample**, not production code or a pixel-perfect specification. It illustrates the general look and feel of the SDP and its administrative surfaces on a desktop browser. Use it as a rough guide for the intended user experience — adapt as needed for the production implementation.

When implementing:

1. **Install Paragon** — `npm install @openedx/paragon`
2. **Apply WGU brand tokens** via the brand package override mechanism (`@wgu/sdp-brand`)
3. **Use Paragon React components** — do not rebuild them. The storyboard's CSS class names (`.pgn__card`, `.btn-primary`, `.pgn__breadcrumb`, etc.) map directly to Paragon's component schema.
4. **Per-persona portals are separately authenticated surfaces** — each has its own LRPS deep link. Tenant Admin, Instructor, and Super Admin should not be combined into a single SPA shell; the auth flow and RBAC scoping are role-bound.
5. **Tenant Admin owns three v1.3 scenarios in one portal** — the screens compose into a single Tenant Admin experience but are documented separately in the catalog.
6. The CSS custom properties in the portal HTML files (`--pgn-*`) map directly to the Paragon token schema.
7. Each persona's [`README.md`](#repo-layout) lists the specific patterns and components introduced for that surface.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full version history.

The latest release is **v4.0** — adds the three v1.3 admin portals, the LRPS landing, and the portal-selector home page; restructures the repo into per-persona subdirectories.

---

<div align="center">

**Western Governors University** | Program Development | JFT SDP

*WGU confidential / proprietary. Do not redistribute without authorization.*

</div>
