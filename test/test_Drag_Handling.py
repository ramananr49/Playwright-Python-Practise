from playwright.sync_api import Playwright, expect

def test_drag_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Drag"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Drag"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Drag me here and there ")
    page.locator('a[href="/draggable"]').click()
    page.wait_for_load_state("networkidle")

    sample_box = page.locator('div[id="sample-box"]')
    sample_box_dimension = sample_box.bounding_box()

    sample_box.hover()

    start_X = sample_box_dimension["x"] + sample_box_dimension["width"]/2
    start_Y = sample_box_dimension["y"] + sample_box_dimension["height"]/2

    page.mouse.move(start_X, start_Y)
    page.mouse.down()
    page.mouse.move(start_X+100, start_Y+100, steps=25)
    page.mouse.up()

    page.wait_for_timeout(4000)

