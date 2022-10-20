import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

URL = 'https://chromedriver.chromium.org/downloads'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.71'}


def get_page(url):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_chrome_driver(chrome_version):
    versions = get_page(URL).find_all(class_="XqQF9c")

    for version in versions:
        try:
            c_version = int(version.get_text().split(" ")[1].split(".")[0])
        except:
            return "Error"
        try:
            if c_version == chrome_version:
                url = f"https://chromedriver.storage.googleapis.com/{version.get_text().split(' ')[1]}/chromedriver_win32.zip"
                # download the chromedriver.zip
                response = requests.get(url, headers=headers)
                file_name = 'chromedriver_win32.zip'
                with open(file_name, 'wb') as f:
                    f.write(response.content)
                # extract the zip file
                with ZipFile(file_name, 'r') as zip:
                    zip.extractall()
                break
        except:
            return "Error"
    return "Done"
