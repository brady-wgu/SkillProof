# Super Admin — Bob · v1.3

[← Back to root README](../README.md) · [Live portal](https://brady-wgu.github.io/JFT_SDP/super_admin/) · [Catalog](../presentation.html#sc-add-04)

![Super Admin Portal hero](screenshots/sc-add-04_step02_screen02.png)

## Persona

**Bob** — WGU platform operations and infrastructure. Authenticates via his own secret LRPS deep link **plus MFA**. Cross-tenant scope: he sees every tenant on the platform and can act on global resource limits.

## Scope

Cross-tenant governance, financial controls, security compliance, global resource management. Bob's responsibilities span billing/cost (token usage, rate limits), security/compliance (TLS 1.3, FERPA), and operational resilience (geo-redundancy, audit log).

## Scenarios

| ID | Description | Screens |
|:---|:------------|:-------:|
| **SC-ADD-04** | **Super Admin Governance & Cost Audit.** LRPS landing → SSO + MFA → portal home (4 KPI gauges + active alerts + recent platform events) → Token Usage Tracking (per-tenant breakdown with utilization meters; PDev flagged with spike) → cost-spike drill-down (30-bar daily cost chart, top consuming subjects, "likely cause" diagnosis) → Global Rate Limits config (form + before/after projection + pending audit-trail entry preview) → Compliance Report (TLS 1.3 across 17 services + cert validity + cipher) → Geo-redundancy (3 region cards with replication lag, recent failover tests, RTO under 4-hr target) → cross-tenant audit log feed. | 8 |

**Total: 1 scenario · 8 screens.**

## Source

JFT SDP User Scenario Catalog: Additional Scenarios **v1.3** (05 May 2026). Authored by Brady Redfearn, WGU Program Development.

## SOW references

§6.4 (Rate Limiting), §6.6 (Token Tracking), §10.7 (Encryption), §9.5 (Geo-redundancy / SLA), §10.1 (FERPA Compliance).

## Files

- [`index.html`](index.html) — interactive storyboard (8 screens)
- `screenshots/` — 8 light-theme PNGs at 1440×900
- `screenshots_dark/` — 8 dark-theme PNGs

## Components introduced in this portal

- **`.spike-card`** + **`.spike-chart`** — 30-bar CSS daily cost trend (no SVG; just `<div>` bars with height % styling). Last days of the spike are highlighted via `.spike` and `.spike.danger` classes.
- **`.util-meter`** — inline mini-bar with right-aligned numeric value (used in the per-tenant token-usage table)
- **`.region-card`** — region card with side-stripe color (success / warning / danger), region name + location, and stat-row table
- **`.gauge-card`** with `.center` variant — KPI gauges (numeric + label + thin progress bar + target sub-text)
- **`.gauge-number`** color variants (`good`, `warning`, `danger`)
- Pending-audit-trail preview panel on the Rate Limits screen — shows the audit log entry that will be written when "Apply" is clicked

## Notes

- The portal models a privileged session: the SSO landing on screen 1 includes an MFA verification step + a "Privileged session" warning that all actions are logged to the cross-tenant audit trail.
- Cost spike workflow on screens 3-5 is end-to-end: identify the high-consumption tenant (PDev) → drill down to see the 30-day trend with last 4 days as a visible spike → adjust rate limits → see the projected effect (MTD spend back inside budget) → "Apply" writes an audit log entry.
- The Compliance Report on screen 6 shows 10 of 17 TLS-1.3 services in the inline table, with a note that 7 additional internal services pass identically (full report in PDF export).
- The cross-tenant audit log on screen 8 deliberately includes events from all the other v1.3 personas (Alice, Charlie, JFT CSM, system) so you can see how cross-tenant operations are surfaced to the Super Admin role.
