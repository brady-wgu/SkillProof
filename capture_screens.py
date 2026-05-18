"""Capture all storyboard screens (5 portals + landing hero × 2 themes) as PNG
screenshots, writing each portal's outputs into its own per-persona subdirectory.

Usage:
    1. Start a local HTTP server from the repo root:
         python -m http.server 63417
    2. Run this script:
         python capture_screens.py

Outputs (per persona):
    student/screenshots/         + student/screenshots_dark/         (18 + 18)
    tenant_admin/screenshots/    + tenant_admin/screenshots_dark/    (21 + 21)
    instructor/screenshots/      + instructor/screenshots_dark/      (9 + 9)
    super_admin/screenshots/     + super_admin/screenshots_dark/     (14 + 14)
    help/screenshots/            + help/screenshots_dark/            (1 + 1)
    assets/landing/light.png     + assets/landing/dark.png           (1 + 1)

Total: 128 PNGs after capture. v4.59 collapsed the standalone LRPS surface into
the storyboard root — the root `index.html` IS the LRPS UI, captured into
assets/landing/. v4.58 rebuilt the student section against the live JFT MVP
(34 -> 18 screens). v4.57 added Access Denied screens to the 3 admin portals
(tenant 20 -> 21, instructor 8 -> 9, super 13 -> 14).

Naming:
    {persona}/screenshots[_dark]/sc-mvp-NN_stepNN_screenNN.png
    {persona}/screenshots[_dark]/sc-add-NN_stepNN_screenNN.png
    help/screenshots[_dark]/help.png
    assets/landing/{light,dark}.png   (root LRPS UI hero)
"""
import asyncio
import os
from playwright.async_api import async_playwright

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "http://localhost:63417"
VIEWPORT = {"width": 1440, "height": 900}

# Each portal: HTML file (relative to repo root) + scenarios.
# Output dir is derived from the HTML's parent directory + theme subdir.
PORTALS = [
    {"file": "student/index.html", "scenarios": [
        ("sc-mvp-01", [1, 2, 3, 4, 5, 6, 7, 8]),
        ("sc-mvp-02", [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        ("sc-mvp-03", [20, 21, 22, 23, 24, 25, 26, 27, 28]),
        ("sc-mvp-04", [29, 30, 31, 32, 33, 34]),
    ]},
    {"file": "tenant_admin/index.html", "scenarios": [
        # v4.25: Team & Roles screen (formerly tenant_admin 22) moved to Super Admin per WGU-
        # stakeholder feedback reshape; old 23 (Instructor Roster) -> 22, old 24 (Subject Lifecycle) -> 23.
        ("sc-add-02", [1, 2, 3, 4, 5, 6, 7, 8, 17, 18, 19, 20]),  # v4.53 end-of-day renumber pass: screens are now sequentially 1-20. Flow A wizard + settings: 1 SSO · 2 portal home · 3 new subject · 4 topics & objectives · 5 model & coaching · 6 AI prompt · 7 deploy review · 8 deploy success · 17 tenant settings · 18 subject lifecycle · 19 analytics & reporting · 20 activity log.
        ("sc-add-06", [9, 10, 11, 12, 13, 14, 15, 16]),  # v4.53 renumber: Flow B incident response. 9 systems OK · 10 LLM down · 11 notification · 12 P1 ticket · 13 ticket submitted · 14 CSM thread · 15 service restored · 16 SLA dashboard.
    ]},
    {"file": "super_admin/index.html", "scenarios": [
        ("sc-add-04", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),  # v4.25 screen 9 User Management; v4.28 screen 10 External Tooling & Integrations; v4.41 screen 11 Data & Integrations Hub; v4.48 screen 12 Instructor Roster & Course Assignment (moved from tenant_admin under Super Admin scope); v4.52 screen 13 School / Tenant Management (Super Admin manages the 4 WGU Schools as tenants).
    ]},
    {"file": "instructor/index.html", "scenarios": [
        ("sc-add-03", [1, 2, 3, 4, 5, 6, 7, 8]),  # v4.4 added 9 Learner Search; v4.9 removed it as not in v1.3 catalog narrative.
    ]},
    {"file": "help/index.html", "scenarios": [
        ("help", [None]),  # v4.38 single-page help & resources surface; capture as-is.
    ]},
    {"file": "index.html", "scenarios": [
        ("landing", [None]),  # v4.59: root IS the LRPS UI (LRPS folded up). Output goes to assets/landing/.
    ]},
]

THEMES = ["light", "dark"]


def out_dir_for(portal_file, theme):
    """student/index.html + light  ->  {repo}/student/screenshots
       student/index.html + dark   ->  {repo}/student/screenshots_dark
       index.html + light/dark     ->  {repo}/assets/landing  (special-case root)"""
    if portal_file == "index.html":
        return os.path.join(REPO_ROOT, "assets", "landing").replace("\\", "/")
    persona_dir = os.path.dirname(portal_file)
    sub = "screenshots" if theme == "light" else "screenshots_dark"
    return os.path.join(REPO_ROOT, persona_dir, sub).replace("\\", "/")


async def capture_portal(page, portal, theme):
    """Open portal HTML, set theme, capture every screen in its scenarios."""
    url = f"{BASE_URL}/{portal['file']}"
    out_dir = out_dir_for(portal["file"], theme)
    os.makedirs(out_dir, exist_ok=True)
    print(f"\n[{theme}] {portal['file']}  ->  {os.path.relpath(out_dir, REPO_ROOT)}")

    await page.add_init_script(
        f"localStorage.setItem('skillproof-theme', '{theme}');"
    )
    await page.goto(url, wait_until="networkidle")

    # Suppress all focus outlines globally for cleaner screenshots
    await page.add_style_tag(content=(
        "*:focus, *:focus-visible {"
        " outline: none !important;"
        " box-shadow: none !important;"
        " border-color: inherit !important;"
        "}"
    ))

    captured = 0
    for scenario_id, screen_ids in portal["scenarios"]:
        for step_idx, screen_id in enumerate(screen_ids, 1):
            if screen_id is None:
                # Single-page portal (e.g., help, landing) — no goToScreen call.
                # v4.59: the root landing IS the LRPS UI now. Scroll the live SkillProof
                # rows into view so the M4 "Not for student use" badges land in the hero
                # screenshot (the alphabetically-sorted OEX rows above add no value).
                if scenario_id == "landing":
                    await page.evaluate(
                        "(() => {"
                        " const row = document.querySelector('tr.live[data-launch=\"student/\"]');"
                        " if (row) {"
                        "   const rect = row.getBoundingClientRect();"
                        "   window.scrollTo({top: window.scrollY + rect.top - 200, behavior: 'instant'});"
                        " }"
                        "})()"
                    )
                await page.wait_for_timeout(300)
                # Special case: root index.html -> assets/landing/{theme}.png
                if portal["file"] == "index.html":
                    fname = f"{out_dir}/{theme}.png"
                else:
                    fname = f"{out_dir}/{scenario_id}.png"
            else:
                await page.evaluate(f"goToScreen({screen_id})")
                await page.evaluate("document.activeElement?.blur()")
                await page.wait_for_timeout(300)
                fname = (
                    f"{out_dir}/{scenario_id}_"
                    f"step{step_idx:02d}_screen{screen_id:02d}.png"
                )
            await page.screenshot(path=fname, full_page=False)
            captured += 1
    print(f"  captured {captured} screens")
    return captured


async def main():
    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for theme in THEMES:
            # Fresh context per theme so the init script localStorage applies
            # cleanly without leaking across portal navigations.
            context = await browser.new_context(viewport=VIEWPORT)
            page = await context.new_page()
            for portal in PORTALS:
                total += await capture_portal(page, portal, theme)
            await context.close()
        await browser.close()
    print(f"\nDone — {total} screenshots written into per-persona subdirs.")


if __name__ == "__main__":
    asyncio.run(main())
