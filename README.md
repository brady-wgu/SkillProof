<div align="center">

# SkillProof

**Medium-fidelity storyboard for WGU's AI-powered Python coding coach + the administrative surfaces around it**

[![Live Demo](https://img.shields.io/badge/Live-GitHub_Pages-0070F0?style=for-the-badge&logo=github)](https://brady-wgu.github.io/SkillProof/)
[![Version](https://img.shields.io/badge/Version-4.165-46B1EF?style=for-the-badge)](CHANGELOG.md)
[![Screens](https://img.shields.io/badge/Screens-46-001730?style=for-the-badge)]()
[![Personas](https://img.shields.io/badge/Personas-4-FBAE40?style=for-the-badge)]()

![Portal selector landing](assets/landing/light.png)

*A medium-fidelity sample — not a pixel-perfect specification. Built with Claude Code on the [SkillProof Design System v1.2](https://github.com/openedx/paragon) (Paragon / Open edX) with WGU FY26 brand tokens.*

</div>

---

## Overview

**SkillProof** is WGU's AI-powered Python coding coach for students, plus the administrative surfaces around it. This repo holds the **medium-fidelity storyboard** that JFT (Jellyfish Technologies) builds against — a self-contained, offline-capable visual sample of all the major surfaces:

- **Sally** (Student) — the v1.2 MVP coaching loop. **JFT shipped this first.** ([student/](student/))
- **Charlie** (Instructor) — At-Risk Intervention dashboard. ([instructor/](instructor/))
- **Alice** (School Admin) — Course + Skill management portal: School Dashboard with Course cards + filter/sort/search, 5-step New Skill wizard with Course Number/Title combobox typeahead, drill-chain mirroring Instructor for diagnostic, 4-level Analytics (School / Course / Skill / Topic). Scope is **Courses + Skills only** — at-risk learner tracking is Instructor's domain; School Settings + cross-School ops are Super Admin's. ([tenant_admin/](tenant_admin/)) — **12 screens**
- **Bob** (Super Admin) — Cross-School governance, financial controls, security compliance, **access control** (role elevation + School Admin → Schools + Instructor → Skills + Skill ownership / deployment), data + integrations hub, **School Management** (per-School branding / thresholds / retention — moved from School Admin v4.114), FERPA-aligned Logs, plus the inherited Course → Skill → Learner drill and 5-level Analytics. ([super_admin/](super_admin/)) — **11 screens**
- Plus **LRPS Landing** at the storyboard root ([`/`](./)) — recreated WGU internal Learning Resource Provisioning System; the realistic entry point for all four personas. **(v4.59: promoted to root; the standalone `/lrps/` URL was retired.)**
- Plus **Help & Resources** ([help/](help/)) — shared self-service support + video training surface linked from every admin portal's navbar.

**Platform-wide:** every *analyzable* data table carries a consistent control bar — **filter chips + search + sort + a unified "Export ▾" dropdown** (shared [`assets/table-controls.js`](assets/table-controls.js)), with export formats matched to the audience (**PDF / CSV** for people, **MD / JSON** for machines such as logs). Editors and pick-lists (Topics/LOs, model picker) carry no controls. Long analytics pages have a **sticky scroll-spy section nav**; status colors use one **heat scale** (red → amber → green) across heatmaps, score pills, badges, dots, and threshold/budget bars; and create / delete / remove flows confirm via **modals**.

Each persona has its own **secret LRPS deep link** in production and authenticates separately. They share the SkillProof Design System v1.2 chrome and the WGU FY26 brand so the suite reads as one cohesive product family.

> **Implementation notes (for JFT).** The School Admin, Instructor, and Super Admin scenarios are the design spec for surfaces JFT has not yet started building. Use this storyboard as the visual North Star for the **full SOW scope**. WGU expects JFT to deliver every binding requirement in the MSA, the SOW body, and Appendix A within the contracted engagement window. The first JFT release was an MVP slice (E010 Coding Coach in `student/`); subsequent releases close the rest of Appendix A across the School Admin, Instructor, and Super Admin portals. The SC-MVP scenarios deploy the existing Cicada coaching loop as-is; the surrounding platform (multi-LLM orchestration, admin portals, observability, exports, integrations, compliance surfaces) is net-new build work per Appendix A. WGU also runs independent accessibility testing against WCAG 2.2 AA in addition to JFT's own self-checks per §16.2 #7.3 (student-facing surfaces; admin surfaces follow standard usability per SOW §3 Assumptions), so plan for remediation cycles inside the engagement window.

### Surfaces

| Surface | URL | Description |
|:--------|:----|:------------|
| **LRPS Landing** (storyboard root) | [`/`](https://brady-wgu.github.io/SkillProof/) | Entry point — table segmented into **Student Skills** (33, incl. 1 broken DEV, 24 E010/D522 skill-level links, and 1 broken skill-level link), **Staff Links** (6, incl. 3 broken DEV), and **Prototypes** (4 storyboard). **Start here.** **v4.166:** added 24 skill-level LRPS links (10 for E010, 14 for D522) from the 16 Jul 2026 link-list update; flagged D522-13 as broken per LOG-033/034 (a post-deploy rename orphaned its LRPS link). **v4.165:** pagination removed — this is a single real, complete page now, not a sample of a huge simulated dataset. **v4.164:** all decorative filler rows removed; every real link from the SkillProof link tracker now represented, including broken DEV entries. **v4.163:** STU101 added. **v4.162:** segmented into 3 sections. **v4.161:** live skill rows added. **v4.59:** promoted to root. |
| **Student Storyboard** | [`/student/`](https://brady-wgu.github.io/SkillProof/student/) | Sally's coaching loop — the v1.2 MVP, rebuilt v4.58 from the live JFT deployment at `wgu.teamjft.com`. **18 screens.** |
| **Instructor Dashboard** | [`/instructor/`](https://brady-wgu.github.io/SkillProof/instructor/) | Charlie — Course overview → class heatmap → Skill/Topic drill → Learner profile, plus Access Denied. **5 screens.** |
| **School Admin Portal** | [`/tenant_admin/`](https://brady-wgu.github.io/SkillProof/tenant_admin/) | Alice — School Dashboard with KPI rollup + Course cards (Skills folded in) + filter/sort/search, Course view, drill-chain to learner detail (S2–S4 mirror of Instructor), New Skill wizard (5 steps) with Course Number/Title combobox, 4-level Analytics + Activity Log. Scope: **Courses + Skills only.** **New Course is now a modal** from the dashboard; delete actions confirm via modal. **12 screens** (v4.152). |
| **Super Admin Portal** | [`/super_admin/`](https://brady-wgu.github.io/SkillProof/super_admin/) | Bob — Super Admin Dashboard (platform KPIs + per-School cost table + quick-links), **Access Control** (People · Skills · Schools tabs; 4-tier roles; min-2-Super-Admins; sole elevator), **School Management** (per-School Branding / Default Thresholds / Data Retention — moved from School Admin v4.114), 5-level Analytics, the inherited Course → Skill → Learner drill, External Tooling, Data Hub, and FERPA-aligned Logs. **Create a School is a modal** and assignment removals confirm via modal. **11 screens.** |
| **Help & Resources** (shared) | [`/help/`](https://brady-wgu.github.io/SkillProof/help/) | Shared self-service support, documentation, and video training surface. Linked from every admin portal navbar. Closes Appendix A §16.4 #9.14 (self-service portal) and #9.15 (video training). |

**Total: 46 screens · 4 personas · 6 surfaces (4 persona portals + LRPS root + Help).**

---

## Live Skills (LRPS)

All live rows open in a new tab from the landing page's Links table, so the shared landing link doubles as a launch hub. The table is segmented into three sections and mirrors `.../SkillProof/g_Beta Test/skillproof-link-list_<DATE>.md` — Brady's own environment link tracker — exactly (no decorative filler rows). PROD isn't listed anywhere below because it doesn't exist as infrastructure yet (JFT todo, ~1-2 weeks after the D522 iteration as of 08 Jul 2026); every entry here is STAGE unless marked DEV.

### Student Skills

| Skill | Environment | LRPS launch URL |
|:------|:------------|:----------------|
| Python | STAGE | https://lrps.wgu.edu/provision/568442570 |
| Professionalism | STAGE | https://lrps.wgu.edu/provision/572550562 |
| Applied UX | STAGE | https://lrps.wgu.edu/provision/572550817 |
| E010 | STAGE | https://lrps.wgu.edu/provision/572551037 |
| Calc | STAGE | https://lrps.wgu.edu/provision/572551265 |
| Teaching Engineering | STAGE | https://lrps.wgu.edu/provision/572551549 |
| D522 — Python for IT Automation | STAGE | https://lrps.wgu.edu/provision/575242504 |
| STU101 — Time Management & Study Skills | STAGE | https://lrps.wgu.edu/provision/576572714 |
| Python (DEV) | **DEV — broken, JFT fix pending** | https://lrps.wgu.edu/provision/560264094 |

### E010 — Foundations of Programming (skill-level, STAGE)

Added 16 Jul 2026. Breaks the single E010 course-level skill above into its 10 constituent Topics for granular LRPS testing.

| Skill | Environment | LRPS launch URL |
|:------|:------------|:----------------|
| E010-01 Python Basics (E010) — master | STAGE | https://lrps.wgu.edu/provision/577937240 |
| E010-02 Terminal Basics | STAGE | https://lrps.wgu.edu/provision/577937133 |
| E010-03 Variables, Data Types & Type Conversion | STAGE | https://lrps.wgu.edu/provision/577937026 |
| E010-04 Reading User Input & String Formatting | STAGE | https://lrps.wgu.edu/provision/577936948 |
| E010-05 Operators | STAGE | https://lrps.wgu.edu/provision/577936808 |
| E010-06 Conditionals & Loops | STAGE | https://lrps.wgu.edu/provision/577936681 |
| E010-07 Strings & Lists | STAGE | https://lrps.wgu.edu/provision/577936540 |
| E010-08 Dictionaries, Tuples & Sets | STAGE | https://lrps.wgu.edu/provision/577936443 |
| E010-09 Functions | STAGE | https://lrps.wgu.edu/provision/577936322 |
| E010-10 datetime, Debugging & Building Small Programs | STAGE | https://lrps.wgu.edu/provision/577936192 |

### D522 — Python for IT Automation (skill-level, STAGE)

Added 16 Jul 2026. Breaks the single D522 course-level skill above into its 14 constituent Topics. D522-13's course slug still reads `building-small-pro` from an earlier renaming test — link works, label is correct, slug is cosmetic-only.

| Skill | Environment | LRPS launch URL |
|:------|:------------|:----------------|
| D522-01B Python Basics for IT Automation — master | STAGE | https://lrps.wgu.edu/provision/577934102 |
| D522-02 Variables, Data Types & File Paths | STAGE | https://lrps.wgu.edu/provision/577933941 |
| D522-03 String Formatting, Lists & Dictionaries | STAGE | https://lrps.wgu.edu/provision/577933773 |
| D522-04 Type Conversion, Variable Naming & Comments | STAGE | https://lrps.wgu.edu/provision/577933647 |
| D522-05 Functions, Docstrings & Script Structure | STAGE | https://lrps.wgu.edu/provision/577933512 |
| D522-06 Conditionals, Loops & Writing a README | STAGE | https://lrps.wgu.edu/provision/577933385 |
| D522-07 Listing Directory Contents, Reading Files & Writing Files | STAGE | https://lrps.wgu.edu/provision/577933189 |
| D522-08 File Metadata & Copying Files | STAGE | https://lrps.wgu.edu/provision/577933021 |
| D522-09 Reading CSV Files, Writing CSV Files & Sorting Data | STAGE | https://lrps.wgu.edu/provision/577932832 |
| D522-10 The datetime Module & Working with JSON | STAGE | https://lrps.wgu.edu/provision/577932611 |
| D522-11 os & socket Modules, Parsing Command Output, subprocess | STAGE | https://lrps.wgu.edu/provision/577932376 |
| D522-12 logging & requests Modules, Exception Handling | STAGE | https://lrps.wgu.edu/provision/577932197 |
| D522-13 paramiko & netmiko Modules | **STAGE — broken, dead link (renamed post-deploy; LOG-033/034)** | https://lrps.wgu.edu/provision/577932056 |
| D522-14 Building Small Programs | STAGE | https://lrps.wgu.edu/provision/577935204 |

### Staff Links

| Role | Environment | LRPS launch URL |
|:-----|:------------|:----------------|
| Instructor Portal | STAGE | https://lrps.wgu.edu/provision/570441081 |
| School Admin | STAGE | https://lrps.wgu.edu/provision/568442441 |
| Super Admin | STAGE | https://lrps.wgu.edu/provision/573162919 |
| Instructor Portal (DEV) | **DEV — broken, JFT fix pending** | https://lrps.wgu.edu/provision/568111823 |
| School Admin (DEV) | **DEV — broken, JFT fix pending** | https://lrps.wgu.edu/provision/568112003 |
| Super Admin (DEV) | **DEV — broken, JFT fix pending** | https://lrps.wgu.edu/provision/575058314 |

### Prototypes (storyboard only)

The four persona storyboard portals (`student/`, `instructor/`, `tenant_admin/`, `super_admin/`) remain at the bottom of the table for reference. They navigate in the same tab.

---

## Repo layout

```
SkillProof/
├── index.html                  LRPS Landing (storyboard root, since v4.59)
├── capture_screens.py          Playwright screenshot pipeline
├── README.md                   This file
├── CHANGELOG.md                Version history
├── assets/
│   ├── wgu-corporation-*.png  WGU FY26 corporate logos (3 variants)
│   ├── wgu-favicon.png        WGU shield (every page's favicon, added v4.46)
│   └── landing/                Root (LRPS) hero screenshots (light + dark)
├── student/                    v1.2 MVP — Sally (rebuilt v4.58 from live wgu.teamjft.com)
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            18 PNGs (light)
│   └── screenshots_dark/       18 PNGs (dark)
├── instructor/                 v1.3 — Charlie (5 screens; SC-ADD-03 At-Risk Intervention)
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            5 PNGs
│   └── screenshots_dark/       5 PNGs
├── tenant_admin/               v1.3 — Alice (12 screens; SC-ADD-02 Skill Configuration)
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            12 PNGs
│   └── screenshots_dark/       12 PNGs
├── super_admin/                v1.3 — Bob (11 screens; SC-ADD-04 Governance + Access Control)
│   ├── index.html
│   ├── README.md
│   ├── screenshots/            11 PNGs
│   └── screenshots_dark/       11 PNGs
└── help/                       Shared self-service support + training (added v4.38)
    ├── index.html
    ├── screenshots/            1 PNG
    └── screenshots_dark/       1 PNG
```

Screenshot filenames follow `screen-NN.png` (since v4.155), 1:1 with on-page screen IDs and the `?screen=N` deep-link URLs.

Click any persona folder to read its dedicated README.

---

## Persona sections

### 🎓 Student (v1.2 MVP) — Sally

**Surface:** [`student/`](student/) · [Live](https://brady-wgu.github.io/SkillProof/student/) · [README](student/README.md)

**Persona:** Sally — Beginner / Intermediate / Advanced Python knowledge. Launches via LTI 1.3 from her zyBooks course page.

**Scope:** This is the **v1.2 MVP scope** — the first JFT release. It deploys the existing Cicada v1 proof-of-concept codebase to production-quality, scalable infrastructure with a polished UI, accessible outside the WGU intranet via LTI 1.3 SSO. No new features, adaptive logic changes, or coaching algorithm modifications are in scope for this v1.2 release.

**Scenarios (4 scenarios · 34 steps across 18 screens):**

| ID | Flow | Screens | Description |
|:---|:-----|:-------:|:------------|
| **SC-MVP-01** | Basic | 8 | First launch. New student with no Python knowledge. Diagnostic → progress map → first coaching task → save. |
| **SC-MVP-02** | Advanced | 11 | Progressive coaching. Partial Python knowledge. Diagnostic → coaching → incorrect-answer feedback → verification → difficulty advance. |
| **SC-MVP-03** | Professional | 9 | Experienced developer fast-tracks. Diagnostic shows mastery; one verification task for Functions & Modular Programming. |
| **SC-MVP-04** | Returning | 6 | Returns after multi-week break. Prior progress preserved. Re-assessment verifies retention before resuming. |

**Source:** SkillProof MVP Scenario Catalog v1.2 (07 Apr 2026).

**v1.2 catalog alignment:** 100% (all 34 catalog steps depicted across the 18 screens). Honest call-outs of what v1 does **not** depict (no real Python execution, no mid-task pause, no error recovery, no re-assessment failure path, etc.) are enumerated in [student/README.md](student/README.md#v1-known-limitations). The v1 student screens are deliberately frozen as a baseline — see that file for the full list of v1.4+ candidate gaps.

---

### 👨‍🏫 Instructor (v1.3) — Charlie

**Surface:** [`instructor/`](instructor/) · [Live](https://brady-wgu.github.io/SkillProof/instructor/) · [README](instructor/README.md)

**Persona:** Charlie — Instructor (per User Profile + SOW §2.5) for E010 Foundations of Programming (Python), E075 Intermediate Python & Libraries, and E135 OOP with Python.

**Scope:** Educator-facing analytics and learner engagement tracking. SkillProof is a practice tool — coaching scores never feed academic records.

**Scenarios (1, 5 screens; sequential 1-5):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-03** | **Instructor Dashboard & At-Risk Intervention.** Instructor Dashboard (active Courses + nested Skills) → Course view → class Skill heatmap (15 learners × Topics, 9-step heat scale; export CTAs per §7.14) → at-risk filter → Sally learner-profile drill → Access Denied (zero-trust deny path). *(Multi-turn transcript + audit-trail screens removed in v4.121 — conversations are single Q+A.)* | 5 |

**Source:** SkillProof User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026).

---

### 🏫 School Admin (v1.3) — Alice

**Surface:** [`tenant_admin/`](tenant_admin/) · [Live](https://brady-wgu.github.io/SkillProof/tenant_admin/) · [README](tenant_admin/README.md)

**Persona:** Alice — WGU Program Development (PDev) employee operating the **School of Technology**. The SOW's contract term for this role is §2.2's admin-portal deliverable; the storyboard and all user-facing chrome call it **"School Admin"** per Brady's terminology lock (24 May 2026), so the role reads clearly to WGU staff outside the small dev team. Authenticates via her own secret LRPS deep link.

**Scope:** Course-as-a-Service authoring (Skills, Topics, Learning Objectives with per-objective passing thresholds via inline expanders), AI coaching prompt configuration, model + coaching style selection, CI/CD-driven deploys, post-deploy manual LRPS provisioning ticket workflow, Skill lifecycle / archival, and analytics & reporting (engagement charts · class insights · program reports + Activity Log). Per-School branding / thresholds / retention moved to the Super Admin portal (v4.114); the School Admin now manages Courses + Skills only.

**Scenarios (1, 12 screens; sequential 1-12):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-02** | **School Admin Portal & Skill Configuration.** School Dashboard (Course cards + KPI rollup) → Course → Skill heatmap → Learner drill (S2–S4) → Access Denied (S5) → 5-step **New Skill** wizard (Skill details → Topics & Learning Objectives → Model & AI prompt → Deploy review → build success + LRPS provisioning ticket; S6–S10) → Analytics & Reporting + Activity Log (S11) → Archived Skills (S12). **New Course** opens a modal from the dashboard; the Archived "permanently delete" confirms via modal. | 12 |

**Source:** SkillProof User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026) + WGU working draft *"SkillProof Authentication, Access Control, and Role Hierarchy" v1.0* (13 May 2026).

---

### 🛡️ Super Admin (v1.3) — Bob

**Surface:** [`super_admin/`](super_admin/) · [Live](https://brady-wgu.github.io/SkillProof/super_admin/) · [README](super_admin/README.md)

**Persona:** Bob — WGU platform operations and infrastructure. Authenticates with MFA in addition to SSO. Cross-School scope and sole controller of platform access; minimum 2 Super Admins required at all times.

**Scope:** Cross-School governance, financial controls, security compliance, global resource management, user role elevation, instructor-to-Skill assignment, and School lifecycle management.

**Scenarios (1, 11 screens; sequential 1-11):**

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-04** | **Super Admin Governance, Access Control, Schools & Data.** SSO + MFA → Dashboard (platform KPIs + cost / budget + per-School table + quick-links) → **Access Control** (People · Skills · Schools tabs; 4-tier role taxonomy; min-2-Super-Admins; assignment removals confirm via modal) (S2) → Access-expired (S3) → **School Management** (per-School Branding / Default Thresholds / Data Retention; + New School = modal) (S4) → 5-level **Analytics** (Platform → School → Course → Skill → Topic) (S5) → inherited Course → Skill → Learner drill (S6–S8) → **External Tooling** (AWS / OpenRouter / Redis / Grafana / Jira / GitHub) (S9) → **Data & Integrations Hub** (export · webhooks · GraphQL · Kafka / Kinesis / Pub-Sub streaming) (S10) → **Logs** (FERPA-aligned cross-School audit; export + tail-live + filters) (S11). | 11 |

**Source:** SkillProof User Scenario Catalog: Additional Scenarios v1.3 (05 May 2026) + WGU working draft *"SkillProof Authentication, Access Control, and Role Hierarchy" v1.0* (13 May 2026).

---

### 🚪 LRPS Landing (Entry Point)

**Surface:** [`/` (storyboard root)](./) · [Live](https://brady-wgu.github.io/SkillProof/) — v4.59 promoted to root; the standalone `lrps/` folder was deleted.

**Persona:** Sally (Student) — this is the LRPS view a learner sees when launching the Coding Coach from her LMS course module. The four live persona rows are present here so stakeholders can preview each persona's portal from one place, but the framing matches the end-learner's entry point.

**Scope:** A recreation of WGU's internal Learning Resource Provisioning System, styled in the SkillProof Design System v1.2. Each of the four persona portals has its own provider row in this table; clicking the row deep-links into the corresponding portal. JFT does not build LRPS — it is modeled here only to make the deep-link source feel authentic.

The LRPS surface includes:
- 4 live SkillProof rows (Student, Instructor, School Admin, Super Admin) — clickable, deep-linked
- Illustrative filler rows (OEX modules, zyBooks, Pearson, ProctorU, Coursera, Cicada legacy, Panopto, etc.) for realistic LRPS density
- A meta-bar quick-launch with chips to all surfaces + the catalog

---

### 📚 Help & Resources (shared surface)

**Surface:** [`help/`](help/) · [Live](https://brady-wgu.github.io/SkillProof/help/)

**Scope:** Single-page self-service support + video training surface. Linked from the Help button in every admin portal's navbar (tenant_admin, super_admin — instructor still pending). Closes Appendix A §16.4 #9.14 (self-service support portal) and #9.15 (video training resources). The Contact JFT Support FAB at the bottom-right opens the support-ticket flow (Zendesk handoff).

---

## Shared persona & course reference

Canonical strings used across all surfaces. Use these verbatim when adding new screens, narrative, or test fixtures so the storyboard remains internally consistent. (Drift here is the most common source of bugs — e.g., a School Admin screen that calls Sally's course "E010" while the Instructor heatmap calls it "Foundations of Programming".)

| String | Canonical value | Notes |
|:-------|:----------------|:------|
| **Student persona** | `Sally` | First name only. Avatar initial: `S`. Used in LTI 1.3 `name` claim. Knowledge level varies by scenario; same Sally across all four. |
| **Course code** | `E010` | Course code for "Foundations of Programming (Python)". |
| **Course title** | `Foundations of Programming (Python)` | Or short form `Python Foundations` in tight UI chrome. Never abbreviate to "FoP" in user-facing copy. |
| **Enrollment model** | `Rolling enrollment` | Per the User Profile, WGU has no fixed cohorts or sections. Every learner enters on their own day and progresses at their own rate. Avoid "Section 042" / "Spring 2026" framing in any new screen copy — talk about *active learners in a Skill* instead. |
| **Tenant (default example)** | `School of Technology` | Tenant slug: `tenant_school_tech`. Alice operates this tenant; she is a WGU Program Development (PDev) employee. |
| **Operating team** | `WGU Program Development` | PDev employees operate the School-tenants. Distinct from a tenant name — PDev does the work *on behalf of* each School. |
| **All 4 WGU Schools (example tenant set)** | `School of Technology`, `School of Business`, `School of Education`, `Leavitt School of Health` | Per WGU's School-as-Tenant model. Additional Schools can be created via the **+ New School** modal in super_admin (School Management). |
| **LMS course identifier** | `WGUE010PythonAY2026` | The LRPS-registered LMS course slug zyBooks renders. Visible on Screen 1 of every SC-MVP scenario. |
| **13 Topics** | Basic Syntax & Data Types · Control Flow & Logic · Data Structures: Lists, Tuples, Sets, Dictionaries · Functions & Modular Programming · Object-Oriented Programming · Error Handling & Exceptions · File I/O & Persistence · Iterators & Generators · Decorators & Closures · Concurrency Basics · Standard Library Essentials · Testing & Debugging · Packaging & Environments | The full Cicada v1 SkillProof Topic taxonomy within the Python Skill of E010. Order is significant: Progress Map renders in this order. |
| **Cost-spike date (SC-ADD-04)** | `04 May 2026` | Bob's cost audit drill-down references this date as the spike origin. |
| **Role taxonomy** | `Student → Instructor → School Admin → Super Admin` | 4-tier RBAC. Only Super Admin can change roles; minimum 2 Super Admins always. |
| **Storyboard version** | `v4.x` | Tracks the visual prototype, not the underlying SkillProof product. SkillProof product versions follow the catalog: v1.2 MVP, v1.3 Additional, etc. |

If you need to change any of these, update them everywhere in the same commit — `Glob` for the literal string across all portals and all per-persona READMEs before opening the PR.

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
| **Heatmap gradient** (9-step) | `--heat-1` through `--heat-9` (red → green via amber midpoints) | `instructor/index.html` screen 3 (15-learner × 4-Topic class heatmap) | Sequential data visualization needs perceptually distinct steps; FY26 has no diverging-scale tokens. |

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
python -m http.server 8000

# 2. In another terminal
python capture_screens.py
```

Output: **96 PNGs total** — 47 per theme (student 18 · instructor 5 · tenant_admin 12 · super_admin 11 · help 1) × 2 themes (light + dark) + 2 landing assets (the root LRPS UI). Filenames are `screen-NN.png` per portal, 1:1 with on-page screen IDs. Output lands in the per-persona `screenshots/` and `screenshots_dark/` subdirs.

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
4. **Per-persona portals are separately authenticated surfaces** — each has its own LRPS deep link. School Admin, Instructor, and Super Admin should not be combined into a single SPA shell; the auth flow and RBAC scoping are role-bound.
5. **Zero-trust authorization** — the LRPS link does not grant authority. Effective role and scope are determined server-side after authentication.
6. **Multi-tenancy maps to WGU Schools** — each WGU School is provisioned as a separate tenant internally. The example storyboard uses School of Technology as Alice's default School; additional Schools can be created via the Super Admin's School Management surface.
7. The CSS custom properties in the portal HTML files (`--pgn-*`) map directly to the Paragon token schema.
8. Each persona's [`README.md`](#repo-layout) lists the specific patterns and components introduced for that surface.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full version history. **Latest: v4.160 (2 Jun 2026)** — unified export: one consistently-placed "Export ▾" dropdown on every filtered table, formats by data nature (PDF/CSV for people, MD/JSON for machines). v4.159 de-duplicated the Logs filter bars, wired the navbar logo to "home", and added dashboard subtitles. v4.158 was the filter/sort placement audit + Result-column removal; v4.157 removed the analytics "AA contrast" chip; v4.156 was the design-system polish pass across the 3 admin portals (8-pt spacing + token consistency, grounded in the SkillProof Design System v1.3) plus leadership-facing enhancements: real export-confirmation toasts, a live institution-branding preview, a visualization key, and a responsive phone preview. Recent milestones: v4.155 screenshots regenerated with `screen-NN.png` naming; v4.152 shared controls module + heat-scale unification + modals; v4.153 `?screen=N` deep-link support; v4.154 dark mode working across all 6 surfaces; the Coda Contract Requirements tracker is fully populated (34 Met / 2 In Progress / 2 Deferred / 54 N/A out of 92 reqs).

Earlier milestones (13 May 2026):

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
