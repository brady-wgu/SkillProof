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
| **SC-ADD-04** | **Super Admin Governance & Cost Audit.** LRPS landing → SSO + MFA (SAML 2.0 SP per §16.3 #8.2; MFA per §16.5 #10.18) → portal home (4 KPI gauges + active alerts + recent platform events + 4 quick-link cards) → Token Usage Tracking (per-tenant breakdown with utilization meters; PDev flagged with spike) → cost-spike drill-down (30-bar daily cost chart, top consuming subjects, "likely cause" diagnosis) → Global Rate Limits config (form + before/after projection + pending audit-trail entry preview) → **Compliance Report — TLS 1.3 + FERPA** (encryption audit §10.7 across all data paths + FERPA privacy audit §10.1 with 4 KPI gauges and a 16-row FERPA control table referencing 34 CFR §§99.10 / 99.31 / 99.32 / 99.37 plus generic WGU institutional policies covering data breach drills and staff FERPA training, with explicit SOW §16.5 control rows added in v4.18: SOC 2 Type II (#10.6), ISO 27001 (#10.13), zero-trust authorization (#10.14), GDPR (#10.12), annual penetration testing (#10.10), AES-256 at rest with cloud KMS (#10.16), MFA for privileged accounts (#10.18), threat detection / SIEM (#10.15), vulnerability scanning + 48-hr critical patch SLA (#10.9 + #10.19), and BC/DR with RTO ≤ 4hr + RPO ≤ 60min (#10.20 + §16.4 #9.4)) → Geo-redundancy (3 region cards with replication lag, recent failover tests, RTO under 4-hr target) → cross-tenant audit log feed. | 8 |

**Total: 1 scenario · 8 screens.**

## Source

JFT SDP User Scenario Catalog: Additional Scenarios **v1.3** (05 May 2026). Authored by WGU Program Development.

## SOW references

§6.4 (Rate Limiting), §6.6 (Token Tracking), §9.5 (Geo-redundancy / SLA), §10.1 (FERPA), §10.4 (Audit Logging), §10.7 (Encryption).

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
- The Compliance Report on screen 6 covers both encryption (§10.7) and FERPA (§10.1) — TLS 1.3 verification across all data paths plus FERPA privacy controls including staff training, audit retention, data deletion thresholds, and explicit FERPA control mapping to 34 CFR sections.
- The cross-tenant audit log on screen 8 deliberately includes events from all the other v1.3 personas (Alice, Charlie, JFT CSM, system) so you can see how cross-tenant operations are surfaced to the Super Admin role.
