from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # 1. Go directly to Live Scores page (always consistent)
        page.goto("https://www.cricbuzz.com/cricket-match/live-scores")
        page.wait_for_timeout(3000)

        # 2. Wait for any match card to load
        page.wait_for_selector(".cb-mtch-lst", timeout=15000)

        # 3. Extract the first match card text
        match_card = page.inner_text(".cb-mtch-lst")
        print("\nLATEST MATCH INFO:")
        print(match_card)

        # 4. Save screenshot
        page.screenshot(path="cricbuzz_latest_score.png")
        print("\nScreenshot saved as cricbuzz_latest_score.png")

        browser.close()

run()
