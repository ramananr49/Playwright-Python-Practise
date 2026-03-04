from playwright.sync_api import Playwright, expect, Download

def test_shadow_dom_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Shadow"]').last
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Shadow"]/parent::header/following-sibling::div//p').last
    expect(contentElement).to_contain_text(" Shadow never leaves us alone ")
    page.locator('a[href="/shadow"]').click()
    # page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    shadow_ele = page.locator('#open-shadow')
    shadow_ele.locator('#fname').fill("Lewis Hamilton")

    page.wait_for_timeout(4000)