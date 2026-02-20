import time

from playwright.sync_api import Playwright, expect, Page

def test_window_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    title_element = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Window"]')
    expect(title_element).to_be_visible()
    content_element = page.locator('//p[normalize-space()="Window"]/parent::header/following-sibling::div//p')
    expect(content_element).to_contain_text(" Switch different types of tabs or windows ")
    page.locator('a[href="/window"]').click()
    page.wait_for_load_state("networkidle")

    # Goto Home
    current_window_title = page.title()
    current_window_url = page.url
    print(current_window_url)
    print(current_window_title)
    with page.expect_popup() as popup_info:
        page.locator('[id="home"]').click()

    newpage = popup_info.value
    newpage.wait_for_load_state("networkidle")
    assert current_window_url != newpage.url
    print(f"previous URL : {current_window_url} and new window url : {newpage.url}")
    assert current_window_title != newpage.title()
    print(f"Previous Title : {current_window_title} and new window title : {newpage.title()}")
    newpage.close()

    # Open muiltple windows
    page.locator('[id="multi"]').click()
    page.wait_for_timeout(4000)
    pages = page.context.pages
    print(f"Total pages count : {len(pages)}")

    for page in pages:
        page.wait_for_load_state("domcontentloaded")
        page.bring_to_front()
        print(page.title())
        print(page.url)
        print("********************")