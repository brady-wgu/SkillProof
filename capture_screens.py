"""Capture all storyboard screens (4 portals × 2 themes) as PNG screenshots.

Usage:
    1. Start a local HTTP server from the repo root:
         python -m http.server 63417
    2. Run this script:
         python capture_screens.py

Outputs:
    screenshots/         (light theme — 73 PNGs)
    screenshots_dark/    (dark theme — 73 PNGs)

Naming:
    sc-mvp-NN_stepNN_screenNN.png   (index.html)
    sc-add-02_stepNN_screenNN.png   (tenant_admin.html screens 1-9)
    sc-add-03_stepNN_screenNN.png   (instructor.html screens 1-8)
    sc-add-04_stepNN_screenNN.png   (super_admin.html screens 1-8)
    sc-add-05_stepNN_screenNN.png   (tenant_admin.html screens 10-15)
    sc-add-06_stepNN_screenNN.png   (tenant_admin.html screens 16-23)
"""
import asyncio
import os
from playwright.async_api import async_playwright

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "http://localhost:63417"
VIEWPORT = {"width": 1440, "height": 900}

# Each portal: (HTML file, scenario_id, screen_ids[]) — screenshot file uses
# scenario_id for the SC-* prefix. Screen ID is the in-file goToScreen target.
PORTALS = [
    # Existing v1.2 student storyboard — index.html
    {"file": "index.html", "scenarios": [
        ("sc-mvp-01", [1, 2, 3, 4, 5, 6, 7, 8]),
        ("sc-mvp-02", [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        ("sc-mvp-03", [20, 21, 22, 23, 24, 25, 26, 27, 28]),
        ("sc-mvp-04", [29, 30, 31, 32, 33, 34]),
    ]},
    # v1.3 Tenant Admin — tenant_admin.html (3 scenarios under one file)
    {"file": "tenant_admin.html", "scenarios": [
        ("sc-add-02", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ("sc-add-05", [10, 11, 12, 13, 14, 15]),
        ("sc-add-06", [16, 17, 18, 19, 20, 21, 22, 23]),
    ]},
    # v1.3 Instructor — instructor.html
    {"file": "instructor.html", "scenarios": [
        ("sc-add-03", [1, 2, 3, 4, 5, 6, 7, 8]),
    ]},
    # v1.3 Super Admin — super_admin.html
    {"file": "super_admin.html", "scenarios": [
        ("sc-add-04", [1, 2, 3, 4, 5, 6, 7, 8]),
    ]},
    # v1.3 LRPS landing page — single page, no goToScreen (special case)
    {"file": "lrps.html", "scenarios": [
        ("lrps", [None]),  # None = no goToScreen call, just capture as-is
    ]},
]

THEMES = [
    ("light", "screenshots"),
    ("dark",  "screenshots_dark"),
]


async def capture_portal(page, portal, theme, out_dir):
    """Open portal HTML, set theme, capture every screen in its scenarios."""
    url = f"{BASE_URL}/{portal['file']}"
    print(f"\n[{theme}] {portal['file']}")
    # Set theme via localStorage BEFORE navigation so first paint matches.
    # (Done at the page level via init script — avoids first-paint flash.)
    await page.add_init_script(
        f"localStorage.setItem('sdp-theme', '{theme}');"
    )
    await page.goto(url, wait_until="networkidle")

    # Suppress all focus outlines globally
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
                # Single-page portal (e.g., lrps.html) — no goToScreen call
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
    # Ensure output dirs exist
    for _, out_subdir in THEMES:
        os.makedirs(os.path.join(REPO_ROOT, out_subdir), exist_ok=True)

    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for theme, out_subdir in THEMES:
            out_dir = os.path.join(REPO_ROOT, out_subdir).replace("\\", "/")
            # Fresh context per theme so the init script localStorage applies
            # cleanly without leaking across portal navigations.
            context = await browser.new_context(viewport=VIEWPORT)
            page = await context.new_page()
            for portal in PORTALS:
                total += await capture_portal(page, portal, theme, out_dir)
            await context.close()
        await browser.close()
    print(f"\nDone — {total} screenshots written to {REPO_ROOT}/screenshots[_dark]/")


if __name__ == "__main__":
    asyncio.run(main())
