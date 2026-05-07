# Changelog

All notable changes to the JFT SDP storyboard. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

The repo's storyboard version (`Storyboard vN.M`) tracks the visual prototype, not the underlying SDP product version that JFT is building. The SDP product follows the user scenario catalog versions (v1.2 MVP, v1.3 Additional, etc.).

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
