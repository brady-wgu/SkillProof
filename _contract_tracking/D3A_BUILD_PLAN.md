# D3a Build Plan — close the 7 true gaps in two themed surfaces

> **Internal WGU planning doc. Not product specification. JFT does not build from this file.**

**Direction sought:** WGU Program Development review and approval before any storyboard HTML changes proceed.

**Author:** WGU Program Development
**Date:** 12 May 2026
**Status:** Proposal — pending review

## Context

The v4.36 D3a re-audit reduced the active gap list from 9 to 7 Appendix A items. Those 7 cluster naturally into two themed surfaces:

| Theme | Contract rows | Where they belong |
|:---|:---|:---|
| **Data & Integrations** (5 rows) | A-6.28 GraphQL API, A-8.8 real-time/batch export, A-8.12 webhooks, A-8.13 GraphQL queries, A-8.14 data streaming | Super Admin portal (cross-tenant scope; v4.22 explicitly moved data-export scope to global / Super Admin) |
| **Support & Training** (2 rows) | A-9.14 self-service support portal, A-9.15 video training resources | New shared Help & Resources surface, accessible from all admin portals |

This document proposes what each surface should contain, what design language to use, and what acceptance criteria the storyboard needs to satisfy for the corresponding tracker rows to move from `Gap` to `Built` status.

The MVP at `wgu.teamjft.com` is unaffected by either theme. `student/index.html` remains frozen.

---

## Theme 1 — Data & Integrations (new Super Admin surface)

### Proposed location

A new Super Admin screen: `super-11 Data & Integrations Hub`. Adds to the existing Super Admin portal as the 11th screen (super_admin/index.html currently has 10 screens). Justification per `SCREEN_JUSTIFICATIONS.md`: Cross-tenant, JFT operates this surface during pilot, transitions to WGU IT post-pilot.

Linked from `super-02 Portal home` as a quick-link card alongside the existing four governance domain cards (Token Usage, Compliance, Geo-redundancy, Audit Log).

### Proposed contents (5 sections, all on one screen)

| Section | Contract row | What the storyboard should show |
|:---|:---|:---|
| Real-time + batch data export | A-8.8 | Two-column card layout: left "Real-time export" (live webhook stream toggle, last-event-received timestamp, retry count); right "Batch export" (schedule picker daily/weekly/monthly, format selector JSON/CSV/XML, last-batch metadata). Both cards link to the same underlying engagement-data pipeline. |
| Webhooks | A-8.12 | Subscribed-events list (table with columns Event Type, Endpoint URL, Signing key fingerprint, Status pill, Last delivery, Retry count). "Register endpoint" CTA opens a side panel form. Sample webhook payload preview in a code block (JSON, syntax-highlighted per the documented code-syntax palette extension). |
| GraphQL endpoint | A-6.28 + A-8.13 | Endpoint URL displayed, OAuth token status, GraphiQL or equivalent "Try a query" link out to external sandbox. Sample query and response in side-by-side code blocks. Depth-limit + complexity-limit metadata strip. |
| Data streaming | A-8.14 | Three provider cards (Kafka / Kinesis / Pub-Sub) with active/inactive status pill and configured topic count. Per-stream lag metric and last-event-flushed timestamp. "Configure stream" CTA opens an external link card (defers to the actual streaming infra dashboard, consistent with the v4.28 External Tooling pattern). |
| REST API reference | (Already covered by A-6.22, A-8.11) | Link card pointing to external Swagger documentation per SOW §2.4. Not a new contract row — just provides a connection point so the surface feels complete. |

### Design constraints

- SDP Design System v1.2 (Paragon + WGU FY26 brand tokens).
- The code-syntax palette extension is permitted for the JSON/GraphQL code blocks (already in use on `tenant-08` and the data console screens). Do not expand the extension to anything outside code blocks.
- The "external dashboard" pattern from `super-10 External Tooling` is the precedent for any control surface that lives outside the SDP (e.g., the actual Kafka admin console, the Swagger UI). Do not duplicate those controls inside the SDP.
- Cross-tenant scope must be visually clear: no per-tenant scoping breadcrumb, consistent with the rest of Super Admin.

### Tracker updates

After this screen ships:

- `CONTRACT_TRACKER.md` rows A-6.28, A-8.8, A-8.12, A-8.13, A-8.14 — Storyboard Coverage column updated from `Gap` to `super-11`; Build Status moves to `In Design`.
- `SCREEN_JUSTIFICATIONS.md` — new row `super-11` added with Primary Grounding listing the 5 contract IDs and Classification = Contract-required.
- `super_admin/index.html` total screen count: 10 → 11.
- `super_admin/README.md` Scenarios section — add a brief note about the new surface.

### Open design questions

1. Does the new surface count as part of `SC-ADD-04` (Super Admin Governance & Cost Audit) or warrant a new scenario ID (`SC-ADD-07` Data & Integrations Hub)?
2. Should the GraphQL endpoint display the actual schema sample inline, or just link to external GraphiQL? The latter is consistent with the v4.28 "don't duplicate" pattern but loses some demo fidelity.
3. Where on `super-02 Portal home` should the new quick-link card go — replacing an existing card, or extending the row from 4 → 5 cards (and how does that affect responsive layout)?

---

## Theme 2 — Support & Training (new shared Help & Resources surface)

### Proposed location

A new shared surface that all three admin portals (Tenant Admin, Instructor, Super Admin) and the student portal could link to. Two possible homes:

- **Option A — Single shared route at `/help/`** (new directory parallel to `lrps/`). Adds a 6th surface to the storyboard. Each admin portal navbar gets a "Help" entry; student portal links to it from a future v1.4 release (not in v4.x given the freeze).
- **Option B — Section on each admin portal's home screen.** No new surface; each portal home gets a "Help & Resources" section card linking to in-page or external documentation. Lower scope, lower fidelity.

Recommendation: **Option A** for full-fidelity coverage and reusability across personas. JFT can implement once and link from each portal.

### Proposed contents (single screen, `help-01`)

| Section | Contract row | What the storyboard should show |
|:---|:---|:---|
| Self-service support portal | A-9.14 | Search bar at top ("Search documentation..."). Three-card row underneath: "Get Started" (onboarding videos + quick-start guides), "Troubleshooting" (common-issue articles), "API Reference" (Swagger link). Below that, a "Recent updates" feed with the last 3-5 documentation changes. Bottom-right floating "Contact JFT Support" button (links to Jira ticket creation, consistent with the existing `tenant-16` workflow). |
| Video training resources | A-9.15 | Video gallery — three rows of three video tiles. Each tile: thumbnail, title, duration, role tag (Student / Instructor / Tenant Admin / Super Admin). Filter chips above to show videos for one role at a time. The first row is "New here? Start with these 3." |

### Design constraints

- Same SDP Design System v1.2 chrome as the other admin portals.
- Video tile thumbnails are illustrative — no need for real video assets in the storyboard. Use placeholder coloured rectangles with a play-button icon overlay.
- Search bar is non-functional in the storyboard (it's design spec, not production code).
- "Contact JFT Support" CTA on the support portal should mirror the Jira ticket workflow on `tenant-16` so the visual pattern is consistent.

### Tracker updates

After this surface ships:

- `CONTRACT_TRACKER.md` rows A-9.14, A-9.15 — Storyboard Coverage column updated from `Gap` to `help-01`; Build Status moves to `In Design`.
- `SCREEN_JUSTIFICATIONS.md` — new row `help-01` added with Primary Grounding A-9.14 + A-9.15 and Classification = Contract-required. Persona = shared (Sally / Charlie / Alice / Bob / LRPS all eligible).
- New top-level repo folder `help/` with `index.html`, `README.md`, `screenshots/`, `screenshots_dark/` following the established 5-surface pattern.
- Root `README.md` updated: surface count 5 → 6; persona table extended to note Help & Resources is shared.
- All four admin portal navbars get a "Help" link entry.

### Open design questions

1. Recommended Option A (new shared surface) vs Option B (section on each portal home)?
2. Does the Help & Resources surface get its own scenario ID (`SC-ADD-07` or `SC-ADD-08` depending on ordering with the Data & Integrations hub)?
3. Should the video tiles show real (placeholder) titles like "Getting Started with the Coding Coach" or stay generic ("Onboarding Video #1")? Generic is safer per the JFT-literal-builders rule (no risk of JFT building from invented titles); real titles are more demonstrably useful for stakeholder reviews.

---

## Sequencing recommendation

Build Support & Training first (smaller, lower-risk, fewer design questions to settle), then Data & Integrations (5 rows in one surface, more substantive). Each as its own focused PR.

Estimated effort once design choices are settled:

- Support & Training (`help-01` surface): one new screen, one new persona-style folder, ~3 hours of HTML composition + screenshots regeneration.
- Data & Integrations Hub (`super-11`): one new screen in the existing super_admin folder, ~4 hours of HTML composition + screenshots.

Both leave the MVP completely untouched.

---

## What this document is NOT

- Not an authorization to build. WGU Program Development review and approval comes first.
- Not a UI mockup. Layout descriptions here are intent-level, not pixel-level. Actual layout will be designed in-place during HTML composition.
- Not a contract amendment. The 7 underlying contract rows are unchanged; this doc only specifies how the storyboard will demonstrate coverage for them.

---

*WGU confidential. Author: WGU Program Development. Not for redistribution outside WGU.*
