from playwright.sync_api import Playwright, expect, Locator

def test_select_dropdown_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Select"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Select"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Interact with different types of drop-down ")
    page.locator('a[href="/dropdowns"]').click()
    page.wait_for_load_state("networkidle")

    # Select the apple using visible text
    fruitDropdown: Locator = page.locator('#fruits')
    fruitDropdown.select_option("Apple")
    expect(page.locator('p[class="subtitle"]')).to_contain_text("Apple")

    fruitDropdown.select_option(value="1")
    expect(page.locator('p[class="subtitle"]')).to_contain_text("Mango")

    fruitDropdown.select_option(index=4)
    expect(page.locator('p[class="subtitle"]')).to_contain_text("Banana")

    # Select your super hero's
    page.locator('[id="superheros"]').select_option(["Ant-Man", "Aquaman", "Batman"])
    print(page.locator('[id="superheros"]').input_value())

    #Select the last programming language and print all the options
    languageDropdwon: Locator = page.locator('[id="lang"]')
    options: Locator = page.locator('[id="lang"] option')
    optionsCount = options.count()

    for i in range(optionsCount):
        print(options.nth(i).text_content())

        if i == optionsCount-1:
            name = options.nth(i).text_content()
            languageDropdwon.select_option(name)
    page.screenshot(path="screenshots/dropdown.png")
    print(languageDropdwon.input_value())
    page.wait_for_timeout(4000)

    # Select India using value & print the selected value
    countyDropdown: Locator = page.locator('[id="country"]')
    countyDropdown.select_option(value="India")
    selectedValue = countyDropdown.input_value()
    print(selectedValue)