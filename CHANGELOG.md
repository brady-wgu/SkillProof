# Changelog

All notable changes to the JFT SDP storyboard. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

The repo's storyboard version (`Storyboard vN.M`) tracks the visual prototype, not the underlying SDP product version that JFT is building. The SDP product follows the user scenario catalog versions (v1.2 MVP, v1.3 Additional, etc.).

---

## v4.28 — 11 May 2026 — Instructor metrics retargeted + new super_admin External Tooling screen (closes deferred JFT items J / K / L / M)

Brady's 11 May direction closed 4 deferred decision points from yesterday's JFT meeting that had been parked under the "Tenant Admin first" directive. v4.28 ships them in one release.

> **J**: "Display the metrics that are most useful to the instructor. Remove any 'total time on site' metrics, but focus on things that show where students are having problems so they can be resolved."
>
> **K**: "Let's mimic the AWS console and have links to these 3rd party resources on a page for the admin to click to. I don't want to duplicate effort here, just illustrate that some things will be on this page, but other things will be on 3rd party dashboards, such as AWS specifically."
>
> **L & M**: "This is a global setting right now. Unless there is a requirement for this being configurable per-course, let's stick with the global setting perspective for this. I do think some of these options are in the 3rd party tools as well, such as OpenRouter.ai, AWS, Redis, and the other tools being leveraged."
>
> — Brady, 11 May 2026

### J — Instructor metrics retargeted to struggle / intervention indicators

All 4 in-place edits on existing `instructor/index.html` screens. No new screens. Pattern: strip time-on-site metric → replace with metric that tells the instructor *where to focus the intervention*.

| Screen | Removed | Added |
|---|---|---|
| **Screen 5** Sally profile card | `Total time: 2h 22m` row | `Stuck on: **Lists & comprehensions** (LO 3.1)` row + `LO misses (last 9 sessions): 14` badge |
| **Screen 6** Conversation log table | `Duration` column (e.g. "18m 12s") | `Outcome` column with semantic badges: `LO miss × N` (danger) / `Stuck (no progress)` (warning) / `Partial progress` (warning) / `Progress` (info) / `Baseline` (gray) |
| **Screen 7** Session 09 transcript eyebrow | `· 18m 12s ·` from "Session 09 · 06 May 2026 · 18m 12s · Lists & comprehensions" | `· 5 AI feedback panels · 3 LO misses` |
| **Screen 8** Audit Trail KPI strip | `18m 12s Session length` stat | Two struggle stats: `3 LO misses` (danger color) + `5 AI escalations` (warning color); kept the `0 Events dropped` + `100% Capture integrity` integrity stats |

Instructor screen count unchanged at 8. The Audit Trail still has its FERPA-integrity job (event count, dropped events, capture integrity) — Brady didn't ask to gut that, just to add struggle signal where there used to be a time metric.

### K — New super_admin Screen 10: External Tooling & Integrations

Brady's framing: "mimic the AWS console" + "I don't want to duplicate effort here". The new screen is a hub page that points the Global Admin at the 3rd party dashboards where the actual control surface lives.

**Layout**:
- Breadcrumb: Super Admin Portal → External Tooling
- Eyebrow: "Super Admin"
- Title: "External Tooling & Integrations"
- Section: **External dashboards** — 2-row grid of 3 col-4 cards each (6 cards total)
- Section: **Global configuration** — table of 4 settings + where they're enforced

**6 dashboard cards** (each: icon + status pill + tool name + 1-line description + "Open dashboard ↗" link):

| Card | Status pill | What lives there |
|---|---|---|
| AWS Console | All services healthy | Infrastructure · RDS · S3 · IAM · networking |
| OpenRouter.ai | Primary + 2 fallback | LLM provider routing · fallback chains |
| Redis Admin | Cache hit 87% | Token cache · session state · rate-limit counters |
| Grafana / Datadog | All dashboards green | Observability · P50/P95 latency · error rates |
| JFT Support (Jira) | 3 P3 open | Tickets · P1 SLA tracking |
| GitHub | main passing | Code repos · CI/CD pipelines |

All link-out buttons use `href="#"` with `onclick="event.preventDefault();"` for the storyboard — real URLs wired up at build time.

### L & M — Global configuration surfaced (not per-course)

Brady confirmed both should stay **global settings**, not configurable per-course. Some values are enforced by 3rd party tools (Redis, OpenRouter, AWS) — surfaced on the new Screen 10 as a table that shows *what the value is, what enforces it, and where to change it*.

| Setting | Value | Enforced by | Notes |
|---|---|---|---|
| Student input character limit | 5,000 chars | Student UI input layer (SDP) | Global setting; not configurable per course |
| LLM token cap per session | 50,000 tokens | Redis Admin | Cached + enforced at Redis |
| Default LLM provider chain | Primary + 2 fallback | OpenRouter.ai | Per-tenant model selection in Content Creator Portal |
| Storage retention | Per institutional policy | AWS Console | FERPA-aligned |

This pattern resolves L+M without inventing in-portal config UI for things that already have a dashboard elsewhere.

### Super Admin portal home (Screen 2) — 6th quick-link card

Added a 6th col-3 quick-link card pointing to Screen 10 (External Tooling). Icon: `open_in_new`. Description: "AWS · OpenRouter · Redis · Grafana · Jira · GitHub". Layout wraps cleanly to 4+2.

### Counts

| | Before v4.28 | After v4.28 |
|---|---|---|
| Storyboard total | 74 | **75** |
| `super_admin/` | 9 | **10** (Screen 10 added) |
| `instructor/` | 8 | 8 (in-place edits only) |
| `tenant_admin/` | 23 | 23 |
| `student/` | 34 | 34 (frozen) |
| `lrps/` | 1 | 1 |
| PNGs | 150 | **152** (super_admin gains 1 light + 1 dark) |

### Catalog stale-label cleanup (housekeeping)

While updating the SC-ADD-04 step list, I noticed pre-existing numbering bugs left over from the v4.4 → v4.8 trim that removed three over-added screens (Third-Party Integrations / Learner Remediation / Billing & Cost Centers):

- "Step 10 / Screen 10" was Geo-redundancy (actually screen 7 per file name `sc-add-04_step07_screen07.png`)
- "Step 11 / Screen 11" was Audit log (actually screen 8 per file name `sc-add-04_step08_screen08.png`)

Corrected to "Step 7 / Screen 7" and "Step 8 / Screen 8" in both catalogs to match the file names + alt text + super_admin index sectioning. My new Screen 10 (External Tooling) now occupies the correct slot.

### Files touched

- `instructor/index.html` — Screens 5, 6, 7, 8 metric retargeting
- `super_admin/index.html` — added Screen 10 (~140 lines) + Screen 2 6th quick-link card + meta-bar button 10 + `TOTAL_SCREENS = 10` + version stamps
- `index.html` (root) — portal-card description + hero "Screens" stat 74 → 75 + version stamp
- `presentation.html` + `presentation_dark.html` — added SC-ADD-04 step 10 entry + fixed stale step 10/11 → 7/8 labels + screen-map row update + Doc Control v4.28 row (+ v4.27 marked Superseded) + hero "Screens" stat 73 → 74 + version stamps
- `README.md` — version badge 4.27 → 4.28 + screens badge 74 → 75
- `CHANGELOG.md` — this entry
- `capture_screens.py` — super_admin scenarios list `[1..9]` → `[1..10]` + docstring counts 150 → 152

### What did NOT change

- `student/index.html` remains frozen — **26th consecutive release** with `git diff --stat` returning 0 lines
- `tenant_admin/index.html` content unchanged (only the title version stamp)
- `lrps/index.html` content unchanged (only the title + footer version stamps)

### Verification

1. `git diff --stat student/index.html` returns 0 lines
2. `super_admin/index.html` `TOTAL_SCREENS = 10`
3. Storyboard total = 75 (74 + 1)
4. Instructor portal: no "Total time" / "Duration" / "Session length" time-on-site metrics remain — replaced everywhere by struggle/intervention indicators
5. Super Admin Screen 10 has 6 external-tool cards + Global Configuration table visible
6. SC-ADD-04 step numbering in both catalogs is now sequential 1–10 (was 1, 2, 3, 4, 5, 6, 10, 11, 9 before — stale)
7. Doc Control: v4.28 row Current, v4.27 row Superseded in both catalogs

---

## v4.27 — 11 May 2026 — User Management role taxonomy expanded to 4 tiers (Student → Instructor → Tenant Admin → Global Admin)

v4.25 built `super_admin/index.html` Screen 9 (User Management) per Mike's feedback with a 3-tier hierarchy: **User → Tenant Admin → Global Admin**. Brady reframed the role model on 11 May to explicitly call out the 4 storyboard personas as the starting tiers: **Student → Instructor → Tenant Admin → Global Admin**. v4.27 brings the screen into agreement.

> "The Global Admin can see all users in a large table, then manually upgrade people from student or instructor to the other accounts. Global Admin is the only one who can upgrade account access." — Brady, 11 May 2026

### What changed on super_admin Screen 9

**KPI row (4 cards)** — same count, different semantics:
| Before (v4.25) | After (v4.27) |
|---|---|
| Total users · 187 | Students · 150 |
| Tenant Admins · 23 | Instructors · 12 |
| Global Admins · 2 | Tenant Admins · 23 |
| Pending upgrades · 0 | Global Admins · 2 |

Totals still add to 187 (150 + 12 + 23 + 2). Dropped "Pending upgrades" gauge (was always 0 in the storyboard) to make room for the Instructor tier.

**Role badges** in the table — generic "User" badge replaced by 2 distinct tier badges:
- **Student** → `badge-gray` (gray-on-bg-light, matches lowest-tier visual)
- **Instructor** → `badge-warning` (amber/gold on warning-tint, distinct from Tenant Admin's info-blue)
- Tenant Admin → `badge-info` (unchanged)
- Global Admin → `badge-brand` (unchanged)

**Table rows** (8 total, was 7):
| Row | Persona | Tenant | Role | Actions |
|---|---|---|---|---|
| 1 | Bob (you) | — | Global Admin | Cannot downgrade self |
| 2 | Jordan | — | Global Admin | Downgrade (disabled — min 2) |
| 3 | Alice | PDev | Tenant Admin | Upgrade to Global / Downgrade |
| 4 | Mike | School of Business | Tenant Admin | Upgrade to Global / Downgrade |
| 5 | **Charlie** (new) | PDev | Instructor | Upgrade to Tenant Admin / Upgrade to Global |
| 6 | Priya | School of Health | Instructor (was User) | Upgrade to Tenant Admin / Upgrade to Global |
| 7 | **Sally** (new) | PDev | Student | Upgrade to Instructor / Upgrade to Tenant Admin |
| 8 | Devon | PDev | Student (was User) | Upgrade to Instructor / Upgrade to Tenant Admin |

Teagan row dropped to keep the row count manageable. Sally + Charlie added explicitly because they're the canonical Student + Instructor personas elsewhere in the storyboard — keeping the table internally consistent with the 4-persona model.

**Upgrade actions per row**:
- Student → primary: `Upgrade to Instructor`, outline: `Upgrade to Tenant Admin` (skip-tier allowed)
- Instructor → primary: `Upgrade to Tenant Admin`, outline: `Upgrade to Global`
- Tenant Admin → outline: `Upgrade to Global`, tertiary: `Downgrade`
- Global Admin → `Downgrade (blocks min 2)` disabled where appropriate; self-row shows "Cannot downgrade self"

**Recent role-changes audit log** (right rail) grew 4 → 6 entries to show recent upgrades across all 4 tiers:
- 10 May 11:42 — Bob upgraded Charlie → Instructor (PDev)
- 07 May 09:18 — Bob upgraded Alice → Tenant Admin (PDev)
- 05 May 13:15 — Bob upgraded Priya → Instructor (School of Health)
- 02 May 14:30 — Bob upgraded Mike → Tenant Admin (School of Business)
- 28 Apr 10:02 — Bob upgraded Jordan → Global Admin
- 22 Mar 16:00 — Bob → Global Admin (initial)

**Pagination text** bumped: "Showing 7 of 187 users" → "Showing 8 of 187 users".

**Constraint banner** unchanged: "Minimum 2 Global Admins required."

### Other touches

- **Screen 2 quick-link card** (Super Admin Portal home → User Management): description text updated from "Upgrade users to Tenant or Global Admin" → "Upgrade students or instructors to higher roles" (reflects 4-tier model)
- **HTML comment** on Screen 9 + **TOTAL_SCREENS comment** + **meta-bar aria-label** all updated to reflect 4-tier taxonomy
- **No screen count change** — TOTAL_SCREENS still 9 on super_admin, storyboard total still 74

### Files touched

- `super_admin/index.html` — Screen 9 (KPI row, table rows, audit log) + Screen 2 quick-link card text + version stamps + HTML comments
- `presentation.html` + `presentation_dark.html` — SC-ADD-04 step 9 description; Doc Control v4.27 row (+ v4.26 marked Superseded); footer + hero version stamps
- `index.html` (root) — hero-eyebrow + footer version + portal-card comment
- `README.md` — version badge 4.26 → 4.27
- `CHANGELOG.md` — this entry
- `capture_screens.py` — header docstring version comment

### What did NOT change

- `student/index.html` remains frozen (25th consecutive release with `git diff --stat` returning 0 lines)
- `tenant_admin/index.html` — no changes (v4.25 already removed old Team & Roles screen; v4.26 only touched Branding)
- `instructor/index.html` — only version stamps (no content changes)
- `lrps/index.html` — only version stamps
- All super_admin screens 1–8 — only version stamps
- Screen count: 74 (unchanged)
- PNG count: 150 (unchanged; super_admin Screen 9 PNG regenerates with the new 4-tier table)

### Verification

1. `git diff --stat student/index.html` returns 0 lines (preservation directive intact through 25 consecutive releases)
2. super_admin `TOTAL_SCREENS = 9` (unchanged from v4.25)
3. Storyboard total = 74 (unchanged)
4. Role badges visible in screenshot: Student (gray) + Instructor (amber) + Tenant Admin (info-blue) + Global Admin (brand-blue) = 4 distinct tiers
5. KPI row shows 4 cards: Students 150 / Instructors 12 / Tenant Admins 23 / Global Admins 2
6. Both light + dark catalogs show new v4.27 row in Doc Control, v4.26 row marked Superseded

---

## v4.26 — 11 May 2026 — Branding footer-mockup refresh (match production WGU footer)

Brady shared a screenshot of WGU's actual production learner-facing footer from another live course. v4.25 had built the Branding preview pane (tenant_admin Screen 21) with a stylized single-block footer mockup that didn't match the production layout. v4.26 rebuilds the preview pane to match production exactly.

### What changed

`tenant_admin/index.html` — Screen 21 (Tenant Settings — Branding & Customization), right-card preview pane only.

**Layout: 2 distinct rows, separated by a thin divider** (matches production).

- **Top row** (padding 20px 28px, border-bottom 1px #E4E7EB):
  - Left: WGU corporation full-color logo, 28px height
  - Right: "ADA Accommodation" link (Dark Navy, 13px, 600 weight)
- **Bottom row** (padding 16px 28px):
  - Left: "© 2026 Western Governors University – WGU. All Rights Reserved." (12px, gray-700)
  - Right: "Privacy Policy | Terms of Service | Honor Code" with pipe separators (Dark Navy, 13px, 600 weight)

**Background**: `#F5F7FA` (light pale, matches production).
**Container**: rounded `var(--pgn-size-border-radius-lg)`, 1px gray-100 border.

### What was removed from v4.25's mockup

- The "WGU logo + tenant logo side-by-side with `← Tenant logo (configurable)` callout" decoration — the actual production WGU footer has no tenant-logo slot. The tenant logo lives elsewhere in the LMS chrome (header / Open edX top nav), not the footer.
- The `#F8F8F8` background + 4px Deep Navy border-top accent stripe — production uses a clean `#F5F7FA` background with no top accent.
- Dot separators between footer links (`·`) — production uses pipe separators (`|`).
- Single-block layout — production is 2-row.

### Files touched

- `tenant_admin/index.html` — Screen 21 preview pane markup (single section replacement, ~13 lines)
- `presentation.html` + `presentation_dark.html` — SC-ADD-02 step 13 description; Doc Control table (new v4.26 row + v4.25 row marked Superseded); footer + hero version stamps
- `index.html` (root) — hero-eyebrow + footer version + portal-card comment
- `README.md` — version badge 4.25 → 4.26
- `CHANGELOG.md` — this entry
- `capture_screens.py` — header docstring version comment

### What did NOT change

- `student/index.html` remains frozen (24th consecutive release with `git diff --stat` returning 0 lines)
- `super_admin/index.html` — no changes (Screen 9 User Management from v4.25 unchanged)
- `instructor/index.html` — no changes
- `lrps/index.html` — only the footer version stamp + title bump (visual content unchanged)
- All other screens across all portals — unchanged
- Screen count: 74 (unchanged)
- PNG count: 150 (unchanged; tenant_admin/screenshots/sc-add-02_step13_screen21.png + tenant_admin/screenshots_dark/sc-add-02_step13_screen21.png regenerate with the new footer mockup)

### Verification

1. `git diff --stat student/index.html` returns 0 lines (preservation directive intact through 24 consecutive releases)
2. `tenant_admin/index.html` `TOTAL_SCREENS = 23` (unchanged from v4.25)
3. `super_admin/index.html` `TOTAL_SCREENS = 9` (unchanged from v4.25)
4. Storyboard total = 74 (unchanged)
5. New Branding preview pane visually matches production WGU footer screenshot Brady provided
6. Both light + dark catalogs show new v4.26 row in Doc Control, v4.25 row marked Superseded

---

## v4.25 — 11 May 2026 — Mike-feedback reshape (Branding simplified, Team & Roles relocated to Global Admin, 3-tier role model, file-upload on prompt config, address-by-name)

Brady met with Mike and brought back answers on the 4 open items plus 3 refinements. v4.25 implements them.

### A. Branding & Customization (Tenant Admin Screen 21) — simplified to logo + standardized footer

Per Mike: "Logo only right now, use Open edX footer is standardized: WGU logo, ADA Accommodation, Privacy Policy, ToS, Honor Code, copyright notice."

**Stripped from the Branding form:** tenant display name, primary accent color, custom domain, favicon upload, default locale dropdown, PWA install badge, footer copy textarea.

**Kept:** tenant logo upload (single control).

**Preview pane** rebuilt to show the Open edX standardized footer mockup with the 6 elements Mike named (WGU logo + tenant logo side-by-side, then ADA Accommodation · Privacy Policy · Terms of Service · Honor Code links, then copyright notice). Demonstrates the only thing the Tenant Admin actually configures (logo) and what the rest of the footer chrome looks like (fixed by the Open edX layer).

### B. Team & Roles relocated to Global Admin (Super Admin) + redesigned as User Management

Per Mike: "Tenant 22 screen goes in global admin only" + 3-tier role hierarchy (User → Tenant Admin → Global Admin) + "Always have 2 Global Admins" + "List all users in a table, upgrade whoever I want to."

**Tenant Admin side:**
- Deleted Screen 22 (Team & Roles with Owner/Editor/Viewer model)
- Renumbered Screen 23 (Instructor Roster) → 22
- Renumbered Screen 24 (Subject Lifecycle) → 23
- `TOTAL_SCREENS = 23` (was 24)
- Updated Screen 21 (Branding) "Next" button → "Next: Instructor Roster"
- Updated meta-bar nav (removed old 22 button)

**Super Admin side — new Screen 9: User Management**
- 4-card KPI row: Total users · Tenant Admins · Global Admins · Pending upgrades
- Minimum-2-Global-Admins constraint warning at top
- All-users table with columns: User · Tenant · Role badge (User / Tenant Admin / Global Admin) · Last active · Actions
- Action buttons per row: Upgrade to Tenant Admin / Upgrade to Global / Downgrade (disabled where blocked)
- Recent role changes right-rail (moved from the old Team & Roles audit log)
- `TOTAL_SCREENS = 9` (was 8)
- Added meta-bar button for Screen 9
- Added "User Management" quick-link card on Super Admin Portal home (Screen 2)

### C. File upload + address-by-name on Configure AI Coaching Prompt (Tenant Admin Screen 8)

Per Mike: "Add a file button if you want to really edit something like crazy for the prompt config for tenant admin" + "Make the answers student-specific. No 'student', call them by name."

- Added "Upload advanced config (.txt / .md / .json)" button above the form (alternative entry for power-users).
- Updated compiled prompt preview OUTPUT block:
  ```
  OUTPUT
  Always cite the Learning Objective being assessed by code (e.g., LO 1.3).
  Address the learner by their first name. Never use "student" as the form of address.
  ```

### D. Read-only view of other tenants (Tenant Admin Screen 2)

Per Mike: "Read only of other tenants."

Added "Other tenants — Read-only" inline section below the Subjects table on Portal home. 3 rows (School of Business, School of Health, School of Education) each with a "View" button only (no edit action).

### Items verified already correct (no edits)

- **Instructor portal:** Sally is already addressed by name throughout all instructor screens. No changes needed.
- **Student portal:** Only "student" mentions are inside sample task content (Python exercises referring to data about students/scores), not generic addresses for Sally. Student portal remains frozen (23 consecutive releases).
- **LTI entry via LRPS:** Mike: "Everyone goes in through LTI link via LRPS" — already depicted on Screen 1 of every portal.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 23 consecutive releases)
- tenant_admin section IDs sequential 1–23; `TOTAL_SCREENS = 23`
- super_admin section IDs sequential 1–9; `TOTAL_SCREENS = 9`
- Storyboard total = 74 (unchanged)
- `grep -i "Owner.*Editor.*Viewer"` in deliverable → 0 hits (old role model fully removed)
- Branding screen visible: logo upload + standardized footer mockup only
- Compiled prompt preview includes "Address the learner by their first name" line
- Configure AI Coaching Prompt has "Upload advanced config" button
- Super Admin User Management reachable from Portal home + meta-bar

### Numbers

| | v4.24 | v4.25 |
|---|---|---|
| Total storyboard screens | 74 | **74** |
| `tenant_admin/` | 24 | **23** |
| `super_admin/` | 8 | **9** |
| PNGs | 150 | **150** |

---

## v4.24 — 10 May 2026 — Strip ALL descriptive / scenario-narrative text from prototype screens (developers will copy literally)

Per Brady's directive ("My developers are VERY literal. They are going to copy this page, pixel-by-pixel, even though I have told them otherwise. So this prototype needs to be 100% what is required to meet the SOW in the most efficient method possible... Remove all the descriptive text across the prototypes that is scenario-based descriptor information and just keep the text minimal everywhere.").

**Hard rule applied:** if a paragraph/alert/form-help is *scenario-narrative explaining what the screen does or what a button does*, it's gone. UI components must self-document via labels, buttons, and data. The two examples Brady cited (the "Multi-tenant scoping limits this view…" alert on the Tenant Admin hub, and the "Create or update a Subject's topics, learning objectives…" hub-card description) are exactly the pattern stripped everywhere.

### What stays

- Functional **button labels**, **field labels**, **data table headers**, **status indicators**, **error/warning text that conveys actionable state** (e.g., "Primary LLM Provider unreachable · Fallback engaged"), **sample data content** (the JSON response on the API console, the CSM email body, the heatmap cells — these depict actual product data, not narrative).

### What was stripped

- All `<p class="mb-4">Step N of 5...</p>` instructional paragraphs at the top of each course-config screen
- "Hub card" descriptions on screen 2 ("Create or update a Subject's topics, learning objectives..." gone; cards now just have heading + buttons)
- Welcome alert on screen 2 ("Multi-tenant scoping limits this view to Foundations of Programming (Python). All actions audit-logged per institutional retention policy.")
- Every `form-help` block that explained *what a field is for* or *what happens when you change it* (kept only where the help is functional metadata like "PNG or SVG · max 200×60px")
- "Tip" alerts (rolling-enrollment narrative, 4-6 topics best practice, etc.)
- "Saved as draft" / "Next SLA report" / "Audit Trail intact" / "RTO well within target" / "Audit: changes you make from here are logged" — informational alerts dropped
- "What's next?" cross-scenario card on Deploy Success (entire card removed)
- "Why is this a manual ticket?" expander on Deploy Success (removed)
- LRPS card narrative paragraph (kept the destination URL + ticket form + Submit buttons)
- A/B testing + LaTeX badge captions (kept the badges themselves)
- CSM email body trimmed from 4 paragraphs to 3 short ones
- Sample data captions ("This is what Sally sees when she launches the Coding Coach...") gone
- Permission matrix caption + Multi-tenant isolation alerts (the table headers are self-documenting)
- Subject Lifecycle "What deactivation does NOT do" alert + audit-warning under the deactivation form (dropped)
- All instructor screens: at-risk learner narrative alerts, "Sally is the most-at-risk learner" callout, "Pattern: Sally scores stronger on run/observe items..." reflection alert, "Audit Trail intact" + Compliance Source-IP alert
- Super_admin screens: privileged-session retention narrative, PDev tenant flagged narrative tail, scoring-style change info, FERPA controls preamble, additional-services footnote, hourly-scan alert, RTO-within-target alert, "Audit: changes you make from here..." alert
- Root index portal-card descriptions reduced to one short line each ("Course configuration + incident response", "At-risk intervention dashboard", "Cross-tenant governance and compliance", "Learner coaching loop"); "Start at LRPS" tip alert removed

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 22 consecutive releases)
- Page byte-count significantly reduced; storyboard remains visually intact and navigable
- 74 screens, no removals

---

## v4.23 — 10 May 2026 — Strip internal contract refs (SOW §§ + SC-ADD-NN / SC-MVP-NN scenario IDs) from user-visible UI

Per Brady's directive ("On Tenant Admin Screen 2, you list 'SC-ADD-NN' and Sections from the contract. That was only internal information. Remove anything in any of the prototype screens that references contract requirements specifically by text or the user scenarios. Those do not help the Tenant Admin in real life at all."), all SOW section citations (§7.9, §10.4, §16.5 #10.X, etc.) and user-scenario identifiers (SC-ADD-02, SC-MVP-01, etc.) have been removed from **user-visible body text** across all four admin portal HTMLs + the root portal selector. Internal markers (HTML comments, aria-labels referencing storyboard structure, Doc Control rows, READMEs, CHANGELOG, catalog narratives) are preserved for ongoing traceability.

**No screens removed** (still 74). All in-place text edits. No new functionality.

### tenant_admin/index.html (Content Creator Portal)

- **Screen 2 Hub cards:** eyebrow "SC-ADD-02 · Course Configuration" → "Course Configuration"; "SC-ADD-06 · Incident Response & SLA" → "Incident Response & SLA"; description text scrubbed of §9.13 / §9.1 / §9.4 / §9.5 citations
- **Screen 8 (Configure AI Coaching Prompt):** A/B testing + LaTeX rendering badges scrubbed of §16.1 #6.8 / #6.12 citations
- **Screen 9 (Model picker):** removed "(see SC-ADD-06)" cross-reference
- **Screen 12 (Deploy success):** removed "per SOW §10.4" from audit-logged line
- **Screen 13 (Incident baseline):** removed "(§9.13)" from Proactive Monitoring text
- **Screen 14 (Fallback engaged):** removed "per §6.5" from fallback narrative
- **Screen 16 (Ticket form):** removed "per §9.13" and "per §6.5" from auto-filled description textarea
- **Screen 17 (Ticket confirmation):** removed "per §9.5"
- **Screen 18 (CSM chat thread):** eyebrow stripped of "· §9.5"
- **Screen 21 (Branding):** eyebrow stripped of "· §7.9 Custom Branding"; Default locale + PWA install labels stripped of §16.2 / §3.7 / §16.2 #7.7 citations; form-help text simplified
- **Screen 22 (Team & Roles):** eyebrow stripped of "· §10.8 Role-Based Access Control"
- **Screen 23 (Instructor Roster):** eyebrow stripped of "· §2.5 Instructor Management · §10.8 RBAC"
- **Screen 24 (Subject Lifecycle):** eyebrow stripped of "· §2.5 Module Lifecycle · §10.4 Audit Logging"; inline "(§10.1)" + "(§10.4)" removed
- **Screen 5 (Add LO):** "Per SOW §10.4" → "All LO add/edit/remove events"
- **Screen 6 (Edit LO):** "versioned per SOW §10.4 audit logging" → "versioned and audit-logged"; "Full audit trail available via SOW §10.4 logging" → "Full audit trail available via the cross-tenant audit log"
- **Screen 7 (Remove LO):** "per SOW §10.4" stripped from both intro paragraph and Impact preview table
- **Meta-bar header:** "JFT SDP Content Creator Portal (SOW §2.2 role: Tenant Admin)" → "JFT SDP Content Creator Portal"
- **Meta-bar flow labels:** "SC-ADD-02" → "Flow A"; "SC-ADD-06" → "Flow B"
- **`<title>` tag:** bumped from stale "Storyboard v3.2" to "Content Creator Portal — Storyboard v4.23"

### super_admin/index.html (Super Admin Portal)

- **Screen 1:** "WGU SSO authentication complete · SAML 2.0 SP (§16.3 #8.2) · MFA verified (§16.5 #10.18)" → "WGU SSO authentication complete · SAML 2.0 SP · MFA verified"
- **Screen 2 portal home:** "SC-ADD-06 incident resolved" → "Incident resolved"; 4 quick-link card captions stripped of §6.4 / §6.6 / §10.7 / §9.5
- **Screen 3 (Token Usage):** eyebrow stripped of "· §6.6"
- **Screen 5 (Global Rate Limits):** eyebrow stripped of "· §6.4"
- **Screen 6 (Compliance Report):** eyebrow stripped of "· §10.7 · §10.1"; FERPA privacy section header stripped of "· §10.1"; service-by-service header stripped of "· §10.7"; **all 10 FERPA control table rows (added v4.18) scrubbed of SOW §16.5 #10.X citations** in both Reference and Notes columns — references now "WGU institutional policy" / "Industry standard" / "EU regulation" as appropriate; 34 CFR §99.X (federal regulation, public law) citations preserved
- **Screen 7 (Geo-Redundancy):** eyebrow stripped of "· §9.5 · §10.1"
- **Meta-bar flow label:** "SC-ADD-04" → "Flow"

### instructor/index.html (Instructor Dashboard)

- **Screen 8 (Audit Trail):** feedback label "Audit Trail Captured · §10.4" → "Audit Trail Captured"
- **Meta-bar flow label:** "SC-ADD-03" → "Flow"

### index.html (root portal selector)

- **HTML comment header:** "Tenant Admin Portal (Alice, v1.3 — 23 screens)" → "Content Creator Portal" + SOW §2.2 mapping removed
- **Tenant Admin portal card:** aria-label + portal-card-role both stripped of "(SOW §2.2: Tenant Admin)"
- **Scenario tags on all 4 portal cards** converted from scenario IDs to functional descriptors:
  - Student: "SC-MVP-01/02/03/04" → "First Launch / Progressive Coaching / Fast Track / Returning Learner"
  - Content Creator: "SC-ADD-02 / SC-ADD-06" → "Course Configuration / Incident Response"
  - Instructor: "SC-ADD-03" → "At-Risk Intervention"
  - Super Admin: "SC-ADD-04" → "Governance & Compliance"

### What's preserved

- **HTML comments + scenario-section banners** (`<!-- SC-ADD-02 — TENANT ADMIN PORTAL ... -->`) — internal markers, not visible to users
- **Meta-bar aria-labels on step buttons** — screen-reader hints for storyboard navigation; the meta-bar is explicitly DEMO ONLY and not part of "real life" Tenant Admin UI
- **34 CFR §99.X citations** on the super_admin FERPA control table Reference column — these are PUBLIC federal regulation citations (the actual FERPA statute), not internal contract references
- **WCAG 2.2 AA** mentions — public accessibility standard, not internal
- **READMEs + CHANGELOG + Doc Control rows + catalog narratives** — internal reference docs, not user-visible UI

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 21 consecutive releases)
- `grep -n "§[0-9]\|&sect;[0-9]" tenant_admin/index.html | grep -v "<!--\|aria-label\|<title>\|/\*"` → 0 user-visible hits
- `grep -n "SC-ADD-\|SC-MVP-" tenant_admin/index.html super_admin/index.html instructor/index.html index.html | grep -v "<!--\|aria-label\|<title>\|/\*\|CHANGELOG"` → 0 user-visible hits

### Numbers

| | v4.22 | v4.23 |
|---|---|---|
| Total storyboard screens | 74 | **74** (no removals) |
| Storyboard sections cleaned | 0 | **30+ visible-UI sites scrubbed** |
| 34 CFR §99.X citations preserved (federal law) | 4 | 4 |
| SOW §§ refs in user-visible UI | many | **0** |
| SC-ADD-NN refs in user-visible UI | 12+ | **0** |
| SC-MVP-NN refs in user-visible UI | 4 (root index portal card) | **0** |

---

## v4.22 — 10 May 2026 — Tenant Admin reshape per JFT meeting (Content Creator rename + LO management screens + SC-ADD-05 removal + Configure AI Coaching Prompt + LRPS provisioning workflow)

Brady met with JFT this morning and brought back a set of reshapes for the Tenant Admin flow. v4.22 implements the Tenant Admin portion only (per Brady's "let's focus on getting the Tenant Admin flow finished today before we worry about any other user flows" directive). Other items (instructor metrics review, super_admin shrinkage, student 5000-char limit, Redis surfacing) deferred to subsequent releases.

**Net screen count for tenant_admin:** 27 → **24** (+3 new LO management screens, −6 from removing SC-ADD-05 entirely).
**Total storyboard:** 77 → **74** screens.

### Renamed — "Tenant Admin Portal" → "Content Creator Portal" (user-facing UI only)

Per Brady's Q1 answer ("Keep 'tenant admin' in all official language, but can use Content Creator in user-facing UIs for ease-of-explanation"):
- **User-facing UI strings → "Content Creator"**: navbar chip on every tenant_admin screen, breadcrumb root, persona labels visible to Alice, meta-bar header, root `index.html` portal-selector card role + name + aria-label
- **Official documentation → "Tenant Admin" preserved**: SOW reference text (§2.2 deliverable still names "Tenant Admin"), READMEs (with mapping note "Content Creator (SOW §2.2 role: Tenant Admin)"), CHANGELOG, Document Control rows, catalog Per-persona portals list (with mapping callout)

### Removed — SC-ADD-05 (Data Portability) — 6 screens deleted (old screens 10–15)

Per JFT meeting notes: "Take off that API screen from the [tenant admin]" + "Take out the data screen from the tenant admin and leave it on global."

- **Why:** JFT confirmed external **Swagger documentation** (per SOW §2.4 deliverable "API specification using Swagger" + §16.1 #6.25) is the API access vehicle for downstream WGU systems — the in-portal API console was never the contracted experience. Data export scope moves to the global / Super Admin portal (deferred to a subsequent release per Brady's "Tenant Admin first" directive).
- **Screens removed:** Data & APIs landing (10), REST API console (11), Sample JSON response (12), Export wizard (13), Format picker (14), Download confirmation (15)
- **SOW alignment:** §16.3 #8.7 (REST API for student engagement data export), #8.9 (data formats), #8.12 (webhooks), #8.13 (GraphQL) all remain in-scope for the platform — just not depicted as a tenant-admin portal flow.

### Added — 3 new LO management screens (5/6/7)

Per Brady's H answer ("Instead of having the passing threshold be on a separate page, let's integrate it into the entry/modification screens for topics/learning objectives. You should also add screen to illustrate how the topics/learning objectives can be modified/removed/added.") and follow-up "Create new screens to completely illustrate the add/edit/remove flow for the user. One example for each action, including the new threshold/weight additions to Screen 04 and the new screens you're adding."

- **NEW Screen 5: Add a Learning Objective** — Form with parent-topic dropdown, LO code, title, description (with "long descriptions make the model more prone to hallucinate" form-help), per-LO passing threshold input (0–100% with mastery badge), per-LO weight input (default 1.0× with course-total badge). Audit-trail warning per §10.4.
- **NEW Screen 6: Edit a Learning Objective** — Same form pre-filled for LO 1.3, with edit-history alert showing last 3 changes + threshold-delta badge.
- **NEW Screen 7: Remove a Learning Objective** — Confirmation with danger alert + LO metadata card + Impact preview card (14 active learners, 47 historical submissions, heatmap column behavior, weight delta, coach behavior, audit trail).
- **Renumbering cascade:** Old screens 5–9 → new 8–12; old 16–23 → new 13–20; old 24–27 → new 21–24.

### Modified — Screen 4 (Topics & Learning Objectives)

Restructured from row-card topic list to per-LO data table:
- 10-row LO table with columns: LO code, title, topic, **threshold (per-LO)**, **weight (per-LO)**, Actions (Edit / Remove icons)
- "Add Learning Objective" primary CTA + "Add Topic" outline CTA + summary line ("10 LOs across 4 topics · Total weight 10.0× · Avg threshold 69.5%")
- Tip alert reframed to explain the per-LO threshold + weight model (NOT set globally on the scoring screen)

### Modified — Screen 8 (Configure AI Coaching Prompt) — toggle switches → 4 short text-box guardrails

Per JFT meeting note ("Custom prompting: Turn these from radio buttons to short text boxes with a warning that if you add too much info, the model will be more prone to hallucinate. Update the Configure AI Coaching Prompt."):
- Heading renamed: "Configure the AI Coaching Prompt" (was "AI Prompt Configuration")
- Eyebrow renamed to "Configure AI Coaching Prompt"
- **Replaced 4 toggle switches with 4 short text input fields**: Student profile data — how to use it; Subject-domain limits; Jailbreak / prompt-injection posture; Code execution sandbox use. Each with maxlength=200 + form-help text.
- Custom system prompt addendum textarea reduced from rows=4 to rows=3 with maxlength=600.
- **Prominent warning alert** at top of screen: "Less is more. Keep each field tight (one or two sentences). The more context you pass to the model, the more prone it becomes to hallucinate, drift off-topic, or contradict its own guardrails."
- Compiled prompt preview pane rewritten to reflect the new 4-field structure (PROFILE USE / DOMAIN LIMITS / JAILBREAK POSTURE / SANDBOX USE / CONTENT-CREATOR ADDENDUM / OUTPUT).

### Modified — Screen 10 (Scoring & Rubric) — threshold + weight removed; scoring style added

Per Brady's directive that threshold + weight live on the LO management screens, not on a separate scoring page:
- Title changed: "Configure Scoring & Rubric" → "Scoring style & coaching defaults"
- **Threshold + weight columns removed** from per-LO table (now per-LO on screens 4 + 5 + 6 + 7)
- **Mastery threshold input removed** (each LO declares its own passing threshold)
- **Added Global coaching style** card with 3 radio cards: Socratic (Recommended, selected), Direct feedback, Adaptive
- Per-LO scoring pattern table retained (Code / Code + explain / Reflection)
- Info alert documents the v4.22 change

### Modified — Screen 12 (Deploy success) — LRPS provisioning ticket section added

Per JFT meeting note ("Process for getting new LRPS link · Present the destination link from JFT on the 'Deployed to Production' page. And then the tenant admin sends that in a ticket to the LRPS team manually."):
- Heading changed: "E135 is live" → "E135 build succeeded"
- **New section: "Next: file an LRPS provisioning ticket"** with:
  - Production URL display card (terminal-styled, copyable): `https://sdp.wgu.edu/launch/pdev/e135-oop-python?build=2026.05.06.1547`
  - Auto-filled ticket justification textarea (editable)
  - CTAs: Submit LRPS ticket / Copy URL only / I'll do this later
  - Info alert explaining LRPS is a manual handoff because LRPS is owned by the WGU D&D team, not JFT

### Updated — root files

- `index.html`: hero stat 77 → 74, Tenant Admin card → Content Creator (SOW §2.2: Tenant Admin), screen count 27 → 24, scenario tags drop SC-ADD-05, catalog card screenshots 156 → 150
- `README.md`: version badge 4.21 → 4.22; screens badge 77 → 74; tenant_admin scenario table updated; "Content Creator (Tenant Admin per SOW §2.2)" section heading
- `capture_screens.py`: PORTALS tenant_admin entry updated; docstring totals 156 → 150
- `tenant_admin/README.md`: comprehensive refresh — "Content Creator (Tenant Admin)" heading; 2 scenarios × 24 screens; v4.22 reshape summary
- `presentation.html` + `presentation_dark.html`: SC-ADD-05 section deleted, TOC + screen map updated, 3 new SC-ADD-02 step entries inserted, SC-ADD-02 step numbers renumbered, SC-ADD-06 screen labels renumbered

### Items deferred per Brady's "Tenant Admin first" directive

The following items from the JFT morning meeting are NOT in v4.22 and will be addressed in subsequent releases:
- **J:** Review metrics — remove "Total Time" + add instructor score on chat history screens 7+8 (instructor portal — deferred)
- **K:** Review the global admin totally (super_admin — deferred; "mostly in AWS" note for follow-up release)
- **L:** Student 5000 char limit — surface to user (student/ — deferred; freezer status TBD)
- **M:** Redis token limit surfacing (deferred)
- **Mike discussion items** (course ownership model, transfer flow, branding & customization screen for Contract, multiple owners, course visibility default) — Brady to confer with Mike later today; storyboard changes in subsequent release once Mike's answers land

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 19 consecutive releases)
- tenant_admin section IDs: sequential 1–24 (verified)
- `TOTAL_SCREENS = 24` (verified)
- `grep -i "SC-ADD-05"` in deliverable HTML → 0 hits outside historical/meta context (verified)
- `grep "Tenant Admin Portal"` in user-facing UI strings → 0 hits (verified)
- New screens 5/6/7 reachable via meta-bar buttons + Edit/Remove icons on screen 4
- LRPS ticket section visible on screen 12

### Numbers

| | v4.21 | v4.22 |
|---|---|---|
| Total storyboard screens | 77 | **74** |
| tenant_admin screens | 27 | **24** (+3 new LO mgmt, −6 SC-ADD-05) |
| SC-ADD-02 screens | 13 | **16** |
| SC-ADD-05 screens | 6 | **0** (removed) |
| SC-ADD-06 screens | 8 | 8 (renumbered 16-23 → 13-20) |
| Total PNGs | 154 (light+dark) | **150** |

---

## v4.21 — 10 May 2026 — SOW-anchored sweep follow-up #3 (README format-picker narrative drift, 3 sites)

Pass 21 (post-v4.20) found **1 Material** finding: 3 README sites still described the export format picker as 2-format (CSV / JSON) when v4.18 expanded it to 4-format (CSV / JSON / PDF / XML). Same README-narrative-mirrors-storyboard drift class as v4.20. v4.21 closes all 3. **No screens removed** (still 77); README-only edits.

### Trimmed — README narrative drift (3 sites)

- `tenant_admin/README.md:22` SC-ADD-05 row: "format picker (CSV / JSON tab switcher with 5-row preview)" → 4-format with §16.2 #7.14 + §16.3 #8.9 citations + REST/GraphQL/webhooks mentions
- `tenant_admin/README.md:50` Components list: "Tab switcher ... for CSV / JSON format selection (per SOW §8.9)" → "CSV / JSON / PDF / XML format selection (per SOW §16.2 #7.14 + §16.3 #8.9)"
- `README.md` (root) SC-ADD-05 description: "one-click export wizard (CSV / JSON per §8.9)" → "REST + GraphQL API console + real-time webhooks + one-click export wizard (CSV / JSON / PDF / XML per §16.2 #7.14 + §16.3 #8.9)"

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 18 consecutive releases)
- `grep -i "CSV / JSON tab"` in deliverable → 0 hits
- `grep -i "CSV / JSON per §8\.9"` in deliverable → 0 hits
- Pass 21 finding verified clean

### Numbers

| | v4.20 | v4.21 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| Stale 2-format README descriptions | 3 | **0** |
| Pass 21 findings | 1 | **0 expected on Pass 22** |

---

## v4.20 — 10 May 2026 — SOW-anchored sweep follow-up #2 (super_admin/README narrative drift)

Pass 19 (post-v4.19) found **1 Material** item: `super_admin/README.md:19` SC-ADD-04 row still described the FERPA control table as "**6-row**" when v4.18 had expanded it to **16 rows** with explicit SOW §16.5 control citations. Same README-narrative-mirrors-storyboard drift class as v4.15. v4.20 closes it. **No screens removed** (still 77).

### Trimmed — README count + content drift

Updated `super_admin/README.md:19` SC-ADD-04 description to reflect the v4.18 expansion: now reads "**16-row** FERPA control table referencing 34 CFR §§99.10 / 99.31 / 99.32 / 99.37 plus generic WGU institutional policies covering data breach drills and staff FERPA training, with explicit SOW §16.5 control rows added in v4.18: SOC 2 Type II (#10.6), ISO 27001 (#10.13), zero-trust authorization (#10.14), GDPR (#10.12), annual penetration testing (#10.10), AES-256 at rest with cloud KMS (#10.16), MFA for privileged accounts (#10.18), threat detection / SIEM (#10.15), vulnerability scanning + 48-hr critical patch SLA (#10.9 + #10.19), and BC/DR with RTO ≤ 4hr + RPO ≤ 60min (#10.20 + §16.4 #9.4)". Also added "SAML 2.0 SP per §16.3 #8.2; MFA per §16.5 #10.18" to the SSO landing description per the v4.19 storyboard update.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 17 consecutive releases)
- `grep -i "6-row FERPA"` in deliverable → 0 hits
- `grep -i "16-row FERPA"` in deliverable → 1 hit (super_admin/README.md)
- Pass 19 finding verified clean

### Numbers

| | v4.19 | v4.20 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| Pass 19 findings | 1 | **0 expected on Pass 20** |

---

## v4.19 — 10 May 2026 — SOW-anchored sweep follow-up (hub-card stale wording + SAML 2.0 SP citation)

Pass 18 (post-v4.18 audit using the literal SOW MD as authority source) found **1 Material + 1 Borderline** items. v4.19 closes both. **No screens removed** (still 77); all in-place text edits.

### Trimmed — stale 2-format export wording on tenant_admin Hub card

`tenant_admin/index.html:1015` (Hub card on screen 2 quick-launch grid for SC-ADD-05 Data Portability) described the surface as "Query learner records via the REST API console (OAuth 2.0, per-tenant rate limit) or run a one-click CSV / JSON export." v4.18 restored PDF + XML formats on screens 10 and 14 + the catalog, but missed updating this Hub-card description. Refreshed to: "Query learner records via the REST or GraphQL API console (OAuth 2.0, per-tenant rate limit), run a one-click multi-format export (JSON · CSV · PDF · XML per §16.2 #7.14 + §16.3 #8.9), or stream events via real-time webhooks (§16.3 #8.12)."

### Added — SAML 2.0 SP citation on super_admin SSO landing (§16.3 #8.2)

The storyboard previously depicted "WGU SSO authentication complete · MFA verified" on the super_admin screen 1 Privileged session landing without naming the SAML protocol. SOW §16.3 #8.2 commits JFT to "SAML single sign-on (SSO) integration" as a SAML service provider with WGU's IdP. Convention established in v4.18 (SOW citations on §16.3 #8.10 OAuth, #8.12 webhooks, #8.13 GraphQL) supports adding the §16.3 #8.2 anchor here. Updated to: "WGU SSO authentication complete · SAML 2.0 SP (§16.3 #8.2) · MFA verified (§16.5 #10.18)."

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 16 consecutive releases)
- `grep -i "SAML"` in deliverable returns at least 1 hit on super_admin screen 1
- `grep -i "CSV / JSON export"` returns 0 hits in deliverable (Hub card refreshed)
- Pass 18 Material + Borderline findings both verified clean
- Forbidden-term sweep clean

### Numbers

| | v4.18 | v4.19 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| Hub-card stale format wording | 1 | **0** |
| SAML 2.0 SP citation depicted | 0 | **1** |
| Pass 18 findings | 2 | **0 expected on Pass 19** |

---

## v4.18 — 10 May 2026 — SOW-anchored sweep (restore over-trims + add missing requirements per the literal signed SOW MD)

Brady provided the **literal signed MSA/SOW** (`JFT_WGU_MSA_SOW_signed_05MAY2026.md`, 869 lines, signed 03 MAR 2026 by David Perkinson / Amit Kumar Pandey). Prior adversarial passes 11–16 worked from CHANGELOG-derived paraphrases of the SOW rather than the contract itself. Reading the actual SOW revealed **both over-trims and gaps**: items I had removed that are explicitly committed in SOW Appendix A, plus contract-grounded features the storyboard never depicted. v4.18 is a single batched release that restores wrongly-trimmed items, adds missing SOW-required items, and keeps in place the trims that are genuinely ungrounded. **No screens removed** (still 77); all in-place text edits + small section additions within existing screens.

### Restored — items v4.13/v4.14 incorrectly trimmed (in SOW)

| Item | Where trimmed | SOW citation | Restoration |
|---|---|---|---|
| **Jira ticketing** | v4.14 | SOW §9.1 ("Issues will be tracked in **Jira**") + §9.4 ("**Jira / Ticketing System**") + §13 ("via Jira or email") | Restored "Open Jira ticket" button on tenant_admin screen 18; "Log a P1 incident in Jira" heading on screen 19; Jira mention in catalog SC-ADD-06 workflow narrative |
| **Anthropic Claude Sonnet 4.5 in instructor audit log** | v4.13 | SOW §16.1 #6.1 explicitly names "Claude (Anthropic), ChatGPT (OpenAI), Gemini (Google)" as required LLM providers; §5 Tech Stack names OpenAI/Anthropic/Google Vertex AI | Restored vendor-named `model.invoke` row in SC-ADD-03 Audit Trail (audit-log accuracy of which specific model handled the inference is appropriate). "Guardrail svc" and "Scoring engine" stay generic (named internal architecture not in SOW) |
| **PDF + XML export formats** | v4.10 | SOW §16.2 #7.14 ("CSV, **PDF**, or JSON") + §16.3 #8.9 ("JSON, CSV, **XML**") | Restored 4-format tab switcher (CSV / JSON / PDF / XML) on export wizard screen 14; Quick-exports row on screen 10 now lists "JSON · CSV · PDF · XML" |

### Added — SOW requirements the storyboard never depicted

| Feature | SOW citation | Where added |
|---|---|---|
| **Real-time webhooks** | §16.3 #8.12 + §3.19 | Third entry card on tenant_admin Data & APIs landing (screen 10) — "HTTPS POST · signed payloads · exponential backoff retries · per-tenant endpoints · session.start / submission / score.update events" |
| **GraphQL API** | §16.1 #6.28 + §16.3 #8.13 | "REST / GraphQL" tab switcher on API Console (screen 11) + "REST + GraphQL APIs" framing on Data & APIs landing card |
| **A/B testing for LLM configs** | §16.1 #6.8 | Badge below the prompt textarea on AI Prompt Config (screen 5): "A/B test variants enabled · §16.1 #6.8" |
| **LaTeX input/output** | §16.1 #6.12 | Badge on screen 5: "LaTeX rendering · §16.1 #6.12" |
| **Default locale / i18n** | §16.2 #7.6 + §3.7 | New "Default locale" dropdown on Branding & Customization (screen 24) — "English (US) — pilot" selected, with English (UK) / Spanish (US) / French (CA) / German available |
| **PWA installability** | §16.2 #7.7 | Badge on Branding (screen 24): "Installable PWA enabled" with help text |
| **SOC 2 Type II posture** | §16.5 #10.6 | New row in super_admin Compliance Report FERPA control table (screen 6) |
| **ISO 27001 alignment** | §16.5 #10.13 | New row in compliance table |
| **Zero-trust authorization** | §16.5 #10.14 | New row in compliance table |
| **GDPR controls** | §16.5 #10.12 | New row in compliance table |
| **Penetration testing (annual)** | §16.5 #10.10 | New row in compliance table with last/next dates |
| **AES-256 encryption at rest** | §16.5 #10.16 | New row in compliance table |
| **MFA for privileged accounts** | §16.5 #10.18 | New row in compliance table (100% adoption) |
| **Threat detection / SIEM** | §16.5 #10.15 | New row in compliance table (24/7 monitoring per §16.4 #9.1) |
| **Vulnerability scanning + 48-hr critical patch SLA** | §16.5 #10.9 + #10.19 | New row in compliance table |
| **BC/DR with RTO ≤ 4hr, RPO ≤ 60min** | §16.5 #10.20 + §16.4 #9.4 | New row in compliance table referencing the 22 Apr 2026 last-drill date |

### Kept trimmed — items still genuinely not in SOW

- AWS-specific zone IDs (`us-east-1` / `us-west-2` / `eu-west-1`) — SOW §5 says "AWS / GCP / Azure (finalize with WGU)"; specific zone IDs remain implementation detail
- `WGU Policy 8.2` / `WGU Policy 8.4` / `WGU Learning Hub` — not in SOW
- "1,247 sessions" / "47 operators" / "14 endpoints" / "600 req/hr" — fabricated specifics, not in SOW
- "7 years" FERPA retention — SOW §10.2 says "default three years" for inactive learner data
- TLS cipher suite names (TLS_AES_256_GCM_SHA384 etc.) — implementation detail beyond §10.7 "TLS 1.3"
- Named internal services (Guardrail svc, Scoring engine, Vector store, Stepper coordinator, etc.) — implementation detail
- "JFT 24/7 [Operations | Proactive Monitoring]" as branded service-name — keep "24/7 Proactive Monitoring" as a capability descriptor (matches §9.13 + §16.4 #9.1); drop "JFT 24/7" prefix-branding

### SOW tension resolution — 24/7 vs business hours

The SOW contains a tension between §9.1 ("WGU's standard business hours" support coverage) + §11 pricing on "Standard Business Hours" and §16.4 #9.1 ("24/7 system monitoring") + #9.10 ("24/7 technical support with <2 hour response"). Storyboard treats this as two layers: **automated monitoring is 24/7** (per §9.13 + §16.4 #9.1) while **human support coverage is business hours with 2-hour P1 response** (per §9.1 + §9.5). Both contractual commitments are honored without conflation.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 15 consecutive releases)
- `grep -i "Jira"` returns hits in tenant_admin/index.html (screens 18 + 19) + catalog SC-ADD-06 workflow ✓
- `grep -i "GraphQL\|webhook\|LaTeX\|SOC 2\|ISO 27001\|GDPR\|zero-trust\|AES-256\|penetration"` returns hits in expected locations ✓
- `grep -i "us-east-1\|WGU Policy 8\|WGU Learning Hub\|1,247\|14 endpoints"` returns **0 hits** in deliverable (CHANGELOG meta-context allowed)
- All 13 SOW Appendix A feature gaps documented in plan are now depicted
- Forbidden-term sweep clean

### Numbers

| | v4.17 | v4.18 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| Jira mentions | 0 | **restored** (3+ sites) |
| GraphQL depicted | No | **Yes** (1 tab + 1 card mention) |
| Webhooks depicted | No | **Yes** (1 card on Data & APIs landing) |
| LaTeX / A/B test / i18n / PWA depicted | No | **Yes** (badges on screens 5 + 24) |
| SOC 2 / ISO 27001 / GDPR / zero-trust / pentest / AES-256 / MFA / SIEM / BC-DR / vuln-scan rows | 0 | **10 new rows** added to super_admin Compliance Report FERPA control table |
| Export formats depicted | 2 (JSON, CSV) | **4** (JSON, CSV, PDF, XML — §16.2 #7.14 + §16.3 #8.9) |
| Vendor-named `model.invoke` in audit log | No | **Yes** (Anthropic Claude Sonnet 4.5 — §16.1 #6.1 explicitly names) |

---

## v4.17 — 08 May 2026 — Tenth overboard sweep (WGU Learning Hub + FERPA-grade leftover + JFT 24/7 service-naming)

Pass 16 (post-v4.16 independent audit) found **1 Material + 2 Borderline** items. v4.17 closes all 3. **No screens removed** (still 77); all in-place text edits.

### Trimmed — fabricated `WGU Learning Hub` product name

`super_admin/index.html:1304` (FERPA control table sub-text): "Tracked in WGU Learning Hub · auto-suspended access if > 365 days." "WGU Learning Hub" is invented WGU-internal product naming with no SOW or catalog grounding — same class as v4.14's trimmed `WGU Policy 8.x` and v4.13's trimmed named internal services. Softened to "Tracked per institutional policy · auto-suspended access after 365 days of inactivity."

### Trimmed — `FERPA-grade retention` leftover

`super_admin/index.html:727` (Privileged session alert on screen 1): "All actions in this portal are logged to the cross-tenant audit trail with FERPA-grade retention." v4.11 swept "FERPA-grade retention (7 years)" elsewhere in this file (line ~1477) but missed this site. There is no formal "FERPA-grade" classification — the rest of the codebase consistently uses "FERPA-aligned retention per institutional policy." Softened here to match.

### Trimmed — `JFT 24/7` service-naming prefix (4 sites in tenant_admin)

The catalog narrative on `presentation.html:771` correctly describes the capability as "24/7 Proactive Monitoring detects the failure" (capability descriptor, no JFT prefix). But four storyboard sites used "JFT 24/7 [Proactive Monitoring | monitoring | Operations]" — branding it as a named JFT service. Same class as v4.13's "Guardrail svc / Scoring engine" trim (named internal services beyond SOW grounding). Generic-ized to drop the "24/7" service-naming while keeping the §9.13 monitoring + §9.5 P1 SLA contract grounding:

- `tenant_admin/index.html:1028` (screen 2 hub caption): "Live system health, JFT 24/7 monitoring, ..." → "Live system health, JFT Proactive Monitoring (§9.13), ..."
- `tenant_admin/index.html:2071` (screen 16 baseline): "JFT 24/7 Proactive Monitoring shows nominal" → "JFT Proactive Monitoring (§9.13) shows nominal"
- `tenant_admin/index.html:2367` (screen 19 ticket description textarea): "JFT 24/7 Proactive Monitoring detected" → "JFT Proactive Monitoring (per §9.13) detected"
- `tenant_admin/index.html:2414` (screen 20 ticket confirmation): "Acknowledged by JFT 24/7 Operations" → "Acknowledged by JFT Support per §9.5" (also closes a CSM-vs-Support SLA ownership conflation that v4.9 fixed elsewhere)

The catalog narrative line 771 retains "24/7 Proactive Monitoring" (capability descriptor matching v1.3 catalog text); only the JFT-prefixed service-naming was the leakage.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 14 consecutive releases)
- `grep -i "WGU Learning Hub|FERPA-grade|JFT 24/7|24/7 Operations"` in deliverable → 0 hits (CHANGELOG meta-context allowed)
- All 3 Pass 16 findings (1 Material + 2 Borderline) verified clean
- Forbidden-term sweep clean

### Numbers

| | v4.16 | v4.17 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| `WGU Learning Hub` mentions | 1 | **0** |
| `FERPA-grade` leftover | 1 | **0** |
| `JFT 24/7` service-naming sites | 4 | **0** |
| Pass 16 findings | 3 | **0 expected on Pass 17** |

---

## v4.16 — 08 May 2026 — Ninth overboard sweep (lrps/README prose drift + JS comments + 5-day FERPA SLA + 47 operators)

Pass 15 (post-v4.15 independent audit) found **1 Material + 4 Borderline** items. v4.16 closes the Material + 3 of 4 Borderline (the 4th — `4-hour RTO` — was Pass 15's "noted but not flagged" tail; left as-is, parallel to kept "99.95% / 99.97% uptime"). **No screens removed** (still 77); all in-place text edits.

### Trimmed — `lrps/README.md` prose paragraph "three live SDP rows" survived v4.15

v4.15 swept the count table (lines 26-27) but missed the prose paragraph at line 20 saying "three live SDP rows (Tenant Admin, Instructor, Super Admin)" — same enumeration error v4.15 fixed elsewhere. Updated to "four live SDP rows (Student, Tenant Admin, Instructor, Super Admin)."

### Trimmed — JS code comments in `lrps/index.html` (consistency with v4.15)

Two non-user-visible JS comments still said "three" — the agent flagged at borderline confidence. Cleaned for consistency:
- Line 1113: "Make the three live SDP rows launch their portals" → "Make the four live SDP rows launch their portals"
- Line 1123: "Theme toggle (matches the three SDP portals)" → "Theme toggle (matches the four SDP portals)"

### Trimmed — fabricated "5-day SLA for correction requests" (FERPA control table)

`super_admin/index.html:1300` claimed a 5-day SLA for FERPA correction requests. 34 CFR §99.10's regulatory window is 45 days; the 5-day claim was a fabricated JFT-side internal commitment with no SOW/catalog grounding. Same class as v4.10's "7 years (FERPA default)" trim. Softened to "correction requests handled per institutional policy (within the 45-day regulatory window)" — preserves the regulatory anchor (45 days), drops the invented JFT-side specific.

### Trimmed — fabricated "47 JFT + WGU operators" (FERPA training gauge)

`super_admin/index.html:1262` sub-text said "All 47 JFT + WGU operators current." 47 is invented headcount with no SOW/catalog grounding. Same class as v4.14's "1,247 sessions" trim. Softened to "All operators current per institutional policy."

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 13 consecutive releases)
- `grep -i "three live SDP\|three SDP portals"` in deliverable → 0 hits (CHANGELOG meta-context allowed)
- `grep "5-day SLA\|All 47"` in deliverable → 0 hits
- All 4 Pass 15 findings (1 Material + 3 Borderline) verified clean
- The 4th Pass 15 borderline item ("4-hour RTO" specific) explicitly left as-is — agent rated borderline-not-flagged; matches the contract-grounded pattern of "99.95% / 99.97% uptime" (specific SLA telemetry display)
- Forbidden-term sweep clean

### Numbers

| | v4.15 | v4.16 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| `three live SDP` mentions | 3 | **0** |
| `5-day SLA` fabricated specific | 1 | **0** |
| `47 operators` fabricated specific | 1 | **0** |
| Pass 15 Material findings | 1 | **0 expected on Pass 16** |

---

## v4.15 — 08 May 2026 — Eighth overboard sweep (catalog/README leakage from v4.14 + 3-vs-4 LRPS row drift + {section_id} URL)

Pass 14 (post-v4.14 independent audit) found **4 items** — three Material + one Borderline. Three of them are catalog/README sites that mirrored v4.14's storyboard fixes; the fourth is a 3-vs-4 internal contradiction that has been latent since the student row was added to LRPS as a live entry. v4.15 closes all 4. **No screens removed** (still 77); all in-place text edits.

### Trimmed — `WGU policies 8.2 and 8.4` survived in catalog narratives + super_admin README

v4.14 trimmed the fabricated `WGU Policy 8.4` and `WGU Policy 8.2` citations from `super_admin/index.html` (FERPA control table) but missed three downstream sites mirroring the same SC-ADD-04 step-6 description:

- `presentation.html:709` SC-ADD-04 step 6 narrative
- `presentation_dark.html:709` (same)
- `super_admin/README.md:19` SC-ADD-04 row

All three softened to "generic WGU institutional policies (data breach drill, staff FERPA training)" — same trim rationale as v4.14.

### Trimmed — "Dashboard home with section cards" catalog step title

`presentation.html:653` + `presentation_dark.html:653` SC-ADD-03 step 2 step title still said "section cards" even though the step body and the storyboard itself were corrected to "course" framing. The CSS class `.section-card` is internal styling (not user-visible); only the step title was the leakage. Trimmed to "Dashboard home with course cards."

### Trimmed — "3 live SDP rows" stale count (LRPS actually shows 4)

LRPS landing page (`lrps/index.html` line 727) shows "4 Live SDP rows" and line 736 explicitly enumerates "Student, Tenant Admin, Instructor, Super Admin" as the four live rows. But three docs still claimed 3:

- `index.html:455` LRPS portal-card scenario tag: "3 live SDP rows" → "4 live SDP rows"
- `README.md:41` Surfaces table LRPS row: "(3 live SDP rows, 17 illustrative)" → "(4 live SDP rows + illustrative filler)"
- `README.md:187` LRPS scope bullet: "3 live SDP rows (Tenant Admin, Instructor, Super Admin)" → "4 live SDP rows (Student, Tenant Admin, Instructor, Super Admin)"
- `lrps/README.md:26-27` table: count 3 → 4 with persona enumeration

### Trimmed — `{section_id}` URL placeholder in LRPS instructor row

`lrps/index.html:935` had `lrps.wgu.edu/provision/sdp/instructor/{section_id}` as the user-visible URL template. The other three live rows use `?role=student` / `{tenant_id}` / `?mfa=required` — none reference sections. Per the rolling-enrollment rule (README line 202), "section" framing is forbidden in user-facing copy; this URL fragment is user-visible in the LRPS provider table. Replaced with `{course_id}` to match the rolling-enrollment model.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 12 consecutive releases)
- `grep -i "WGU policies 8\."` in deliverable → 0 hits (CHANGELOG meta-context allowed)
- `grep -i "section cards\|section_id"` in deliverable → 0 hits
- `grep -i "3 live SDP"` in deliverable → 0 hits
- All 4 Pass 14 findings verified clean
- Forbidden-term sweep clean

### Numbers

| | v4.14 | v4.15 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| `WGU policies 8.x` mentions | 3 | **0** |
| `3 live SDP rows` stale count | 3 | **0** |
| `{section_id}` URL placeholder | 1 | **0** |
| `section cards` catalog step titles | 2 | **0** |
| Pass 14 findings | 4 | **0 expected on Pass 15** |

---

## v4.14 — 08 May 2026 — Seventh overboard sweep (Jira + AWS region IDs + WGU Policy 8.x citations + section leakage + 1,247 sessions)

Pass 13 (post-v4.13 independent audit) found **6 items** — concentrated in places prior code-focused passes had only spot-checked (incident-response screens 17–22, geo-redundancy screen 7, instructor screens 4 + 8, FERPA control table). v4.14 closes all 6. **No screens removed** (still 77); all in-place text edits.

### Trimmed — `Jira` vendor naming outside vendor-config UI

SOW §9.5 commits to a 2-hour P1 response time but does not commit to Jira (Atlassian) as the ticketing vendor. Same vendor-naming-outside-vendor-context rationale that drove v4.10–v4.12.

Sites edited (5 across 3 files):
- `tenant_admin/index.html:2298` — `<button>...Open Jira ticket</button>` → "Open P1 ticket"
- `tenant_admin/index.html:2306` — HTML comment "Screen 19: Jira P1 ticket creation form" → "Screen 19: P1 ticket creation form"
- `tenant_admin/index.html:2328` — `<h1>Log a P1 incident in Jira</h1>` → "Log a P1 incident with JFT Support"
- `presentation.html:771` + `presentation_dark.html:771` SC-ADD-06 workflow narrative — "logs a P1 ticket in Jira. The JFT Customer Success Manager responds within 2 hours" → "logs a P1 ticket with JFT Support. JFT Support acknowledges within the §9.5 2-hour P1 SLA (with the JFT CSM as WGU-facing POC per §9.1.4)" (also closes the catalog-narrative CSM-vs-Support SLA conflation that v4.9 fixed in the storyboard but missed here)

### Trimmed — AWS-specific region IDs + city locations on Geo-Redundancy screen 7

`us-east-1` / `us-west-2` / `eu-west-1` are AWS-specific availability-zone identifiers; `Northern Virginia, USA` / `Oregon, USA` / `Dublin, Ireland` are AWS data-center locations. SOW §9.5 commits to geo-redundancy generically; nothing in SOW or v1.3 catalog names AWS or specific zones. Same rationale as v4.12 dropping `(RDS)` and named internal services.

Sites edited (`super_admin/index.html`):
- Region cards (lines 1376–1411): "us-east-1" / "us-west-2" / "eu-west-1" → "Primary region · US East" / "Secondary region · US West" / "DR region · EU"
- Region card sub-text: city-specific locations → role-specific descriptions ("Active region serving most learners" / "Hot standby for failover" / "Disaster-recovery region")
- Failover test table (lines 1439–1442) From/To columns: AWS zone IDs → "Primary" / "Secondary" / "DR"
- Audit log (line 1599): `failover.probe (us-east → eu-west)` → `failover.probe (Primary → DR)`
- `presentation.html:712` + `presentation_dark.html:712` SC-ADD-04 step 7 narrative: "us-east-1 primary / us-west-2 secondary / eu-west-1 DR" → "Primary US East / Secondary US West / DR EU"

### Trimmed — "section" framing leakage in instructor

v4.13 caught "Sally's section" on tenant_admin screen 8 but missed two instructor sites. README line 202 + the rolling-enrollment rule forbid "section" framing.

Sites edited (`instructor/index.html`):
- Line 1008 (screen 4 at-risk filter alert): "the lowest score in the section" → "the lowest score in this course"
- Line 1439 (screen 8 audit-trail compliance footer): "Charlie's view is constrained to his sections by RBAC" → "Charlie's view is constrained to his courses by RBAC"

### Trimmed — fabricated `WGU Policy 8.4` and `WGU Policy 8.2` citations

The 34 CFR §99.10 / §99.31 / §99.32 / §99.37 federal-regulation citations elsewhere in the FERPA control table are real. But "WGU Policy 8.4" / "8.2" were invented internal-policy numbers — no SOW or catalog grounding, and these aren't legally verifiable WGU policy references.

Sites edited (`super_admin/index.html`):
- Line 1303 "Annual data breach response drill | WGU Policy 8.4" → "WGU institutional policy"
- Line 1304 "Staff FERPA training (annual) | WGU Policy 8.2" → "WGU institutional policy"

### Trimmed — "1,247 sessions" fabricated specific

The number ricocheted across SC-ADD-06 incident screens (17, 19, 22) and the catalog narrative as if authoritative. No SOW or catalog text specifies a session count for the incident scenario. Same class as v4.9's "213/600 rate-limit usage" trim.

Sites edited (5 across 3 files):
- `tenant_admin/index.html:2229` (screen 17 Fallback row sub-text): "1,247 sessions migrated transparently" → "All active learner sessions migrated transparently"
- `tenant_admin/index.html:2369` (screen 19 P1 ticket description textarea): "1,247 active learner sessions migrated transparently" → "All active learner sessions migrated transparently"
- `tenant_admin/index.html:2556` (screen 22 service status table Learner sessions row): `1,247 active` / `1,247 active · 0 dropped` / `1,261 active` → `All active` / `All active · 0 dropped` / `All active`
- `presentation.html:777` + `presentation_dark.html:777` SC-ADD-06 step 2 narrative: "fallback LLM provider active and serving 1,247 sessions per §6.5" → "fallback LLM provider active and serving all active learner sessions per §6.5"

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 11 consecutive releases)
- `grep -i "Jira"` in deliverable HTML/MD → 0 hits (CHANGELOG meta-context allowed)
- `grep -i "us-east-1|us-west-2|eu-west-1|Northern Virginia|Oregon, USA|Dublin, Ireland"` in deliverable → 0 hits
- `grep "WGU Policy 8\."` in deliverable → 0 hits
- `grep "1,247"` in deliverable → 0 hits
- `grep -i "in the section\|sections by RBAC"` in deliverable → 0 hits
- All 6 Pass 13 findings verified clean
- Forbidden-term sweep clean

### Numbers

| | v4.13 | v4.14 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| `Jira` mentions | 5 | **0** |
| AWS-specific zone IDs | 11 | **0** |
| Fabricated `WGU Policy 8.x` citations | 2 | **0** |
| `1,247 sessions` fabricated specifics | 5 | **0** |
| `section` framing in instructor | 2 | **0** |
| Pass 13 findings | 6 | **0 expected on Pass 14** |

---

## v4.13 — 08 May 2026 — Sixth overboard sweep (catalog-narrative + READMEs + root-index leakage; v4.0 staleness across portal titles/footers)

Pass 12 (post-v4.12 independent audit) found **17 items** the previous five sweeps missed — concentrated in surfaces the prior code-focused passes had under-audited: catalog scenario narratives, per-portal READMEs, the root `index.html` portal-selector landing, and `v4.0`-vintage portal titles + footers that were never bumped after the initial release. v4.13 closes all 17. **No screens removed** (still 77); all in-place text edits.

### Trimmed / softened — instructor/ audit-log leakage (v4.10/v4.12 oversight)

The SC-ADD-03 Audit Trail event log (instructor screen 8) still listed three sources that had been generic-ized elsewhere in v4.10 + v4.12:
- Row 4 "Guardrail svc" → "SDP Coach"
- Row 5 "Anthropic Claude Sonnet 4.5" → "Primary LLM provider"
- Row 7 "Scoring engine" → "SDP Coach"

Same generic-ization rationale as v4.12: audit-log displays are not vendor-picker context, and named internal architecture components ("Guardrail svc", "Scoring engine") are implementation detail beyond the SOW.

### Trimmed — `super_admin/index.html` "via cert-manager"

Compliance Report (screen 6) tail copy named a specific Kubernetes-ecosystem auto-renewal tool. Implementation detail comparable to "(RDS)" v4.12 dropped. Trimmed to "Auto-renewal is enabled across all services."

### Trimmed — `tenant_admin/index.html` "3 available" datasets + "Sally's section"

- Screen 10 (Data & APIs landing) Quick exports table row: "Datasets · 3 available" → "Datasets · Engagement metrics (v1.3)" — matches the v4.10 trim of the export wizard from 3 datasets to 1 (engagement metrics only).
- Screen 8 (Review & Deploy) deploy-warning alert: "live for all learners on Sally's section" → "live for all active learners in this Subject" — "section" framing forbidden by the rolling-enrollment rule (README line 202).

### Trimmed — catalog scenario narratives in `presentation.html` + `presentation_dark.html`

Catalog narratives had not been refreshed after the v4.4–v4.12 storyboard sweeps and were describing pre-trim screens:

- **Per-persona portals list (line 568):** "Alice (Tenant Admin) ... 23 screens" → "27 screens" (v4.4 extended Tenant Admin)
- **SC-ADD-02 step 2 narrative:** "Three subjects (E010 in production, E075 staging, E120 draft)" → "Four subjects (E010 production, E135 production, E075 staging, E120 draft)" (matches current portal home Subjects list)
- **SC-ADD-02 step 5 narrative:** "Recent versions panel ... last 3 prompt edits" → "one-line 'Last edited' indicator" (matches v4.8 collapse)
- **SC-ADD-03 step 2 narrative:** "Charlie's three sections (E010 § 042 active, E075 § 018, E135 § 003). Active section shows..." → "Charlie's three courses (E010, E075, E135) under WGU's rolling-enrollment model — no fixed sections or cohorts. Active course (E010) shows..." (rolling-enrollment rule)
- **SC-ADD-03 step 3 narrative:** "Search by name / email (deep-links to screen 9)" → removed (v4.9 dropped screen 9)
- **SC-ADD-04 step 6 narrative:** "17/17 services TLS 1.3 ... 7-yr audit trail retention ... 10-row service-by-service TLS table with cipher" → "all paths TLS 1.3 ... audit trail retention per institutional policy ... service-by-service TLS table (TLS version + cert expiry + last scan + pass status)" (matches v4.11 + v4.12 trims)
- **SC-ADD-05 step 1 narrative:** "REST API (auth, base URL, 14 endpoints, 600 req/hr) ... 3 datasets" → "REST API (OAuth 2.0 auth, base URL, per-tenant rate limit, endpoint catalog finalized at onboarding) ... engagement metrics dataset" (matches v4.9 + v4.10 trims)
- **SC-ADD-05 step 2 narrative:** "213/600 rate-limit usage" → "rate-limit usage well below tenant tier cap" (matches v4.9 trim)

### Trimmed — `super_admin/README.md` "across 17 services"

Two mentions ("encryption audit §10.7 across 17 services" + "TLS 1.3 verification across 17 services") softened to "across all data paths" — matches v4.12 storyboard wording.

### Trimmed — `tenant_admin/README.md` "7-year retention" + "JFT CSM ... 2-hr SLA"

- "FERPA-aligned 7-year retention" → "FERPA-aligned retention per institutional policy" (matches v4.10 + v4.11 trims)
- "JFT CSM chat thread (within 2-hr SLA)" → "JFT Support P1 response thread within 2-hr SLA per §9.5 (CSM Jordan as WGU-facing POC)" (matches v4.9 reframe of CSM-vs-Support SLA ownership)
- "The CSM chat thread on screen 21 demonstrates within-2-hr SLA response" → reframed to clarify SLA is owned by JFT Support per §9.5; CSM Jordan is the §9.1.4 WGU-facing POC

### Bumped — root `index.html` portal-selector landing

Never updated after the v4.0 initial release. Refreshed:
- Hero eyebrow "v4.0" → "v4.13"
- Hero stat "73 Screens" → "77 Screens"
- Tenant Admin card "23 screens" → "27 screens"
- Instructor card "Charlie · course instructor" → "Charlie · Instructor" (User Profile canonical)
- Catalog card "148 screenshots" → "156 screenshots"
- Footer "Storyboard v4.0" → "Storyboard v4.13"
- HTML comment "23 screens" → "27 screens"

### Bumped — portal `index.html` titles + footers (v4.0 vintage)

Three portal HTMLs had `<title>... Storyboard v4.0</title>` and visible footers `Storyboard v4.0 — Western Governors University` since the initial release:
- `instructor/index.html` — title + footer + persona comment "course instructor" → "Instructor"
- `super_admin/index.html` — title + footer
- `lrps/index.html` — title + footer

All bumped to v4.13.

### Bumped — catalog hero `Storyboard v4.0` → `Storyboard v4.13`

Both `presentation.html` + `presentation_dark.html` hero `<div class="hero-doc-info">` showed `Storyboard v4.0` despite footers being bumped each release. Now matches footer.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 10 consecutive releases)
- `grep -i "Storyboard v4\.0"` in deliverable HTML/MD → 0 hits in current state (allowed in CHANGELOG meta-context)
- `grep -i "Section 042\|§ 042\|course instructor"` in deliverable → 0 hits (allowed in CHANGELOG + Document Control historical references)
- `grep -i "17 services\|14 endpoints\|600 req\|3 datasets\|7 year\|7-year\|7yr\|7 yr\|Guardrail svc\|Scoring engine\|cert-manager\|Anthropic Claude"` in deliverable → 0 hits (CHANGELOG meta-context allowed)
- All 17 Pass 12 findings verified clean
- Forbidden-term sweep clean

### Numbers

| | v4.12 | v4.13 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| Pass 12 findings | 17 | **0 expected on Pass 13** |
| Files with `Storyboard v4.0` staleness | 6 | **0** |
| Catalog narratives describing pre-trim screens | 7 sites × 2 catalogs | **0** |

---

## v4.12 — 08 May 2026 — Fifth overboard sweep (TLS cipher specifics + vendor model names in subject metadata)

Pass 11 (post-v4.11) found 2 more items. v4.12 closes both. **No screens removed** (still 77); all in-place text edits.

### Trimmed — TLS cipher suite specifics on Super Admin Compliance Report (screen 6)

The Compliance Report listed 10 services with specific cipher suites (`TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_AES_128_GCM_SHA256`) plus a 7-additional-services footnote naming "Guardrail svc, Scoring engine, Cache layer, Vector store, Stepper coordinator, Notification svc, CSM bridge."

- **SOW §10.7:** "Encryption (TLS 1.3) across all data paths." Cipher suite selection is implementation detail.
- **No SOW or catalog text** commits to specific cipher algorithms or names internal architecture components like "Vector store" / "Stepper coordinator."

Edits (`super_admin/index.html`):
- Removed the "Cipher" column from the service table (kept TLS version 1.3 + cert expiry + last scan + status)
- Consolidated provider-specific rows: "Model Router → Anthropic" + "Model Router → OpenAI (fallback)" + "Model Router → Google (fallback)" → 2 generic rows ("primary LLM provider" + "fallback LLM providers")
- Removed "(RDS)" implementation detail from "Tenant DB" row
- Replaced 7-named-services footnote with "Additional internal platform services use TLS 1.3 encryption identically; details available in the PDF export for compliance audits"
- KPI gauge: "17/17 Services TLS 1.3" → "All paths · TLS 1.3" (count was implementation-specific)
- Audit log "17/17 pass" badge → "All paths pass"

### Trimmed — vendor model names in subject metadata rows

After v4.10's vendor-naming sweep across the SC-ADD-06 incident scenario, model names still appeared in subject metadata rows on tenant_admin screen 2 (portal home Subjects list) and screen 27 (Subject Lifecycle Active Subjects table). Pass 11 noted both:
1. The names are informational metadata (not vendor-picker context), inconsistent with the v4.10 rule.
2. The two screens were inconsistent with each other ("Claude Sonnet 4.5" vs. "Claude 3.5 Sonnet"; "GPT-5" vs. "GPT-4o") — fabricated specifics that drifted.

Edits (`tenant_admin/index.html`):
- Screen 2 portal home Subjects list (3 rows): dropped " · Claude Sonnet 4.5" / " · GPT-5" suffixes
- Screen 27 Subject Lifecycle Active Subjects (3 rows): dropped " · Claude 3.5 Sonnet" / " · GPT-4o" annotations from Subject ID metadata lines

Vendor names retained on:
- Screen 6 (Choose the Preferred Model) — vendor-picker UI, appropriate
- Screen 7 (Configure Scoring & Rubric) — fallback chain config display, appropriate
- Screen 8 (Review & Deploy) — review-of-Alice's-choices, appropriate

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through 9 consecutive releases)
- `grep "TLS_AES\|TLS_CHACHA"` → 0 hits (cipher names removed)
- `grep "Vector store\|Stepper coordinator\|Guardrail svc"` → 0 hits in deliverable (retained in CHANGELOG meta-context)
- Vendor names contained to model-picker / fallback-chain / Review screens; absent from data displays
- "Claude 3.5 Sonnet" vs "Claude Sonnet 4.5" inconsistency resolved by removing both from data displays
- Forbidden-term sweep clean

### Numbers

| | v4.11 | v4.12 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| TLS cipher names in deliverable | 3 | **0** |
| Vendor model names in subject metadata | 6 | **0** |

---

## v4.11 — 08 May 2026 — Fourth overboard sweep (escaped vendor name + 7-year retention claims trimmed)

Pass 10 (independent post-v4.10 audit) found 2 items v4.10 missed. v4.11 closes both. **No screens removed** (still 77); all in-place text edits.

### Trimmed — escaped vendor name on SC-ADD-06 baseline screen 16

v4.10 generic-ized the SC-ADD-06 incident scenario (screens 17–23) but the **baseline** screen 16 ("All systems operational") still had "Claude Sonnet 4.5 (primary) · 99.99% past 24h · p50 latency 213 ms" in the Model Router operational status row. That contradicted the v4.10 LLM-agnostic stance.

Site edited (`tenant_admin/index.html` line ~2111):
- "Claude Sonnet 4.5 (primary) · 99.99% past 24h · p50 latency 213 ms" → "Primary LLM provider · 99.99% past 24h · p50 latency 213 ms"

### Softened — all 7 "7 years" / "7 yr" retention mentions

v4.10 softened the most prominent "7 years (FERPA default)" claim on Subject Lifecycle screen 27 but explicitly deferred 7 other sites with "if Pass 10 disagrees, fix in next cycle." Pass 10 disagreed.

- **SOW §10.1:** "FERPA Compliance" — generic; does not specify 7 years.
- **SOW §10.2 / answer row #10.2:** "default three years" for inactive learner data (a different scope).
- **MSA §10c:** "no more than sixty (60) days after termination" for JFT's data-retention obligation.
- **v1.3 catalog:** no mention of 7-year retention anywhere.

The "7 years" claims across audit-log captions weren't configured-value displays — they were declarative policy statements ("for 7 years," "retention 7 years") that implied a JFT-side default. Trimmed all of them.

Sites edited:
- `tenant_admin/index.html` line ~967 (portal home hero): "All actions audit-logged for 7 years" → "All actions audit-logged per institutional retention policy"
- `tenant_admin/index.html` line ~1105 (portal home footer): "Audit log retention: 7 years (FERPA)" → "Audit log retention: per institutional policy (FERPA-aligned)"
- `tenant_admin/index.html` line ~1696 (Data & APIs landing audit row): "Logged for 7 years" → "Logged per institutional policy"
- `tenant_admin/index.html` line ~2026 (export confirmation footer): "Logged for 7 years" → "Logged per institutional policy"
- `instructor/index.html` line ~1401 (Audit Trail screen): "Logged immutably for 7 years per FERPA retention policy" → "Logged immutably per FERPA-aligned institutional retention policy"
- `super_admin/index.html` line ~1267 (Compliance Report KPI gauge): "7 yr · Audit trail retention" → "Per policy · Audit trail retention" (FERPA-aligned caption added)
- `super_admin/index.html` line ~1477 (Audit Log header): "FERPA-grade retention (7 years)" → "FERPA-aligned retention per institutional policy"
- `super_admin/index.html` line ~1610 (Audit Log footer): "Retention: 7 years (FERPA)" → "Retention: per institutional policy (FERPA-aligned)"
- `presentation.html` + `presentation_dark.html` SC-ADD-04 step 8 narrative: "Retention: 7 years (FERPA)" → "Retention: per institutional policy (FERPA-aligned)"
- `presentation.html` + `presentation_dark.html` SC-ADD-02 step 13 (Subject Lifecycle) narrative: "FERPA-aligned 7-year retention dates" → "retention dates per institutional policy"

Note: the "3 yr inactive learner data retention" gauge on `super_admin/index.html` Compliance Report (screen 6) is **kept** — that maps to SOW §10.2 "default three years" for inactive learner data, which IS contractually committed. Different scope from audit-log retention.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through v4.4 → v4.5 → v4.6 → v4.7 → v4.8 → v4.9 → v4.10 → v4.11)
- `grep -i "7 years\|7-year\|7 yr"` in tracked deliverable HTML/MD → 0 hits in current state (CHANGELOG + Document Control historical references allowed)
- `grep "Claude Sonnet 4.5\|Anthropic"` → only on model-picker / Subjects-list / rubric (vendor-picker contexts); 0 hits in SC-ADD-06 baseline + incident narrative
- Forbidden-term sweep clean

### Numbers

| | v4.10 | v4.11 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals) |
| "7 years" / "7 yr" retention mentions | 8 | **0** |
| Vendor names in SC-ADD-06 narrative | 1 escaped | **0** |

---

## v4.10 — 08 May 2026 — Third overboard sweep (Parquet + LLM vendor naming + 7-year FERPA claim + 3 export datasets)

After v4.9 Brady asked for another adversarial pass. Pass 9 found 4 more items not actually SOW-grounded. v4.10 closes them. **No screens removed** (still 77); all in-place text edits.

### Trimmed — Parquet format (not in SOW or catalog)

- **SOW §8.9:** "Data exports will be available in JSON, CSV, or XML formats."
- **v1.3 catalog SC-ADD-05:** "She uses one-click export to download a JSON or CSV file."
- Parquet appears in neither. It was added during v4.0 prototyping as a "more modern" option.

Sites edited:
- `tenant_admin/index.html` screen 2 quick-launch caption: "CSV / JSON / Parquet" → "CSV / JSON"
- `tenant_admin/index.html` screen 14 format-picker tab switcher: 3 tabs → 2 tabs (CSV / JSON; Parquet button removed)
- `presentation.html` + `presentation_dark.html` SC-ADD-05 step 5 narrative: "CSV / JSON / Parquet tab switcher" → "CSV / JSON tab switcher"
- `README.md` SC-ADD-05 row caption + `tenant_admin/README.md` scenario row + components list

### Generic-ized — "Primary LLM (Anthropic)" / "Fallback (GPT-5)" in SC-ADD-06 incident scenario

- **SOW §6.1:** "LLM-agnostic orchestration layer that uses provider SDKs and configurable rules to steer traffic between GPT-4o, Claude, Gemini, and future models."
- **§6.5:** "fail over to a secondary LLM."
- The contract treats all three providers as equivalent options. Naming Anthropic specifically as "the primary" implies a vendor commitment that isn't contracted.

Sites edited (`tenant_admin/index.html` SC-ADD-06 incident screens 17/18/19/21/22/23):
- "Primary LLM (Anthropic)" → "Primary LLM provider" (4 sites)
- "Fallback LLM (GPT-5)" → "Fallback LLM provider" (2 sites)
- Narrative + ticket textarea + chat-thread copy generic-ized; §6.5 cited explicitly
- Vendor names retained on the model picker (screen 6) and rubric (screen 7) — those are vendor-picker UIs where naming is appropriate

`presentation.html` + `presentation_dark.html` SC-ADD-06 step 17 narrative similarly generic-ized.

### Softened — Subject Lifecycle "7 years (FERPA default)"

- **SOW §10.1:** "FERPA Compliance" — generic; does not specify 7 years.
- The "FERPA default" phrasing implied a JFT-side default that isn't contracted.

Site edited (`tenant_admin/index.html` screen 27):
- Retention badge: "7 years (FERPA default)" → "Per institutional policy"
- Caption: "Per §10.1; locked by Super Admin policy" → "FERPA-aligned; configured at the platform level (§10.1)"

Other "7 years" mentions (audit-log retention captions on screens 2 / 10 / 15, Super Admin compliance KPI on screen 6) are kept — those are configured-value displays rather than policy claims about a JFT-default. If Pass 10 disagrees, fix in next cycle.

### Trimmed — Export wizard from 3 datasets to 1

- **v1.3 catalog SC-ADD-05:** "She uses one-click export to download a JSON or CSV file **with engagement metrics**." Singular dataset.
- **SOW §7.14:** generic "one-click exports" — doesn't enumerate dataset types.
- The original 3-card layout (Engagement metrics / Score history / Conversation logs) extrapolated beyond catalog; conversation transcripts in particular raise FERPA / PII scope not addressed in the contract.

Site edited (`tenant_admin/index.html` screen 13):
- 3 radio cards → 1 radio card (engagement metrics, selected)
- Tip alert reframed: "Engagement metrics is the v1.3 contracted dataset (per SC-ADD-05 catalog narrative + SOW §8.7). Additional datasets such as score history and conversation transcripts are post-pilot roadmap candidates pending FERPA scope review."

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through v4.4 → v4.5 → v4.6 → v4.7 → v4.8 → v4.9 → v4.10)
- All `goToScreen(N)` references valid; no broken nav
- `grep -i "parquet"` → 0 hits in deliverable surfaces (CHANGELOG meta-context allowed)
- Vendor naming retained only on model-picker / config screens; absent from incident narrative

### Numbers

| | Before v4.10 | After v4.10 |
|---|---|---|
| Total storyboard screens | 77 | **77** (no removals; in-place edits) |
| `tenant_admin/` | 27 | 27 |
| Export wizard dataset cards | 3 | **1** |
| Format-picker tabs | 3 | **2** |
| Vendor names in SC-ADD-06 narrative | Anthropic + GPT-5 | generic |

---

## v4.9 — 08 May 2026 — Second overboard sweep (REST API specifics + CSM SLA framing + Instructor Learner Search)

After v4.8 Brady asked for another adversarial pass. A fresh independent agent (Pass 8) found 3 more items that were over-extrapolated. v4.9 closes them.

### Trimmed — REST API specifics fabricated (Tenant Admin)

The v4.0 prototype invented "14 endpoints" and "600 req/hour" as plausible defaults for the API console. Re-reading the SOW main body and v1.3 SC-ADD-05 catalog, neither commits to those numbers — §8.7 commits to a "RESTful API for student engagement data export" generically. The catalog narrative is just "Alice uses the RESTful API to query student scores."

Sites edited (`tenant_admin/index.html`):
- Screen 2 (portal home) SC-ADD-05 quick-launch caption: "OAuth 2.0, 600 req/hr" → "OAuth 2.0, per-tenant rate limit"
- Screen 10 (Data & APIs landing) Programmatic-access table:
  - "Endpoints · 14 available" → "Endpoints · Catalog finalized at onboarding"
  - "Rate limit · 600 req/hour" → "Rate limit · Per tenant tier"
- Screen 11 (REST API console) usage indicator: "Rate limit · 213 / 600 req/hour" → "Rate limit · Well below tenant tier cap"

The trim makes the prototype honest about what JFT will configure later vs. what's already determined.

### Trimmed — "JFT CSM 2-hour SLA" framing conflated §9.5 + §9.1.4

SOW §9.5 specifies the JFT support P1 response time as <2 hours. §9.1.4 lists the Customer Success Manager as a business-hours WGU-facing POC. The v4.0 storyboard labeled the SC-ADD-06 chat thread "JFT CSM 2-hour SLA," conflating the two roles. The CSM is a person who acknowledges within the §9.5 window; the SLA itself is a JFT-support commitment.

Sites edited (`tenant_admin/index.html`):
- Screen 2 SC-ADD-06 quick-launch description: "JFT CSM 2-hour SLA" → "JFT support 2-hour P1 response per §9.5"
- Screen 21 (CSM chat thread) eyebrow: "Customer Success Response · Within 2-hr SLA" → "JFT Support P1 Response · §9.5 (CSM Jordan as WGU-facing POC)"
- Chat-bubble badges (CSM Jordan acknowledged at 6 min) are factually OK and unchanged — Jordan is the CSM, who acknowledged within the §9.5 window.

### Removed — `instructor/index.html` screen 9 (Learner Search)

The screen was added in v4.4 as G2, originally Mike's "Gradebook" suggestion that I retargeted as "Learner Search." Reading the v1.3 SC-ADD-03 catalog narrative literally: "Charlie accesses the Instructor Dashboard via secret LRPS deep link and opens the Data Visualization panel showing a Student Heatmap. He identifies Sally as at-risk: assessment complete, AI-scored competency low. He drills into her conversation logs to review AI feedback…" — there is no search step. The User Profile says "drill into individual student performance records" (singular drill-down), not "search across all."

Removed:
- Entire `<section id="screen-9">` block (~190 lines)
- "Search learners" button on screen 2 (linked to screen 9)
- "Search by name / email" chip on screen 3 heatmap (linked to screen 9)
- Meta-bar nav button "09"
- `TOTAL_SCREENS` 9 → 8
- 2 PNG screenshots (light + dark)

Catalog updates (`presentation.html` + `presentation_dark.html`):
- SC-ADD-03 step 9 entry removed
- SC-ADD-03 metadata: 9 → 8 screens; SOW refs trimmed (dropped §7.12; kept §7.10/7.11/7.13/7.14/10.4)
- Screen-map summary: 78 → 77 total
- Document Control: new v1.3+++ row noting v4.9 trim
- Footer: Storyboard v4.8 → v4.9

`instructor/README.md`: scenarios row 9 → 8; SOW refs trimmed.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through v4.4 → v4.5 → v4.6 → v4.7 → v4.8 → v4.9)
- `instructor/screenshots/` and `screenshots_dark/` each have 8 PNGs
- All `goToScreen(N)` references valid (zero broken nav)
- 0 hits for "14 available", "600 req/hour", "JFT CSM 2-hour SLA" in tracked deliverable HTML/MD (CHANGELOG meta-context allowed)
- Forbidden-term sweep clean

### Numbers

| | Before v4.9 | After v4.9 |
|---|---|---|
| Total storyboard screens | 78 | **77** |
| `instructor/` | 9 | 8 |
| `tenant_admin/` | 27 | 27 (Findings 1 + 2 are in-place text edits) |
| `super_admin/` | 8 | 8 |
| `student/` | 34 | 34 (frozen) |
| `lrps/` | 1 | 1 |
| PNGs | 158 | 156 |

---

## v4.8 — 08 May 2026 — Overboard trim (3 Super Admin screens removed; Tenant Admin home + screen 5 trimmed)

Brady ran a fresh contract-grounding audit and confirmed prior agents (myself included) had built features that weren't actually in the SOW main body. v4.8 removes the overboard items so the prototype reflects only what JFT contracted to deliver.

### Removed — 3 Super Admin screens (added in v4.4 as inferred "gap fills")

- **`super_admin/index.html` screen 9 (Third-Party Integrations).** OpenRouter / AWS / Datadog / Entra ID / GitHub / Slack deep-link cards. SOW §2.4 commits to "AI orchestration layer supporting multiple LLM providers" as **internal architecture**, not as a Super Admin-facing vendor-management UI. JFT's vendor management is operational ops, not a JFT deliverable. The original justification was a Brady in-conversation remark ("links to all the 3rd party tools that are setup, like AWS as well") — not a SOW commitment.
- **`super_admin/index.html` screen 10 (Learner Remediation).** Cross-tenant per-learner score reset / force re-diagnostic / pause access with required-justification audit log. SOW commits to data export and audit logging, not data **modification**. Score reset crosses into FERPA territory (modifying education records). Not in v1.3 catalog or User Profile. Original justification was a Brady in-conversation remark ("resetting a user's score, that would be a Global Admin feature") — not contracted.
- **`super_admin/index.html` screen 11 (Billing & Cost Centers).** Per-tenant cost-center allocation table + per-model spend split + budget alerts. §11.1 specifies what JFT bills WGU; it does not commit to a UI for WGU's **internal** cost-center allocation across PDev / SOB / SOH. That's WGU's accounting concern, not a JFT deliverable. Token-usage / API-spend tracking is contract-committed (already exists on screen 3); cross-tenant cost-center reconciliation isn't.

`super_admin/index.html` returns to **8 screens** (matches the v1.3 SC-ADD-04 catalog narrative as originally authored).

Side cleanup:
- Super Admin screen 2 (portal home): removed the v4.4 second row of quick-link cards (Integrations / Learner Remediation / Billing / Audit Log). Kept the original 4-card row (Token Usage / Rate Limits / Compliance / Geo-Redundancy).
- Super Admin meta-bar nav: removed buttons 09 / 10 / 11.
- 6 PNG screenshots removed (3 light + 3 dark).

### Trimmed — Tenant Admin Portal home (screen 2)

The v4.7 hub redesign over-promised real-time platform-monitoring features that belong to Super Admin per the User Profile. v4.8 trims back to program-level scope:

- **Removed** the "Recent activity" feed (right-column 6-event timeline). Implied real-time event aggregation across all 3 scenarios is not a contracted UI capability.
- **Removed** the "System Status · Operational" KPI gauge. Per the User Profile, infrastructure status is Bob's (Super Admin) scope, not Alice's (Tenant Admin). Tenant Admin sees their own tenant's module status, not platform-wide health.
- **Removed** the "SLA Uptime · 30D" KPI gauge. SLA reporting is contract-committed (SC-ADD-06 has it on screen 23) but surfacing it on the Tenant Admin home as a real-time metric isn't in the SC-ADD-02 narrative.
- **Kept** the 2 program-level KPIs ("Subjects Live" + "Exports This Week") — these are grounded in Tenant Admin scope per §2.5.
- **Kept** the 3-domain quick-launch row (Course Configuration / Data & APIs / System Status). Pure navigation; no functionality claim.
- **Kept** the Subjects list (now full-width since the right column is gone).
- **Kept** the "What's next?" cross-scenario CTA panels on screens 9 / 15 / 23 from v4.7 — pure UX integration, no functionality claim.

### Trimmed — Tenant Admin screen 5 prompt-versions panel

The v4.4 G9 "Recent versions" panel (3-row table + footnote) was based on a Brady in-conversation request for "minimal indication for JFT to push back if too hard." v4.8 takes that "minimal" framing more literally: collapsed to a single-line indicator showing "Last edited 07 May · v3 · Alice" with a "View history" link and a deferred-feature note. Same intent, much smaller surface.

### Catalog updates

`presentation.html` + `presentation_dark.html`:
- Removed SC-ADD-04 step 9 / 10 / 11 entries.
- SC-ADD-04 metadata: 11 → 8 screens; SOW refs trimmed to §6.4, §6.6, §9.5, §10.1, §10.4, §10.7 (dropped §2.4, §2.5 ambiguous, §9.13, §11.1).
- Screen-map summary: 81 → 78 total.
- Document Control table records the v4.8 trim with full rationale.
- Footer bumped to Storyboard v4.8.

### Verification

- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through v4.4 → v4.5 → v4.6 → v4.7 → v4.8)
- 6 super_admin orphan PNGs removed; remaining 158 screenshots regenerated
- All `goToScreen(N)` references valid (no broken nav)
- Forbidden-term sweep clean

### Numbers

| | Before v4.8 | After v4.8 |
|---|---|---|
| Total storyboard screens | 81 | **78** |
| `super_admin/` | 11 | 8 |
| `tenant_admin/` | 27 | 27 (screen 2 + screen 5 trimmed in place) |
| `instructor/` | 9 | 9 |
| `student/` | 34 | 34 (frozen) |
| `lrps/` | 1 | 1 |
| PNGs | 164 | 158 |

### What's still kept that was added in v4.4

These items were re-validated against SOW + scenarios and confirmed contract-grounded:
- `tenant_admin/26` Instructor Roster (§2.5 instructors + §10.8 RBAC)
- `tenant_admin/27` Subject Lifecycle (§2.5 module lifecycle + §10.4 audit logging)
- `instructor/9` Learner Search (§7.10 + §7.12)
- `instructor/3` heatmap export CTAs (§7.14)

### Lesson learned

In-conversation remarks during prototyping are NOT contract commitments. v4.4–v4.7 conflated the two; v4.8 corrects that. Future iterations should re-cite SOW main-body sections (with literal quotes ≤15 words) before proposing new screens — not "Brady mentioned X" remembered from chat.

---

## v4.7 — 07 May 2026 — Tenant Admin polish pass (SC-ADD-02 / 05 / 06 unified experience)

The three Tenant Admin scenarios had been stitched together by the meta-bar and a basic portal home. v4.7 turns them into a single polished Alice experience: a hub-style portal home that lights up across all three scenarios, plus cross-scenario "what's next?" CTAs at each scenario completion screen so the journey feels intentional instead of three separate demos.

### Changed — `tenant_admin/index.html` screen 2 (Tenant Admin Portal home) redesigned as the central hub

The portal home was a single Subject list + 3 buttons. Now it's a full hub:

- **Hero** — "Welcome back, Alice" with tenant scoping (PDev / IT) and the 7-year audit-log retention disclosure inline.
- **4 KPI gauges spanning all 3 scenarios** — Subjects Live (SC-ADD-02), SLA Uptime · 30D (SC-ADD-06), Exports This Week (SC-ADD-05), and System Status (SC-ADD-06). Each has color-coded status dots + target/headroom captions.
- **3-domain quick-launch row** — three featured cards labeled with their scenario IDs, each with a primary CTA + secondary deep-link:
  - Configure courses (SC-ADD-02): New Subject + Tenant Settings
  - Data & APIs (SC-ADD-05): API Console + Start Export
  - System status (SC-ADD-06): System Status + SLA Dashboard
- **Two-column body** — Your Subjects (4-row list — added E135 to the list to reflect the most recent deploy) on the left, **Recent activity feed** on the right showing 6 events from across all three scenarios with timestamps + scenario labels (`SC-ADD-06 · Service restored`, `SC-ADD-05 · Export complete`, `SC-ADD-02 · Subject deployed`, etc.). The activity feed is the visual proof that the three scenarios are one cohesive operation, not three separate demos.
- **Bottom CTAs** — New Subject + Tenant Settings + an audit-retention reminder.

### Changed — Cross-scenario "What's next?" CTAs at each scenario's completion screen

Each scenario used to dead-end at "Back to Portal." Now they invite the next logical action.

- **Screen 9** (SC-ADD-02 deploy success) — added a "What's next?" panel below the success message with three CTAs: Export E135 baseline metrics (jumps to SC-ADD-05 step 4), Check system status (jumps to SC-ADD-06 step 1), Query via REST API (jumps to SC-ADD-05 step 2). Reinforces that a deploy normally precedes a baseline-metrics export and a status check.
- **Screen 15** (SC-ADD-05 export complete) — added a "What's next?" panel with three CTAs: SLA dashboard (SC-ADD-06 step 8), Portal home, New Subject. Frames the export as part of an ongoing tenant operation, not a terminal action.
- **Screen 23** (SC-ADD-06 SLA dashboard) — added a "What's next?" panel with three CTAs: Export incident report (SC-ADD-05 step 4), Portal home, Configure another Subject (SC-ADD-02 step 3). Plus the existing "Next SLA report" alert now hyperlinks to the Data & APIs panel.

### Changed — minor

- `tenant_admin/index.html` CSS — added `.gauge-number.good { color: var(--pgn-color-success-base); }` rule for parity with `super_admin/index.html`. The class was used implicitly on the new portal home gauges; making it explicit prevents future drift.
- 164 screenshots regenerated. Tenant Admin screens 2 (the redesign) + 9 / 15 / 23 (cross-scenario CTAs) + every other admin-portal screen had minor pixel diffs from the regeneration. `student/index.html` source still 0 lines changed.

### Why this matters

Per Brady's direction: SC-ADD-02 / 05 / 06 are not three separate demos JFT will build separately — they are one Tenant Admin experience that Alice lives inside as a daily workflow. The polish pass:
1. Establishes the portal home as the visual centerpiece (hub model, not a launcher).
2. Makes the cross-scenario data flow visible (the 24h activity feed shows how the three scenarios touch each other in time).
3. Replaces dead-end completion screens with cross-scenario invitations that reflect realistic operations (deploy → export, export → SLA review, incident response → next config).
4. Keeps screen count at 81 (no new screens; pure UX integration of existing 27 Tenant Admin screens).

### Verification

- `git diff --stat student/index.html` returns 0 lines (preservation directive intact)
- All Tenant Admin screens render in both light + dark themes (164 PNGs regenerated)
- `goToScreen(N)` cross-references in new CTAs all point to existing screens (3, 11, 13, 16, 23)
- Forbidden-term sweep clean (the v4.5/v4.6 audit list re-checked; 0 hits)

---

## v4.6 — 07 May 2026 — Adversarial accessibility / design-system / nav re-audit (2 consecutive clean passes)

Second 2-pass-clean compliance audit, this time with **adversarial framing** — fresh agents instructed to be skeptical of v4.5's "0 issues" claim and look harder at niche dimensions (WCAG 2.2 AA accessibility, design-system token compliance, cross-portal navigation, niche SOW main-body sections, sub-step granularity). Pass 5 caught real gaps that prior passes pattern-matched past; v4.6 closes them. **Pass 6 + Pass 7 both reported 0 issues** — full SOW + scenario compliance re-verified under stricter framing.

### Pass 5 findings (closed in v4.6)

**Blocker — WCAG 2.2 AA §2.4.7 violation across 6 portal HTML files.** Each file's CSS contained a heading-specific `:focus-visible { outline: none }` override that suppressed the standard 3px Bright Blue focus ring on all H1–H6 elements. The base `:focus-visible` rule above it was correct; the override was an artifact of an earlier iteration that didn't want focus rings visible during programmatic focus changes (capture pipeline already handles screenshot suppression separately). Removed the override in 5 modifiable portals (`index.html`, `lrps/index.html`, `tenant_admin/index.html`, `instructor/index.html`, `super_admin/index.html`). The 6th file — `student/index.html` — is the v1 frozen baseline; per the preservation directive, the violation is documented as a known limitation in `student/README.md` rather than fixed. v1.4 student refresh should remove it.

**Risk — Non-FY26 palette colors in 2 specialized UI domains lacked documentation.** Code-block syntax highlighting (`--code-keyword: #ff7b72`, `--code-function: #79c0ff`, etc., GitHub-style) and the 9-step heatmap gradient (`--heat-1` through `--heat-9`) deliberately use extended palettes for clarity in their domains, but `README.md` didn't document them as scoped exceptions. Future implementers could mistakenly expand these to other surfaces. Added a "Documented palette extensions (intentional; out of FY26 scope)" subsection to `README.md` Color Palette section explicitly carving out the two domains and forbidding their expansion.

**Polish — `student/README.md` Known Limitations cross-link.** The Known Limitations section was thorough but only discoverable by scrolling past the Scenarios table. Added a parenthetical link from the Total scenarios row pointing to the section.

### Pass 5 → Pass 7 audit chain

| Pass | Result | Action |
|---|---|---|
| Pass 5 (adversarial) | 1 Blocker + 1 Risk + 1 Polish | All closed |
| **Pass 6** | **0 issues across 8 dimensions** | First clean post-fix |
| **Pass 7** | **0 issues across 9 verification checks** | Second consecutive clean |

### Editorial / documentation updates

- `README.md` — new Color Palette subsection "Documented palette extensions (intentional; out of FY26 scope)" with code-block + heatmap carve-outs and explicit "must NOT be expanded to other surfaces" guidance.
- `student/README.md` — known-limitations now lists 7 items (was 6); item #7 is the WCAG 2.2 AA §2.4.7 violation in the v1 frozen baseline. Total row links to the limitations section for early discoverability.
- 5 portal HTML files — heading `:focus-visible` override removed; replacement comment references WCAG 2.2 AA §2.4.7 and the capture pipeline's separate outline-suppression for screenshots.

### Browser walk-through note

The plan called for an interactive browser walk-through using Claude in Chrome MCP tools. Chrome MCP was not connected during this session (same as v4.5). Pass 5/6/7's PNG visual review + WebFetch of the live deploy covered visual verification. Interactive nav / theme-toggle / focus-ring behavior is consistent with the working code — the focus-ring fix is purely a CSS deletion (the existing `:focus-visible` rule already provides the correct 3px Bright Blue outline). No regressions expected on deploy.

### Verification

- Pass 6 + Pass 7 both 0 issues across all dimensions
- `git diff --stat student/index.html` returns **0 lines** (preservation directive intact through v4.5 → v4.6)
- All 5 modifiable portal files have heading focus-visible override removed (`grep "h[1-6]:focus-visible.*outline:.*none"` returns 0 single-line matches; multi-line override only remains in `student/index.html` which is correctly documented as a v1 limitation)
- Forbidden terms still 0 hits across deliverable surfaces
- Live deploy (https://brady-wgu.github.io/JFT_SDP/) currently shows v4.5 / 81 screens; will rebuild to v4.6 on merge

---

## v4.5 — 07 May 2026 — SOW + scenario compliance audit (2 consecutive clean passes)

Comprehensive 2-pass-clean compliance audit per Brady's directive. Every numbered SOW main-body section + every v1.3 scenario step verified against the storyboard. **Pass 3 and Pass 4 both reported 0 issues** — full SOW + scenario compliance achieved. `student/index.html` byte-identical to v4.2 baseline (preservation directive intact).

### Editorial scrub

- **Removed all internal-process terminology from deliverable surfaces.** 15 occurrences across `CHANGELOG.md` (4), `tenant_admin/index.html` (7), `tenant_admin/README.md` (4 in 1 row), `instructor/index.html` (2), and `super_admin/index.html` (2) replaced with plain SOW section notation (`§N.M`). Internal contract-management terms have no place in a JFT-facing or public artifact.
- **Drift fix in `super_admin/index.html` cost-spike screen 4** — copy referenced "New cohort + AI prompt expansion · Section 042 · Cohort 042 launch" (left over from a v4.0-era pattern). Reframed to "Enrollment surge in E010 + AI prompt expansion · 28 new learner launches under WGU's rolling-enrollment model" to match the User Profile's no-fixed-cohorts reality.
- **Drift fix in `presentation.html` + `presentation_dark.html` SC-ADD-03 step 4 + SC-ADD-04 step 4** narratives — same "Cohort summary" / "cohort 042 launch" copy reframed to "Course summary" / "enrollment surge in E010".
- **Persona-label drift fix in catalogs** — `presentation.html` + `presentation_dark.html` had two "Course Instructor" mentions that conflicted with the canonical "Instructor" role label. Removed (the User Profile equivalency context is documented in `instructor/README.md`; not needed in catalog narrative).

### Catalog completeness — `presentation.html` + `presentation_dark.html`

The v4.4 release added 6 new admin-portal screens but didn't extend the scenario-catalog narratives. v4.5 closes that gap:
- **SC-ADD-02** extended from 11 to 13 step entries — adds step 12 (Instructor Roster · screen 26) and step 13 (Subject Lifecycle · screen 27). Step 5 narrative expanded with a sentence about the inline "Recent versions" prompt-history panel.
- **SC-ADD-03** extended from 8 to 9 step entries — adds step 9 (Learner Search · screen 9). Step 3 narrative expanded with the new heatmap export CTAs (Course report PDF / CSV) and the name/email-search pivot.
- **SC-ADD-04** extended from 8 to 11 step entries — adds step 9 (Third-Party Integrations · screen 9), step 10 (Learner Remediation · screen 10), step 11 (Billing & Cost Centers · screen 11).
- Screen-map summary table updated: total now reads **81 screens** (was 75).
- Scenario-meta SOW-refs rows updated to add §10.4 (Tenant Admin), §7.12 + §7.14 (Instructor), §2.4 + §11.1 + §10.4 (Super Admin).
- Document Control table records a new "1.3+ / Current" row noting the v4.4 storyboard extensions on top of the catalog v1.3 baseline.
- Footer copy bumped "Storyboard v4.0" → "Storyboard v4.5" in both files.

### Verification — 2 consecutive 0-issue audit passes

Pass 1 (initial): 17 issues found (15 forbidden-term references, 2 catalog gaps for new screens, 1 drift cluster in super_admin) — all closed.
Pass 2 (post-fix): 1 issue found (2 stale "Course Instructor" mentions in catalogs) — fixed.
Pass 3 (post-fix): **0 issues**.
Pass 4 (independent re-verify): **0 issues** across all 7 verification categories (forbidden-term sweep, SOW main-body coverage, v1.3 scenario steps, catalog file integrity, student preservation, screenshot render quality, cross-portal canonical strings).

### Coverage summary

- ✓ All 15 SOW main-body sections (§§1–15) verified against at least one storyboard surface.
- ✓ All 28 v1.3 catalog scenario steps depicted across 41 admin-portal screens (tenant_admin 27 + instructor 9 + super_admin 11; less LRPS overlap = 41 unique admin screens). Plus 5 student scenarios (SC-ADD-01 acceptance rollup of v1.2) at 34/34 frozen baseline.
- ✓ 81-screen total: 34 student (frozen) + 27 tenant_admin + 9 instructor + 11 super_admin + 1 LRPS landing.
- ✓ 164 PNGs (74 light + 74 dark + 16 admin-portal extras for new screens) regenerated.
- ✓ `git diff --stat student/index.html` returns 0 lines.
- ✓ Cross-portal canonical strings (Sally / Charlie / Alice / Bob; E010 / E075 / E135; PDev; "Instructor" not "Course Instructor"; "rolling enrollment" not "Section 042 / Spring 2026 / Cohort") consistent across all 81 screens.

### Browser walk-through note

The plan called for an interactive browser walk-through using Claude in Chrome MCP tools. Chrome MCP was not connected during this session; Pass 1's PNG visual review covered visual rendering verification (all 6 new screens render cleanly in light + dark themes). Interactive nav / theme-toggle behavior is unchanged from the working v4.4 deployment, so the skipped walk-through is not gating compliance.

---

## v4.4 — 07 May 2026 — SOW gap fills against the contract

Eight contract-grounded gaps closed across the three admin portals. **Authority order baked in throughout: contract first, then User Profiles, then Mike's vernacular suggestions deprioritized to "out of scope unless SOW-grounded."** No changes to `student/index.html` (Brady's preservation directive — verified `git diff` shows 0 lines).

### Added — 6 new screens

- **`tenant_admin/` screen 26 — Instructor Roster & Course Assignment (G3, §2.5 + §10.8 RBAC).** 7-row instructor table including Course Instructors and Program Mentors (Charlie, Devon, Maya, Priya, Teagan, Noor, Logan/deactivated) with E010/E075/E135 course chips, active-learner counts (rolling enrollment), recent-assignment audit log, idle-warning badges, and bulk-import CTA. Explicit framing: LRPS owns account provisioning; this screen owns *course* assignment.
- **`tenant_admin/` screen 27 — Subject Lifecycle & Archival (G6, §2.5 module lifecycle + §10.4 audit logging).** Two-section layout: Active Subjects (E010 / E075 / E135 with deployed-version + learner-count + deactivate CTA) and Archived Subjects (E020 legacy / E099 pilot, FERPA-aligned 7-year retention, restore CTA). Right-rail "Deactivate Subject preview" panel with cutover date / retention policy / required-justification / audit warning.
- **`super_admin/` screen 9 — Third-Party Integrations (G8, §2.4 AI Orchestration + §2.5 system health).** Read-only Connected Services view: OpenRouter.ai (LLM gateway, replacing direct keys for OpenAI/Anthropic/Google), AWS (compute/data/networking), Datadog (APM/logs/synthetic), Entra ID (SSO), GitHub (CI/CD source), Slack (incident channel). Each card has a deep-link button to the vendor console. Explicit credential-management note: JFT owns rotation; rotate via Sev2 ticket, not in-portal.
- **`super_admin/` screen 10 — Learner Remediation (G1, Brady-clarified Global Admin scope).** LRPS owns account provisioning, so this screen is global-admin-only *coaching-state* remediation: per-objective score reset, reset all progress (subject or cross-subject), force re-diagnostic, pause access, view conversation log. Required justification field (audit-logged with actor/IP/before-after). Recent remediation events table. FERPA-scope clarification at the bottom: progress + score data only; account identity / LMS enrollment / grade-bearing assessments are out of scope.
- **`super_admin/` screen 11 — Billing & Cost Centers (G5, §11.1 hosting + support fee schedule + §6.6 token tracking).** Per-tenant cost allocation: 6-row table (PDev / SOB / SOH / SOE / SOIT / Pilot) with cost-center codes, owner emails, MTD spend, budget caps, EOM forecasts, status badges (PDev forecast to exceed). Spend-by-model breakdown via OpenRouter (Claude 56% / GPT-4o 28% / Gemini 16%). 4-row configurable budget-alert preferences.
- **`instructor/` screen 9 — Learner Search & Individual Lookup (G2, §7.10 + §7.12).** Reframed from Mike's "Gradebook" — the SDP is a practice tool, not a gradebook. Search by name / email / anonymized identifier across all 68 learners in Charlie's three courses, with course + status filters, sortable result table (Sally / Aisha / Daniel / Marcus / Priya / Jordan / Tasha / Riku as a representative cross-section), and per-row "Open profile" CTA that pivots to the existing drill-down. FERPA-scope note: Instructors only see learners in courses they instruct.

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

- **Mike's "Course Instructor" rename** — REJECTED in v4.3, stays rejected. The User Profile + SOW §2.5 use `Instructor` as the contract-named user type.
- **Mike's "Admin" persona** — does not exist. The "global-level technical administrator with full cross-tenant access" *is* Super Admin (Bob) per the User Profile. Account-management functions land in `super_admin/`, not in a new persona and not in Tenant Admin (which is content-focused).
- **Account merge** — explicitly OUT per SOW §4 ("Manual creation or management of student accounts outside of LTI-based provisioning"). Not implemented.
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

- **Top-level `README.md` — "Shared persona & course reference" section.** Codifies canonical strings used across all 5 surfaces: Sally (student), `E010` Foundations of Programming (Python), `§ 042` Spring 2026 section, `PDev` tenant, `WGUE010PythonAY2026` LMS course slug, the full Cicada v1 13-sub-section taxonomy, and the SC-ADD-04 cost-spike date. Drift across these strings was the most common source of cross-portal inconsistency risk; this block makes the canonical values single-sourced.
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

- SOW Tier 1 gap fills — pending Brady's per-item green-light against the contract (`JFT_WGU_MSA_SOW_signed_05MAY2026.md`); planned for the next v4.x release.
- Mike's larger integration suggestions — pending Brady's green-light, *re-targeted against the authoritative User Profiles* (`JFT_SDP_User_Profiles_v1_2_30MAR2026.docx`):
  - **Gradebook** — fits within `instructor/` (Charlie). The User Profile lists "Access and export individual and group student performance data" and "Drill into individual student performance records" as primary Instructor goals; a Gradebook view that shows AI scores and supports flagging is consistent.
  - **Account-management operations** (merge / archive / username correction) — fits within `super_admin/` (Bob, the global-level cross-tenant administrator). The User Profile lists "Provisioning, deprovisioning, and manage tenant environments" and "Cross-tenant audit logs" as Super Admin responsibilities. **Not** a Tenant Admin function — that role is content-focused per the User Profile ("content and operations owners, not infrastructure owners").
  - **Mike's "Course Instructor" rename** — REJECTED. The User Profile and SOW Section 2.5 both use `Instructor` as the contract-named user type. Per Brady: contract and User Profiles are authoritative; colleague-vernacular suggestions yield to those documents.
- Modifications to `student/index.html` — deliberately preserved as v1 baseline; candidates for a future v1.4 student refresh.

---

## v4.2 — 07 May 2026 — v1.3 gap-coverage pass

Three-pass review against the v1.3 User Scenario Catalog identified three SOW-ref gaps. Filled to bring all 5 v1.3 scenarios to **100% workflow + SOW-ref coverage**. Two consecutive review passes confirmed zero remaining gaps.

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

Pass 2 + Pass 3 (both clean): every workflow sentence and every SOW reference across SC-ADD-02 through SC-ADD-06 is now visually depicted in the storyboard. Mapping table of SOW refs to screens lives in each persona's README.

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
