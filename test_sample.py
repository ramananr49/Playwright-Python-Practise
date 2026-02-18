from playwright.sync_api import Playwright


def test_firsttest():
    print("Testing the Pytest playwright")


def test_sample_pw_python(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.letcode.in")
    page.wait_for_timeout(4000)

