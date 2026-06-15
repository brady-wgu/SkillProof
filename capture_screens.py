"""Capture all storyboard screens (5 portals + landing hero + help × 2 themes) as
PNG screenshots, writing each portal's outputs into its own per-persona subdir.

v4.155 (2 Jun 2026) — naming simplified to `screen-NN.png`, 1:1 with the
on-page screen IDs and the new `?screen=N` deep-link URLs. The prior
SC-MVP-NN_stepNN_screenNN.png convention encoded the User Scenario Catalog
narrative-step grouping; that mapping (34 steps across 18 student screens,
etc.) lives in the per-portal README scenario tables — not in filenames.

Usage:
    1. Start a local HTTP server from the repo root:
         python -m http.server 8000
    2. Run this script:
         python capture_screens.py

Outputs:
    student/screenshots/         + student/screenshots_dark/         (18 + 18)
    instructor/screenshots/      + instructor/screenshots_dark/      ( 5 +  5)
    tenant_admin/screenshots/    + tenant_admin/screenshots_dark/    (12 + 12)
    super_admin/screenshots/     + super_admin/screenshots_dark/     (11 + 11)
    help/screenshots/            + help/screenshots_dark/            ( 1 +  1)
    assets/landing/light.png     + assets/landing/dark.png           ( 1 +  1)

Total: 96 PNGs after capture (47 light + 47 dark + 2 landing).
"""
import asyncio
import os
from playwright.async_api import async_playwright

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "http://localhost:8000"
VIEWPORT = {"width": 1440, "height": 900}

# Each portal: HTML file (relative to repo root) + screen count.
# Output dir is derived from the HTML's parent directory + theme subdir.
PORTALS = [
    {"file": "student/index.html", "screens": 18},
    {"file": "instructor/index.html", "screens": 5},
    {"file": "tenant_admin/index.html", "screens": 12},
    {"file": "super_admin/index.html", "screens": 11},
    {"file": "help/index.html", "screens": 0, "singlePage": "help"},
    {"file": "index.html", "screens": 0, "singlePage": "landing"},
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
    """Open portal HTML, set theme, capture every screen."""
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
    if portal.get("singlePage"):
        # Single-page surface (help or root landing). For landing, scroll the
        # live SkillProof rows into view so the "Not for student use" badges
        # land in the hero shot (the alphabetically-sorted OEX rows above add
        # no value to the hero).
        if portal["singlePage"] == "landing":
            # Hero (v4.161): capture from the top so the Providers table header
            # and the six live Skill launch rows lead the shot.
            await page.evaluate(
                "window.scrollTo({top: 0, behavior: 'instant'})"
            )
        await page.wait_for_timeout(300)
        if portal["singlePage"] == "landing":
            fname = f"{out_dir}/{theme}.png"
        else:
            fname = f"{out_dir}/{portal['singlePage']}.png"
        await page.screenshot(path=fname, full_page=False)
        captured = 1
    else:
        for screen_id in range(1, portal["screens"] + 1):
            await page.evaluate(f"goToScreen({screen_id})")
            await page.evaluate("document.activeElement?.blur()")
            await page.wait_for_timeout(300)
            fname = f"{out_dir}/screen-{screen_id:02d}.png"
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
    print(f"\nDone -- {total} screenshots written into per-persona subdirs.")


if __name__ == "__main__":
    asyncio.run(main())
