from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,      # 👈 browser will be visible
        slow_mo=500          # 👈 500ms delay between actions
    )
    page = browser.new_page()
    page.goto("https://github.com/")
    page.wait_for_timeout(3000)  # wait 3 seconds

