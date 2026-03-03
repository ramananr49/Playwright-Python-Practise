from playwright.sync_api import Playwright, expect

def test_slider_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Slider"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Slider"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Hmm.. Can you slide me? ")
    page.locator('a[href="/slider"]').click()
    page.wait_for_load_state("networkidle")

    inputs = ["5", "15", "20"]
    for i in range(len(inputs)):
        page.locator("#generate").fill(inputs[i])
        page.get_by_role("button", name="Get Countries").click()
        page.wait_for_timeout(1000)
        raw_text = page.locator('[class^="notification"] > p').text_content()
        countries = raw_text.split(" - ")
        exp_count = str(len(countries))
        print(f"Expected Count {exp_count}")
        assert exp_count == inputs[i]
        print(f"Expected Count = {exp_count} and Actual Count : {inputs[i]}")
        page.wait_for_timeout(2000)