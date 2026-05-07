# Student — Sally · v1.2 MVP

[← Back to root README](../README.md) · [Live storyboard](https://brady-wgu.github.io/JFT_SDP/student/) · [Catalog (light)](../presentation.html#sc-mvp-01) · [Catalog (dark)](../presentation_dark.html#sc-mvp-01)

![Student storyboard hero](screenshots/sc-mvp-01_step02_screen02.png)

## Persona

**Sally** — WGU student in **E010 Foundations of Programming (Python)**. Knowledge level varies (Beginner / Intermediate / Advanced). Launches the Coding Coach from her zyBooks course page via LTI 1.3.

## Scope

This is the **v1.2 MVP scope** — the first JFT release. It deploys the existing Cicada v1 proof-of-concept codebase to production-quality, scalable infrastructure with a polished UI, accessible outside the WGU intranet via LTI 1.3 SSO. **No new features, adaptive logic changes, or coaching algorithm modifications are in scope for the v1.2 release.**

## Scenarios

| ID | Flow | Screens | What happens |
|:---|:-----|:-------:|:-------------|
| **SC-MVP-01** | Basic | 8 | First launch. New student with no Python knowledge completes diagnostic, views progress map, begins first coaching task, saves session. |
| **SC-MVP-02** | Advanced | 11 | Progressive coaching with targeted feedback. Partial Python knowledge → diagnostic → foundational coaching → incorrect answer with specific error feedback → gap-resolution verification → difficulty advance. |
| **SC-MVP-03** | Professional | 9 | Experienced developer fast-tracks. Diagnostic demonstrates mastery across all sub-sections. One verification task required for Functions & Modular Programming. |
| **SC-MVP-04** | Returning | 6 | Student returns after multi-week break. Prior progress preserved. Re-assessment verifies retention before resuming coaching at prior difficulty level. |

**Total: 4 scenarios · 34 screens.**

## Source

JFT SDP MVP Scenario Catalog **v1.2** (07 Apr 2026). Authored by Brady Redfearn, WGU Program Development.

## SOW references

§8.1, §8.4 (LTI / fallback), §7.1–7.3 (UX / Accessibility), §6.1–6.7 (AI Orchestration / Safety).

## Files

- [`index.html`](index.html) — interactive storyboard (34 screens)
- `screenshots/` — 34 light-theme PNGs at 1440×900
- `screenshots_dark/` — 34 dark-theme PNGs at 1440×900

## Navigation

- **Arrow keys** step through screens
- **Meta-bar at bottom** has scenario-grouped numbered jump buttons
- **Theme toggle** in the top-right header (preference persists via `localStorage`)

## Notes

- The student storyboard logo loads via inline base64 (legacy from v3.0). The v1.3 admin portals load logos from `../assets/` instead. This is intentional — base64 keeps the student page fully self-contained for offline LTI launch demos, even without the broader repo.
- Real Python execution is **not** modeled in the MVP. Submitted code is evaluated by the LLM as text. JFT should flag any sub-sections in the v1 codebase where text-based LLM evaluation is insufficient for reliable competency assessment.
