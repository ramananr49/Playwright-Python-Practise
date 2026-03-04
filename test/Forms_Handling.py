from playwright.sync_api import Playwright, expect


def test_forms_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Forms"]').last
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Forms"]/parent::header/following-sibling::div//p').last
    expect(contentElement).to_contain_text(" Interact with everything ")
    page.locator('a[href="/forms"]').click()
    # page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    page.locator('#firstname').fill("Hemanth")
    page.locator('#lasttname').fill("Rewanth")
    page.locator('#email').click()
    page.locator('#email').fill("gmail.com")
    country_code = page.locator('//label[@id="countrycode"]/following-sibling::div//select')
    country_code.select_option(value="91")
    page.locator('#Phno').fill("9876543210")
    page.locator('#Addl1').fill("No 4, Lilly Apartment")
    page.locator('#Addl2').fill("East Avenue")
    page.locator('#state').fill("Kerala")
    page.locator('#postalcode').fill("560070")
    page.locator('//label[@id="country"]/following-sibling::div//select').select_option("India")
    page.locator('#Date').fill("1993-11-25")
    page.locator('#male').check()
    page.locator('[type="checkbox"]').check()
    page.wait_for_timeout(4000)
    page.locator('[type="submit"]').click()

