def test_first_test(browser, url):
    browser.get(url)
    assert browser.title == "Your Store"
