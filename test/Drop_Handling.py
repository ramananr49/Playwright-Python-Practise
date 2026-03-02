from playwright.sync_api import Playwright, expect


def test_drop_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Drop"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Drop"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Feel free to bounce me ")
    page.locator('a[href="/droppable"]').click()
    page.wait_for_load_state("networkidle")

    source_ele = page.locator('[id="draggable"]')
    target_ele = page.locator('[id="droppable"]')

    source_ele_dimension = source_ele.bounding_box()
    target_ele_dimension = target_ele.bounding_box()

    start_x = source_ele_dimension["x"] + source_ele_dimension["width"]/2
    start_y = source_ele_dimension["y"] + source_ele_dimension["height"]/2

    end_x = target_ele_dimension["x"] + target_ele_dimension["width"]/2
    end_y = target_ele_dimension["y"] + target_ele_dimension["height"]/2

    source_ele.hover()
    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(end_x, end_y, steps=25)
    page.mouse.up()

    page.wait_for_timeout(3000)