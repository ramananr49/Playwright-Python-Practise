from playwright.sync_api import Playwright, expect, Page

def test_window_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto('https://letcode.in/')
    page.locator('[id="testing"][href="/test"]').click()
    title_element = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="Elements"]')
    expect(title_element).to_be_visible()
    content_element = page.locator('//p[normalize-space()="Elements"]/parent::header/following-sibling::div//p')
    expect(content_element).to_contain_text(" Play with element and smash them ")
    page.locator('a[href="/elements"]').click()
    # page.wait_for_load_state("networkidle")


    # Type and Enter your Git username
    page.locator('[name="username"]').fill("rama4")
    page.locator('#search').click()

    expect(page.locator('[class="media-content"] > p[class^="title"]')).to_have_text("Rama Narasimhan")
    print(page.locator('[class="media-content"] > p[class^="title"]').text_content())

    expect(page.locator('[class="media-content"] > p[class^="subtitle"]')).to_have_text(" San Francisco ")
    print(page.locator('[class="media-content"] > p[class^="subtitle"]').text_content())

    public_repos = page.locator("//p[text()='Public Repos']/following-sibling::p").text_content()
    public_gists = page.locator("//p[text()='Public Gists']/following-sibling::p").text_content()
    followers = page.locator("//p[text()='Followers']/following-sibling::p").text_content()
    print(public_gists)
    print(public_repos)
    print(followers)
    expect(page.locator("//p[text()='Followers']/following-sibling::p")).to_contain_text("7")

    common_link = page.locator('a[class="has-text-link"]')
    previous_btn = page.locator('button[class="pagination-previous"]')
    next_btn = page.locator('button[class="pagination-next"]')

    count = int(public_repos)//10
    print(count)
    repo_list = {}
    expect(previous_btn).to_be_disabled()
    for i in range(count):
        print(i)
        current_count = common_link.count()
        page.wait_for_timeout(2000)
        for j in range(current_count):
            text = common_link.nth(j).text_content()
            link = common_link.nth(j).get_attribute("href")
            repo_list[text] = link
        next_btn.click()
        page.wait_for_timeout(2000)
        print(i)

    print(repo_list)
    for k, v in repo_list.items():
        print(f"{k} : {v}")


    # Assert that user has image
    # //Print the user name & other informations
    # //Assert that no.of public repositories are listed correctly
    # //eg. if Public Repos has 10 then in the list 10 links should be available