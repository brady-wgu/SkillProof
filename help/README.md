# Help & Resources — shared surface

[← Back to root README](../README.md) · [Live surface](https://brady-wgu.github.io/JFT_SDP/help/)

## What this is

A shared documentation, training, and support surface for the JFT SDP. Closes two Appendix A items that previously had no storyboard coverage:

- **§16.4 #9.14 Self-service support portal** — search bar, three documentation-domain cards (Get Started, Troubleshooting, API Reference), recent updates feed, and a floating Contact JFT Support button.
- **§16.4 #9.15 Video training resources** — role-filtered video gallery with a "Start with these three" featured callout, plus nine illustrative video tiles spanning all four personas.

## Persona

Shared. Accessible from every admin portal (Tenant Admin / Instructor / Super Admin) via a Help link in the portal navbar, and reachable from the root portal selector. Linkable from the student portal in a future release (the student portal is frozen at v1.2 MVP).

## Scope

- Self-service documentation surfaces, role-filtered video library, JFT Support escalation entry point.
- The search bar is non-functional in the storyboard (design spec, not production code).
- Video thumbnails are placeholder gradient blocks with a play-icon overlay — no real video assets ship with the storyboard.
- The "Contact JFT Support" floating button mirrors the Jira ticket workflow on `tenant-16`. Clicking it in production opens a pre-filled P1/P2/P3 ticket form per the SOW §9.1 + §9.4 support channels.

## SOW references

§16.4 #9.14 (Self-service support portal); §16.4 #9.15 (Video training resources); supporting: §9.1 (Support Plan), §9.4 (Support channels), §9.11 (Comprehensive documentation and user training materials).

## Files

- [`index.html`](index.html) — single-page surface (search bar + 3 cards + updates feed + video gallery + floating Contact button)
- `screenshots/` — light-theme PNG (capture via `capture_screens.py`)
- `screenshots_dark/` — dark-theme PNG (same)

## Components introduced in this surface

- **`.search-wrap`** — full-width pill search bar with leading search icon and trailing keyboard-hint chip.
- **`.card-grid`** — 3-column responsive card layout for documentation domains.
- **`.updates-feed`** — vertical list of update entries with status tags (New / Updated) and inline metadata.
- **`.role-chips`** — pill-shaped filter chips with active state for role-based video filtering.
- **`.featured-callout`** — full-width gradient banner highlighting onboarding videos.
- **`.video-tile`** — 16:9 thumbnail with duration overlay and metadata strip below.
- **`.contact-fab`** — fixed-position floating action button anchored bottom-right for support escalation.

## Notes

- Container max-width matches the rest of the storyboard (1192px) for visual consistency across surfaces.
- Theme toggle in the navbar persists user preference via `localStorage` (`sdp-theme` key) — same pattern as the other surfaces.
- Video tile thumbnails use three gradient alternates (default navy, bright-blue, amber-orange) cycled across the gallery to provide visual variety without requiring real video assets.
- The floating Contact button stays anchored bottom-right regardless of scroll position. Production should preserve that positioning for predictability.
- All copy is illustrative. Production video titles, documentation article titles, and update entries should be sourced from the actual content library WGU and JFT build during the engagement.

## Future enhancements (post-v4.38)

- Role-filter chip filtering JS hook is currently visual-only — production should filter the video grid.
- Search bar non-functional in storyboard; production needs full-text search across documentation + video transcripts.
- Recent updates feed currently shows static items; production should pull from a CMS or markdown file.
- Video tile click handlers are placeholders; production should open an inline player modal or external video host.
