"""Capture all storyboard screens (5 portals × 2 themes) as PNG screenshots,
writing each portal's outputs into its own per-persona subdirectory.

Usage:
    1. Start a local HTTP server from the repo root:
         python -m http.server 63417
    2. Run this script:
         python capture_screens.py

Outputs (per persona):
    student/screenshots/         + student/screenshots_dark/         (34 + 34)
    tenant_admin/screenshots/    + tenant_admin/screenshots_dark/    (23 + 23)
    instructor/screenshots/      + instructor/screenshots_dark/      (8 + 8)
    super_admin/screenshots/     + super_admin/screenshots_dark/     (10 + 10)
    lrps/screenshots/            + lrps/screenshots_dark/            (1 + 1)

Total: 152 PNGs (v4.36: D3a re-audit downgraded 2 of 9 Gap classifications to Partial in CONTRACT_TRACKER (A-6.8 + A-6.12 have adequate medium-fidelity badge coverage on tenant-08); 7 true gaps remain for D3a build phase; no storyboard UI changes; PNG counts unchanged from v4.35).

Naming:
    {persona}/screenshots[_dark]/sc-mvp-NN_stepNN_screenNN.png
    {persona}/screenshots[_dark]/sc-add-NN_stepNN_screenNN.png
    lrps/screenshots[_dark]/lrps.png
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
        ("sc-add-02", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 21, 22, 23]),  # 21 Branding, 22 Instructor Roster, 23 Subject Lifecycle
        ("sc-add-06", [13, 14, 15, 16, 17, 18, 19, 20]),
    ]},
    {"file": "super_admin/index.html", "scenarios": [
        ("sc-add-04", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),  # v4.25: screen 9 (User Management); v4.28: screen 10 (External Tooling & Integrations per WGU direction for AWS-centric tooling).
    ]},
    {"file": "instructor/index.html", "scenarios": [
        ("sc-add-03", [1, 2, 3, 4, 5, 6, 7, 8]),  # v4.4 added 9 Learner Search; v4.9 removed it as not in v1.3 catalog narrative.
    ]},
    {"file": "lrps/index.html", "scenarios": [
        ("lrps", [None]),  # None = no goToScreen call, just capture as-is
    ]},
]

THEMES = ["light", "dark"]


def out_dir_for(portal_file, theme):
    """student/index.html + light  ->  {repo}/student/screenshots
       student/index.html + dark   ->  {repo}/student/screenshots_dark"""
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
        f"localStorage.setItem('sdp-theme', '{theme}');"
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
                # Single-page portal (e.g., lrps) — no goToScreen call.
                # For LRPS, scroll the live SDP rows into view so the M4
                # "Not for student use" badges land in the hero screenshot
                # (the alphabetically-sorted OEX rows above add no value).
                await page.evaluate(
                    "(() => {"
                    " const row = document.querySelector('tr.live[data-launch=\"../student/\"]');"
                    " if (row) {"
                    "   const rect = row.getBoundingClientRect();"
                    "   window.scrollTo({top: window.scrollY + rect.top - 200, behavior: 'instant'});"
                    " }"
                    "})()"
                )
                await page.wait_for_timeout(300)
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
