from playwright.sync_api import Playwright, expect

def test_input_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://letcode.in/');
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Input"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Input"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Interact with different types of input fields ")
    page.locator('a[href="/edit"]').click()
    page.wait_for_load_state("networkidle")

    #Enter your full Name
    page.locator('#fullName').fill("Lewis Hamilton")

    #Append a text and press keyboard tab
    page.locator('#join').click()
    page.locator('#join').fill(" F1 Driver")
    page.keyboard.press('Tab')

    #What is inside the text box
    acttext = page.locator('#getMe').text_content()
    print(acttext)
    expect(page.locator('#getMe')).to_have_value("ortonikc")

    #Clear the text
    beforeAction = page.locator('#clearMe').input_value()
    page.locator('#clearMe').clear()
    afterAction = page.locator('#clearMe').input_value()
    assert beforeAction != afterAction
    print(f"{beforeAction} and {afterAction}")

    #Confirm edit field is disabled
    expect(page.locator('#noEdit')).to_be_disabled()

    #Confirm text is readonly
    expect(page.locator('#dontwrite')).to_have_attribute("readonly", "")


    
