# Contract tracking — WGU internal

> **This folder is WGU contract tracking. It is NOT product specification. JFT must not build features for content in this folder.**

This subfolder holds Brady's contract-defense artifacts for the JFT SDP engagement. Two trackers establish bidirectional traceability between the signed JFT MSA / SOW (executed 03 Mar 2026) and the storyboard:

| File | Direction | Question it answers |
|:---|:---|:---|
| [`CONTRACT_TRACKER.md`](CONTRACT_TRACKER.md) | Contract → Storyboard | For each contract requirement, where is it in the storyboard? Is JFT building it? |
| [`SCREEN_JUSTIFICATIONS.md`](SCREEN_JUSTIFICATIONS.md) | Storyboard → Contract | For each storyboard screen, what contract requirement does it satisfy? Why does the screen exist? |

## Why this folder exists

The storyboard at `brady-wgu/JFT_SDP` is the visual North Star JFT builds against. The storyboard intentionally contains only the UI elements the production SDP should ship with. It carries no inline contract citations, no annotations, no commentary, no implementation guidance. Anything visible in the storyboard is a build instruction.

Contract traceability lives here instead. When a question arises about whether a feature is in scope, the trackers in this folder are the source of truth — not anything in the storyboard itself.

## Folder boundary rules

- **Build rule for JFT:** Content in this folder is not part of the SDP product. Do not implement anything described here unless it is also reflected in the storyboard (which is the build spec).
- **Build rule for the storyboard:** Storyboard HTML must contain only production-bound UI. Contract IDs, traceability notes, and audit commentary go here, never in the storyboard.
- **Visibility rule:** Folders prefixed with a leading underscore are excluded from the Jekyll/GitHub Pages build by default, so the live storyboard at `https://brady-wgu.github.io/JFT_SDP/` does not surface these files.

## File status

| File | Status | Last updated |
|:---|:---|:---|
| `CONTRACT_TRACKER.md` | v1.0 — initial baseline | 12 May 2026 |
| `SCREEN_JUSTIFICATIONS.md` | v1.0 — initial baseline | 12 May 2026 |

## Defense narrative

When JFT pushes back on a feature or screen, the response is deterministic:

1. Locate the screen in `SCREEN_JUSTIFICATIONS.md`. Read the Primary Grounding column.
2. Locate the contract requirement in `CONTRACT_TRACKER.md`. Confirm JFT Commitment is Yes or referenced under SOW §2.5 build scope.
3. Send JFT the row IDs.

When JFT claims a feature is missing from the storyboard:

1. Locate the requirement in `CONTRACT_TRACKER.md`.
2. If Storyboard Coverage is Gap, concede and add the screen in a follow-up commit. If it is a screen anchor, send the anchor.

No conversation about extra work happens without these IDs.

---

*WGU confidential. Author: Brady Redfearn, Program Development. Not for redistribution outside WGU.*
