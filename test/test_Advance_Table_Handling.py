from playwright.sync_api import Playwright, expect

def test_advance_table_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Table"]').last
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Table"]/parent::header/following-sibling::div//p').last
    expect(contentElement).to_contain_text(" It's little complicated but give a try ")
    page.locator('a[href="/advancedtable"]').click()
    # page.wait_for_load_state("networkidle")

    # page.wait_for_timeout(2000)

    page.locator('input[class="dt-input"]').fill("newport")
    expect(page.locator('//table[@id="advancedtable"]/tbody/tr')).to_have_count(2)
    page.locator('input[class="dt-input"]').clear()
    expect(page.locator('//table[@id="advancedtable"]/tbody/tr')).to_have_count(5)

    pagination_dropdown = page.locator('//select[@aria-controls="advancedtable"]')

    paginations_list = ["25", "10", "5"]

    for i in range(len(paginations_list)):
        print(i)
        pagination_dropdown.select_option(value={paginations_list[i]})
        expect(page.locator('//table[@id="advancedtable"]/tbody/tr')).to_have_count(int(paginations_list[i]))
        # page.wait_for_timeout(2000)

    page.wait_for_timeout(3000)


