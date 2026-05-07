<div align="center">

# JFT SDP Storyboard

**Interactive Prototype for the WGU Skills Development Platform**

[![Live Demo](https://img.shields.io/badge/Live_Demo-GitHub_Pages-0070F0?style=for-the-badge&logo=github)](https://brady-wgu.github.io/JFT_SDP_MVP/)
[![Presentation](https://img.shields.io/badge/Presentation-Light-001730?style=for-the-badge)](https://brady-wgu.github.io/JFT_SDP_MVP/presentation.html)
[![Presentation Dark](https://img.shields.io/badge/Presentation-Dark-0E2841?style=for-the-badge)](https://brady-wgu.github.io/JFT_SDP_MVP/presentation_dark.html)
[![Version](https://img.shields.io/badge/Version-4.0-46B1EF?style=for-the-badge)]()
[![Screens](https://img.shields.io/badge/Screens-73-001730?style=for-the-badge)]()

---

*A medium-fidelity sample storyboard for the JFT SDP Coding Coach — not a pixel-perfect specification.*
*Built with Claude Code on the [SDP Design System v1.2](https://github.com/openedx/paragon) (Paragon / Open edX) with WGU FY26 brand tokens.*

</div>

---

## Overview

This storyboard is a medium-fidelity visual sample for the **JFT Skills Development Platform (SDP)** — an AI-powered Python coding coach for WGU students, plus the administrative surfaces that surround it.

It now covers **all nine v1.2 + v1.3 user scenarios across four personas**:
- **Sally** (Student) — the original v1.2 MVP coaching loop (4 scenarios, 34 screens, `index.html`)
- **Alice** (Tenant Admin / PDev content owner) — Portal & Course Configuration, Data Portability, and Critical Incident Response (3 scenarios, 23 screens, `tenant_admin.html`)
- **Charlie** (Instructor) — Instructor Dashboard & At-Risk Intervention (1 scenario, 8 screens, `instructor.html`)
- **Bob** (Super Admin / Platform Operations) — Governance & Cost Audit (1 scenario, 8 screens, `super_admin.html`)

Each persona has its own **secret LRPS deep link** and authenticates separately, so the four HTML files are independently loaded surfaces. They share the SDP Design System v1.2 chrome and the WGU FY26 brand so the suite reads as one cohesive product family.

The prototype consists of self-contained HTML files that work offline, require no build step, and render in any modern browser. These illustrate roughly what the SDP could look like on a desktop browser — they are **not** pixel-perfect specifications to be duplicated exactly. This prototype was built with Claude Code for rapid visualization, has not been formally audited for accessibility, and has not been tested for mobile responsiveness.

> **Note for JFT:** Tenant Admin, Instructor, and Super Admin scenarios have not been started by JFT yet. This storyboard is the design spec for those new surfaces — use it as the visual North Star while building, not a frozen contract. The first JFT release is an MVP and will be iterated on several times during the contract.

### Pages

| Page | URL | Description |
|:-----|:----|:------------|
| **Student Storyboard** | [`index.html`](https://brady-wgu.github.io/JFT_SDP_MVP/) | 34-screen interactive prototype for SC-MVP-01 through SC-MVP-04 (Sally's coaching loop) |
| **Tenant Admin Portal** | [`tenant_admin.html`](https://brady-wgu.github.io/JFT_SDP_MVP/tenant_admin.html) | 23-screen portal for SC-ADD-02 (Course Configuration) + SC-ADD-05 (Data Portability) + SC-ADD-06 (Incident Response) — Alice |
| **Instructor Dashboard** | [`instructor.html`](https://brady-wgu.github.io/JFT_SDP_MVP/instructor.html) | 8-screen dashboard for SC-ADD-03 (At-Risk Intervention) — Charlie |
| **Super Admin Portal** | [`super_admin.html`](https://brady-wgu.github.io/JFT_SDP_MVP/super_admin.html) | 8-screen console for SC-ADD-04 (Governance & Cost Audit) — Bob |
| **Scenario Catalog (Light)** | [`presentation.html`](https://brady-wgu.github.io/JFT_SDP_MVP/presentation.html) | Scrollable presentation with all 9 scenarios annotated with light-mode screenshots |
| **Scenario Catalog (Dark)** | [`presentation_dark.html`](https://brady-wgu.github.io/JFT_SDP_MVP/presentation_dark.html) | Same presentation with dark-mode screenshots |

---

## Scenarios

### v1.2 — Student (Sally) — `index.html`

| Scenario | Flow | Screens | Description |
|:---------|:-----|:-------:|:------------|
| **SC-MVP-01** | Basic | 8 | First launch of the Coding Coach. New student with no Python knowledge completes diagnostic, views progress map, begins first coaching task, saves session. |
| **SC-MVP-02** | Advanced | 11 | Progressive coaching with targeted feedback. Student with partial Python knowledge completes diagnostic, receives foundational coaching, encounters incorrect answer with specific error feedback, verifies gap resolution, advances difficulty. |
| **SC-MVP-03** | Professional | 9 | Experienced developer fast-tracks through the coaching baseline. Diagnostic demonstrates mastery across all sub-sections. One verification task required for Functions & Modular Programming. |
| **SC-MVP-04** | Returning | 6 | Student returns after a multi-week break. Prior progress preserved. Re-assessment verifies retention before resuming coaching at prior difficulty level. |

### v1.3 — Additional Scenarios (Tenant Admin / Instructor / Super Admin)

| Scenario | Persona | File | Screens | Description |
|:---------|:--------|:-----|:-------:|:------------|
| **SC-ADD-01** | Sally | — | — | Acceptance rollup of v1.2 MVP scenarios. In progress separately; no new scope. |
| **SC-ADD-02** | Alice | `tenant_admin.html` | 9 | Tenant Admin Portal & Course Configuration. Multi-tenant scoping, Subject creation, Topics & LOs, AI prompt config, model picker, scoring rubric, deploy via CI/CD. |
| **SC-ADD-03** | Charlie | `instructor.html` | 8 | Instructor Dashboard & At-Risk Intervention. Section overview, class heatmap, at-risk filter, student drill-down, conversation logs, transcript with AI feedback, Audit Trail. |
| **SC-ADD-04** | Bob | `super_admin.html` | 8 | Super Admin Governance & Cost Audit. Cross-tenant overview, Token Usage Tracking, cost-spike drill-down, Global Rate Limits, Compliance Report (TLS 1.3), Geo-redundancy, audit log. |
| **SC-ADD-05** | Alice | `tenant_admin.html` | 6 | Data Portability. REST API console, sample JSON response, one-click export wizard, CSV/JSON/Parquet picker, download confirmation. |
| **SC-ADD-06** | Alice | `tenant_admin.html` | 8 | Critical Incident Response & SLA. All-systems-operational baseline, LLM fallback engaged, notification, P1 ticket, JFT CSM thread, service restored, SLA dashboard. |

**Total: 73 screens across 4 HTML files.**

---

## Design System

The storyboard implements the **SDP Design System v1.2**, which is a brand theme layer on top of [Paragon](https://github.com/openedx/paragon) (Open edX's open-source design system).

| Layer | Purpose |
|:------|:--------|
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

All colors aligned to the WGU FY26 Design System Specification. Where FY26 and SDP Figma tokens conflict, FY26 values take precedence.

### Typography

- **Headings:** Sora Bold (H1: 40px, H2: 32px, H3: 28px, H4: 24px, H5: 20px)
- **Body:** Lato Regular 16px / 1.5 line-height
- **Type scale:** 12, 14, 16, 18, 20, 24, 28, 32, 40, 48px (strict — no off-scale sizes)
- **Code blocks:** Lato 14px on `#0d1117` for JSON / API consoles; light-mode student-storyboard code blocks use white background with SDP-palette syntax highlighting.

### Spacing

All padding, margin, and gap values follow an **8-point grid** (multiples of 8px: 8, 16, 24, 32, 40, 48px).

### Branding

The four portals use the **official WGU FY26 Corporation logo** (`assets/wgu-corporation-*.png`) instead of a wordmark placeholder:

- **Light theme:** Full-Color Reverse logo on the navy header (FY26 preferred for dark backgrounds)
- **Dark theme:** White logo on the navy header (FY26 single-color variant for dark backgrounds)
- The wordmark text label has been dropped — the logo stands alone, per Brady's branding rule.

---

## Features

- **73 interactive screens** across 4 self-contained per-persona portal HTMLs
- **Per-persona LRPS deep links** — each portal authenticates separately (Tenant Admin, Instructor, Super Admin all sign in via their own deep link). Screen 1 of each portal models the SSO landing.
- **Theme-aware logo swap** — Full-Color Reverse on light theme, White on dark theme; both render correctly on the navy header.
- **Real WGU FY26 Corporation logos** — `assets/wgu-corporation-white.png`, `wgu-corporation-full-color.png`, `wgu-corporation-full-color-reverse.png` (placeholder wordmark dropped).
- **Dark mode toggle** (moon/sun icon in header) with `localStorage` persistence shared across portals
- **Keyboard navigation** (arrow keys between screens within each portal)
- **Storyboard meta-bar** with 3-column layout: scenario ID, description, numbered screen buttons (per portal)
- **Presentation pages** — scrollable scenario catalogs with annotated screenshots (light and dark variants), now covering all 9 scenarios
- **Basic accessibility patterns** applied (semantic HTML, ARIA landmarks, heading hierarchy, focus-visible outlines) but no formal WCAG audit has been performed
- **FY26 brand compliance** — all colors, typography, and spacing validated against the WGU FY26 Design System Specification
- **Fully offline** — self-contained HTML files, no external dependencies beyond Google Fonts (Sora + Lato + Material Icons Outlined)
- **Paragon-compatible CSS** class names (`--pgn-*` tokens, `.btn-primary`, `.pgn__card`, `.pgn__breadcrumb`, `.pgn__data-table`, `.pgn__stepper`, etc.)

### New components introduced in v4.0

- `.heatmap-grid` + `.heatmap-cell` (h1–h9 9-step color scale) — instructor class heatmap
- `.score-pill` (low / med / high tints) — instructor objective scores
- `.api-console` + `.api-method` + `.api-endpoint` + `.api-params` — REST API console
- `.tab-switcher` — segmented control (CSV / JSON / Parquet)
- `.file-meta` — download confirmation file metadata card
- `.gauge-card` + `.gauge-number` + `.gauge-bar` — uptime / SLA / cost gauges
- `.chat-card` + `.chat-thread` + `.chat-bubble` + `.chat-avatar` — CSM ticket thread + AI coaching transcript
- `.spike-card` + `.spike-chart` + `.spike-bar` — daily cost trend (CSS bars, no SVG)
- `.util-meter` — inline utilization meter for tenant rows
- `.region-card` — geo-redundancy region cards with status stripe
- `.stepper-card` + `.stepper-bullet` + `.stepper-line` — CI/CD pipeline progress
- `.feedback-panel` (success / warning / danger) — fallback verification, deploy success, audit confirmation

---

## How to Use

### Online

| Page | URL |
|:-----|:----|
| Student Storyboard | **[brady-wgu.github.io/JFT_SDP_MVP](https://brady-wgu.github.io/JFT_SDP_MVP/)** |
| Tenant Admin Portal | **[brady-wgu.github.io/JFT_SDP_MVP/tenant_admin.html](https://brady-wgu.github.io/JFT_SDP_MVP/tenant_admin.html)** |
| Instructor Dashboard | **[brady-wgu.github.io/JFT_SDP_MVP/instructor.html](https://brady-wgu.github.io/JFT_SDP_MVP/instructor.html)** |
| Super Admin Portal | **[brady-wgu.github.io/JFT_SDP_MVP/super_admin.html](https://brady-wgu.github.io/JFT_SDP_MVP/super_admin.html)** |
| Scenario Catalog (Light) | **[brady-wgu.github.io/JFT_SDP_MVP/presentation.html](https://brady-wgu.github.io/JFT_SDP_MVP/presentation.html)** |
| Scenario Catalog (Dark) | **[brady-wgu.github.io/JFT_SDP_MVP/presentation_dark.html](https://brady-wgu.github.io/JFT_SDP_MVP/presentation_dark.html)** |

### Offline
Download the HTML files, the `assets/` directory (WGU logos), and the `screenshots/` / `screenshots_dark/` directories. Open in any browser. No server required.

### Navigation
- Use the **storyboard meta-bar** at the bottom of each portal to jump between scenarios and screens
- Use **arrow keys** (left/right) to step through screens sequentially within the active portal
- Toggle **dark mode** with the moon/sun icon in the upper-right corner — preference persists across portals via `localStorage`

### Regenerating screenshots

```bash
# 1. Start a static HTTP server from the repo root
python -m http.server 63417

# 2. In another terminal, run the capture pipeline
python capture_screens.py
```

Output: ~146 PNGs (73 per theme) into `screenshots/` and `screenshots_dark/`.

---

## Changelog (v4.0)

Changes applied since v3.1 (v1.2 student storyboard):

- **v1.3 Tenant Admin Portal** — new `tenant_admin.html` (23 screens) covering SC-ADD-02 (Portal & Course Configuration), SC-ADD-05 (Data Portability), SC-ADD-06 (Critical Incident Response & SLA Verification). Persona: Alice. Components include a 5-step CI/CD Stepper, REST API console with method/endpoint/params, JSON syntax-highlighted code blocks, JFT CSM chat thread, SLA gauge dashboard.
- **v1.3 Instructor Dashboard** — new `instructor.html` (8 screens) covering SC-ADD-03 (Instructor Dashboard & At-Risk Intervention). Persona: Charlie. Components include a CSS-grid student-competency heatmap (15 learners × 4 competencies, 9-step color scale), per-objective score pills, AI coaching transcript with feedback panels, Audit Trail event log with sha256 hashes.
- **v1.3 Super Admin Portal** — new `super_admin.html` (8 screens) covering SC-ADD-04 (Governance & Cost Audit). Persona: Bob. Components include cross-tenant overview gauges, 30-bar daily cost spike chart, per-tenant utilization meters, TLS 1.3 compliance report, geo-redundancy region cards, cross-tenant audit log feed.
- **Per-persona LRPS deep links** — each portal authenticates separately. Each Screen 1 models the LRPS landing → SSO → role mapping (Tenant Admin / Instructor / Super Admin · Platform Operations).
- **Real WGU FY26 Corporation logos** — placeholder wordmark replaced across the new portals. Theme-aware swap: Full-Color Reverse on light theme, White on dark theme. Logos under `assets/wgu-corporation-*.png`.
- **Wordmark text removed** — the logo image stands alone in the navbar (Brady's branding rule).
- **Personas use first names only** — `A Alice`, `C Charlie`, `B Bob` (matches Brady's existing convention).
- **Catalog presentations updated** — `presentation.html` and `presentation_dark.html` extended with full SC-ADD-02 / 03 / 04 / 05 / 06 walkthroughs (39 new annotated screenshots per theme). v1.2 student walkthroughs preserved unchanged. Document Control table extended with v1.3 entry.
- **Screenshot pipeline rewritten** — `capture_screens.py` now iterates four portals × two themes (light/dark) with theme-aware localStorage init. Output: 73 PNGs per theme.
- **TOC + navbar** — updated across both presentation files to include all 9 scenarios.

---

## Source Documents

This storyboard is grounded in the following WGU Program Development deliverables:

| Document | Version | Date |
|:---------|:--------|:-----|
| JFT SDP User Scenario Catalog: Additional Scenarios | v1.3 | 05 May 2026 |
| JFT SDP MVP Scenario Catalog | v1.2 | 07 Apr 2026 |
| JFT SDP User Profiles | v1.2 | 30 Mar 2026 |
| SDP Design System Specification | v1.2 | 30 Mar 2026 |
| WGU FY26 Design System Specification | v1.0 | 25 Mar 2025 |
| WGU Design Systems Differential Analysis | v2.0 | 16 Apr 2026 |

Upstream design system: [@openedx/paragon](https://github.com/openedx/paragon) (release-23.x, v23.19.1)

---

## For Developers (JFT)

This storyboard is a **medium-fidelity sample**, not production code or a pixel-perfect specification. It was built with Claude Code for rapid visualization and is meant to illustrate the general look and feel of the SDP and its administrative surfaces on a desktop browser. Do not attempt to replicate it exactly — use it as a rough guide for the intended user experience.

When implementing:

1. **Install Paragon** — `npm install @openedx/paragon`
2. **Apply WGU brand tokens** via the brand package override mechanism (`@wgu/sdp-brand`)
3. **Use Paragon React components** — do not rebuild them. The storyboard's CSS class names (`.pgn__card`, `.btn-primary`, `.pgn__breadcrumb`, etc.) map directly to Paragon's component schema.
4. **Per-persona portals are separate authenticated surfaces** — each has its own LRPS deep link. Tenant Admin, Instructor, and Super Admin should not be combined into a single SPA shell; the auth flow and RBAC scoping are role-bound.
5. **Tenant Admin owns three v1.3 scenarios in one portal** — SC-ADD-02 (Course Configuration), SC-ADD-05 (Data Portability), SC-ADD-06 (Incident Response). The screens compose into a single Tenant Admin experience but are documented separately in the catalog.
6. The CSS custom properties in the portal HTML files (`--pgn-*`) map directly to the Paragon token schema.
7. The screen layouts, component patterns, and interaction flows shown here illustrate the general direction — adapt them as needed for the production implementation.

---

<div align="center">

**Western Governors University** | Program Development | JFT SDP

*WGU confidential/proprietary. Do not redistribute without authorization.*

</div>
