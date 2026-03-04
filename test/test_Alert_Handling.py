from playwright.sync_api import Playwright, expect, Locator, Page

def test_alert_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Alert"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Alert"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Interact with different types of dialog boxes ")
    page.locator('a[href="/alert"]').click()
    page.wait_for_load_state("networkidle")

    # Accept the Alert
    def handle_accept_dialog(dialog):
        print(dialog.message)
        dialog.accept()

    page.once("dialog", handle_accept_dialog)
    page.locator('[id="accept"]').click()

    # Dismiss the Alert & print the alert text
    def handle_confirm_dialog(dialog):
        print(dialog.message)
        dialog.dismiss()

    page.once("dialog", handle_confirm_dialog)
    page.locator('#confirm').click()

    #Type your name & accept
    def handle_prompt_dialog(dialog):
        print(dialog.message)
        dialog.accept("Lewis Hamilton")

    page.once("dialog", handle_prompt_dialog)
    page.locator('#prompt').click()
    expect(page.locator('#myName')).to_contain_text("Lewis Hamilton")
    print(page.locator('#myName').text_content())

    # Sweet alert
    page.locator('#modern').click()
    expect(page.locator('p[class="title"]')).to_be_visible()
    expect(page.locator('p[class="title"]')).to_contain_text('Modern Alert - Some people address me as sweet alert as well ')
    page.locator('button[aria-label="close"]').click()
    print(page.locator('p[class="title"]').text_content())
