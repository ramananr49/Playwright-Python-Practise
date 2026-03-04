from playwright.sync_api import Playwright, expect, Page

def test_radio_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    title_element = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Radio"]')
    expect(title_element).to_be_visible()
    content_element = page.locator('//p[normalize-space()="Radio"]/parent::header/following-sibling::div//p')
    expect(content_element).to_contain_text(" Interact with different types of radio & check boxes ")
    page.locator('a[href="/radio"]').click()
    page.wait_for_load_state("networkidle")

    # page.wait_for_timeout(3000)
    # Select any one
    yes_radio = page.locator('[id="yes"]')
    no_radio = page.locator('[id="no"]')
    expect(yes_radio).not_to_be_checked()
    expect(no_radio).not_to_be_checked()
    yes_radio.check()
    expect(yes_radio).to_be_checked()
    expect(no_radio).not_to_be_checked()
    no_radio.check()
    expect(yes_radio).not_to_be_checked()
    expect(no_radio).to_be_checked()

    # Cofirm you can select only one radio button
    yes1_radio = page.locator('[id="one"]')
    no1_radio = page.locator('[id="two"]')
    expect(yes1_radio).not_to_be_checked()
    expect(no1_radio).not_to_be_checked()
    yes1_radio.check()
    expect(yes1_radio).to_be_checked()
    expect(no1_radio).not_to_be_checked()
    no1_radio.check()
    expect(yes1_radio).not_to_be_checked()
    expect(no1_radio).to_be_checked()

    # Find the bug
    yes2_radio = page.locator('[id="nobug"]')
    no2_radio = page.locator('[id="bug"]')
    expect(yes2_radio).not_to_be_checked()
    expect(no2_radio).not_to_be_checked()
    yes2_radio.check()
    no2_radio.check()
    expect(yes2_radio).to_be_checked()
    expect(no2_radio).to_be_checked()

    # Find which one is selected
    foo_radio = page.locator('[id="foo"]')
    bar_radio = page.locator('[id="notfoo"]')

    if foo_radio.is_checked():
        print(f"Foo radio button is selected : {foo_radio.is_checked()}")
    else:
        print(f"Foo radio button is selected : {foo_radio.is_checked()}")

    if bar_radio.is_checked():
        print(f"Bar radio button is selected : {bar_radio.is_checked()}")
    else:
        print(f"Bar radio button is selected : {bar_radio.is_checked()}")

    # Confirm last field is disabled
    plan_radio = page.locator('[name="plan"]')

    for i in range(plan_radio.count()):
        if i+1 == plan_radio.count():
            assert plan_radio.nth(i).is_disabled()
            print(f"{i} element is disabled :{plan_radio.nth(i).get_attribute("id")}")
        else:
            assert plan_radio.nth(i).is_enabled()
            print(f"{i} element is enabled :{plan_radio.nth(i).get_attribute("id")}")

    # Find if the checkbox is selected?
    remember_me = page.locator('[type="checkbox"]')

    if remember_me.first.is_checked():
        print(f"Remember me check box is checked: {remember_me.first.is_checked()}")
    else:
        print(f"Remember me check box is not checked: {not remember_me.first.is_checked()}")

    # Accept the T&C
    remember_me.last.check()
    if remember_me.last.is_checked():
        print("I agree Checkbox is checked")
    else:
        print("I agree Checkbox is not checked")