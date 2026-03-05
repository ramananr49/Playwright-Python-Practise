from playwright.sync_api import Playwright


def test_get_book_api(playwright: Playwright):
    request_context = playwright.request.new_context(base_url="http://216.10.245.166")
    res = request_context.get("/Library/GetBook.php?AuthorName=Hamilton")
    assert res.status == 200
    data =  res.json()
    assert len(data) == 4
    for i in range(len(data)):
        if i != 0:
            assert data[i]["isbn"] == "RRAY"
            print(data[i]["book_name"])
            print(data[i]["aisle"])