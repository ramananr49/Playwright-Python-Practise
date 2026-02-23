from playwright.sync_api import Playwright, expect, Page

def test_window_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    title_element = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Calendar"]')
    expect(title_element).to_be_visible()
    content_element = page.locator('//p[normalize-space()="Calendar"]/parent::header/following-sibling::div//p')
    expect(content_element).to_contain_text(" My time is precious & your? ")
    page.locator('a[href="/calendar"]').click()
    page.wait_for_load_state("networkidle")