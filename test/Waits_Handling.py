from playwright.sync_api import Playwright, expect

def test_waits_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Waits"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Waits"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" It's ok to wait but you know.. ")
    page.locator('a[href="/waits"]').click()
    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(3000)

    # Accept the Alert
    def handle_accept_dialog(dialog):
        print(dialog.message)
        dialog.accept()

    page.locator('#accept').click()
    dialog = page.wait_for_event("dialog", timeout=5000)
    print(dialog.message)
    dialog.accept()

