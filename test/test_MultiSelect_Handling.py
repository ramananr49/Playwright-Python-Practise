from playwright.sync_api import Playwright, expect

def test_multi_select_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Multi-Select"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Multi-Select"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Be a multi-tasker ")
    page.locator('a[href="/selectable"]').click()
    page.wait_for_load_state("networkidle")

    options_common = page.locator('div[class="list-container"] > div')

    count = options_common.count()
    print(count)

    for i in range(count):
        expect(options_common.nth(i)).not_to_have_attribute("class", "selected")
        options_common.nth(i).click()
        page.wait_for_timeout(2000)
        expect(options_common.nth(i)).to_have_attribute("class", "ng-star-inserted selected")

    print("validation Completed")