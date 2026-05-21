# Changelog

All notable changes to the SkillProof storyboard. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

The repo's storyboard version (`Storyboard vN.M`) tracks the visual prototype, not the underlying SkillProof product version that JFT is building. The SkillProof product follows the user scenario catalog versions (v1.2 MVP, v1.3 Additional, etc.).

This is a prototype repo — entries below cover the active JFT meeting follow-up phases (v4.69 – v4.81). Earlier history exists in git but isn't tracked here.

---

## v4.109 — 21 May 2026 — S8 Audit Trail walkthrough + cross-platform chip-filter rollout + "no LO-aggregate data" rule + "Capture integrity" removal

Three threads landed:

### Thread 1: S8 Audit Trail walkthrough (S8-01 through S8-06)

- **S8-01** Removed "Sample design only" banner.
- **S8-02** Expanded breadcrumb to **`Dashboard › E010 › Python Skill › Sally › Session 09 › Audit Trail`** (6 levels, full Course + Skill context — matches the S7 expansion).
- **S8-03** Renamed column header **"Timestamp (UTC)" → "Date"** (values were already date-only since v4.99 — header was lying to the user).
- **S8-04** Stat tile label **"Learning Objective misses" → "AI evaluation misses"** (Brady's "no LO-aggregate-data" principle).
- **S8-05** Moved bottom buttons into the in-flow `.floating-actions` block (consistent with S2/S3/S5/S6/S7).
- **S8-06** Standardized **Source column** to `[Actor type]: [Identifier]` — e.g., `AI: SkillProof Coach`, `Learner: Sally (198.51.x.x)`, `Model: Anthropic Claude Sonnet 4.5`, `Guardrail: SkillProof Coach`.

### Thread 2: "No Learning Objective-level data in aggregate" — new global rule

Brady (21 May 2026): *"No learning-objective-level data. Stop suggesting we keep that level of detail because most students will never have data across all learning objectives, only across topics consistently."*

- **S8 stat tile** renamed "Learning Objective misses" → "AI evaluation misses".
- **S7 description** updated: "3 Learning Objective misses" → **"3 AI evaluation misses"**.
- The per-message **"Feedback · objective miss"** badge inside the actual transcript chat thread (S7) **stays** — it's event-level AI evaluation feedback at the moment the AI judged a turn, not aggregate LO data.

### Thread 3: "Capture integrity" removal (platform-wide)

Brady (21 May 2026): *"I have no idea what that means at all or what that tells the instructor. Remove 'Capture Integrity' entirely from all UIs across the platform."*

- **S8** stat tile "1.00 Capture integrity" — removed.
- Cross-platform grep confirmed no other instances of "Capture integrity" across student, instructor, tenant_admin, super_admin, help portals.

### Thread 4: Chip-filter rollout — multi-portal pass (partial)

Brady (21 May 2026): *"Add filter chips to all tables globally. This works well on the screens we have already reviewed, so apply them to the entire platform for all tables."*

New filters added in this pass:

| Surface | Filter chips | Categories |
|---|---|---|
| **Instructor S5** Sally Per-Topic table | All Topics (13) · Coached since diagnostic (5) · Diagnostic only (8) | `data-topic-cat` |
| **Instructor S6** Coaching sessions | All sessions (9) · Diagnostic (1) · Coaching (8) | `data-session-cat` |
| **Instructor S8** Audit event log | All events (47) · AI events (12) · Learner submissions (18) · Model invocations (9) · Guardrails (8) | `data-event-cat` |
| **Super Admin S9** Access Control · People tab | All (8 of 187) · Super Admin (2) · Tenant Admin (2) · Instructor (2) · Student (2) | `data-user-cat` |

Existing chip-filtered tables (unchanged):
- Instructor S1 cross-Course at-risk roster (v4.96)
- Instructor S3 Topic mastery heatmap (v4.97)
- Instructor S4 At-risk mini-heatmap (v4.98)
- Instructor S7 Transcript message filter (v4.108)

New reusable helper added: `chipFilterTable(scopeSelector, filterValue, dataAttr, chipAttr)` in both instructor and super_admin portals — factors out the duplicated logic across screen-specific wrapper functions. JFT can reuse this for production tables.

**Deferred to follow-up commit** — partial pass only:

| Portal | Tables not yet filtered | Reason |
|---|---|---|
| Super Admin S9 | Skills tab (31 rows), Schools tab (4 rows) | Skills tab worth doing next; Schools tab is only 4 rows so chip-filter has low value |
| Super Admin S4 | Per-school cost breakdown (4 rows) | Only 4 rows; chip filter would have 1-2 items per chip |
| Super Admin S10, S11, S12, S13 | Various operational/Skill-management tables | Need per-screen judgment on chip categories |
| Tenant Admin | Skill builder LO tables (×4), Skill lifecycle, activity log, Settings tables | Each table needs context-specific chip categories |
| Student portal | Progress Map detail rows | Re-evaluate after student walkthrough |

All deferred tables documented as the natural next pass; they're not skipped permanently.

### Live verification

- **S5** filter "Coached since diagnostic" → 5 visible ✓
- **S6** filter "Diagnostic" → 1 visible ✓
- **S8** filter "Learner submissions" → 3 visible ✓
- **S8** stats: 4 tiles (47 Messages · 3 AI evaluation misses · 5 AI escalations · 0 Events dropped) — Capture integrity removed ✓
- **S8** breadcrumb: 5 links + current page (6 levels) ✓
- **S8** column header: "Date" (was Timestamp UTC) ✓
- **S8** Source: "AI: SkillProof Coach" / "Learner: Sally (198.51.x.x)" / "Model: Anthropic Claude Sonnet 4.5" / "Guardrail: SkillProof Coach" ✓

### Storyboard stamp

v4.109 instructor + super_admin portals. Tenant admin + student portals stay at v4.107.

---

## v4.108 — 21 May 2026 — S7 Conversation Transcript walkthrough complete

Resolves S7-01 through S7-07 per Brady's verdicts.

### What changed

- **S7-01** Removed "Sample design only" banner.
- **S7-02** Added in-flow `.floating-actions` block at the bottom-right: **"Back to Conversation logs"** → S6.
- **S7-03** Expanded breadcrumb from `Dashboard › Sally › Logs › Session 09` to **`Dashboard › E010 › Python Skill › Sally › Session 09`** (5 levels, full Course + Skill context). Removed the "Logs" intermediate — the Back button covers immediate-parent navigation.
- **S7-04** Trimmed description: dropped redundant "AI feedback panels shown inline" (already in description) → **"All 47 messages captured by the Audit Trail. AI score 0.15 · 5 feedback panels · 3 Learning Objective misses."**
- **S7-05** Reorganized eyebrow: removed counts (5 feedback panels, 3 Learning Objective misses) → moved into description. Eyebrow now reads **"Session 09 · 06 May 2026 · Data Structures: Lists, Tuples, Sets, Dictionaries"** (Topic-level context only).
- **S7-06** Replaced LO reference "Lists & comprehensions" with the canonical Topic name **"Data Structures: Lists, Tuples, Sets, Dictionaries"** in the eyebrow. Brady's directive: *"Topics are what we show the Instructor in detail, not the learning objectives."*
- **S7-07** Added a chip-filter bar above the chat thread:
  - **All messages (47)** — default active
  - **AI feedback only (5)** — hides learner-side bubbles; shows AI prompts/feedback/reframes
  - **Objective misses only (3)** — shows only AI feedback bubbles with the "objective miss" badge
  - Each chat-row now has `data-msg-type` attribute: `prompt`, `learner`, `feedback-miss`, `reframe`
  - New JS function `filterTranscript(filter)` toggles row visibility and chip active state

### Live verification

- Filter "Objective misses only" → 2 visible bubbles (matches the 2 feedback-miss data-msg-type rows; 1 more lives in the hidden 36 messages)
- Filter "AI feedback only" → 4 visible (3 AI feedback/reframe/prompt rows on the AI side)
- Filter "All" → 7 visible (all rows restored)
- Back button label: "Back to Conversation logs" ✓

### Note for JFT

The chat-row filter currently hides learner-side messages when "AI feedback only" is selected — this strips conversational context. Production may want a different pattern (e.g., scroll-to-next-miss with highlight, or a "show in context" toggle that keeps the surrounding turn visible). This is a prototype demo of the filter UX.

### Storyboard stamp

v4.108 instructor portal.

---

## v4.107 — 21 May 2026 — S6 Conversation Logs rewrite + platform-wide 0-1 scoring standardization

Two threads landed together: the S6 walkthrough verdicts (most of S6-01 through S6-09) and a cross-platform scoring scale change.

### Phase 1: S6 Coaching Sessions List rewrite

Resolves S6-01 through S6-09 per Brady's verdicts:

- **S6-01** Removed "Sample design only" banner.
- **S6-02** **All 9 rows clickable → S7** (was only session 09). `cursor: pointer` + onclick.
- **S6-03** Added in-flow **Back to Sally's profile** button → S5.
- **S6-04** Eyebrow "AI Coaching · Conversation logs" → **"Python Skill · Conversation logs"**.
- **S6-05** Removed the Audit column (every row was an identical "Captured" badge). Replaced with a footer note: *"All 9 sessions captured to the Audit Trail. View full event log on the Audit Trail screen."* (clickable → S8).
- **S6-06** Added upper-right Export group: **"Export Sally's Conversation Log"** + [PDF] + [CSV] following the v4.105 pattern.
- **S6-07** (modified per Brady) Removed the Outcome column entirely. AI score column carries the signal alone.
- **S6-08** Description trimmed: *"Most recent first. Click any row to read the full transcript."*
- **S6-09** (modified per Brady) Removed the Learning Objective column entirely. *"Too much information. The transcript is what tells the story to the instructor because not all Learning Objectives will be answered by the student unless they spend a lot of time using the Skill."*

Final table is 4 columns: Session · Date · Topic · AI score.

### Phase 2: Platform-wide 0-1 scoring standardization

Per Brady (21 May 2026): "The actual scoring by the LLM is zero-to-one scale, I believe. JFT knows how the code works, so they are already doing this point-to-percent translation somewhere, but my prototype UI needs to display this consistently at all levels and to all users."

**The new convention:** All scores display as 0.00–1.00 decimals (2 decimal places). Eliminates the 0-100 percent translation step JFT's UI was doing on top of the 0-1 data model.

**Implementation — instructor portal:**

- **New `standardizeScoresTo0to1()` JS function** runs on page load before `hydrateHeatmap()`. Targets:
  - `.score-pill` (S5 Per-Topic table = 13 cells, S6 sessions list = 9 cells)
  - `.heatmap-cell` (S3 = 195 cells, S4 = 52 cells)
  - `.section-stat-num` with `^\d+%$` pattern (S1 Course-card avg, S2 Skill-card avg)
  - Pure-integer guard so re-running doesn't double-transform
- **Hydrated heatmap cell tooltips** updated from "Score X/100" → "Score X.XX (of 1.00)".
- **S1 inline Skill rows** (6 instances across E010/E075/E135) — source edits: e.g., "76% avg Topic mastery" → "0.76 avg Topic mastery".
- **S3 description**: "AI-scored Topic mastery (0–100)" → **"(0.00–1.00)"**.
- **S3 legend bar** numbers: "0 25 50 75 100" → **"0.00 0.25 0.50 0.75 1.00"**.
- **S4 filter description**: "Topic mastery < 60" → **"< 0.60"**.
- **S4 summary card** rows: "Avg score (at-risk): 42.4" → **"0.42"**; "Mastery threshold: 80%" → **"0.80 (set by Alice)"**.
- **S7 description**: "AI score 15" → **"AI score 0.15"**.

**Implementation — student portal:**
- Baseline result header: "Overall 12%" → **"Overall 0.12"**.
- result-skill-score cells: "100%" → **"1.00"**, "0%" (×3) → **"0.00"**.
- pm-card-sub: "Completed · Score 100%" → **"1.00"**, "Score 0%" (×2) → **"0.00"**.

**Implementation — tenant_admin portal:**
- Form input "Overall Skill passing threshold": `min="0" max="100" value="70"` with `%` suffix → `min="0" max="1" step="0.01" value="0.70"` with "(0.00–1.00 scale)" hint. Default text "Defaults to 70%." → "Defaults to 0.70."
- Detail-table row "70%" → **"0.70"**.
- Skill-detail intro text now reads: *"Set the overall Skill passing threshold on the 0.00–1.00 scale..."*

**Sample verification (live runtime):**
- S1 E010 Avg Skill Score: `0.76` ✓
- S3 first heatmap cell (A.J. on Basic Syntax): `0.98` ✓
- S4 first heatmap cell (Sally on Basic Syntax): `0.62` ✓
- S4 Mastery threshold: `0.80 (set by Alice)` ✓
- S5 Sally first row (Basic Syntax & Data Types): `0.62` ✓
- S6 session 09 row: `0.15` ✓

### Note for JFT

The prototype source HTML now uses 0-1 displayed values directly (matching the underlying LLM data model). Where the JS hydrates from integer 0-100 stored in the markup, it's documented as a temporary prototype-time transformation; production should serialize 0-1 floats end-to-end and skip the conversion entirely.

### Storyboard stamp

v4.107 across instructor, student, and tenant_admin portals. Super admin + help unchanged (no scoring surfaces).

---

## v4.106 — 21 May 2026 — S6 Coaching Sessions List rewrite (Phase 1 of v4.107)

Folded into v4.107.

---

## v4.105 — 21 May 2026 — Platform-wide data-export button pattern: "Export [Context]" + format-only buttons in upper-right

Per Brady: "The label should say 'Export Python Skill Report' and then the 2 buttons are 'PDF' and 'CSV'. You should be able to derive this pattern and execute it across the platform in a similar manner so all these 'data export' features are displayed in a similar fashion across the platform, in the upper, right corner of the screen."

### The standardized pattern

```
<div class="d-flex justify-content-between align-items-start mb-3">
  <div><!-- eyebrow + h1 + description --></div>
  <div class="d-flex gap-2 align-items-center" style="flex-shrink:0; flex-wrap:nowrap; white-space:nowrap;">
    <span class="text-muted small">Export [Context Name]</span>
    <button class="btn btn-outline-primary btn-sm" aria-label="Export [Context] as PDF">
      <span class="material-icons-outlined">picture_as_pdf</span>PDF
    </button>
    <!-- one button per format: PDF · CSV · MD · JSON -->
  </div>
</div>
```

Rules:
- Label communicates **what's being exported** (e.g., "Export Python Skill Report", "Export Session 09 Transcript", "Export Session 09 Audit Log").
- Buttons are **format-only**: PDF, CSV, MD, JSON. Each has its own format-appropriate Material icon (picture_as_pdf, table_view, description, data_object).
- Every button gets a descriptive `aria-label` (e.g., "Export Python Skill Report as PDF") so screen readers hear the full intent.
- Group lives in the **upper-right of the screen**, inline with the H1 and eyebrow. Locked together via `flex-shrink:0` + `flex-wrap:nowrap` + `white-space:nowrap`.

### Applied to (instructor portal)

**S3 Skill heatmap**
- Old: "Export:" + button "Python Skill report (PDF)" + button "CSV"
- New: "Export Python Skill Report" + [PDF] + [CSV]

**S7 Conversation transcript**
- Old: 2 export buttons at the bottom alongside "View Audit Trail" — full label inside the button text ("Export transcript (PDF)")
- New: upper-right "Export Session 09 Transcript" + [PDF] + [MD]
- Old upper-right badges (47 messages captured, AI score: 15) folded into the description line: "All 47 messages captured by the Audit Trail · AI score 15 · AI feedback panels shown inline."
- Bottom row simplified to just "View Audit Trail"

**S8 Audit Trail**
- Old: 1 export button at the bottom ("Export full log (JSON)") between two navigation buttons
- New: upper-right "Export Session 09 Audit Log" + [JSON]
- Feedback-panel restructured into a flex-justify-between row with the panel on left and the Export group on right
- Bottom row simplified to just navigation (Back to transcript, Back to dashboard)

### Not changed in this pass

- **`super_admin` inline "Export" buttons** in tables (lines ~1019, 1594) — these are per-row inline actions, not screen-level exports. Different UX context.
- **`tenant_admin` "Export Reports" + "Export incident report (CSV)" buttons** — these are CTAs inside content cards, also inline rather than screen-level. Pattern doesn't fit directly. Flagged for a future pass if Brady wants in-card export buttons standardized.

### Storyboard stamp

v4.105 instructor portal.

---

## v4.104 — 21 May 2026 — S3 header: shorten description, keep PDF + CSV co-located

Per Brady: "This line is awkward on S3: '[the description text]' with the CSV button next to it. Reduce this descriptive text by 50% and update the placement of the CSV download button to be co-located with the Python Skill report button."

### What changed (S3 only)

- **Description text shortened ~50%**: was "Each cell shows a learner's AI-scored Topic mastery (0–100) for the Python Skill in E010. Topics refresh after every coaching session." (130 chars). Now: **"AI-scored Topic mastery (0–100) per learner. Updates after each coaching session."** (81 chars). Information density preserved; Skill+Course context is already in the eyebrow + breadcrumb above.
- **PDF + CSV buttons now lock together on one line**: the right-side Export container had `flex-wrap: wrap` which let the CSV button drop to a new row when the parent row got tight. Changed to `flex-wrap: nowrap` + `white-space: nowrap` + `flex-shrink: 0` so the Export label + PDF button + CSV button stay co-located as a single horizontal group regardless of the left-side text length.

### Storyboard stamp

v4.104 instructor portal.

---

## v4.103 — 21 May 2026 — Horizontal scroll discoverability: fade + scrollbar + hint label

Per Brady: "I like the scroll, but let's make it a little more obvious and clear that there is more to see. I don't want the user thinking there is nothing else to look at to the right of this viewport."

### Three complementary cues added to S3 + S4 heatmaps

1. **Right-edge fade gradient** — `.heatmap-scroll-container::after` pseudo-element renders a 56px-wide white→transparent gradient on the right edge. Signals visually that content is cut off. Fades out (`opacity:0`) when the user has scrolled to the right edge via JS-toggled `.at-end` class.
2. **Prominent brand-blue scrollbar** — `.heatmap-card::-webkit-scrollbar` styled 12px tall with `--pgn-color-brand-base` thumb. `scrollbar-color` set for Firefox. Visible affordance even when no scrolling has happened.
3. **Italic hint label below the heatmap** — pill-style block with `swap_horiz` icon, brand-blue text on brand-tint background: *"Scroll horizontally to see all 13 Topics — try the scrollbar below, shift + mouse wheel, or trackpad swipe"*. Educates users on the available scroll methods. Dims to 50% opacity when scrolled to right end.

### Wiring

- Wrapped both heatmaps in `<div class="heatmap-scroll-container">` (was `.heatmap-card` directly).
- Added `<div class="heatmap-scroll-hint" role="note">` as sibling below each `.heatmap-card`.
- New JS function `setupHeatmapScrollState(screenSelector)` listens for `scroll`, window `resize`, and uses `ResizeObserver` to recalculate when the heatmap first becomes visible (handles the display:none → visible transition when user navigates to S3 or S4). Toggles `.at-end` class on the container when `scrollLeft >= scrollWidth - clientWidth - 4`.

### Behavior

- On page load: fade gradient + hint at full opacity → signals "more to the right"
- User scrolls right: fade gradient stays visible until reaching the end
- Scrolled to right edge: fade gradient opacity goes to 0, hint dims to 50% → signals "you've seen everything"
- Viewport wider than 1580px (no scroll needed): `.at-end` is automatically added, so fade + dim are applied

### Storyboard stamp

v4.103 instructor portal.

---

## v4.102 — 21 May 2026 — S3/S4 heatmaps + S6 sessions expanded to 13 canonical Topics

Per Brady (21 May 2026): "Let's see what happens when you have many more topics. I would expect this to naturally maximize at ~20 topics, so 13 is a great average to visualize. Update those related heatmaps and session information now."

### CSS

`.heatmap-grid` grid-template-columns expanded from 4 to **13 columns**:
```css
grid-template-columns: 160px repeat(13, minmax(108px, 1fr));
min-width: 1580px;
```
Container's `overflow-x: auto` kicks in on smaller viewports for horizontal scroll. Designed to scale up to ~20 Topics per Brady's expected ceiling.

### S3 (Skill heatmap)

- Column headers: 4 action-statement labels → **13 canonical Topic names** matching the student portal taxonomy (Basic Syntax & Data Types · Control Flow & Logic · Functions & Modular Programming · Data Structures: Lists, Tuples, Sets, Dictionaries · Working with Files & I/O · Error Handling & Debugging · Object-Oriented Programming (OOP) · Python Libraries & Modules · Advanced Data Handling · Regular Expressions & String Manipulation · Working with Databases · Introduction to Automation · Introduction to Machine Learning).
- All 15 visible learner rows now have **13 cells each** (195 cells total). Score distributions per learner status:
  - Mastery (A.J., K.L., M.K., D.W.): scores 84–98 (h7–h9 darker greens)
  - On-track (P.A., J.T., R.M., E.G., N.B., L.O.): scores 63–82 (h5–h7 light greens)
  - Watch (T.V.): scores 54–68 (h3–h5 amber/transitional)
  - At-risk (Sally, B.F., C.S., H.D.): scores 15–62 (h1–h3 reds), with Sally's exact 13 values matching her S5 Per-Topic table

### S4 (At-risk mini-heatmap)

- Same column expansion: 4 → 13 canonical Topic names.
- 4 at-risk rows × 13 cells (52 cells total).
- Right-side summary card "Lowest Topic score" value updated from "Manipulates Data Structures" → **"Data Structures: Lists, Tuples, Sets, Dictionaries"** (canonical name).

### S6 (Coaching sessions list)

Topic column values updated from action-statement labels to canonical Topic names. Mapping based on each session's LO context:

| Session | Old Topic | New Topic |
|---|---|---|
| 09 | Manipulates Data Structures | Data Structures: Lists, Tuples, Sets, Dictionaries |
| 08 | Manipulates Data Structures | Data Structures: Lists, Tuples, Sets, Dictionaries |
| 07 | Identifies Python Constructs | Control Flow & Logic |
| 06 | Executes Python Code | Error Handling & Debugging |
| 05 | Creates Functional Programs | Functions & Modular Programming |
| 04 | Creates Functional Programs | Functions & Modular Programming |
| 03 | Executes Python Code | Basic Syntax & Data Types |
| 02 | Identifies Python Constructs | Basic Syntax & Data Types |
| 01 | Diagnostic | Diagnostic (all 13 Topics) |

LO column values (Lists & comprehensions, Define variables & types, etc.) stay unchanged — those were already LO-level and remain accurate within their canonical Topic.

### Canonical Topic taxonomy now consistent across

| Surface | Status |
|---|---|
| Student portal sidebar/snapshot | ✅ 13 Topics (canonical source) |
| S1 Dashboard (no Topic surface) | n/a |
| S2 Course view Skill cards | shows count "4 Topics" / "3 Topics" — count only, no names |
| **S3 heatmap (this commit)** | ✅ 13 canonical Topics |
| **S4 mini-heatmap (this commit)** | ✅ 13 canonical Topics |
| S5 Sally Per-Topic table | ✅ 13 canonical Topics (from v4.101) |
| **S6 sessions Topic column (this commit)** | ✅ Canonical Topic names |
| S7 transcript eyebrow | "Lists & comprehensions" — LO-level reference, accurate |

### Storyboard stamp

v4.102 instructor portal.

---

## v4.101 — 21 May 2026 — S5 Topic naming aligned to student-portal canonical taxonomy; all 13 Topics scored

Per Brady (21 May 2026): "It says the diagnostic assessment was completed, so all 13 topics should have scores and last attempts. Do not leave those rows blank. Also, use the actual topic names, you have those in the student storyboard view, those are not mysteries or in need of random generation."

### What changed (S5 only)

**Replaced all 13 Topic rows with the canonical student-portal Topic taxonomy**, and gave Sally a diagnostic-baseline score on every Topic. Diagnostic-only Topics show "30 Apr 2026" (diagnostic date); coached Topics show their last-coaching-session date.

| # | Topic | Score | Last attempt |
|---|---|---|---|
| 1 | Basic Syntax & Data Types | 62 | 01 May 2026 |
| 2 | Control Flow & Logic | 28 | 05 May 2026 |
| 3 | Functions & Modular Programming | 44 | 04 May 2026 |
| 4 | Data Structures: Lists, Tuples, Sets, Dictionaries | 22 | 06 May 2026 |
| 5 | Working with Files & I/O | 38 | 30 Apr 2026 |
| 6 | Error Handling & Debugging | 33 | 05 May 2026 |
| 7 | Object-Oriented Programming (OOP) | 41 | 30 Apr 2026 |
| 8 | Python Libraries & Modules | 25 | 30 Apr 2026 |
| 9 | Advanced Data Handling | 18 | 30 Apr 2026 |
| 10 | Regular Expressions & String Manipulation | 22 | 30 Apr 2026 |
| 11 | Working with Databases | 30 | 30 Apr 2026 |
| 12 | Introduction to Automation | 19 | 30 Apr 2026 |
| 13 | Introduction to Machine Learning | 15 | 30 Apr 2026 |

- Every Topic has a real score (no em-dashes, no "Not yet attempted") — consistent with "Diagnostic Complete: Yes" in the Profile card.
- Topics with continued coaching (#1, 2, 3, 4, 6) have last-attempt dates after diagnostic (30 Apr); the other 8 are at diagnostic baseline.
- **Profile card "Stuck on Topic"** updated from "Manipulates Data Structures" → **"Data Structures: Lists, Tuples, Sets, Dictionaries"** (matches table row #4, the canonical student-portal Topic name).

### Cross-screen alignment status (after v4.101)

| Screen | Topic naming convention | Reconciled to student-portal taxonomy? |
|---|---|---|
| **Student portal** (sidebar, progress map, snapshot) | Basic Syntax & Data Types, Control Flow & Logic, ... | ✅ Canonical source |
| **S5 instructor profile** (this commit) | Same as student portal | ✅ Aligned |
| **S3 instructor heatmap** | Identifies Python Constructs, Executes Python Code, Manipulates Data Structures, Creates Functional Programs | ❌ Still uses old 4 action-statement labels |
| **S4 at-risk mini-heatmap** | Same 4 action-statement labels as S3 | ❌ Still uses old labels |
| **S6 coaching sessions list** | Topic column shows 4 action-statement labels | ❌ Still uses old labels |

### Open follow-up — explicit

**S3-06 / S5-09 reconciliation still pending.** S3 heatmap columns, S4 mini-heatmap columns, and S6 "Topic" column values all reference the 4 old action-statement labels. With S5 + student portal now using the 13 canonical Topic names, the heatmaps need to either expand to 13 columns OR be restructured around the canonical taxonomy. This is the next coordinated cross-screen pass.

### Storyboard stamp

v4.101 instructor portal.

---

## v4.100 — 21 May 2026 — S5 Per-Topic table populated to all 13 Python Skill Topics

Per Brady: "Populate the rest of the per-topic scores table with the other Python topic areas so JFT doesn't think I only listed 4 on purpose."

### What changed

Extended S5's Per-Topic scores table from 4 rows to **all 13 Topics** of the Python Skill, matching the canonical taxonomy:

| # | Topic | Sally's score | Last attempt |
|---|---|---|---|
| 1 | Identifies Python Constructs | 42 | 05 May 2026 |
| 2 | Executes Python Code | 55 | 06 May 2026 |
| 3 | Manipulates Data Structures | 28 | 06 May 2026 |
| 4 | Creates Functional Programs | 38 | 04 May 2026 |
| 5 | Working with Files & I/O | 44 | 02 May 2026 |
| 6 | Error Handling & Debugging | 33 | 30 Apr 2026 |
| 7 | Object-Oriented Programming (OOP) | — | Not yet attempted |
| 8 | Python Libraries & Modules | — | Not yet attempted |
| 9 | Advanced Data Handling | — | Not yet attempted |
| 10 | Regular Expressions & String Manipulation | — | Not yet attempted |
| 11 | Working with Databases | — | Not yet attempted |
| 12 | Introduction to Automation | — | Not yet attempted |
| 13 | Introduction to Machine Learning | — | Not yet attempted |

- Sally's profile reflects an at-risk learner: scores on 6 of 13 Topics (all low/med), 7 Topics not yet attempted.
- All 13 rows clickable → S6 conversation logs (consistent affordance). Unstarted Topics will show empty-state in production per JFT implementation.
- "0 of 13 Topics mastered" in the Profile card now reads correctly against the table.

### Known follow-up (reiterated)

Rows 1–4 (action-statement names like "Identifies Python Constructs") and rows 5–13 (student-portal Topic names like "Working with Files & I/O") use **two different naming conventions** within the same table. The S3 heatmap and rows 1–4 of this S5 table use the original action-statement labels; rows 5–13 + the student portal use the descriptive Topic-name convention. Hierarchical content reconciliation — picking ONE convention and applying it everywhere — remains the open S3-06 / S5-09 follow-up.

### Storyboard stamp

v4.100 instructor portal.

---

## v4.99 — 21 May 2026 — S5 Sally Profile rewrite + global no-"LO"-abbreviation + global date-only display

Three threads landed in this commit per Brady's S5 walkthrough verdicts + two cross-portal global directives.

### S5 Sally Profile — rewrite to Topic-level only

- **Removed** the "Sample design only" banner.
- **Eyebrow** "AT-RISK LEARNER PROFILE" → **"LEARNER PROFILE"** (generic; every learner row on S1's cross-Course roster routes here regardless of status).
- **Removed** the "Anonymized identifier `lnr_4a3b2c1d` · E010 · 28 active learners (rolling enrollment)" subtitle entirely — H1 "Sally" stands alone.
- **Profile card simplifications:**
  - LAST ACTIVE: "06 May 2026 17:54 UTC" → **"06 May 2026"** (date only)
  - STUCK ON: "Lists & comprehensions (Learning Objective 3.1)" → **STUCK ON TOPIC: "Manipulates Data Structures"** (Topic-level only)
  - **Removed** the "Learning Objective misses (last 9 sessions): 14" row — instructor reviews specific LO data via S6/S7 logs and transcript
  - MASTERY ACHIEVED "0 of 4" → **TOPICS MASTERED "0 of 13"** (aligned to the 13 Topics that make up the Python Skill)
- **Right card rebuilt as Per-Topic scores:**
  - Eyebrow "PER-LEARNING OBJECTIVE SCORES" → **"PER-TOPIC SCORES"**
  - Removed `Learning Objective` and `Pattern` columns
  - Removed all 8 LO rows; replaced with 4 Topic rows (Sally's per-Topic averages: Identifies Python Constructs 42 · Executes Python Code 55 · Manipulates Data Structures 28 · Creates Functional Programs 38)
  - Every row clickable → S6 (Conversation logs for that Topic)
  - Caption added: "Click any row to open Sally's conversation logs for that Topic."
- **Back button** label: "Back" → **"Back to At-risk filter"** (consistent with other screens)

### Global directive 1 — no "LO" abbreviation anywhere

Per Brady (21 May 2026): never shorten "Learning Objective" to "LO" in any user-facing surface.

- **tenant_admin/index.html**: 3 instances replaced
  - Production section copy: "(rename, threshold change, add LO)" → "(rename, threshold change, add Learning Objective)"
  - Meta-bar button label: "04 Topics & LOs" → "04 Topics & Learning Objectives"
  - JS tooltip in `enforceLoMinimum()`: "Add another LO before removing..." → "Add another Learning Objective..."
- **Coda RBAC canonical hierarchy callout**: removed the previous sanction of "LO" as acceptable shorthand. Now reads: *"'Learning Objective' is the correct term for each individual LLM coaching target. Never abbreviate to 'LO' anywhere in UI copy, code, docs, or communication (Brady's directive, 2026-05-21)."*
- "objective miss" event-term shorthand in badges is **still allowed** (Brady didn't ban that specific shorthand).

### Global directive 2 — date-only display in student + instructor views

Per Brady: no time-of-day timestamps in student or instructor views. Apply globally.

- **instructor/index.html** — stripped times from:
  - S1 cross-Course at-risk roster (4 rows: e.g., "06 May 17:54" → "06 May 2026")
  - S6 Coaching sessions list (9 rows: e.g., "06 May 18:21 UTC" → "06 May 2026")
  - S7 Conversation transcript chat-meta (7 spans removed: e.g., `<span>18:21:04</span>` deleted; conversation date stays in S7 eyebrow)
  - S8 Audit Trail event log (10 rows: e.g., "2026-05-06 18:21:00" → "06 May 2026")
  - S9 Access Denied footer: "Logged · 18 May 2026 14:22:07 UTC · evt_b1d5e342" → "Logged · 18 May 2026 · evt_b1d5e342"
- **student/index.html** — no changes needed (already date-only).
- **Note for §10.4 forensic audit logging**: S8 displays date-only per Brady's directive; the underlying audit-log data model in production must still retain full timestamps for forensic value. Display ≠ storage.

### Known follow-up

**S5-09 (new):** the Python Skill heatmap on S3 currently shows 4 Topic columns, but the canonical truth (per Brady) is 13 Topics in the Python Skill (matching the student-portal Topic taxonomy). S5 now displays "0 of 13 Topics mastered" while S3 displays 4 columns. Hierarchical content reconciliation is a separate pass — flagged earlier as S3-06 and now reinforced.

### Storyboard stamp

v4.99 instructor + tenant_admin portals. Other 4 portals unchanged.

---

## v4.98 — 20 May 2026 — S4 At-risk filter: extend v4.97 patterns + breadcrumb + summary card relabel

Extends the v4.97 S3 hydration to S4 (At-risk filter) and applies the same cleanup playbook.

### Behavior changes

- **Generalized `hydrateHeatmap()`** — now hydrates both `#screen-3` (15 visible learners) and `#screen-4` (4 at-risk learners) with the same ARIA grid + tooltips + clickable rows pattern. Status maps per screen so the row-level data-row-status is correct on both.
- **S4 row labels now clickable** → S5 (all 4 at-risk rows: Sally, B.F., C.S., H.D.) — was only Sally before.
- **S4 cells get hover tooltips**: `"Sally · Identifies Python Constructs · Score 42/100"` etc.
- **Filter chips on S4 wired** — All/Mastery/On track/Watch now navigate to S3 AND apply that filter (using `goToScreen(3); filterHeatmap('xxx');`). The At risk chip remains the active state.

### Copy and layout

- **Removed "Sample design only" banner** from S4 (matches S3 removal)
- **Fixed breadcrumb formatting**: was "Heatmap · At risk" as a single span; now properly split into "Heatmap" (clickable to S3) + chevron + "At risk" (current page)
- **Removed Sally's inconsistent arrow icon** + her bespoke onclick handlers on row+cells — Sally now renders identically to the other 3 at-risk learners, all hydrated by the JS
- **Right summary card eyebrow** "Course summary" → **"Python Skill summary"** (Skill-level naming per the metric ladder)

### Storyboard stamp

v4.98 instructor portal. Other 5 portals unchanged.

---

## v4.97 — 20 May 2026 — S3 Skill heatmap: filter wiring, ARIA grid, hover tooltips, back button, copy fixes

Resolves S3 (Python Skill heatmap) walkthrough findings S3-01 through S3-10.

### Behavior changes (S3-02, S3-03, S3-04, S3-10)

Added a v4.97 hydration block to the JS that runs on initial S3 setup:
- **`hydrateHeatmap()`** — converts the heatmap into a proper ARIA grid:
  - `role="grid"`, `aria-readonly="true"`, `aria-label` describing the grid dimensions
  - Each column header gets `role="columnheader"` + `aria-colindex`
  - Each row label gets `role="rowheader"` + `aria-rowindex` + `data-row-status` (mastery/on-track/watch/at-risk based on the 15 visible learners)
  - Each cell gets `role="gridcell"` + `aria-rowindex` + `aria-colindex`
  - Each cell gets a `title` tooltip: `"Sally · Manipulates Data Structures · Score 28/100"`
  - Each row label is now clickable → S5 (Sally profile placeholder) with cursor:pointer + hover effect + aria-label
- **`filterHeatmap(status)`** — actually filters the heatmap:
  - Hides/shows rows based on `data-row-status` attribute
  - Updates the active chip styling
  - Updates the "Showing X of N learners" footer dynamically
  - Wired to chip onclicks via `data-filter-status` attribute

### Copy and layout changes

- **S3-01** — Renamed export button "Course report (PDF)" → **"Python Skill report (PDF)"** (Skill-level naming per the metric ladder)
- **S3-05** — Added the in-flow Back button block: **"Back to Course view"** → S2 (was missing entirely)
- **S3-07** — Removed `.heatmap-row-label.sally` CSS rule (red tinting + bold) — Sally's row now renders in default plaintext; heatmap-cell colors carry the at-risk cue
- **S3-08** — Removed the bottom alert "4 learners at risk. Sally lowest on Manipulates Data Structures" — heatmap colors and the red-dot status make the same point
- **S3-09** — Renamed eyebrow "Python Skill · Class heatmap" → **"Python Skill · Heatmap"** (no "class"; rolling enrollment, no fixed cohort)
- Removed the "Sample design only" banner from S3 (per Brady's directive)

### Known follow-up (S3-06)

The 4 heatmap column names ("Identifies Python Constructs", "Executes Python Code", "Manipulates Data Structures", "Creates Functional Programs") roll up Sally's 8 Learning Objectives — that satisfies the "Topic rolling up LOs" rule per Brady's exception. But the **13 Topics on the student portal don't match the 4 Topics in the instructor heatmap.** Hierarchical content reconciliation is a separate pass.

### S3-11 deferred

Cell-click drill-down to per-Topic Learning Objective breakdown — nice-to-have, not blocking.

### Storyboard stamp

v4.97 instructor portal. Other 5 portals unchanged.

---

## v4.96 — 20 May 2026 — Relocate Course Roster from S2 to S1 (cross-Course at-risk view)

Per Brady's second-pass feedback: the "Course Roster" on S2 (Course Detail) was conceptually misplaced — S2 should hold only Skill-specific data per the metric ladder. The roster data belonged on S1 (cross-Course view) or S3 (per-Skill view; the heatmap already serves that role).

### What changed (instructor portal only)

**S2 — Removed the entire Course Roster section:**
- "COURSE ROSTER" eyebrow + "Learners in E010" H2 — gone
- "Open Python Skill heatmap" standalone button — gone (each Skill card already has its own "Open Heatmap" button)
- Chip-filter bar (All / Mastery / On track / Watch list / At risk) — gone
- Roster table with per-Skill score columns — gone
- "—" footnote — gone

**S2 is now focused on Skill-level data only:** breadcrumb → header → 2 Skill cards → Back to Dashboard. Clean and on-spec.

**S1 — Added cross-Course "Learners needing attention" section** below the 3 Course cards:
- "ACROSS ALL YOUR COURSES" eyebrow
- H2: "Learners needing attention"
- Chip-filter bar with cross-Course totals: All (68) · Mastery (7) · On track (56) · Watch list (1) · At risk (4) [active]
- 4-row table: Learner | Course | Status | Last active | View profile
- All 4 at-risk learners currently in E010 (placeholder data); Course column shows which Course they're at-risk in
- Each row → S5 (Sally profile); "View profile" buttons → S5

### Conceptual model after v4.96

| Screen | Data scope | What's there |
|---|---|---|
| **S1 Dashboard** | Multi-Course + cross-Course roster | 3 Course cards + at-risk roster across all Courses |
| **S2 Course Detail** | Per-Skill within one Course | Skills (2 active) + Skill KPIs |
| **S3 Skill View** | Per-Topic within one Skill (the heatmap) | Topic × Learner grid |
| **S4 At-risk Filter** | Per-Skill at-risk subset | Filtered heatmap |
| **S5 Sally Profile** | Individual learner | Per-Learning-Objective scores |

### Storyboard stamp

v4.96 across the instructor portal. Other 5 portals stay at v4.91 (or v4.95 for tenant_admin / super_admin which got the floating-actions fix).

---

## v4.95 — 20 May 2026 — S2 second-pass refinements + cross-portal floating-actions accessibility fix

Resolves S2-13 through S2-19 from the S2 (Course view) second-pass walkthrough, plus a cross-portal layout fix to remove the floating-overlay button.

### S2 Course view refinements (instructor portal)

- **S2-13 — Python Skill card "4 learners at risk" badge now clickable** → routes to S4 At-risk filter (matches the S1 E010 card pattern). Uses `event.stopPropagation()` so it doesn't bubble up to the card-level S3 navigation.
- **S2-14 — Skill cards on S2 now have full a11y attributes:** `role="button"`, `tabindex="0"`, `aria-label` ("Open Python Skill heatmap" / "Open Git & Version Control Skill heatmap"). Matches the S1 E010 card a11y pattern.
- **S2-15 — Replaced uninformative "Active" eyebrow with a "Live" status badge** inline with the Skill title. Cross-platform status terminology proposed: **Testing** (amber/warning) for Skills under verification by admins/instructors, and **Live** (green/success) for Skills deployed to students with Topics locked. Recommended for ALL 4 user types (Student, Instructor, Tenant Admin, Super Admin) — "Testing" is clearer than "Test", "Live" is less technical than "Production"/"Prod".
- **S2-16 — Renamed "View full roster (heatmap)" button** to **"Open Python Skill heatmap"** — specific to which Skill's heatmap opens (was ambiguous with 2 Skills now in E010).
- **S2-18 — Removed `<strong>` bold from Sally's name in Roster table.** All learner names now render in default plaintext (matches default font styling site-wide).
- **S2-19 — Added chip-filter bar to Course Roster:** All (28) · Mastery (7) · On track (17) · Watch list (1) · At risk (4) [active]. Same pattern as the S3 heatmap filter.
- **Bonus:** Renamed roster heading from "Learners needing attention (4 of 28)" to **"Learners in E010"** — the filter chip below now communicates which subset is shown, no need to bake "4 of 28" into the heading.
- **Bonus:** All 4 at-risk row "View profile" buttons now route to **S5 Sally profile** (was S4 for non-Sally rows). Matches Brady's "clicking this row goes to Screen 05" verdict — JFT will parameterize per-learner profile in production.

### S2-17 — Cross-portal floating-actions accessibility fix (3 admin portals)

The old `.floating-actions` CSS used `position: fixed; bottom: 200px; right: 32px;` to overlay the page — caused overlap with content (e.g., the roster table on S2) and broke keyboard/screen-reader flow.

**New `.floating-actions` rule** (applied to instructor, super_admin, and tenant_admin portals):
```css
.floating-actions {
  display: flex; gap: var(--pgn-spacing-2);
  justify-content: flex-end;
  margin-top: var(--pgn-spacing-5);
  padding: var(--pgn-spacing-3) 0;
}
```

- Removed: `position: fixed`, `bottom`, `right`, `background`, `backdrop-filter`, `padding`, `border-radius`, `border`, `box-shadow`, `z-index`
- Added: in-flow flex layout, right-aligned, vertical spacing above the footer
- Removed associated dark-mode override (no overlay → no background to override)
- Net effect: the Back/return button now renders at the bottom-right of the page content, just above the footer — matches the student portal's `.pm-bottom-actions` pattern

### Storyboard stamp

v4.95 across instructor, super_admin, tenant_admin. Student and help portals stay at v4.91.

---

## v4.94 — 20 May 2026 — Instructor S1 Dashboard: full E010 card clickable, regional click routing

Follow-up to v4.93 per Brady's directive: the big E010 Course card on the Dashboard needs more clickable regions, not just the title link and "Open Course details" button.

### What changed (instructor portal only)

- **Entire E010 Course card now clickable** → routes to **S2 Course view**.
  - `<div class="section-card recommended">` gained `onclick="goToScreen(2)"`, `cursor:pointer`, `role="button"`, `tabindex="0"`, and `aria-label="Open E010 Course details"`.
  - The course-title `<a>` link was simplified (still readable as a course title, no longer needs its own onclick — the parent card handles navigation).
- **Skill region clicks now route to S3** correctly via `event.stopPropagation()`.
  - Python Skill nested card and Git Skill nested card both got `event.stopPropagation(); goToScreen(3);` on their onclick, so clicks inside the Skills region don't bubble up to the parent E010 card.
- **"4 at risk" header badge is now a clickable link** → routes to **S4 At-risk filter** (consistent with the same badge on S2). Uses `event.stopPropagation()` to prevent bubbling to the parent E010 card.

### Click-region map verified (functional test)

| Clicked region | Lands on |
|---|---|
| E010 card body (KPIs, eyebrow, title, subtitle) | **S2** Course view |
| `4 at risk` header badge | **S4** At-risk filter |
| Python Skill nested card | **S3** Skill view (heatmap) |
| Git Skill nested card | **S3** Skill view (heatmap) |
| Either "Open Heatmap" button inside Skill cards | **S3** Skill view (heatmap) |

### Storyboard stamp

v4.94 across the instructor portal. Other 5 portals stay at v4.91.

---

## v4.93 — 20 May 2026 — Instructor S2 Course view refined: Skill-level metrics only, second Skill added, learner roster surfaced

Resolves the S2 (Course view) walkthrough findings S2-07 through S2-12 per Brady's verdicts.

### What changed (instructor portal only)

- **Removed** the "Course aggregate metrics" card (`Across all Skills in this Course` with 6 KPI tiles) — duplicated S1 Dashboard E010 KPIs and violated the "Skill-level perspective" rule for S2.
- **Removed** the "Sample design only" disclaimer banner from S2.
- **Renamed** section heading `Coaching modules (1 active)` → `Skills (2 active)` (terminology enforcement — "module" is on the banned-terms list per the RBAC canonical hierarchy callout).
- **Made the header badge `4 learners at risk` a real link** — now routes to S4 At-risk filter (was non-clickable static badge).
- **Dropped redundant "Skill" from card eyebrows** — eyebrow now reads `Active` instead of `Skill · Active` (the card title `Python Skill` already names the entity).
- **Added a second Skill — Git & Version Control Skill** — appears on S2 (full card with KPIs + Open Heatmap CTA) and on S1 Dashboard's E010 card (compact row). Course E010 now shows `SKILLS IN THIS COURSE (2 active)` instead of `(1 active)`. Sample data: 22 learners practicing, 68% avg Topic mastery, 3 Topics, 0 at risk.
- **Added a Course Roster section to S2** — `Learners needing attention (4 of 28)` compact table showing the 4 at-risk learners (Sally, B.F., C.S., H.D.) with per-Skill scores across both Python Skill and Git Skill. "—" indicates learner has not started practicing that Skill yet. Each row links to the at-risk filter or Sally's profile.
- **NO time-related metrics anywhere** — per Brady's directive: no "time-on-platform", no "average session length", no "time-since-last-active" beyond the human-readable "last active" timestamp.

### Followed Brady's framing of the metric ladder

| Screen | Granularity | Example KPIs |
|---|---|---|
| **S1 Dashboard** | per-Course | 28 active learners · 76% Avg Skill score · 4 at risk |
| **S2 Course view** | per-Skill | Python Skill: 28 practicing, 76% avg Topic mastery; Git Skill: 22 practicing, 68% |
| **S3 Skill view (heatmap)** | per-Topic | Cell = learner × Topic mastery within one Skill |

### Storyboard stamp

v4.93 across the instructor portal. Other 5 portals stay at v4.91.

---

## v4.92 — 20 May 2026 — Instructor portal: Course view inserted as Screen 02, screens renumbered 01-09, S2 findings cleared

Resumes the S2 critical walkthrough by acting on Brady's verdict on S2-01 through S2-06 (per session findings). Major architectural change to the instructor flow.

### What changed

- **Screen renumbering: all 8 instructor screens renumbered 01-09 starting at Screen 01 (Dashboard)** — the original Screen 01 (SSO splash) was removed in v4.85; this pass closes that gap. New navigation hierarchy:
  - **Screen 01** — Instructor Dashboard (Course list with Skills nested in each Course card)
  - **Screen 02** — Course view (NEW — aggregate Course metrics + Skills deployed in the Course)
  - **Screen 03** — Skill view (Python Skill heatmap, was old Screen 03 reframed as Skill-level)
  - **Screen 04** — At-risk filter applied
  - **Screen 05** — Sally drill-down
  - **Screen 06** — Coaching sessions
  - **Screen 07** — Session transcript
  - **Screen 08** — Audit trail
  - **Screen 09** — Access denied
- **Screen 01 Dashboard restructure** — Each Course card now shows its Skills nested inline. E010 card shows the Python Skill with mastery stats + Open Heatmap CTA. E075 and E135 show their Skills (Python Intermediate, Libraries, OOP, Design Patterns) as compact rows.
- **Screen 02 Course view (new)** — Opens when instructor clicks `E010 · Foundations of Programming (Python)` from Dashboard, or via the "Open Course details" link. Shows Course aggregate metrics, Skills deployed in the Course, and per-Skill drill-down CTAs.
- **Screen 03 Skill view (relabeling)** — Heatmap now framed as a Skill-level view. Header reads `Python Skill — Topic mastery`, breadcrumb now reads `Instructor Dashboard › E010 › Python Skill › Heatmap` (Skill node added).
- **Breadcrumbs across S3-S8** — `goToScreen(2)` (Dashboard) updated to `goToScreen(1)` everywhere; E010 link in S4/S5/S6 breadcrumbs now routes to Course view (S2) instead of Heatmap (S3).
- **Floating "Back to dashboard" actions on S8 and S9** — updated to `goToScreen(1)`.
- **Meta-bar** — 9 buttons starting at "01 Dashboard home" with new "02 Course view" and "03 Skill view" labels.
- **TOTAL_SCREENS comment** updated to note v4.92 renumbering.

### S2 walkthrough findings resolved (S2-01 through S2-06)

- **S2-01 + S2-03** (dead E075/E135 cards + E010-only drill-down) — Resolved by the new Course view + Skills-nested-in-Course pattern. Course cards no longer have dead `cursor:pointer`; all Skill drill-downs are explicit clickable elements.
- **S2-04** (redundant alert "4 learners flagged at-risk in E010 today") — Removed entirely.
- **S2-05** (degenerate single-item breadcrumb on entry screen) — Removed.
- **S2-06** ("Diagnostic in flight" on E135) — Removed. E135 now shows real KPIs (18 learners, 71% Avg Skill score, 0 at risk).

### Known follow-ups

- Screenshots in `instructor/screenshots/` and `instructor/screenshots_dark/` are still numbered against the old 02-09 sequence. Regeneration deferred until the storyboard fully stabilizes.
- S7 and S8 breadcrumbs still skip the Course + Python Skill layers (`Dashboard › Sally › ...`) — pragmatic shortcut for the deeper screens; can be revisited.

### Storyboard stamp

v4.92 across the instructor portal. Other 5 portals stay at v4.91 (no changes).

---

## v4.91 — 20 May 2026 — Correct hierarchy terminology: Topic / Learning Objective (replaces v4.90 mislabeling)

Mid-session correction after Brady clarified the full 6-level platform hierarchy. v4.90 had renamed Topics as Skills in the student portal — wrong granularity. v4.91 corrects to the canonical hierarchy: **Platform > School > Course > Skill > Topic > Learning Objective**.

### What changed (corrections to v4.90)

- **Student portal** — "13 Skills" / "sub-sections" → **"13 Topics"** (8 instances: sidebar card label, aria-label, footer note, progress map stats, welcome-back table rows, session snapshot rows)
- **Help portal** — reverted the v4.90 meaning-change bug: "Retiring a Skill from production" → **"Retiring a Topic from a production Skill"** (the original intent was Topic-level lifecycle, not Skill-level)

### What changed (new in v4.91)

- **Instructor portal (all 8 screens)** — "competency" / "Competency" / "objective" / "Objective" replaced in user-facing copy:
  - S2 stat tile: "Avg competency" → "Avg Skill score"
  - S3 heading + cell labels: "competency mastery" + "Competency →" → "Topic mastery" + "Topic →"
  - S4 filter description + summary: "Lowest competency" → "Lowest Topic score"
  - S5 badge: "AI-scored competency: Low" → "AI-scored Skill mastery: Low"
  - S5 table headers: "Competency" → "Topic", "Objective" → "Learning Objective"
  - S5 profile: "(Objective 3.1)" → "(Learning Objective 3.1)", "objective misses" → "Learning Objective misses"
  - S5 eyebrow: "Per-objective scores" → "Per-Learning Objective scores"
  - S6 table header: "Objective" → "Learning Objective"
  - S7 eyebrow: "3 objective misses" → "3 Learning Objective misses"
  - S8 stat tile: "objective misses" → "Learning Objective misses"
- **READMEs** — terminology fixes in `README.md`, `instructor/README.md`, `student/README.md`, `tenant_admin/README.md` (8 instances across "sub-sections", "competency", "Program Subject")
- **Coda RBAC doc** — replaced v4.90 4-level callout with corrected 6-level Canonical Terminology block (Platform → School → Course → Skill → Topic → Learning Objective) plus enforced terminology rules

### What is NOT changed

- "objective miss" badges in instructor S6 / S7 (e.g., `objective miss × 3`) — retained as established SkillProof event-term shorthand, sanctioned in the RBAC callout
- CSS class names like `.practice-areas-card` — internal selectors retained for v4.91; rename deferred to a follow-up commit
- CHANGELOG historical entries (e.g., v4.73 "Program Subject" note) — immutable history

### Storyboard stamp

v4.91 across the 6 portals.

---

## v4.90 — 20 May 2026 — Standardize Skill/Course/School/Platform hierarchy terminology site-wide (initial pass, superseded by v4.91)

Initial hierarchy standardization based on Brady's 4-level model (Platform / School / Course / Skill). Subsequently corrected by v4.91 after Brady clarified the full 6-level model adds Topic and Learning Objective beneath Skill. See v4.91 for the canonical hierarchy.

### What changed

- Student portal — "Practice Areas" / "sub-sections" → "Skills" (later corrected to "Topics" in v4.91)
- Student portal — added `E010` Course node to all 6 coaching breadcrumbs (retained in v4.91)
- Super Admin portal — "Coaching module" → "Skill" (5 instances; retained)
- Tenant Admin portal — "Program Subject" → "Course" (2 instances; retained)
- Help portal — "Retiring a topic from a production Skill" → "Retiring a Skill from production" (reverted in v4.91 as meaning-change)
- Coda RBAC doc — added hierarchy callout (later replaced with 6-level version in v4.91); fixed §4.1 Instructor-assigned-to-Course error (retained)

### Storyboard stamp

v4.90 (superseded by v4.91 same day).

---

## v4.89 — 19 May 2026 — Strip superfluous labels (LRPS demo shortcut + Not for student use + build stamp) and passive governance banners

Two cleanup passes per Brady's directive.

### What changed

- **LRPS landing** (`index.html`) — removed three label families:
  - `demo shortcut` badges on the Tenant Admin + Super Admin rows (×2 elements)
  - `(demo shortcut)` suffix trimmed from the two corresponding `aria-label`s
  - `Not for student use` badges on the Instructor, Tenant Admin, Super Admin rows (×3 elements)
  - Footer build stamp paragraph `Build: 20260507 · LRPS v3.4.2 · SkillProof-styled storyboard recreation`
  - Associated CSS: `.no-student-badge` rule block + the comment + `max-width / overflow / text-overflow` overrides in `.pgn__data-table tr.live .lrps-name` that existed solely to accommodate the badge
- **Tenant Admin Screen 4** (`tenant_admin/index.html`) — removed both passive informational alert banners:
  - "This Skill is in Production. Topics cannot be removed once a Skill is live…"
  - "Every topic must have at least one Learning Objective…"
  - These rules are now enforced exclusively by action-triggered UI (disabled `Remove topic` buttons with `title=` tooltip + `enforceLoMinimum()` JS) — the same enforcement that was already in place. Rules themselves migrate to user instruction docs.

### Storyboard stamp

v4.89 across the 6 portals.

---

## v4.88 — 19 May 2026 — Strip 'SkillProof Design System v1.2' from HTML comments

Follow-up to v4.87 — Brady's directive was "anywhere," so the phrase was also stripped from the developer comments at the top of each portal file. Each occurrence of `SkillProof Design System v1.2` replaced with `design tokens` so the surrounding comment text still reads.

### Storyboard stamp

v4.88 across the 6 portals.

---

## v4.87 — 19 May 2026 — Strip 'SkillProof Design System v1.2' meta-bar text + remove unrequested 'Technical contact' footer link

Two clean-up passes per Brady's directive.

### What changed

- **Meta-bar header** in 4 portals (root LRPS, instructor, tenant_admin, super_admin) — removed the `· SkillProof Design System v1.2 ·` segment. Now reads `DEMO ONLY · [Portal name] · Persona: [Name]`.
- **Footer** in all 6 portals (root, student, instructor, tenant_admin, super_admin, help) — removed the `| Technical contact: Vivek` `mailto:vivek@wgu.edu` link I had added in v4.78 without explicit ask. Footer now ends at Honor Code.
- **Screen 17 identity card** in tenant_admin — removed the `Contact Vivek for changes` mention; now reads `Tenant ID tenant_school_tech · managed centrally by WGU.` and stops there.

### Storyboard stamp

v4.87 across the 6 portals.

---

## v4.86 — 19 May 2026 — Apply student-style storyboard shortcut bar to all 3 admin portals

Brady: *"I like the update you did to the student flow shortcut bar at the bottom of the page with the 'back' button in the upper right corner of the shortcut bar that goes back to the LRPS page. I also like that you added a short description along with the screen numbering in that bar. Apply all of those updates to all the other prototype screens in the other 3 user scenarios."*

### What changed

For each of `super_admin/`, `tenant_admin/`, `instructor/`:

1. **`← Storyboard Index` link** added to the upper-right of the meta-bar-header, pointing back to the LRPS root (`../`). Uses the new `.meta-link` CSS rule (mirrors student's pattern).
2. **Short descriptions** appended to every step-btn label so you can see what each screen is at a glance:
   - super_admin: `02 Portal home` · `03 Token usage` · `04 Cost spike` · `05 Rate limits` · `06 Compliance` · `07 Geo-redundancy` · `08 Audit log` · `09 Access Control` · `10 External Tooling` · `11 Data Hub` · `12 Instructor Roster` · `13 School Mgmt` · `14 Access Denied`
   - tenant_admin Flow A: `02 Portal home` · `03 New Skill` · `04 Topics & LOs` · `05 Model & Coaching` · `07 Deploy review` · `08 Deploy success` · `17 School Settings` · `18 Skill Lifecycle` · `19 Analytics` · `20 Activity Log` · `21 Access Denied`
   - tenant_admin Flow B: `09 All systems OK` · `10 LLM down` · `11 Notification` · `12 P1 ticket` · `13 Ticket submitted` · `14 CSM response` · `15 Service restored` · `16 SLA dashboard`
   - instructor: `02 Dashboard home` · `03 Class heatmap` · `04 At-risk filter` · `05 Sally profile` · `06 Conversation logs` · `07 Session transcript` · `08 Audit Trail` · `09 Access Denied`

### Storyboard stamp

v4.86 across the 6 portals.

---

## v4.85 — 19 May 2026 — Remove Screen 01 (SSO landing) from admin portals

Brady: *"Let's remove Screen 01 from the instructor, tenant admin, and super admin. Those are informational only and should have been removed a long time ago when I directed that we only include the screens and features for JFT to implement. No extra features or text or buttons or anything else that is outside of the requirements of the contract language."*

The SSO landing screens were illustrative — they showed the authentication handshake (LRPS deep link verified · WGU SSO complete · LTI role + elevation) but nothing for JFT to build. Auth is contractually LTI 1.3 + WGU SSO; the prototype shouldn't depict the auth ceremony at all.

### What was removed

- `super_admin/index.html` — Screen 1 (~50 lines): "Welcome to the Super Admin Portal" SSO splash + Continue button + meta-bar `01` step-btn
- `tenant_admin/index.html` — Screen 1 (~45 lines): "Welcome to the School Admin Portal" SSO splash + Continue button + meta-bar `01` step-btn
- `instructor/index.html` — Screen 1 (~45 lines): "Welcome to the Instructor Dashboard" SSO splash + Continue button + meta-bar `01` step-btn

In each portal, screen-2 (the actual portal home) is now marked `class="screen active"` so it's the default screen on load. The meta-bar's `02` step-btn carries the `active` class.

### What is NOT changed

- `student/` Screen 1 (the Coding Coach intro / Begin Diagnostic landing) stays. It's a legitimate first screen of the student flow, not an SSO splash.
- LRPS landing (root `index.html`) stays — it's the entry point that distributes to each persona portal.
- TOTAL_SCREENS counter and arrow-key navigation already had fall-through for missing screen IDs (since v4.74 / v4.85 introduced the screen-1 + screen-6 gaps in admin portals).
- `goToScreen(2)` references unchanged — that's now the entry point.

### Storyboard stamp

v4.85 across the 6 portals.

---

## v4.84 — 19 May 2026 — Larger school logos in navbar (so 'School of X' text reads)

Brady: *"Now increase the school-level logo in the upper-left corner to the larger size you did with the standard WGU logo. Right now, it's so small I can't read the lettering for 'School of XXX'."*

The school logos have a stacked WGU + horizontal line + school-name layout, so at the 40px shared height set in v4.80 the school-name text portion was only ~13px tall — illegible. Bumped to **64px** specifically for school logos via the `[data-school-logo]` attribute selector, leaving the WGU corporate logos at 40px:

```css
.navbar-brand-logo { height: 40px; width: auto; }
.navbar-brand-logo[data-school-logo] { height: 64px; }
```

Applied to all 6 portals (only the school-logo navbars in `tenant_admin/`, `student/`, `instructor/` actually pick up the override; the others have WGU corporate logos without the data attribute).

### Storyboard stamp

v4.84 across the 6 portals.

---

## v4.83 — 19 May 2026 — Dark-mode footer theming (deep navy + white text, all 6 portals)

Brady's directive: *"The dark mode footer needs to have the dark navy background and white text like the header does so it's legible and accessible in dark mode. All you did in the footer was update the logo file. Apply the other dark mode theming and make sure that's also deployed across every page of the prototype."*

The footer markup uses hardcoded inline styles (`background: #F5F7FA`, `color: #002855`, etc.) that don't respond to `[data-theme="dark"]`. Added a CSS override block to each of the 6 portals that targets `footer[role="contentinfo"]` with `!important` to win over the inline styles:

```css
[data-theme="dark"] footer[role="contentinfo"] {
  background: var(--color-deep-navy) !important;
  border-top-color: rgba(255,255,255,0.1) !important;
}
[data-theme="dark"] footer[role="contentinfo"] > div {
  border-bottom-color: rgba(255,255,255,0.1) !important;
}
[data-theme="dark"] footer[role="contentinfo"] a { color: #fff !important; }
[data-theme="dark"] footer[role="contentinfo"] span { color: rgba(255,255,255,0.7) !important; }
```

Applied identically to root `index.html`, `student/`, `instructor/`, `tenant_admin/`, `super_admin/`, and `help/`.

Light-mode header + footer were already consistent across all 6 portals; no light-mode changes needed.

### Verification

- Toggle dark mode on any portal → footer flips to deep-navy background with white link text, semi-transparent white copyright + divider pipe colors
- All 6 portals respond identically
- Light mode unchanged

### Storyboard stamp

v4.83 across the 6 portals.

---

## v4.82 — 19 May 2026 — Help button in every navbar

Brady's directive: *"The help button should be in the header across ALL pages on the site, no matter what."*

The LRPS landing root (`index.html`) had no Help button. Added one next to the theme toggle (matches the `.btn-theme-toggle` icon pattern used by other admin portals, links to `help/index.html#submit-request`).

The help page itself (`help/index.html`) also got a Help icon button in its navbar — it re-anchors to the form on the same page (`#submit-request`).

All 6 portals now carry a Help icon in their navbar:

| Portal | Pattern | Target |
|---|---|---|
| `/` (LRPS landing) | `.btn-theme-toggle` icon link | `help/index.html#submit-request` |
| `student/` | `.btn-theme-toggle` icon link | `../help/index.html#submit-request` |
| `instructor/` | `.btn-theme-toggle` icon link | `../help/index.html#submit-request` |
| `tenant_admin/` | `.navbar-help-link` pill (existing) | `../help/index.html#submit-request` |
| `super_admin/` | `.btn-theme-toggle` icon link | `../help/index.html#submit-request` |
| `help/` | `.btn-theme-toggle` icon link | `#submit-request` (re-anchor) |

### Storyboard stamp

v4.82 across the 6 portals.

---

## v4.81 — 19 May 2026 — Help page rewrite + remove floating support pill + CHANGELOG prune

Four-item batch from the second audit follow-up.

### What changed

- **`help/index.html` rewritten end-to-end** to match the rest of the site's chrome (Paragon-aligned tokens, WGU corporate navbar with theme toggle + Help & Support chip + 40px logo, standard WGU footer with Vivek link). 823-line page collapsed to ~330 lines.
- **Page content trimmed to two sections only**:
  1. The Zendesk-style support form (`id="submit-request"` anchor preserved, so existing portal Help-button anchor links still work)
  2. A flat help-docs list — 15 role-tagged article links (Student / Instructor / Tenant Admin / Super Admin / All admin roles). No cards, no videos, no external links.
- **Removed** from the help page: the floating "Contact JFT Support" pill, the 4-card Self-service support grid, the Recent updates feed, the entire Video training resources section (role-chip filter, featured callout, video tiles), and the custom-styled brand-logo gradient block.
- **CHANGELOG pruned** — pre-v4.69 entries (v4.0–v4.68, ~3,300 lines) replaced with a one-line "history exists in git" note. Per Brady's directive: this is a prototype; incremental change documentation isn't important. Pre-v4.69 references to deleted files (`presentation.html`, `presentation_dark.html`, `_contract_tracking/`) cleared in the same pass.
- **Storyboard stamp** v4.80 → v4.81 across all 6 portals.

### Why

Brady's audit response:
- *"Remove the support pill. We don't need it."*
- *"That help page is terrible. It needs a complete rewrite to come into compliance with the header/footer/styling we've implemented across the site. I also only want the help form and help docs. No videos and external links. This page is much too complicated right now."*
- *"I don't care much about the changelog. This is a prototype, so incremental change documentation is not very important."*

### Verification

- `https://brady-wgu.github.io/SkillProof/help/` → standard WGU navbar at top (matches admin portals); standard WGU footer at bottom with Vivek link; Zendesk-styled support form; below the form, the flat docs list; no floating Contact JFT pill; no video tiles; no Recent updates feed; no external links other than the WGU policy URLs in the footer.
- Help button on every portal still anchors to `help/index.html#submit-request` and lands on the form.

---

## v4.80 — 19 May 2026 — Audit follow-ups (School identity trim · bigger logos · Zendesk-styled help · student Help link)

Follow-up batch after the v4.79 review. Five-item delivery:

### 1. Screen 17 School identity card simplified

The 6-row info table (Tenant ID, Parent Org, Operated by, LRPS launch URL, Assigned JFT CSM, Your role scope) was redundant — none of those fields are user-modifiable, so the School Admin couldn't act on any of it. Replaced the whole table with a single sentence:

> Tenant ID `tenant_school_tech` · managed centrally by WGU. Contact Vivek for changes.

The school name (h2) stays for context; the Tenant ID stays in a `<code>` for support-ticket reference. Brady's directive: *"Remove almost everything in that box because they are not things the School Admin can change or modify in any way."*

### 2. Header + footer logos enlarged

Bumped logo height from `28px` → `40px` across all 6 portals — both the navbar (`.navbar-brand-logo { height: 40px; }`) and footer image inline styles. Brady's directive: *"The sizes of these in our prototype are WAY too small, so they need to be made much larger to be the same height as the other buttons and labels on the header and footer rows."*

Student portal's old `.navbar-brand-logo { width: 36px; height: 36px; }` rule (which was sized for a square text-mark) was simplified to `height: 40px; width: auto;` to fit the v4.72 school-logo image swap.

### 3. Help form refined to mimic a real Zendesk page

Replaced the bare form with a 2-column Zendesk-style layout on `help/index.html`:

- **Left column**: "WGU Support · powered by Zendesk" badge + h2 + form card with Subject + Description + LRPS-reissue request type + drag-drop Attachments area + Submit / Cancel buttons + success-state with request-ID copy
- **Right column**: "Suggested articles" aside with 5 article links + response-time note ("usually within 1 business day; P1 paged immediately")
- Form wrapper carries `id="submit-request"` so Help-button links anchor directly to it
- Required-field asterisks throughout

### 4. Help buttons across the site route to the form

Every Help button now uses `#submit-request` anchor so clicking lands the user directly on the support form:

- super_admin · tenant_admin · instructor — existing `<a class="navbar-help-link" href="../help/index.html#submit-request">` (or `btn-theme-toggle` variant)
- **student/** — added a Help icon button (previously had none); now matches admin portals

### 5. Version increment

v4.79 → v4.80 across the 6 portals. Future: every commit/push that ships UI changes should bump this version so Brady can spot when GitHub gets out of sync with local pushes.

### Companion external document

Started `OneDrive\_SkillProof\c_Deliverables\_From Brady to JFT\g_User Documentation\SkillProof_User_Documentation_Outline_v0_1_19MAY2026.md` — a bulleted outline organizing what to include in the eventual user-instruction docs for Tenant Admins, Instructors, Students, and Super Admins. Lives in OneDrive (not the public repo), per Brady's separation of prototype vs. supporting docs.

### Verification

- Screen 17 identity card → reads "School of Technology" + the one-line tenant ID sentence; no other rows
- Hard-refresh `https://brady-wgu.github.io/SkillProof/` → header WGU logo + each portal navbar logo + footer WGU logo all render at the new 40px height
- `help/index.html#submit-request` → lands at the form; the Zendesk styling is visible (powered-by badge, sidebar, attachments box)
- student/ navbar shows a Help icon next to the theme toggle
- v4.80 title stamp on all 6 portals

---

## v4.79 — 19 May 2026 — Analytics page iteration (no more timing things)

Phase K — the final phase of the original JFT meeting follow-ups. Per Brady's note *"Iterate on the analytics page. No more timing things,"* the arbitrary time-on-task metric is gone, replaced with a more meaningful active-learners trend.

### What changed (tenant_admin/index.html · Screen 19 Analytics & Reporting)

- **Engagement section, left panel** rebuilt:
  - Eyebrow: "Time on task · last 30 days" → "Active learners · last 30 days"
  - Subhead: "Median 18 min · per session" → "178 active learners · +14% vs prior 30 days"
  - Aria-label: "Time-on-task trend chart..." → "Active learners trend chart..."
  - Icon: `schedule` → `groups`
  - The existing SVG line chart stays (visually a learner-growth trend); only the framing changes from time-duration to learner-count.

The Submissions chart (right side), Class Insights table, Billing & Usage gauges, Cost by Skill table, and Program Reports section all stay as-is — none used arbitrary timing data.

### What stays as contractually-required SLA timings

Incident Response screens (SC-ADD-06, Screens 14–16) keep their SLA timings — 6-min first response, 60–90 min ETA — because those are signed in SOW §9.5 (P1 SLA = 2-hour response). Those are contractual, not arbitrary.

### Storyboard stamp

v4.79 across the 6 portals.

---

## v4.78 — 19 May 2026 — Help / Support flows + Vivek footer link

Phase J. Wires up the Submit LRPS Ticket button to a real `mailto:` action, refreshes the help page with an LRPS deep-link distribution note, and adds the Vivek technical-contact footer link across all 6 portals.

### What changed

- **tenant_admin Screen 8 (Deploy success)** — Submit LRPS ticket button is now an `<a>` with a `mailto:wgu-lrps-support@wgu.edu` link, pre-filled subject `LRPS Ticket — E135 OOP Python (School of Technology)` and a multi-line body including Tenant Admin, Skill, Build, Destination URL, and a Justification stub.
- **help/index.html** — added an "LRPS deep links" tile to the self-service card grid explaining WGU IT distributes the URL out-of-band. *(Tile was later removed in v4.81's help-page rewrite.)*
- **Footer — Vivek technical contact** added to all 6 portal footers (`super_admin/`, `tenant_admin/`, `instructor/`, `student/`, `help/`, root `index.html`). Pipe-separated next to Honor Code, `mailto:vivek@wgu.edu` placeholder.

### Storyboard stamp

v4.78 across the 6 portals.

---

## v4.77 — 19 May 2026 — Super Admin demotion tooltips + Instructor Downgrade affordance

Phase H. Brady's JFT note: *"Demotion to lower levels is also important to remember."* The v4.68 Access Control screen already had Downgrade buttons for Tenant Admins and Super Admin. This release adds context-specific tooltips explaining what each demotion does to scope assignments, and surfaces the missing Instructor → Student demotion affordance.

### What changed (super_admin/index.html · Screen 9 Access Control · People tab)

- **Jordan (Super Admin, disabled Downgrade)** — title tooltip: *"Demoting to Tenant Admin requires assignment to at least one School afterward. Currently blocked: minimum 2 Super Admins required at all times."*
- **Alice + Miguel (Tenant Admin Downgrade)** — title tooltip: *"Demoting to Instructor removes all School assignments and reverts to baseline read-only access on assigned Skills."*
- **Charlie + Priya (Instructor)** — added a third button "Downgrade" with title tooltip: *"Demoting to Student removes all Skill assignments and reverts to learner-only access."*
- Sally + Devon (Student) — stay as-is (Student is the baseline; no lower role to demote to).

### Storyboard stamp

v4.77 across the 6 portals.

---

## v4.76 — 19 May 2026 — School Settings rebuild (Screen 17)

Phase G. Tenant Settings renamed and simplified per Brady's JFT direction.

### What changed (tenant_admin/index.html · Screen 17)

- **Renamed to "School Settings"** across the surface — breadcrumb, eyebrow, h1, identity card eyebrow ("School identity"), branding h2 ("School logo"). The architectural identifier "Tenant ID" stays as the underlying tech name (matches the SOW).
- **Removed the accent color box** + the standalone "Accent color" form group.
- **"Parent organization" → "Parent Org"**.
- **Logo upload helper text added**: *"Max 2 MB · PNG or SVG · recommended 400 × 120 px"* directly under the School logo heading.
- **Logo preview images** swapped to the active school's logo with `data-school-logo` markers so they update on Switch School.
- **Cross-screen label sweep** — every other "Tenant Settings" user-visible reference now reads "School Settings" / "Skill Lifecycle".

*(In v4.80, the identity-card info table was further trimmed to a one-line sentence.)*

### Storyboard stamp

v4.76 across the 6 portals.

---

## v4.75 — 19 May 2026 — Skill Production Governance (topic remove + LO≥1 + deploy stages)

Phase F. Surface the production-Skill rules in the UI so JFT builds the right affordances. When a Skill is in Production, topics cannot be removed and the UI shows that constraint explicitly. Learning Objectives have a `≥ 1 per topic` floor enforced via UI state.

### What changed (tenant_admin/index.html)

**Screen 4 (Topics & Learning Objectives):**

- **Production-status banner** (alert-warning) above the topic list explaining production constraints
- **LO ≥ 1 banner** (alert-info) explaining the per-topic floor
- **All 4 "Remove topic" buttons disabled** with tooltip
- **New `enforceLoMinimum()` JS**: scans every topic on load + after `addTopic()`. If a topic has only 1 LO, that LO's delete button is disabled + tooltip

**Screen 7 (Review & Deploy):**

- **Bare 2-button deploy row replaced** with two explanatory cards side-by-side (Staging vs Production) with access-scope copy.
- **Step 3 summary table** updated to reflect the v4.74 wizard rebuild
- **Step 4 summary table** removed (no longer a separate wizard step).

### Storyboard stamp

v4.75 across the 6 portals.

---

## v4.74 — 19 May 2026 — Skill Creation Wizard rebuild (combined Screens 5+6)

Phase E. The wizard's "Model & Coaching" (Screen 5) and "AI Coaching Prompt" (Screen 6) merge into a single Screen 5; preset prompt fields replaced with free-text inputs; jailbreak + sandbox boxes removed (enforced globally per JFT); default model changed to gpt-4o-mini with OpenAI top-3 + OpenRouter browse-all; "Add topic" button wired to insert a new row; MD upload + download flow added.

### What changed (tenant_admin/index.html)

- **Screen 5 rebuilt end-to-end** as Step 3 of 4:
  - Model picker defaults to **gpt-4o-mini** (Recommended); top-3 alternatives are **gpt-4o** + **gpt-4-turbo** (all OpenAI). 1M / 1M token callout.
  - **"Browse all OpenRouter models"** `<details>` block expands to a 6-row table (Claude / Gemini / Llama / Mistral).
  - **Fallback chain** alert updated to OpenAI siblings.
  - **"Global coaching style"** → **"Coaching style"**. The 3 radio options (Socratic / Direct / Adaptive) stay.
  - **NEW inline "AI coaching prompt" section** below the coaching style:
    - **MD upload + download buttons** — preferred format `.md`. Upload disables the three text inputs.
    - **3 free-text inputs** with example placeholders (Student profile / Examples should be / Other), blank by default.
    - **Compiled prompt preview** column showing the assembled prompt.
- **Screen 6 deleted entirely.** Stub comment left in markup. `TOTAL_SCREENS` stays at 21 (max ID); arrow-key navigation has fall-through.
- **Step counter** on the remaining wizard screens: "of 5" → "of 4".
- **Meta-bar step-btn 06** removed from Flow A nav.
- **"Add Topic" button** on Screen 4 now wired to `addTopic()` — clones the last topic block, clears values, opens it, scrolls into view.

### Storyboard stamp

v4.74 across the 6 portals.

---

## v4.73 — 19 May 2026 — Subject → Skill terminology sweep

Brady's JFT direction: *"Make sure everything is 'topics' and 'learning objectives' for a 'skill'."* The prototype previously used "Subject" as the top-level concept; aligned to "Skill" across the user-visible UI and the persona READMEs. Topics + Learning Objectives stay as the canonical sub-units.

### What changed (user-visible)

**`tenant_admin/index.html`** (the heaviest target — ~40 unique strings):

- Section + heading: "Your Subjects" → "Your Skills", "Subject Lifecycle & Archival" → "Skill Lifecycle & Archival"
- Wizard steps: "Create a new Subject" / "Step 1 of 5 · Subject Details" / "Subject summary" → Skill variants
- Buttons + CTAs: "New Subject" / "Configure another Subject" / "Deactivate Subject" / "Create subject" → Skill variants
- Form labels: "Subject code" / "Subject title" / "Subject-domain limits" → Skill variants
- Identifier copy: "Subject ID" → "Skill ID"; Breadcrumb hub "Subjects" → "Skills"
- Analytics filter label + select id: `rep-subject` → `rep-skill`, "All subjects" → "All Skills"
- Table headers + counters + aria-labels — all swept
- "Course Configuration" → "Skill Configuration"

**`super_admin/index.html`** (Cost-spike screen + audit feed):

- "Top consuming subjects" → "Top consuming Skills"
- `<th>Subject</th>` → `<th>Skill</th>`
- Rate-limit + cap + JSON keys + audit event `subject.deploy` → `skill.deploy`
- Form ID `f-subject` → `f-skill`

**Root `index.html`** (LRPS landing illustrative URL): `lti/launch?subject=e010` → `lti/launch?skill=e010`

### What is NOT changed

- **"Program Subject"** form-field label — refers to the WGU program/course field that HOSTS a Skill, not the SkillProof internal entity.
- **"course code"** literal — preserved for URL-generation consistency.
- **"data subject rights"** in the GDPR compliance row — GDPR legal term, not the SkillProof concept.

### Storyboard stamp

v4.73 across the 6 portals.

---

## v4.72 — 19 May 2026 — Per-school branding (4 WGU School logos + Switch School)

Brady's JFT note: *"Add the custom branding for each of the 4 schools."* Each WGU School (Technology / Business / Education / Leavitt Health) now has its own logo swapped into the navbar based on the active tenant context. The Switch School menu in the Tenant Admin user profile expands from 2 to all 4 schools.

### What changed

- **8 new logo assets** copied from OneDrive `WGU FY26 Design System / School Logos`:
  - `assets/school-tech-{light,dark}.png`
  - `assets/school-business-{light,dark}.png`
  - `assets/school-education-{light,dark}.png`
  - `assets/school-health-{light,dark}.png`
- **tenant_admin navbar logos** → default to `school-tech-*` with `data-school-logo` markers
- **student/ + instructor/ navbars** → swap to school-tech default
- **super_admin, help, root** → stay WGU corporate (cross-tenant / utility surfaces)
- **Switch School menu** expanded from 2 schools to all 4
- **`switchSchool(name)` JS extended** with school slug map, tenant ID map, `applySchoolLogos()` helper, `localStorage` persistence under key `skillproof-active-school`, on-load restore
- **Tenant identity card** wired with `data-tenant-name`, `data-tenant-id`, `data-tenant-scope` attributes

### Storyboard stamp

v4.72 across the 6 portals.

---

## v4.71 — 19 May 2026 — Delete scenario-catalog pages and contract-tracking docs

Brady's direction: this repo is for the SkillProof UI prototypes only. Supporting docs (scenario catalogs, contract trackers) are no longer maintained in the public repo. They live in Coda.io now.

### What was deleted

- The 2 scenario-catalog HTML pages (light + dark variants)
- `_contract_tracking/CONTRACT_TRACKER.md`
- `_contract_tracking/SCREEN_JUSTIFICATIONS.md`
- `_contract_tracking/D3A_BUILD_PLAN.md`
- `_contract_tracking/README.md`
- All in-repo references to the above (badges, surface table rows, repo-layout tree, per-persona README "Catalog" links)

Note: git history still contains these files at older commits. No history rewrite was performed.

### What stays

The 6 UI surfaces (4 persona portals + LRPS root + Help) are now the entire repo deliverable. All future phases ship UI changes only.

### Storyboard stamp

v4.71 across all 6 portals.

---

## v4.70 — 19 May 2026 — Site-wide UI polish (help icon, footer logo, sign-out, timing copy)

Phase B of the JFT meeting follow-up sweep. Fixes UI bugs that have accumulated since v4.62 plus a copy cleanup.

### What changed

- **Light-mode help icon visibility** — the navbar help icon (and theme-toggle icon) was visually faint in light mode because the icon glyph color was inheriting from a dark-navbar context. Added explicit `color: var(--color-deep-navy)` + `font-weight: 500` for `.btn-theme-toggle .material-icons-outlined` in light mode, with `#fff` override for dark mode. Applied across all portal navbars.
- **Removed the Sign out button** from the Tenant Admin user-profile menu — Brady's JFT note: *"I don't think we need the sign out button."* Authentication is LRPS / SSO-managed.
- **"No more timing things"** — removed arbitrary duration copy that wasn't tied to a contractual SLA:
  - Student onboarding "Takes about 5–8 minutes" hint on the diagnostic CTA
  - Student session-snapshot "Session duration · 14 min" row
  - Analytics-page Median 18 min · per session deferred to Phase K (v4.79)
  - All SLA references preserved as contractual.

### Storyboard stamp

v4.70 across all 6 portals.

---

## v4.69 — 19 May 2026 — URGENT: LRPS landing reframed to Sally (Student) for leadership preview

Brady is sharing the storyboard URL with leadership for EOD review. The LRPS landing root was framed as Alice's (Tenant Admin's) view since v4.65, since Alice's role per User Profile Catalog v1.3 explicitly includes managing LRPS deep links. For the leadership preview, the framing reverts to Sally (Student) so the entry point matches what an end-learner actually sees when launching the Coding Coach from their LMS course module.

### What changed

- **`index.html`** meta-bar persona line: `Persona: Alice (Tenant Admin · manages SkillProof LRPS links per User Profile Catalog v1.3)` → `Persona: Sally (Student · this is the LRPS view a learner sees when launching the Coding Coach from their LMS course module)`.
- **`README.md`** LRPS Landing section "Persona:" line reverted to a Sally-centered description.
- **Storyboard stamps** → v4.69 across all 6 portals.

### Why

Direct quote from Brady's JFT meeting notes: *"LRPS link directing to /tenant-admin — Put this back to the /student view so I can send to leadership tomorrow at EOD."*

---

## Pre-v4.69 history

Earlier release entries (v4.0 – v4.68) are no longer tracked in this file. This is a prototype repo and incremental change documentation isn't a priority. Full commit history with file-level diffs is in git (`git log --all`).
