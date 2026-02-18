from playwright.sync_api import Playwright, expect, Locator

def test_button_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Button"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Button"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Interact with different types of buttons ")
    page.locator('a[href="/button"]').click()
    page.wait_for_load_state("networkidle")

    #Goto Home and come back here using driver commanda
    page.locator('#home').click()
    afterURL = page.url
    page.locator('[id="testing"][href="/test"]').click()
    page.locator('a[href="/button"]').click()
    curURL = page.url
    print(f"{afterURL} is After URL")
    print(f"{curURL} is Current URL")
    assert afterURL != curURL

    # Get the X & Y co-ordinates
    locationOfBtn = page.locator('#position').bounding_box()
    print(locationOfBtn['x'])
    print(locationOfBtn['y'])

    # Find the color of the button
    color = page.locator('#color').evaluate("el => getComputedStyle(el).backgroundColor")
    print(f"Color of the Button is {color}")

    # Find the height & width of the button
    dimentionBtn = page.get_by_role("button", name="How tall & fat I am?").bounding_box()
    print(f"Height of the button {dimentionBtn['height']}")
    print(f"Width of the button {dimentionBtn['width']}")

    # Confirm button is disabled
    expect(page.locator('#isDisabled[class*="is-info"]')).to_be_disabled()

    # Click and Hold Button
    clickAndHoldBtn: Locator = page.locator('[id="isDisabled"]').last
    initialText = clickAndHoldBtn.text_content()
    clickAndHoldBtn.hover()
    page.mouse.down()
    page.wait_for_timeout(3000)
    page.mouse.up()
    afterText = clickAndHoldBtn.text_content()
    print(initialText)
    print(afterText)
    assert initialText != afterText