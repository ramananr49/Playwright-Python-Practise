import os.path

from playwright.sync_api import Playwright, expect, Download


def test_forms_handling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://letcode.in/")
    page.locator('[id="testing"][href="/test"]').click()
    titleElement = page.locator('//p[contains(@class, "card-header-title") and normalize-space()="File"]').last
    expect(titleElement).to_be_visible()
    contentElement = page.locator('//p[normalize-space()="File"]/parent::header/following-sibling::div//p').last
    expect(contentElement).to_contain_text(" All your data is secured! ")
    page.locator('a[href="/file"]').click()
    # page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    # File Upload Scenario Validation
    file_ele = page.locator('input[type="file"]')
    file_path = "resources/uploadFile.pdf"
    file_ele.set_input_files(file_path)
    expect(page.locator('p[class*="label"]')).to_contain_text('Selected File: uploadFile.pdf')

    # File Download Scenario Validation
    download_excel = page.locator('a[id="xls"]')
    download_pdf = page.locator('a[id="pdf"]')
    download_text = page.locator('a[id="txt"]')

    # Verify Excel Download
    with page.expect_download() as download_info:
        download_excel.click()
    downloadExcel = download_info.value
    assert downloadExcel.suggested_filename == "sample.xlsx"
    downloadExcel.save_as("downloads/sample.xlsx")

    # Verify PDF Download
    with page.expect_download() as download_info1:
        download_pdf.click()
    downloadpdf = download_info1.value
    assert downloadpdf.suggested_filename == "sample.pdf"
    downloadpdf.save_as("downloads/sample.pdf")

    # Verify Text Download
    with page.expect_download() as download_info2:
        download_text.click()
    downloadtext = download_info2.value
    assert downloadtext.suggested_filename == "sample.txt"
    downloadtext.save_as("downloads/sample.txt")

    files_to_delete = ["downloads/sample.xlsx",
                       "downloads/sample.pdf",
                       "downloads/sample.txt"]

    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed the file {file}")