# Contract Requirements Tracker — Contract to Storyboard

> **Internal WGU tracker. Not product specification. JFT does not build from this file.**

**Direction:** Contract → Storyboard. For each binding requirement in the MSA and SOW, where is it in the storyboard? Is JFT building it?

**Version:** v1.0 (initial baseline)
**Date:** 12 May 2026
**Author:** WGU Program Development
**Source:** Signed JFT MSA / SOW (executed 2026)
**Storyboard baseline:** brady-wgu/JFT_SDP at v4.41

## How to read this file

Every binding requirement in the contract appears exactly once. Each row carries:

- **ID** — stable identifier. `MSA-N` for MSA sections, `SOW-N.N` for SOW core, `A-N.N` for Appendix A items.
- **Requirement** — abridged contract text. Refer to the signed PDF for the verbatim wording.
- **Type** — Legal / Process / Feature / Operational / Compliance.
- **JFT Commitment** — Yes / No / Partial / N/A (legal terms binding both parties without a Yes/No checkbox).
- **Storyboard Coverage** — specific screen IDs (matching `SCREEN_JUSTIFICATIONS.md`) where this requirement is visualized. **Gap** means no prototype representation yet. **Non-visual** means the requirement is not expressible as a screen (legal / process / infrastructure).
- **Build Status** — Not Started / In Design / In Dev / Built / Tested / Deployed. WGU updates this column as JFT delivers each row.
- **Owner** — JFT / WGU / Both.
- **Acceptance** — what "Deployed" looks like for this row.
- **Notes** — caveats, dependencies, related rows.

## Section index

- [MSA §§ 1-16](#msa-master-services-agreement) — 30 rows (legal / process / FERPA / security breach / governing law)
- [SOW §§ 1-15 core](#sow-statement-of-work-core) — 28 rows (scope, technology stack, support plan, team, terms)
- [SOW Appendix A § 16.1 Technical](#appendix-a-161-technical-requirements) — 28 rows
- [SOW Appendix A § 16.2 User Experience and Design](#appendix-a-162-user-experience-and-design) — 14 rows
- [SOW Appendix A § 16.3 Integration](#appendix-a-163-integration-requirements) — 15 rows
- [SOW Appendix A § 16.4 Operational](#appendix-a-164-operational-requirements) — 15 rows
- [SOW Appendix A § 16.5 Compliance and Security](#appendix-a-165-compliance-and-security-requirements) — 20 rows
- [Totals and verification](#totals-and-verification)

---

## MSA — Master Services Agreement

Status convention for MSA rows: most are legal/process obligations that are "Always Active" once signed (not deployable features). For those, Build Status reads `Active` rather than progressing through Dev/Test/Deployed.

| ID | Source | Requirement | Type | Commitment | Storyboard Coverage | Build Status | Owner | Acceptance | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| MSA-1 | MSA §1 | Provider provides Services per SOW; SOW specifies scope, fees, timeline; acceptance based on substantial conformance | Process | N/A | Non-visual | Active | Both | SOW signed; deliverables match | Operational since 2026. |
| MSA-2.a | MSA §2.a | Payment per net terms with WGU PO; final invoice within 30 days of SOW completion | Process | N/A | Non-visual | Active | JFT | Invoices follow contract terms | Excludes taxes. |
| MSA-2.b | MSA §2.b | Out-of-pocket expenses require pre-approval in writing | Process | N/A | Non-visual | Active | JFT | Pre-approval emails on file | |
| MSA-2.c | MSA §2.c | Provider invoices no later than 90 days after month services rendered; otherwise waives right to payment | Process | N/A | Non-visual | Active | JFT | All invoices within 90-day window | WGU defense against late-billing claims. |
| MSA-2.d | MSA §2.d | All fees invoiced by and paid to Jellyfish Technologies Ltd., India | Process | N/A | Non-visual | Active | Both | Payments routed to India entity | |
| MSA-3 | MSA §3 | Term: 12 months from Effective Date or active SOW period, whichever later | Legal | N/A | Non-visual | Active | Both | Term in effect 2026 onward | |
| MSA-3.a | MSA §3.a | WGU may terminate without penalty with 30 days written notice | Legal | N/A | Non-visual | Active | WGU right | Notice path documented | |
| MSA-3.b | MSA §3.b | Termination for cause: material breach + 15-day cure; insolvency or 50%+ ownership change triggers immediate termination | Legal | N/A | Non-visual | Active | Both | Cure procedures documented | |
| MSA-3.c | MSA §3.c | Individual SOW termination for convenience with 10 days notice | Legal | N/A | Non-visual | Active | Both | | |
| MSA-3.d | MSA §3.d | Upon termination: pay amounts due, refund unearned, return/destroy Confidential Information within reasonable time | Legal | N/A | Non-visual | Active | Both | Return / destruction certificate on request | |
| MSA-4.a | MSA §4.a | Each party warrants authority + no conflicting prior commitments | Legal | N/A | Non-visual | Active | Both | | |
| MSA-4.b.i | MSA §4.b.i | Services performed in professional, ethical, efficient manner per industry standards | Legal | N/A | Non-visual | Active | JFT | Quality standard | |
| MSA-4.b.ii | MSA §4.b.ii | Services conform in all material respects to SOW specs | Legal | N/A | Non-visual | Active | JFT | Specs satisfied | |
| MSA-4.b.iii | MSA §4.b.iii | Services do not infringe third-party IP rights | Legal | N/A | Non-visual | Active | JFT | No IP infringement claims | |
| MSA-4.b.iv | MSA §4.b.iv | Compliance with all applicable laws, permits, licenses | Legal | N/A | Non-visual | Active | JFT | | |
| MSA-4.b.v | MSA §4.b.v | Commercially reasonable measures to not introduce viruses / harmful code | Legal | N/A | Non-visual | Active | JFT | Code scanning evidence | |
| MSA-5 | MSA §5 | Provider maintains records; provides Customer reasonable access; T&M records include hours, rate, dates | Process | N/A | Non-visual | Active | JFT | Records available within 30 days of WGU request | Fixed-cost SOW; T&M not currently engaged. |
| MSA-6.a | MSA §6.a | Confidential Information defined; includes business info, trade secrets, curricula, content, student/employee info | Legal | N/A | Non-visual | Active | Both | | |
| MSA-6.b | MSA §6.b | Non-disclosure standard of care: no third party without consent, no employees/contractors except as needed | Legal | N/A | Non-visual | Active | Both | Confidentiality breaches escalated per MSA-11 | |
| MSA-6.c | MSA §6.c | **FERPA**: WGU designates JFT a school official; JFT maintains education records per FERPA | Compliance | N/A | Non-visual (operational) | Active | JFT | FERPA-compliant data handling; staff training documented | Cross-references A-10.1, A-10.2, A-10.3. School-official designation effective 2026. |
| MSA-6.d | MSA §6.d | Confidential Information exclusions (lawful prior possession, independent development, public knowledge) | Legal | N/A | Non-visual | Active | Both | | |
| MSA-7 | MSA §7 | IP retention by each party; Customer data is WGU's; feedback is not Confidential | Legal | N/A | Non-visual | Active | Both | | |
| MSA-8.a | MSA §8.a | **Work-for-hire**: SDP output is WGU's exclusive property to the extent permitted by law | Legal | N/A | Non-visual | Active | JFT | All deliverables transferred to WGU | Critical for post-pilot WGU operational handoff. |
| MSA-8.b | MSA §8.b | Assignment of IP if not deemed work-for-hire; cooperation in establishing WGU's rights | Legal | N/A | Non-visual | Active | JFT | Assignment documents executed on request | |
| MSA-8.c | MSA §8.c | Pre-existing JFT materials in work product: WGU gets irrevocable worldwide license | Legal | N/A | Non-visual | Active | JFT | Pre-existing materials license documented | |
| MSA-9 | MSA §9 | Use of name/logo/publicity requires prior written consent | Legal | N/A | Non-visual | Active | Both | | |
| MSA-10 | MSA §10 (a-e) | **Information Security & Use of Data**: data protection, security measures, retention (60 days max post-termination), subcontracting consent, de-identified data | Compliance | N/A | Non-visual (operational) | Active | JFT | Encryption in transit/rest; certificate of deletion on request; subcontractor consent on file | Cross-references A-10.x compliance rows. |
| MSA-11 | MSA §11 (a-b) | **Security Breach**: 24-hour telephone + email notification; mitigation; reimburse forensic + credit monitoring + identity restoration | Compliance | N/A | Non-visual (operational) | Active | JFT | Breach notification procedure documented and tested | 24-hour notification window critical. |
| MSA-12 | MSA §12 | Provider supports additional third-party technologies as reasonably needed | Process | N/A | Non-visual | Active | JFT | | |
| MSA-13 | MSA §13 | LIMITATION ON DAMAGES: no indirect/incidental/consequential damages, with exclusions for indemnification, confidentiality, IP, willful misconduct | Legal | N/A | Non-visual | Active | Both | | |
| MSA-14.a | MSA §14.a | Mutual indemnification for breaches, willful misconduct, law violations; JFT additionally for IP infringement | Legal | N/A | Non-visual | Active | Both | | |
| MSA-14.b | MSA §14.b | Each party maintains insurance covering obligations | Process | N/A | Non-visual | Active | Both | Certificates of insurance on file | |
| MSA-15.a | MSA §15.a | Nondiscrimination | Legal | N/A | Non-visual | Active | Both | | |
| MSA-15.b | MSA §15.b | **Digital Accessibility**: WCAG Level AA conformance; accessibility maintained through upgrades; parity with other JFT customers | Compliance | N/A | All persona screens (universal) | In Dev | JFT | WCAG 2.2 AA audit pass; ACR / VPAT current | WGU runs independent accessibility testing per WGU Tech Context. Cross-references A-7.3. |
| MSA-16 | MSA §16 (a-k) | General provisions: entire agreement, counterparts, precedence, no relationship, assignment, notices, dispute resolution, governing law (Utah / Salt Lake County), force majeure, waiver, attorney fees | Legal | N/A | Non-visual | Active | Both | | Utah law / Salt Lake County exclusive jurisdiction. |

MSA totals: 30 rows. All Active. 28 Non-visual; MSA-15.b Digital Accessibility intersects every persona screen.

---

## SOW — Statement of Work core

| ID | Source | Requirement | Type | Commitment | Storyboard Coverage | Build Status | Owner | Acceptance | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| SOW-1 | SOW §1 Introduction | SDP: production-ready, scalable, secure, multi-tenant SaaS built from prototype | Process | Yes | All persona portals | In Dev | JFT | Production SaaS deployed | Full SOW scope, not MVP-only (per WGU direction). |
| SOW-2.2 | SOW §2.2 Discovery | Workflow docs for Students / AI Engine / Tenant Admin / Super Admin; technical architecture outline; implementation roadmap; backlog | Process | Yes | Non-visual (delivered as documents) | In Dev | JFT | Workflow docs, architecture doc, roadmap, backlog approved by WGU | Roles cross-reference User Profiles v1.2. |
| SOW-2.3 | SOW §2.3 UX/UI Design | Designing UI/UX, WCAG 2.2 AA, iterative reviews, UI component library | Process | Yes | All persona portals | In Dev | JFT | High-fidelity designs + component library | Storyboard is the visual spec. |
| SOW-2.4 | SOW §2.4 Architecture | Multi-tenant architecture, LTI auth, AI orchestration, API contracts, DB schema, caching/fallback, logging/monitoring, CI/CD | Process | Yes | super-10 (External Tooling) implies infrastructure; otherwise non-visual | In Dev | JFT | Architecture doc + Swagger API specs delivered | Swagger explicitly required per JFT meeting 10 May 2026. |
| SOW-2.5 | SOW §2.5 Development | **Student Web Experience** (LTI auth, chat, AI scoring, feedback, error/retry), **AI Engine** (multi-LLM, routing, prompts, token/cost/latency, fallback, guardrails), **Admin Portal** (tenant controls, modules, instructors, analytics, reporting, audit logs), **Data & Integration Services** (LTI 1.3, API export, logging) | Feature | Yes | Student portal · Tenant Admin portal · Instructor portal · Super Admin portal (all surfaces) | In Dev | JFT | All four user-type portals deployed | Spine of the SDP build. Replaces MVP-only framing. |
| SOW-2.6 | SOW §2.6 Testing & QA | Functional, LTI, AI scoring consistency, API, regression, cross-browser, accessibility, security, performance/load | Process | Yes | Non-visual (test artifacts) | Not Started | JFT | Test plan + defect logs + QA sign-off report | |
| SOW-2.7 | SOW §2.7 Deployment | Environment provisioning, CI/CD, staging+production deploys, logging/monitoring/alerting, LMS-side LTI setup support, deployment walkthrough | Process | Yes | tenant-11 (Deploy stepper) · super-02 (monitoring) | In Dev | JFT | Production deploy + release notes + deployment checklist | |
| SOW-2.8 | SOW §2.8 Support | Pilot support: monitoring, critical/high issue resolution, AI debugging, fixes/patches, analytics/logs support | Process | Yes | tenant-13..tenant-20 (SC-ADD-06 SLA flow) | In Dev | JFT | Support SLAs met; weekly/biweekly status updates delivered | |
| SOW-3 | SOW §3 Assumptions | 25+ assumptions including prototype access, LTI 1.3 config, WGU-provided content/rubrics, English-only pilot, geo-redundant DNS, FERPA compliance, no mobile app, etc. | Process | N/A | Non-visual | Active | Both | Assumptions documented and tracked | Each assumption deviation may trigger a Change Request. |
| SOW-4 | SOW §4 Out of Scope | 18 explicit exclusions: native mobile, non-LTI auth, SIS/CRM integrations, content authoring CMS, multimedia uploads, non-English pilot, offline, 3rd-party licensing, internal WGU SSO build, etc. | Legal | N/A | Non-visual | Active | Both | Out-of-scope items not built; CR required if added | WGU defense against scope creep claims. |
| SOW-5 | SOW §5 Technology Stack | React.js + Tailwind/MUI · Node.js (Express/NestJS) · OpenAI/Anthropic/Google Vertex AI · Redis · PostgreSQL/MySQL · LTI 1.3 · AWS/GCP/Azure · CloudFront/Cloudflare · S3/GCP Storage · TLS 1.3 · AWS Secrets Manager · CloudWatch · GitHub Actions · Prometheus + Grafana · ELK Stack · Jest / Playwright · k6 | Process | Yes | super-10 (External Tooling hub) | In Dev | JFT | Stack matches SOW table; deviations documented | |
| SOW-6 | SOW §6 Roles & Responsibilities | Project governance, requirements, design, LTI integration, content/task, AI governance, data/compliance, environments, testing, production readiness, support, change requests | Process | N/A | Non-visual | Active | Both | RACI documented | |
| SOW-7 | SOW §7 Communication Plan | Kick-off (once); Weekly project update; Bi-weekly status report; Milestone review; Design review; Technical/architecture review; Change request; Issue resolution; UAT review; Pre-deployment readiness; Post-deployment check-in (daily 1-2 weeks); Monthly support review; Project closure | Process | N/A | Non-visual | Active | Both | All meetings cadence honored | |
| SOW-8 | SOW §8 Escalation Matrix | L1 dev team · L2 PM · L3 VP-IT / Architect · L4 CTO/CEO · Parallel Account Manager | Process | N/A | Non-visual | Active | JFT | Escalation followed during incidents | |
| SOW-9.1 | SOW §9.1 Support Overview | Tech support, issue resolution, operational assistance; WGU business hours; Jira ticketing | Process | Yes | tenant-16, tenant-17 (Jira ticket creation) | In Dev | JFT | Jira project provisioned; SLAs published | |
| SOW-9.2 | SOW §9.2 Support Tiers | L1 / L2 / L3 / DevOps support tiers with example scope | Process | Yes | Non-visual | Active | JFT | Tier structure documented | |
| SOW-9.3 | SOW §9.3 Support Scope | In-scope: incident resolution, AI/LLM, LTI, performance monitoring, hotfix, user assistance, configuration. Out: new features, model retraining, multi-tenant rollout | Process | Yes | Non-visual | Active | JFT | Support scope adhered to | |
| SOW-9.4 | SOW §9.4 Support Channels | Email · Jira · Video calls · Slack/Teams (optional) · CSM | Process | Yes | tenant-16..tenant-18 | In Dev | JFT | Channels operational | |
| SOW-9.5 | SOW §9.5 SLAs | P1 <2hr / 4-8hr · P2 <4hr / 24hr · P3 <1 business day / 72hr · P4 <2 business days / next release | Process | Yes | tenant-18 (CSM 2hr response thread) · tenant-20 (SLA dashboard) | In Dev | JFT | SLAs published; first incidents meet targets | |
| SOW-10 | SOW §10 Team Structure | Technical Architect · PM · AI/LLM Lead · AI/LLM Engineer · Backend Lead · Backend Devs · Frontend Lead · Frontend Devs · UI/UX Lead · UI/UX Designer · QA Lead · Manual & Automation Testers · DevOps & Security Engineer · Customer Success Manager · Support Staff | Process | Yes | Non-visual | Active | JFT | Team rostered; roles assigned | |
| SOW-11 | SOW §11 Unit Costs | Fixed-cost SOW with hourly rate × contracted hours; monthly hosting + support tiers quoted separately (not under fixed contract) | Process | N/A | Non-visual | Active | Both | Invoices match agreed unit costs | Hosting and support fees require a separate engagement beyond pilot. |
| SOW-11-Note-1 | SOW §11 Note 1 | Offer-validity window expired prior to signing; signed SOW functions as re-affirmation | Legal | N/A | Non-visual | Active | Both | | Worth knowing if future amendments are negotiated. |
| SOW-11-Note-4 | SOW §11 Note 4 | Fixed-cost basis; additional dev costs require pre-approval in writing | Legal | N/A | Non-visual | Active | Both | | |
| SOW-11-Note-5 | SOW §11 Note 5 | Pricing excludes hardware, infrastructure, hosting, third-party licensing — WGU pays those directly | Legal | N/A | super-03 (token usage by tenant) · super-04 (cost spike) · super-05 (rate limits) | In Dev | WGU | WGU holds LLM API contracts; spend tracked | LLM API costs are WGU's, hence the Super Admin cost telemetry. |
| SOW-11.1 | SOW §11.1 Payment Terms | Milestone-based payment schedule per signed SOW | Process | N/A | Non-visual | Active | Both | Payment milestone events documented | |
| SOW-12 | SOW §12 Terms and Conditions | Termination on 30-day uncured material breach; deliverables are work-for-hire post-payment | Legal | N/A | Non-visual | Active | Both | | |
| SOW-13 | SOW §13 Change Management | Jira / email submission; impact analysis; written approval before implementation; tracked to closure | Process | Yes | tenant-16..tenant-18 (Jira workflow illustrated) | Active | Both | Change requests documented via Jira | |
| SOW-14 | SOW §14 Primary Contacts | Primary contacts on each side per signed SOW | Process | N/A | Non-visual | Active | Both | Contacts kept current per contract | WGU contact roster maintained internally. |
| SOW-15 | SOW §15 SOW Acceptance | Signed by both parties in 2026 | Legal | N/A | Non-visual | Active | Both | Signed and on file | |

SOW core totals: 28 rows.

---

## Appendix A § 16.1 — Technical Requirements

| ID | Requirement | Commitment | Storyboard Coverage | Build Status | Owner | Acceptance | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| A-6.1 | Multi-LLM providers (Claude, ChatGPT, Gemini, others) — orchestration layer | Yes | tenant-09 model picker · super-10 external tooling · throughout student coaching loop | In Dev | JFT | Provider switching demonstrated in UAT | LLM-agnostic orchestration. |
| A-6.2 | Route requests to different LLMs by use case / configuration | Yes | tenant-09 model picker · super-10 | In Dev | JFT | Routing policies enforced and audited | |
| A-6.3 | LLM response caching and cost optimization | Yes | Non-visual (operational) · referenced super-04 cost analysis | Not Started | JFT | Cache hit metrics surfaced | |
| A-6.4 | Rate limiting and quota management per user / institution | Yes | super-03, super-04, super-05 (PDev rate-limit tighten) | In Dev | JFT | Rate limits configurable per tenant | |
| A-6.5 | Fallback mechanisms for LLM service interruptions | Yes | tenant-14, tenant-15 (fallback engaged) · tenant-19 (service restored) | In Dev | JFT | Fallback engages within seconds; demonstrated in SC-ADD-06 | |
| A-6.6 | Token usage tracking and reporting | Yes | super-03 (per-tenant) · super-04 (drill-down) | In Dev | JFT | Token / cost telemetry by institution / course / provider | Critical for WGU's LLM API cost control (SOW §11 Note 5). |
| A-6.7 | Configurable standard guardrails on all prompts for all LLMs | Yes | tenant-08 (4 short text-box guardrails) · referenced in student coaching | In Dev | JFT | Centralized guardrails injected into every prompt | |
| A-6.8 | A/B testing framework for LLM configurations | Yes | tenant-08 ("A/B test variants" badge on Configure AI Coaching Prompt) | In Design | JFT | A/B experiments with statistical reporting | Partial coverage: medium-fidelity badge declares the capability; full A/B test config + results surface is a future enhancement. v4.41 re-audit downgraded Gap → Partial. |
| A-6.9 | Handle multiple concurrent LLM requests per user | Yes | Non-visual (operational) | Not Started | JFT | Concurrent request load test passes | |
| A-6.10 | Custom fine-tuning capabilities | **No** | Non-visual (out of scope) | Not Applicable | — | — | Only out-of-scope item in Appendix A. RAG used instead. |
| A-6.11 | Real-time model performance monitoring | Yes | super-02 (KPI gauges) · super-04 (performance trends) | In Dev | JFT | Real-time latency / error / accuracy / fallback metrics | |
| A-6.12 | LaTeX support for inputs and outputs | Yes | tenant-08 ("LaTeX rendering" badge on Configure AI Coaching Prompt) | In Design | JFT | LaTeX rendering on student + admin screens | Partial coverage: medium-fidelity badge declares the capability; inline LaTeX preview verification surface is a future enhancement. v4.41 re-audit downgraded Gap → Partial. |
| A-6.13 | Support 50,000+ daily active users | Yes | Non-visual (load test) | Not Started | JFT | k6 load test to 50K+ DAU passes | |
| A-6.14 | Auto-scaling infrastructure for peak usage | Yes | super-02 (system health) | Not Started | JFT | Auto-scale events observable in monitoring | |
| A-6.15 | Response times <3s for 95% of requests | Yes | super-02 (KPI) | Not Started | JFT | 95p latency under 3s in production | |
| A-6.16 | Global Content Delivery Network (CDN) | Yes | Non-visual (operational; super-07 geo-redundancy adjacent) | Not Started | JFT | CDN serving static + semi-dynamic assets | |
| A-6.17 | Geographic load balancing | Yes | super-07 (cross-region resilience) | In Dev | JFT | DNS / regional LB demonstrated in failover test | |
| A-6.18 | Predictive scaling by usage patterns | Yes | Non-visual (operational) | Not Started | JFT | Predictive scale schedule documented | |
| A-6.19 | Performance monitoring and alerting | Yes | super-02 (alerts) | In Dev | JFT | APM + logs + metrics + traces operational | |
| A-6.20 | Cloud-native architecture (AWS / GCP / Azure) | Yes | super-10 (AWS Console card) | In Dev | JFT | Deployed on managed cloud; 12-factor | |
| A-6.21 | Microservices architecture with containerization | Yes | Non-visual (architectural) | In Dev | JFT | Architecture doc + container deploy | |
| A-6.22 | RESTful API design | Yes | Non-visual (Swagger doc external) | In Dev | JFT | Swagger published | Per SOW §2.4 deliverable. |
| A-6.23 | Database optimization for high-volume concurrent access | Yes | Non-visual (architectural) | Not Started | JFT | Postgres replicas + Redis + CDC operational | |
| A-6.24 | Automated CI/CD pipeline | Yes | tenant-11 (5-step CI/CD Stepper) · super-10 GitHub Actions | In Dev | JFT | Blue/green deploys via GitHub Actions | |
| A-6.25 | Version control and code documentation | Yes | super-10 GitHub link card | In Dev | JFT | Repo + Confluence docs current | |
| A-6.26 | Serverless components where appropriate | Yes | Non-visual (architectural) | Not Started | JFT | Serverless functions deployed for bursty jobs | |
| A-6.27 | Event-driven architecture | Yes | Non-visual (architectural) | Not Started | JFT | Kafka / Pub/Sub / EventBridge backbone operational | |
| A-6.28 | GraphQL API support | Yes | super-11 (Data & Integrations Hub — GraphQL endpoint card + sample query) | In Design | JFT | GraphQL alongside REST for low over-fetch contexts | v4.41 closed this gap on the new super-11 surface. |

§ 16.1 totals: 28 rows. 27 Yes commitments + 1 No (A-6.10).

---

## Appendix A § 16.2 — User Experience and Design

| ID | Requirement | Commitment | Storyboard Coverage | Build Status | Owner | Acceptance | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| A-7.1 | Modern, responsive web design | Yes | All persona portals | In Dev | JFT | Cross-browser QA matrix passes | |
| A-7.2 | Mobile-first approach with cross-device compatibility | Yes | student portal (Sally is mobile-first); admin portals desktop-primary | In Dev | JFT | Mobile breakpoints documented | Per User Profiles: admins desktop-primary by role context. |
| A-7.3 | WCAG 2.2 AA compliance | Yes | All persona portals (universal) | In Dev | JFT | WCAG 2.2 AA audit pass; ACR / VPAT current | Cross-references MSA-15.b. WGU runs independent testing. |
| A-7.4 | User testing and iterative design process | Yes | Non-visual (process) | In Dev | Both | Iterative review meetings logged | |
| A-7.5 | Intuitive interface for non-technical users | Yes | All persona portals | In Dev | JFT | Usability testing meets heuristics | |
| A-7.6 | Multi-language support capability | Yes | tenant-21 (Branding — default locale dropdown) | In Dev | JFT | Localization framework in place; English-only at pilot | English-only at pilot per SOW Assumption. |
| A-7.7 | Progressive Web App (PWA) functionality | Yes | tenant-21 (PWA install badge) | Not Started | JFT | Installable PWA on student portal | v4.18 added the badge; functionality TBD. |
| A-7.8 | Dark / light mode options | Yes | All persona portals (theme toggle implemented) | Built | JFT | Theme toggle persists via localStorage | Storyboard demonstrates both themes (light + dark PNGs). |
| A-7.9 | Customizable interface for institutions | Yes | tenant-21 (Branding & Customization) | In Dev | JFT | Logos, colors, domain configurable per tenant | |
| A-7.10 | Comprehensive student engagement tracking | Yes | instructor-02..instructor-08 · student-06 progress map | In Dev | JFT | Engagement dashboards live for educators | FERPA-bounded per A-10.1. |
| A-7.11 | Learning analytics dashboard for educators | Yes | instructor-02..instructor-08 | In Dev | JFT | Class-wide insights + at-risk flagging + drill-down | |
| A-7.12 | Usage statistics and reporting | Yes | super-03 token usage · instructor-02 KPIs | In Dev | JFT | Usage reports filterable + exportable | |
| A-7.13 | Data visualization tools | Yes | instructor-03 heatmap · super-02 KPI gauges · super-04 cost chart | In Dev | JFT | Charts accessible (screen reader, hover context) | |
| A-7.14 | Export capabilities for all reports | Yes | instructor-03 PDF/CSV CTAs | In Dev | JFT | CSV / PDF / JSON / XML one-click exports | XML added per v4.18 (§16.3 #8.9 alignment). |

§ 16.2 totals: 14 rows. All Yes.

---

## Appendix A § 16.3 — Integration Requirements

| ID | Requirement | Commitment | Storyboard Coverage | Build Status | Owner | Acceptance | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| A-8.1 | Full LTI 1.3 (including Advantage services) compliance for student authentication | Yes | student-01 (LTI launch context) · tenant-12 (LRPS launch URL) · lrps-01 | In Dev | JFT | SSO + grade return + deep linking + names/roles provisioning | Pilot uses Basic LTI 1.3 only; Advantage features are post-pilot per WGU direction. |
| A-8.2 | SAML SSO integration | Yes | super-01 (SAML 2.0 SP login) · tenant-01 · instructor-01 | In Dev | JFT | SP configured with WGU Entra ID; role mapping documented | |
| A-8.3 | Deep linking support | Yes | tenant-12 (LRPS deep-link provisioning) · lrps-01 | In Dev | JFT | LTI Advantage deep linking operational | Future-state: per-sub-section deep links. |
| A-8.4 | LTI 1.1 backward compatibility | Yes | Non-visual (adapter) | Not Started | JFT | Legacy LTI 1.1 launches succeed | |
| A-8.5 | Custom LTI extensions | Yes | Non-visual (case-by-case) | Not Started | Both | Extensions scoped on request | |
| A-8.6 | Multi-tenancy support for different institutions | Yes | tenant-02 (multi-tenant scoping callout) · super-02 (cross-tenant view) | In Dev | JFT | Logical isolation across data, auth, branding per tenant | |
| A-8.7 | RESTful API for student engagement data export | Yes | Non-visual (Swagger external) | In Dev | JFT | API consumes engagement data with OAuth + filtering + pagination | |
| A-8.8 | Real-time and batch data export capabilities | Yes | super-11 (Data export section — real-time + batch cards) | In Design | JFT | Real-time webhooks + scheduled batch exports | v4.41 closed this gap on the new super-11 surface. |
| A-8.9 | Support for common data formats (JSON, CSV, XML) | Yes | instructor-03 (Export CTAs) | In Dev | JFT | JSON / CSV / XML exports validated | XML added per v4.18 sweep. |
| A-8.10 | API rate limiting and authentication | Yes | super-05 (rate limits) | In Dev | JFT | OAuth tokens + tenant-aware rate limits | |
| A-8.11 | Comprehensive API documentation | Yes | Non-visual (Swagger external) | In Dev | JFT | Swagger + Postman collection published | Per JFT meeting 10 May 2026. |
| A-8.12 | Webhook support for real-time notifications | Yes | super-11 (Webhook subscriptions section — 4-row event table + register endpoint CTA) | In Design | JFT | Configurable signed webhooks with retry/backoff | v4.41 closed this gap on the new super-11 surface. |
| A-8.13 | GraphQL API for flexible data queries | Yes | super-11 (GraphQL API section — endpoint card + sample query code block) | In Design | JFT | Optional GraphQL with depth limits + FERPA-aware auth | v4.41 closed this gap on the new super-11 surface. |
| A-8.14 | Data streaming capabilities | Yes | super-11 (Data streaming section — 3 provider cards Kafka / Kinesis / Pub-Sub) | In Design | JFT | Kafka / Kinesis / Pub/Sub streaming for analytics | v4.41 closed this gap on the new super-11 surface. |
| A-8.15 | Custom integration development | Yes | Non-visual (case-by-case) | Not Started | Both | Custom integrations scoped on request | |

§ 16.3 totals: 15 rows. All Yes.

---

## Appendix A § 16.4 — Operational Requirements

| ID | Requirement | Commitment | Storyboard Coverage | Build Status | Owner | Acceptance | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| A-9.1 | 24/7 system monitoring | Yes | super-02 (active alerts) · tenant-13 (all systems operational) | In Dev | JFT | 24x7 cloud + application monitoring operational | |
| A-9.2 | 99.95% uptime SLA | Yes | tenant-20 (SLA dashboard) · super-02 | In Dev | JFT | Quarterly SLA report meets 99.95% | ~4.4 hours downtime budget per year. |
| A-9.3 | Automated backup with point-in-time recovery | Yes | Non-visual (operational) | Not Started | JFT | Backup + PITR demonstrated in DR drill | |
| A-9.4 | Disaster recovery plan with RTO < 4 hours | Yes | super-07 (cross-region resilience) | In Dev | JFT | DR drill restores service within 4 hours | |
| A-9.5 | Geographic redundancy | Yes | super-07 | In Dev | JFT | Multi-region failover documented | |
| A-9.6 | Regular infrastructure updates and patching | Yes | Non-visual (process) | Active | JFT | Patch SLA met (48hr critical) | |
| A-9.7 | Dedicated customer success manager | Yes | tenant-18 (CSM Jordan in chat thread) | Active | JFT | CSM Jordan assigned per §9.7 | |
| A-9.8 | Regular software updates and feature enhancements | Yes | Non-visual (process) | Active | JFT | Maintenance cycle published | |
| A-9.9 | Bug fix SLA: Critical 4hr / High 24hr / Medium 72hr | Yes | tenant-20 SLA dashboard | In Dev | JFT | Bug fix SLA reports meet targets | |
| A-9.10 | 24/7 technical support with <2hr response for critical | Yes | tenant-18 (P1 SLA <2hr) | In Dev | JFT | First-incident response <2hr | |
| A-9.11 | Comprehensive documentation and user training materials | Yes | Non-visual (delivered as docs/videos) | Not Started | JFT | Documentation + training delivered for each role | |
| A-9.12 | Scheduled maintenance with minimum 2-week notice | Yes | Non-visual (process) | Active | JFT | Maintenance notices on file | Rolling enrollment makes window selection nontrivial. |
| A-9.13 | Proactive monitoring, alerting, issue resolution | Yes | super-02 (alerts) · tenant-13 (baseline) · tenant-14 (degradation) | In Dev | JFT | Alerts route to on-call engineer | |
| A-9.14 | Self-service support portal | Yes | help-01 (Help & Resources surface — self-service section: search, 3 cards, updates feed, Contact JFT Support button) | In Design | JFT | Self-service portal scoped + delivered | v4.41 added the surface in a new shared `help/` folder linkable from every admin portal. |
| A-9.15 | Video training resources | Yes | help-01 (Help & Resources surface — role-filtered video gallery with 9 tiles + featured callout) | In Design | JFT | Video modules per audience in support library | v4.41 added the surface alongside the self-service section in the same shared `help/` folder. |

§ 16.4 totals: 15 rows. All Yes.

---

## Appendix A § 16.5 — Compliance and Security Requirements

| ID | Requirement | Commitment | Storyboard Coverage | Build Status | Owner | Acceptance | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| A-10.1 | Full FERPA compliance for all student data handling | Yes | super-06 (Compliance Report — FERPA section, 16-row control table) | In Dev | JFT | FERPA audit passes; access limited to authenticated roles | Cross-references MSA-6.c. |
| A-10.2 | Data retention and deletion policies compliant with FERPA | Yes | tenant-23 (Subject Lifecycle & Archival) · super-06 | In Dev | JFT | 3-year default retention; coordinated deletion across primaries/backups | Cross-references MSA-10. |
| A-10.3 | Staff training on FERPA requirements | Yes | Non-visual (operational) | Active | JFT | FERPA training completion records on file | |
| A-10.4 | Audit logging for all data access and modifications | Yes | super-08 (cross-tenant audit log) · instructor-08 (audit trail) · tenant-23 (audit ref) | In Dev | JFT | Immutable audit logs for read/write actions | |
| A-10.5 | Annual compliance auditing and reporting | Yes | super-06 (compliance report screen) | Not Started | JFT | Annual audit findings shared; critical findings closed | |
| A-10.6 | SOC 2 Type II certification or equivalent | Yes | super-06 (control row) | In Dev | JFT | SOC 2/ISO-certified cloud + own SOC 2 readiness | v4.18 added explicit row. |
| A-10.7 | HTTPS / TLS 1.3 for all communications | Yes | super-06 (TLS 1.3 audit) | In Dev | JFT | TLS 1.3 enforced; HSTS; auto certificate management | |
| A-10.8 | Role-based access control (RBAC) | Yes | super-09 (User Management) · tenant-22 (Roster) · tenant-01 (elevation) | In Dev | JFT | Granular RBAC across UI + API; logged approvals | |
| A-10.9 | Regular security vulnerability assessments | Yes | super-06 (vuln scan + 48hr patch SLA control row) | In Dev | JFT | Vulnerability scans every release; critical < 48hr remediated | |
| A-10.10 | Penetration testing (annual minimum) | Yes | super-06 (annual pentest control row) | Not Started | JFT | Annual pentest report + remediation plan | |
| A-10.11 | Data breach response plan and notification procedures | Yes | Non-visual (operational); cross-ref MSA-11 | Active | JFT | Breach playbook tested and current | Cross-references MSA-11 (24-hour notification). |
| A-10.12 | GDPR compliance for international users | Yes | super-06 (GDPR control row) | Not Started | JFT | GDPR controls activated when international learners scoped | |
| A-10.13 | ISO 27001 certification | Yes | super-06 (ISO 27001 control row) | Not Started | JFT | ISO 27001 alignment with provider cert + own readiness | v4.18 added explicit row. |
| A-10.14 | Zero-trust security model | Yes | super-06 (zero-trust authz control row) · super-01 (MFA gating) | In Dev | JFT | Authentication + authorization + encryption at each service call | |
| A-10.15 | Advanced threat detection and monitoring | Yes | super-06 (SIEM control row) | Not Started | JFT | SIEM + cloud-native detection alerts active | |
| A-10.16 | Encrypt sensitive data at rest and in transit | Yes | super-06 (AES-256 at rest with KMS) | In Dev | JFT | AES-256 at rest + TLS 1.3 in transit; KMS-managed key rotation | |
| A-10.17 | Dedicated security team and formal security policy | Yes | Non-visual (organizational) | Active | JFT | Security policies documented; annual review evidence | |
| A-10.18 | Strong authentication standards (MFA, password policies) | Yes | super-01 (MFA login) · super-06 (MFA control row) · super-09 (User Mgmt elevation) | In Dev | JFT | 100% MFA on privileged accounts; password policy per NIST SP 800-63B | |
| A-10.19 | Change and patch management process | Yes | super-06 (vuln scan + 48hr patch SLA control row) | In Dev | JFT | CI/CD-enforced changes; patch SLA met | |
| A-10.20 | Business Continuity and Disaster Recovery (BC/DR) plan | Yes | super-06 (BC/DR control row) · super-07 (geo-redundancy) | In Dev | JFT | BC/DR plan documented; RTO ≤ 4hr + RPO ≤ 60min validated | |

§ 16.5 totals: 20 rows. All Yes.

---

## Totals and verification

| Section | Rows | Yes | No | N/A |
|:---|:---:|:---:|:---:|:---:|
| MSA §§ 1-16 | 30 | — | — | 30 (legal/process) |
| SOW §§ 1-15 core | 28 | 14 features/process | — | 14 legal/process |
| Appendix A § 16.1 Technical | 28 | 27 | 1 | — |
| Appendix A § 16.2 UX & Design | 14 | 14 | — | — |
| Appendix A § 16.3 Integration | 15 | 15 | — | — |
| Appendix A § 16.4 Operational | 15 | 15 | — | — |
| Appendix A § 16.5 Compliance & Security | 20 | 20 | — | — |
| **Total** | **150** | **105** | **1** | **44** |

### Gaps requiring D3a follow-up

The following Appendix A rows have Storyboard Coverage = Gap and are first-priority candidates for prototype gap closure (after v4.41 re-audit):

- A-6.28 GraphQL API (no UI mention anywhere in the current storyboard; could be a card on super-10 External Tooling or part of a new data/integrations surface)
- A-8.8 Real-time and batch data export (had coverage on the tenant_admin SC-ADD-05 Data & APIs landing in v4.18; removed in v4.22 when SC-ADD-05 was deleted and data-export scope moved to global / Super Admin)
- A-8.12 Webhook support (same — removed in v4.22)
- A-8.13 GraphQL API queries (same — removed in v4.22)
- A-8.14 Data streaming (no prior coverage)
- ~~A-9.14 Self-service support portal~~ (closed in v4.41 on the new `help-01` Help & Resources surface)
- ~~A-9.15 Video training resources~~ (closed in v4.41 on the new `help-01` Help & Resources surface)

Total true gaps remaining: **0 out of 92** Appendix A items. D3a build phase complete; all Appendix A items now have at least Partial storyboard coverage.

**Closure history:**
- **v4.36 D3a re-audit** downgraded A-6.8 (A/B testing framework) and A-6.12 (LaTeX rendering) from Gap to Partial after verifying both badges added in v4.18 are still present on tenant-08 (Configure AI Coaching Prompt). Medium-fidelity badge coverage is adequate for declaring the capability; fuller surfaces are future enhancements but not contract-required.
- **v4.38 D3a build phase 1** closed A-9.14 (self-service support portal) and A-9.15 (video training resources) on the new `help-01` Help & Resources surface.
- **v4.41 D3a build phase 2** closed A-6.28 (GraphQL API), A-8.8 (real-time/batch data export), A-8.12 (webhook support), A-8.13 (GraphQL API queries), and A-8.14 (data streaming) on the new `super-11` Data & Integrations Hub surface.

### Out-of-scope items (no build expected)

- A-6.10 Custom fine-tuning capabilities (only **No** in Appendix A; RAG used instead)
- SOW §4 Out of Scope list: 18 explicit exclusions (native mobile, non-LTI auth, SIS/CRM, content authoring CMS, multimedia uploads, non-English pilot, offline, 3rd-party licensing, etc.)

---

## Change log

| Version | Date | Status | Notes |
|:---|:---|:---|:---|
| 1.0 | 12 May 2026 | Current | Initial baseline. 156 rows enumerated across MSA + SOW + Appendix A. 9 gaps identified for D3a follow-up. Storyboard baseline: v4.41. |

---

*WGU confidential. Author: WGU Program Development. Not for redistribution outside WGU.*
