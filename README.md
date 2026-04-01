<div align="center">

# JFT SDP MVP Storyboard

**Interactive Prototype for the WGU Skills Development Platform**

[![Live Demo](https://img.shields.io/badge/Live_Demo-GitHub_Pages-0055D4?style=for-the-badge&logo=github)](https://brady-wgu.github.io/JFT_SDP_MVP/)
[![Version](https://img.shields.io/badge/Version-3.0-4DB5E8?style=for-the-badge)]()
[![Screens](https://img.shields.io/badge/Screens-34-0A1E3C?style=for-the-badge)]()
[![WCAG](https://img.shields.io/badge/WCAG_2.2-AA-2E7D32?style=for-the-badge)]()

---

*A medium-fidelity HTML storyboard for the JFT SDP Coding Coach MVP release.*
*Built on the [SDP Design System v1.2](https://github.com/openedx/paragon) (Paragon / Open edX) with WGU brand tokens.*

</div>

---

## Overview

This storyboard is the authoritative UX reference for the **JFT Skills Development Platform (SDP) MVP** -- an AI-powered Python coding coach for WGU students. It covers all four MVP user scenarios defined in the JFT SDP MVP Scenario Catalog v1.1.

The prototype is a **single self-contained HTML file** that works offline, requires no build step, and renders in any modern browser. Developers should use it as the pixel-level reference for all student-facing screens in the MVP.

---

## Scenarios

| Scenario | Flow | Screens | Description |
|:---------|:-----|:-------:|:------------|
| **SC-MVP-01** | Basic | 8 | First launch of the Coding Coach. New student with no Python knowledge completes diagnostic, views progress map, begins first coaching task, saves session. |
| **SC-MVP-02** | Advanced | 11 | Progressive coaching with targeted feedback. Student with partial Python knowledge completes diagnostic, receives foundational coaching, encounters incorrect answer with specific error feedback, verifies gap resolution, advances difficulty. |
| **SC-MVP-03** | Professional | 9 | Experienced developer fast-tracks through the coaching baseline. Diagnostic demonstrates mastery across all sub-sections. One verification task required for Functions & Modular Programming. |
| **SC-MVP-04** | Returning | 6 | Student returns after a multi-week break. Prior progress preserved. Re-assessment verifies retention before resuming coaching at prior difficulty level. |

---

## Design System

The storyboard implements the **SDP Design System v1.2**, which is a brand theme layer on top of [Paragon](https://github.com/openedx/paragon) (Open edX's open-source design system).

| Layer | Purpose |
|:------|:--------|
| **Paragon** | Component structure, accessibility, base CSS (`@openedx/paragon`) |
| **WGU Brand Tokens** | Color, typography, spacing overrides (`--pgn-*` CSS custom properties) |
| **SDP Product** | Page composition, content structure, learning interactions |

### Color Palette

| Token | Hex | Role |
|:------|:----|:-----|
| Brand Dark Navy | `#0A1E3C` | Headers, structural elements |
| Brand Blue | `#0055D4` | Primary actions, CTAs, links |
| Brand Sky Blue | `#4DB5E8` | Accents, progress, info states |
| Accent Red | `#C13232` | Error states, emphasis |
| Deep Navy (FY26) | `#001730` | Navbar backgrounds |
| Ice Blue (FY26) | `#EEF6F9` | Light surface backgrounds |

### Typography

- **Headings:** Sora Bold (H1: 40px, H2: 32px, H3: 28px, H4: 24px, H5: 20px)
- **Body:** Lato Regular 16px / 1.5 line-height
- **Code:** Courier New 14px on `#0d1117` dark background

---

## Features

- **34 interactive screens** across 4 self-contained scenario flows
- **Dark mode toggle** (moon/sun icon in navbar) with localStorage persistence
- **Official WGU Corporation logos** embedded as base64 PNG
- **Keyboard navigation** (arrow keys between screens)
- **Admin bar** with 3-column layout: scenario ID, description, numbered screen buttons
- **WCAG 2.2 AA** compliant: semantic HTML, ARIA labels, focus styles, contrast-verified
- **Fully offline** -- single HTML file, no external dependencies
- **Paragon-compatible CSS** class names (`--pgn-*` tokens, `.btn-primary`, `.pgn__card`, etc.)

---

## How to Use

### Online
Visit the live demo: **[brady-wgu.github.io/JFT_SDP_MVP](https://brady-wgu.github.io/JFT_SDP_MVP/)**

### Offline
Download `index.html` and open it in any browser. No server required.

### Navigation
- Use the **admin bar** at the bottom to jump between scenarios and screens
- Use **arrow keys** (left/right) to step through screens sequentially
- Use the **Next/Back buttons** in each screen's footer
- Click interactive elements (sidebar links, CTAs, Submit buttons) to follow the scenario flow
- Toggle **dark mode** with the moon/sun icon in the upper-right corner

---

## Source Documents

This storyboard is grounded in the following WGU Program Development deliverables:

| Document | Version | Date |
|:---------|:--------|:-----|
| JFT SDP MVP Scenario Catalog | v1.1 | 30 Mar 2026 |
| JFT SDP User Profiles | v1.2 | 30 Mar 2026 |
| SDP Design System Specification | v1.2 | 30 Mar 2026 |

Upstream design system: [@openedx/paragon](https://github.com/openedx/paragon) (release-23.x, v23.19.1)

---

## For Developers

This storyboard is a **design reference**, not production code. When implementing:

1. Install Paragon: `npm install @openedx/paragon`
2. Apply WGU brand tokens via the brand package override mechanism
3. Use Paragon React components -- do not rebuild them
4. The CSS custom properties in this file (`--pgn-*`) map directly to the Paragon token schema
5. All screen layouts, component patterns, and interaction flows shown here are the implementation target

---

<div align="center">

**Western Governors University** | Program Development | JFT SDP

*WGU confidential/proprietary. Do not redistribute without authorization.*

</div>
