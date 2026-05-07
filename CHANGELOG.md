# Changelog

All notable changes to the JFT SDP storyboard. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

The repo's storyboard version (`Storyboard vN.M`) tracks the visual prototype, not the underlying SDP product version that JFT is building. The SDP product follows the user scenario catalog versions (v1.2 MVP, v1.3 Additional, etc.).

---

## v4.4 — 07 May 2026 — requirements gap fills against the contract

Eight contract-grounded gaps closed across the three admin portals. **Authority order baked in throughout: contract first, then User Profiles, then Mike's vernacular suggestions deprioritized to "out of scope unless requirements-grounded."** No changes to `student/index.html` (Brady's preservation directive — verified `git diff` shows 0 lines).

### Added — 6 new screens

- **`tenant_admin/` screen 26 — Instructor Roster & Course Assignment (G3, §2.5 + Zycus 10.8 RBAC).** 7-row instructor table including Course Instructors and Program Mentors (Charlie, Devon, Maya, Priya, Teagan, Noor, Logan/deactivated) with E010/E075/E135 course chips, active-learner counts (rolling enrollment), recent-assignment audit log, idle-warning badges, and bulk-import CTA. Explicit framing: LRPS owns account provisioning; this screen owns *course* assignment.
- **`tenant_admin/` screen 27 — Subject Lifecycle & Archival (G6, §2.5 module lifecycle + Zycus 10.4 audit logging).** Two-section layout: Active Subjects (E010 / E075 / E135 with deployed-version + learner-count + deactivate CTA) and Archived Subjects (E020 legacy / E099 pilot, FERPA-aligned 7-year retention, restore CTA). Right-rail "Deactivate Subject preview" panel with cutover date / retention policy / required-justification / audit warning.
- **`super_admin/` screen 9 — Third-Party Integrations (G8, §2.4 AI Orchestration + §2.5 system health).** Read-only Connected Services view: OpenRouter.ai (LLM gateway, replacing direct keys for OpenAI/Anthropic/Google), AWS (compute/data/networking), Datadog (APM/logs/synthetic), Entra ID (SSO), GitHub (CI/CD source), Slack (incident channel). Each card has a deep-link button to the vendor console. Explicit credential-management note: JFT owns rotation; rotate via Sev2 ticket, not in-portal.
- **`super_admin/` screen 10 — Learner Remediation (G1, Brady-clarified Global Admin scope).** LRPS owns account provisioning, so this screen is global-admin-only *coaching-state* remediation: per-objective score reset, reset all progress (subject or cross-subject), force re-diagnostic, pause access, view conversation log. Required justification field (audit-logged with actor/IP/before-after). Recent remediation events table. FERPA-scope clarification at the bottom: progress + score data only; account identity / LMS enrollment / grade-bearing assessments are out of scope.
- **`super_admin/` screen 11 — Billing & Cost Centers (G5, §11.1 hosting + support fee schedule + Zycus 6.6 token tracking).** Per-tenant cost allocation: 6-row table (PDev / SOB / SOH / SOE / SOIT / Pilot) with cost-center codes, owner emails, MTD spend, budget caps, EOM forecasts, status badges (PDev forecast to exceed). Spend-by-model breakdown via OpenRouter (Claude 56% / GPT-4o 28% / Gemini 16%). 4-row configurable budget-alert preferences.
- **`instructor/` screen 9 — Learner Search & Individual Lookup (G2, Zycus 7.10 + 7.12).** Reframed from Mike's "Gradebook" — the SDP is a practice tool, not a gradebook. Search by name / email / anonymized identifier across all 68 learners in Charlie's three courses, with course + status filters, sortable result table (Sally / Aisha / Daniel / Marcus / Priya / Jordan / Tasha / Riku as a representative cross-section), and per-row "Open profile" CTA that pivots to the existing drill-down. FERPA-scope note: Instructors only see learners in courses they instruct.

### Changed — small edits to existing surfaces

- **`tenant_admin/` screen 5 (AI Prompt Configuration)** — added a minimal "Recent versions" panel (G9) below the existing two-column form, showing the last 3 prompt edits with author, timestamp, and a one-line note. v3 marked as "live"; v2 + v1 read-only. Footnote explicitly defers diff view and rollback for JFT effort estimation. Per Brady: "minimal indication for JFT to see and push back if too hard."
- **`instructor/` screen 2 (Dashboard home)** — eyebrow chip "Active Section · Recommended next" → "Active Course · Recommended next". Stat caption "Spring 2026 · Sally and 27 others" → "28 active learners (rolling enrollment) · Sally + 27 others". "Roster" button → "Search learners" (deep-links to screen 9). E075/E135 cards: "Section" → "Course"; section numbers + Spring 2026 dropped.
- **`instructor/` screen 3 (Class heatmap)** — added export CTAs (Course report PDF / CSV) and a "Search by name / email" pivot to screen 9 (G10). Breadcrumb "E010 § 042" → "E010".
- **`instructor/` screen 5 (Sally profile)** — copy "E010 Section 042 · Cohort: Spring 2026" → "E010 · 28 active learners (rolling enrollment)". Breadcrumb sections updated.
- **`instructor/` screen 6 (Conversation logs)** — eyebrow "Cohort summary" → "Course summary".
- **`super_admin/` screen 2 (Portal home)** — Quick links extended from 4 cards to 8 (added Integrations / Learner Remediation / Billing / Audit Log).
- **Meta-bars** updated for `tenant_admin` (steps 26 + 27 added) and `super_admin` (steps 09 + 10 + 11 added) and `instructor` (step 09 added).
- **`capture_screens.py`** — PORTALS list updated; LRPS capture now scrolls the page so the live SDP rows + v4.3 "Not for student use" badges land in the hero shot (replacing the old top-of-page OEX-rows view that didn't communicate the page's purpose).

### Authority decisions documented in this release

Brady's directive: *"the contract rules everything. The User Profiles document is authoritative for persona naming and scope."* Items deprioritized accordingly:

- **Mike's "Course Instructor" rename** — REJECTED in v4.3, stays rejected. The User Profile + the requirements use `Instructor` as the contract-named user type.
- **Mike's "Admin" persona** — does not exist. The "global-level technical administrator with full cross-tenant access" *is* Super Admin (Bob) per the User Profile. Account-management functions land in `super_admin/`, not in a new persona and not in Tenant Admin (which is content-focused).
- **Account merge** — explicitly OUT per the requirements ("Manual creation or management of student accounts outside of LTI-based provisioning"). Not implemented.
- **AI score override authority for Instructors (G7)** — DROPPED. The SDP is a practice tool; coaching scores never feed academic records. There's no record to override.
- **Tenant Admin notification preferences (G4)** — DROPPED. The §9 Communication Plan is JFT→WGU rollout documentation, not runtime tenant-configurable alerting.
- **G11 (Tenant Onboarding Wizard) and G12 (Subject Usage Analytics heatmap)** — deferred per Brady direction.

### v4.4 size summary

- **6 new screens** (+ inline G9 panel + G10 heatmap CTAs)
- `tenant_admin` 25 → 27 · `instructor` 8 → 9 · `super_admin` 8 → 11
- **Total storyboard screens: 75 → 81**
- 164 PNGs regenerated (was 148)

---

## v4.3 — 07 May 2026 — v1.2 catalog cross-reference + LRPS admin labels

Catalog & narrative clarifications driven by a holistic re-read of the v1.2 student catalog (`JFT_SDP_MVP_Scenario_Catalog_v1_2_07APR2026.docx`) plus Mike's vernacular feedback. **No changes to `student/index.html`** — the v1 student screens are deliberately preserved as a baseline; all clarifications live in supporting narrative, READMEs, and the LRPS landing.

### Added

- **Top-level `README.md` — "Shared persona & course reference" section.** Codifies canonical strings used across all 5 surfaces: Sally (student), `E010` Foundations of Programming (Python), `§ 042` Spring 2026 section, `PDev` tenant, `WGUE010PythonAY2026` LMS course slug, the full prototype v1 13-sub-section taxonomy, and the SC-ADD-04 cost-spike date. Drift across these strings was the most common source of cross-portal inconsistency risk; this block makes the canonical values single-sourced.
- **Top-level `README.md` Student section — "v1.2 catalog alignment" note.** Documents 100% catalog coverage (34/34 screens) and points readers at `presentation.html` for elaborated UX details and `student/README.md` for known v1 limitations.
- **`student/README.md` — "Screen 1 (zyBooks landing) is reference design only" callout.** Per the v1.2 catalog, the zyBooks course-page screen exists to contextualize the LTI launch; it is not part of the Coding Coach application or a JFT deliverable.
- **`student/README.md` — "v1 Known Limitations" section.** Six honest call-outs of what v1 does not depict (no real Python execution, no mid-task pause/resume, no error recovery flows, no re-assessment failure path, only 3 of 13 sub-sections detailed in narrative, educator feedback loop invisible from student storyboard alone). Candidates for a v1.4 student refresh.
- **`lrps/README.md` — "LMS → LRPS → LTI provisioning chain (student-facing flow)" section.** Documents how the student-facing Coding Coach link is provisioned: D&D registers SDP as an LRPS provider → places the link on the zyBooks E010 course page → Sally clicks → LRPS handles SSO + issues an LTI 1.3 launch carrying her WGU student ID, course context, and Learner role. Per-persona deep links (Tenant Admin / Instructor / Super Admin) use the same chain with admin role mappings. Basic LTI 1.3, not LTI Advantage.

### Changed

- **`presentation.html` and `presentation_dark.html` — four SC-MVP step narrative expansions (mirrored across both files):**
  - SC-MVP-01 step 3 (Diagnostic Q1) — describes the "Need a Hint?" interaction (scaffolding without giving away the answer) and the AI evaluation messaging (text-based LLM evaluation, same logic that drives later coaching feedback).
  - SC-MVP-02 step 10 (Difficulty Advances) — itemizes the three persistent session-stats fields (Sub-section / Tasks completed / Current difficulty) shown across coaching screens.
  - SC-MVP-03 step 7 (Fast-Track Results) — narrates *why* 12 of 13 sub-sections check off from the diagnostic while Functions & Modular Programming alone requires hands-on verification (the diagnostic question pool does not adequately sample module-level skills like `__name__ == "__main__"` guards).
  - SC-MVP-04 step 3 (Re-Assessment Q1) — calls out the "Re-Assessment · Welcome Back" badge prominence and frames the 2-question check as a retention check (not a fresh diagnostic) before coaching resumes at Sally's prior difficulty level.
- **`lrps/index.html` — "Not for student use" amber badges on the three live SDP admin rows** (SDP-TA / SDP-IN / SDP-SA). Material `block` icon + 10.5px uppercase label in the warning-tint amber. Theme-aware (lighter on dark theme). Mike's feedback: LRPS is admin-visible in some contexts where students might also browse the page, and the admin rows must never be confused for student-facing resources. The student row (SDP-ST) is unchanged.

### Verification

- `student/index.html` byte-identical to v4.2 — Brady's preservation directive honored. Verify with `git diff student/index.html` (expects 0 changes).
- LRPS screenshots regenerated to capture the new admin-row badges (light + dark themes).
- All four SC-MVP step narrative expansions parse correctly in both `presentation.html` and `presentation_dark.html`.

### Out of scope (this release)

- requirements Tier 1 gap fills — pending Brady's per-item green-light against the contract (`JFT_WGU_MSA_SOW_signed_05MAY2026.md`); planned for the next v4.x release.
- Mike's larger integration suggestions — pending Brady's green-light, *re-targeted against the authoritative User Profiles* (`JFT_SDP_User_Profiles_v1_2_30MAR2026.docx`):
  - **Gradebook** — fits within `instructor/` (Charlie). The User Profile lists "Access and export individual and group student performance data" and "Drill into individual student performance records" as primary Instructor goals; a Gradebook view that shows AI scores and supports flagging is consistent.
  - **Account-management operations** (merge / archive / username correction) — fits within `super_admin/` (Bob, the global-level cross-tenant administrator). The User Profile lists "Provisioning, deprovisioning, and manage tenant environments" and "Cross-tenant audit logs" as Super Admin responsibilities. **Not** a Tenant Admin function — that role is content-focused per the User Profile ("content and operations owners, not infrastructure owners").
  - **Mike's "Course Instructor" rename** — REJECTED. The User Profile and requirements Section 2.5 both use `Instructor` as the contract-named user type. Per Brady: contract and User Profiles are authoritative; colleague-vernacular suggestions yield to those documents.
- Modifications to `student/index.html` — deliberately preserved as v1 baseline; candidates for a future v1.4 student refresh.

---

## v4.2 — 07 May 2026 — v1.3 gap-coverage pass

Three-pass review against the v1.3 User Scenario Catalog identified three requirements-ref gaps. Filled to bring all 5 v1.3 scenarios to **100% workflow + requirements-ref coverage**. Two consecutive review passes confirmed zero remaining gaps.

### Added (3 fills)
- **`tenant_admin/` screen 24 — Tenant Settings: Branding & Customization (§7.9 Custom Branding).** Two-column tenant configuration with form + learner-facing preview. Form fields: tenant display name, logo upload (with current preview), primary accent color picker, custom domain (with DNS-verified status), favicon, footer copy. Preview pane shows a mock of how Sally sees the WGU PDev branding when she launches the Coding Coach.
- **`tenant_admin/` screen 25 — Tenant Settings: Team & Role-Based Access (§10.8 RBAC).** 5-row team table (Alice + Sam + Robin + Quinn + pending Kit invite) with Owner / Editor / Viewer role badges. Recent role-change audit log. 10-row permissions matrix showing what each role can do. Multi-tenant isolation alert.
- **`super_admin/` screen 6 — Compliance Report enhancement (§10.1 FERPA Compliance).** Added a FERPA privacy compliance section above the existing TLS service-by-service table. 4 FERPA KPI gauges (100% staff training / 7-yr audit retention / 3-yr inactive learner data retention / N/A parental notification — adult learners only). 6-row FERPA control table referencing 34 CFR §§99.10 / 99.31 / 99.32 / 99.37 plus WGU policies 8.2 and 8.4. Eyebrow updated to "Encryption + Privacy Audit · §10.7 · §10.1."

### Changed
- `tenant_admin/` portal home (screen 2) gains a "Tenant Settings" button alongside the existing New Subject + Cross-Subject Analytics CTAs.
- Meta-bar SC-ADD-02 navigation extended from 9 buttons to 11 (steps 10/11 link to screens 24/25).
- `tenant_admin` `TOTAL_SCREENS` bumped 23 → 25.
- `capture_screens.py` PORTALS list extends `sc-add-02` screen ids with `[24, 25]` so the pipeline captures the new screens.
- `presentation.html` and `presentation_dark.html` extended with new SC-ADD-02 step 10 + 11 entries, SC-ADD-04 step 6 description enriched with FERPA, screen-map summary updated (SC-ADD-02 row 9 → 11; total 73 → 75).
- README, per-persona READMEs, and version badges updated to reflect 75-screen total.

### Coverage verification

Pass 2 + Pass 3 (both clean): every workflow sentence and every requirements reference across SC-ADD-02 through SC-ADD-06 is now visually depicted in the storyboard. Mapping table of requirements refs to screens lives in each persona's README.

---

## v4.1 — 07 May 2026 — Repo restructure

Reorganization-only release. No new scenarios or screen content.

### Changed
- **Repo renamed** `brady-wgu/JFT_SDP_MVP` → `brady-wgu/JFT_SDP`. The MVP suffix no longer reflects scope (storyboard now spans 4 personas, not just the v1.2 MVP).
- **Per-persona subdirectories.** Each portal moved into its own folder with its own `index.html`, `README.md`, `screenshots/`, and `screenshots_dark/`:
  - `index.html` → `student/index.html`
  - `tenant_admin.html` → `tenant_admin/index.html`
  - `instructor.html` → `instructor/index.html`
  - `super_admin.html` → `super_admin/index.html`
  - `lrps.html` → `lrps/index.html`
  - All 148 PNGs distributed into the corresponding per-persona screenshot directories.
- **`index.html` at root is now a portal-selector landing page** with cards for every surface (LRPS, Student, Tenant Admin, Instructor, Super Admin, Catalog) and 4 hero stats.
- **`README.md` rewritten** organized by user group / persona. The MVP-specific language now lives in the Student section. Each persona section covers scope, scenarios, screens, and links into the persona's subdirectory README.
- **Each persona subdirectory has its own README** — short summary, scenario IDs, screen count, embedded hero screenshot, links back to root.
- **Catalog screenshot paths updated** in `presentation.html` / `presentation_dark.html` to reference the new per-persona directories (146 total path rewrites across both files).
- **`capture_screens.py` rewritten** to derive output paths from each portal's HTML location — outputs now land in `{persona}/screenshots/` and `{persona}/screenshots_dark/`.
- **`CHANGELOG.md` extracted from README** so the README can stay current without bloating.
- **`.gitignore` added** for `.claude/`, OS junk, Python caches, node_modules.

### URL changes (post-rename, GitHub Pages auto-redirects for ~1 month)

| Old | New |
|---|---|
| `/JFT_SDP_MVP/` | `/JFT_SDP/` (now portal selector) |
| `/JFT_SDP_MVP/` (student) | `/JFT_SDP/student/` |
| `/JFT_SDP_MVP/tenant_admin.html` | `/JFT_SDP/tenant_admin/` |
| `/JFT_SDP_MVP/instructor.html` | `/JFT_SDP/instructor/` |
| `/JFT_SDP_MVP/super_admin.html` | `/JFT_SDP/super_admin/` |
| `/JFT_SDP_MVP/lrps.html` | `/JFT_SDP/lrps/` |
| `/JFT_SDP_MVP/presentation.html` | `/JFT_SDP/presentation.html` (path stable) |

---

## v4.0 — 07 May 2026 — Full v1.3 admin portal coverage

Major release adding the three v1.3 admin portals (Tenant Admin, Instructor, Super Admin) and the LRPS landing — bringing the storyboard from one persona (Sally) to four.

### Added
- **Tenant Admin Portal** (`tenant_admin/`) — Alice. 23 screens covering SC-ADD-02 (Portal & Course Configuration), SC-ADD-05 (Data Portability), SC-ADD-06 (Critical Incident Response & SLA Verification). New components: 5-step CI/CD Stepper, REST API console with method/endpoint/params, JSON syntax-highlighted code blocks, JFT CSM chat thread, SLA gauge dashboard.
- **Instructor Dashboard** (`instructor/`) — Charlie. 8 screens covering SC-ADD-03 (At-Risk Intervention). New components: CSS-grid student-competency heatmap (15 learners × 4 competencies, 9-step color scale), per-objective score pills, AI coaching transcript with feedback panels, Audit Trail event log with sha256 hashes.
- **Super Admin Portal** (`super_admin/`) — Bob. 8 screens covering SC-ADD-04 (Governance & Cost Audit). New components: cross-tenant overview gauges, 30-bar daily cost-spike chart, per-tenant utilization meters, TLS 1.3 compliance report, geo-redundancy region cards, cross-tenant audit log feed.
- **LRPS Landing** (`lrps/`) — recreation of WGU's internal Learning Resource Provisioning System. Originally faithful to the legacy enterprise aesthetic; restyled with the SDP Design System v1.2 in commit `e735361`. Each persona's secret LRPS deep link maps to a clickable provider row.
- **Real WGU FY26 Corporation logos** in `assets/`. Theme-aware swap: Full-Color Reverse on light theme, White on dark theme. Wordmark text removed (Brady's branding rule).
- **Per-persona LRPS deep links** modeled in each portal's screen 1 (SSO landing → role mapping).

### Changed
- **README bumped to v4.0**. Pages table extended; scenarios split into v1.2 (Sally) and v1.3 (Alice / Charlie / Bob) groups; new components enumerated.
- **`presentation.html` / `presentation_dark.html`** extended with full SC-ADD walkthroughs for SC-ADD-02 through SC-ADD-06 (39 new annotated steps each, ~250 lines added per file). Navbar / TOC / Document Control updated to cover all 9 scenarios.
- **`capture_screens.py` rewritten** to capture all 5 portals × 2 themes (148 PNGs total) with per-theme localStorage init.

### Notes
- SC-ADD-01 (acceptance rollup of v1.2 MVP) is in progress separately, no new scope. Mentioned in catalog but no new screens.
- LRPS layout fixed in `8704b3b` to eliminate a large left gutter at wide viewports (container max-width bumped 1300 → 1920px, side padding tightened, `minmax(0, 1fr)` added to the shell grid).

---

## v3.1 — 30 Apr 2026 — v1.2 catalog alignment

Polish release for the v1.2 student MVP storyboard.

### Added
- `presentation_dark.html` — dark-theme catalog with all 34 dark-theme screenshots.
- Skip navigation links, `<main>` landmark, contentinfo footer, focus indicators, responsive breakpoints, touch-target sizing, contrast-ratio fixes.

### Changed
- **zyBooks landing page** replaces the mock WGU Student Portal LMS page (Screen 01) across all four scenarios. "Coding Coach" CTA placed next to the Competencies section as the new entry point.
- **Sequential screen numbering** — all 34 screens renumbered sequentially (01–08 SC-MVP-01, 09–19 SC-MVP-02, 20–28 SC-MVP-03, 29–34 SC-MVP-04). Admin bar shows true screen numbers.
- **Presentation text sync** — `presentation.html` / `presentation_dark.html` aligned with v1.2 Scenario Catalog (07 Apr 2026), including expanded LRPS descriptions per WGU LRPS team review.
- **Design system audit** — 271 fixes across `index.html` and `presentation.html` for WCAG 2.2 AA compliance, FY26 color palette alignment, typography scale enforcement, 8-point spacing grid.
- **FY26 palette reconciliation** — `--pgn-*` tokens updated from SDP Figma values to FY26 authoritative values.
- **Light-mode code blocks** — white background with SDP palette syntax highlighting; dark mode retains `#0d1117`.
- All 68 screenshots (34 light + 34 dark) recaptured at 1440×900 with sequential filenames matching new screen IDs.

### Removed
- "Screen X of Y" navigation bar from all screens.

### Fixed
- `:focus-visible` outline on headings after programmatic focus suppressed.

---

## v3.0 — 30 Mar 2026 — Initial MVP storyboard

First complete v1.2 MVP storyboard release. 34 screens across the 4 student scenarios (SC-MVP-01 through SC-MVP-04). Single-page interactive prototype + scrollable presentation catalog. Built with Claude Code on the SDP Design System v1.2.

---

*Earlier internal iterations (v1.x, v2.x) are not included in this changelog.*
