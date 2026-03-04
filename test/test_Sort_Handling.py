from playwright.sync_api import Playwright, expect

def test_sort_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Sort"]')
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="Sort"]/parent::header/following-sibling::div//p')
    expect(contentElement).to_contain_text(" Sort out the problem quickly ")
    page.locator('a[href="/sortable"]').click()
    page.wait_for_load_state("networkidle")

    todo_list = page.locator('//h2[text()="To do"]/following-sibling::div/div')
    done_list = page.locator('//h2[text()="Done"]/following-sibling::div/div')

    todo_count = todo_list.count()
    print(todo_count)

    for i in range(todo_count):
        todo_dim = todo_list.first.bounding_box()
        start_x = todo_dim["x"] + todo_dim["width"]/2
        start_y = todo_dim["y"] + todo_dim["height"]/2

        done_dim = done_list.last.bounding_box()
        end_x = done_dim["x"] + done_dim["width"]/2
        end_y = done_dim["y"] + done_dim["height"]
        print(f"Iteration {i} Started")
        page.mouse.move(start_x, start_y)
        page.mouse.down()
        page.mouse.move(end_x, end_y, steps=25)
        page.mouse.up()
        page.wait_for_timeout(1500)
        print(f"Iteration {i} Completed")

    page.wait_for_timeout(3000)