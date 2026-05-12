# LRPS Landing — Entry point for the admin portals

[← Back to root README](../README.md) · [Live LRPS](https://brady-wgu.github.io/JFT_SDP/lrps/)

![LRPS landing hero](screenshots/lrps.png)

## What this is

A recreation of WGU's internal **Learning Resource Provisioning System (LRPS)**, styled in the SDP Design System v1.2. The real LRPS is a legacy enterprise admin tool that lives behind WGU SSO; the original (linked in the storyboard) is at `lrps.wgu.edu/provision/...`. **JFT does not build LRPS** — it's modeled here only to make the deep-link source feel authentic.

## Why it exists in the storyboard

Each persona's secret LRPS deep link is what gets them into their respective admin portal. So the realistic flow is:

1. WGU staff (the LRPS admin) opens LRPS
2. They locate the appropriate provider row (e.g., "SDP Tenant Admin Portal — Course Configuration")
3. They click → deep link launches → the persona's portal opens with the SSO landing screen
4. SSO completes, role is mapped, the persona is in their portal

This LRPS landing models step 2. The four live SDP rows (Student, Tenant Admin, Instructor, Super Admin) are clickable and deep-link straight into the corresponding portal HTML in this storyboard.

## What's in the table

| Type | Count | Behavior |
|:-----|:-----:|:---------|
| **Live SDP rows** | 4 | Clickable → launch the corresponding portal (Student, Tenant Admin, Instructor, Super Admin) |
| **Illustrative filler rows** | many | Static, not clickable. Mix of real WGU LRPS provider types: OEX modules, zyBooks, Pearson MyMathLab, ProctorU, Coursera, Cicada legacy, Panopto, OEX Studio, Instructional Designer Review, etc. |
| **Inactive rows** | 1 | "Cicada PoC v1.0 (Retired)" — demonstrates the "Show Inactive Providers" toggle behavior |

The table also has a sidebar quick-launch section that links directly to the three SDP admin portals, and a meta-bar at the bottom with quick-launch chips to all 5 surfaces + the catalog.

## LMS → LRPS → LTI provisioning chain (student-facing flow)

LRPS is what produces the **student-facing** Coding Coach link as well. The provisioning chain that gets Sally into the SDP from her zyBooks course page works like this:

1. **WGU's D&D (Design & Development) team** registers the SDP Coding Coach as an LRPS provider — a row in the LRPS provider table similar to the SDP-TA / SDP-IN / SDP-SA admin rows shown in this storyboard, but configured as a student-facing resource (no MFA, learner role mapping).
2. **The D&D team places an LRPS-generated link** on the relevant zyBooks E010 course page. zyBooks (Wiley) renders it as a "Coding Coach" button next to the Competencies section — that's the button you see on Screen 1 of every SC-MVP scenario.
3. **Sally clicks the button**. Because she's already authenticated to the WGU LMS, LRPS handles SSO transparently — there's no second login prompt.
4. **LRPS issues an LTI 1.3 launch** to the SDP platform. The LTI payload carries Sally's WGU student ID, course context (E010), and role (`Learner`).
5. **The SDP receives the launch**, looks up or creates Sally's session against her WGU student ID, and opens the Coding Coach welcome screen.

Important properties of this chain:

- **JFT does not own LMS-side link placement.** The D&D team manages all LMS resource links. JFT's responsibility is to expose a stable launch URL that does not change when course content is reorganized.
- **The launch URL must be stable.** If JFT changes the launch endpoint, every LMS link breaks until D&D re-provisions them through LRPS. Versioning the launch endpoint is therefore a coordination cost, not a free refactor.
- **Per-persona deep links use the same chain.** The admin portals (Tenant Admin, Instructor, Super Admin) are provisioned the same way as the student Coding Coach link, but with admin role mappings and (for Super Admin) MFA enforced at the LRPS level. The "Quick Launch · Live" sidebar in this LRPS landing demonstrates the admin-side equivalent.
- **Basic LTI 1.3, not LTI Advantage.** No grade passback, no NRPS, no deep-linking content selection. The student MVP scope deliberately avoids LTI Advantage to keep FERPA scope minimal and the integration surface small.

The LRPS integration and its role in the LTI launch flow were reviewed with JFT by the WGU LRPS team on 06 Apr 2026.

## Files

- [`index.html`](index.html) — single-page LRPS landing
- `screenshots/lrps.png` — light-theme screenshot
- `screenshots_dark/lrps.png` — dark-theme screenshot

## Visual style

The LRPS landing was originally rendered in the legacy enterprise Bootstrap aesthetic (matching the actual internal tool). It was **restyled with the SDP Design System v1.2** in commit `e735361` so it reads as part of the SDP product family. Notable patterns:

- Standard SDP navbar (navy + WGU FY26 corporate logo + dark mode toggle + product chip + user avatar)
- Sidebar nav as an SDP card (Learning Resources / Search / Quick Launch · Live)
- `.pgn__data-table` styling for the provider table — sticky header with sortable arrow icons, status pills (green dot + "Active" / gray dot + "Inactive"), Lato monospace for description / driver-class columns
- Live SDP rows tinted Ice Blue with a 4px brand-blue left edge and a "Launch ↗" link in the actions column
- SDP-styled pagination footer with `.btn-tertiary` icon buttons and form-control pager input

## Notes

- The **DEMO ONLY banner** at the top of the table makes it clear to anyone landing here that this is a recreation, not the real LRPS.
- Container max-width is `1920px` to use the full widescreen viewport — the real LRPS is a data-dense admin tool, and the SDP's default 1192px container made the table too cramped (see commit `8704b3b` for the layout fix).
- The user avatar shows "Lana" because the real LRPS shows the logged-in WGU admin's identity. In the storyboard context, Lana is the fictional LRPS admin persona who provisions the deep links for Alice, Charlie, and Bob.

## Custom integration boundary for WGU's distributed LMS

WGU does not use a single off-the-shelf LMS (Canvas, Blackboard, Brightspace). It operates a distributed system across multiple platforms with LRPS as the in-house provisioning layer. Generic "LTI 1.3 compliance" claims from vendors do not, by themselves, guarantee compatibility with WGU's environment. Integration testing against the actual LRPS provider table, identity flows, and deep-link URI patterns is required. Any LRPS-specific integration work that goes beyond baseline LTI 1.3 (custom claim shapes, sub-tenant scoping, custom deep-link parameters) is scoped explicitly between JFT and WGU rather than assumed to be free.
