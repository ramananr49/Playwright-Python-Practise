from playwright.sync_api import Playwright, expect

def test_simple_table_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Table"]').first
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Table"]/parent::header/following-sibling::div//p').first
    expect(contentElement).to_contain_text(" It's all about rows & columns ")
    page.locator('a[href="/table"]').click()
    # page.wait_for_load_state("networkidle")

    #Shopping List Table Handling
    product_price = page.locator('//table[@id="shopping"]/tbody/tr/td[2]')
    total_price = page.locator('//table[@id="shopping"]/tfoot/td[2]')

    count = product_price.count()
    print(count)
    calculated_total = 0
    for i in range(count):
        price_str = product_price.nth(i).text_content()
        print(price_str)
        calculated_total += int(price_str)
    print(calculated_total)
    total_str = total_price.text_content()
    assert int(total_str) == calculated_total
    print(f"Actual Total : {total_str} and Calculated Total : {str(calculated_total)}")


    #~ Mark Raj as present
    common_first_name_cell = page.locator('//table[@id="simpletable"]/tbody/tr/td[1]')
    common_second_name_cell = page.locator('//table[@id="simpletable"]/tbody/tr/td[2]')

    row_count = common_first_name_cell.count()
    for i in range(row_count):
        if common_first_name_cell.nth(i).text_content() == "Raj":
            common_first_name_cell.nth(i).locator('xpath=following-sibling::td/input').check()
        elif common_second_name_cell.nth(i).text_content() == "Raj":
            common_second_name_cell.nth(i).locator('xpath=following-sibling::td/input').check()

    # page.wait_for_timeout(3000)

    # ~ Check if the sorting is working properly
    desert_col = page.locator('[mat-sort-header="name"]')
    names_cell = page.locator('table[class*="mat-sort"] tr td:nth-child(1)')

    initial_names_list = []
    for i in range(names_cell.count()):
        temp = names_cell.nth(i).text_content()
        print(temp)
        initial_names_list.append(temp)
    print(initial_names_list)

    desert_col.click()

    act_sorted_names_list = []
    for i in range(names_cell.count()):
        temp = names_cell.nth(i).text_content()
        print(temp)
        act_sorted_names_list.append(temp)
    print(act_sorted_names_list)

    initial_names_list.sort()
    print(initial_names_list)
    assert initial_names_list == act_sorted_names_list