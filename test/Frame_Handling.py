from playwright.sync_api import Playwright, expect, Page

def test_frame_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    titleelement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Frame"]')
    expect(titleelement).to_be_visible()
    contentelement = page.locator('//p[normalize-space()="Frame"]/parent::header/following-sibling::div//p')
    expect(contentelement).to_contain_text(" Interact with different types of frames/iframes ")
    page.locator('a[href="/frame"]').click()
    page.wait_for_load_state("networkidle")

    parent_frame_ele = page.frame_locator('#firstFr')
    parent_frame_ele.locator('input[name="fname"]').fill("Lewis")
    parent_frame_ele.locator('input[name="lname"]').fill("Hamilton")

    child_frame_ele = parent_frame_ele.frame_locator('iframe[src="innerframe"]')
    child_frame_ele.locator('[name="email"]').fill("Lewishamilton@fiaf1.com")

    expect(parent_frame_ele.locator('input[name="fname"]')).to_have_value("Lewis")
    expect(parent_frame_ele.locator('input[name="lname"]')).to_have_value("Hamilton")
    expect(child_frame_ele.locator('[name="email"]')).to_have_value("Lewishamilton@fiaf1.com")
    page.wait_for_timeout(3000)