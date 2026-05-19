# Changelog

All notable changes to the SkillProof storyboard. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

The repo's storyboard version (`Storyboard vN.M`) tracks the visual prototype, not the underlying SkillProof product version that JFT is building. The SkillProof product follows the user scenario catalog versions (v1.2 MVP, v1.3 Additional, etc.).

This is a prototype repo — entries below cover the active JFT meeting follow-up phases (v4.69 – v4.81). Earlier history exists in git but isn't tracked here.

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
