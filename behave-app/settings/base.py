import os


WEBDRIVER_URL = str(os.environ.get(
    'BEHAVE_WEBDRIVER', 'http://127.0.0.1:4444/wd/hub'))

DESIRED_CAPABILITIES = {
    'platform': 'ANY',
    'browserName': 'chrome',
    'version': '',
    'javascriptEnabled': True
}

PAGE_URLS = {
    'mainPage': 'http://127.0.0.1:8000/'
}
