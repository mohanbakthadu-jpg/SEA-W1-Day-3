"""Open Cricbuzz's live scores page and save a screenshot.

Run with: python circbuzz_score.py
The screenshot is written beside this script as latest_score.png.
"""

from pathlib import Path
import re
import sys
from datetime import datetime

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


LIVE_SCORES_URL = "https://www.cricbuzz.com/cricket-match/live-scores"
OUTPUT_FILE = Path(__file__).resolve().with_name("latest_score.png")


def run() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page(
            viewport={"width": 1440, "height": 1000},
            device_scale_factor=1,
        )

        try:
            response = page.goto(
                LIVE_SCORES_URL,
                wait_until="domcontentloaded",
                timeout=60000,
            )
            if response and response.status >= 400:
                raise RuntimeError(f"Cricbuzz returned HTTP {response.status}")

            # Wait for rendered page content instead of a brittle CSS class.
            page.locator("body").wait_for(state="visible", timeout=20000)
            try:
                page.wait_for_load_state("networkidle", timeout=12000)
            except PlaywrightTimeoutError:
                # Live updates or analytics can keep the network busy.
                pass

            page.wait_for_timeout(2500)
            page.evaluate("window.scrollTo(0, 0)")

            body_text = page.locator("body").inner_text(timeout=10000)
            if not re.search(
                r"\b(live|score|innings|overs|won|vs\.?|match)\b",
                body_text,
                re.I,
            ):
                raise RuntimeError(
                    "The page opened, but no cricket score content was detected. "
                    "Cricbuzz may be showing a CAPTCHA, access-denied page, "
                    "or a changed layout."
                )

            page.screenshot(path=str(OUTPUT_FILE), full_page=True)
            print(f"Screenshot saved: {OUTPUT_FILE}")
            print(
                "Captured:",
                datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"),
            )
        finally:
            browser.close()


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        print(f"Could not capture Cricbuzz scores: {error}", file=sys.stderr)
        print(
            "Check your internet connection and confirm Playwright Chromium is installed.",
            file=sys.stderr,
        )
        raise SystemExit(1)