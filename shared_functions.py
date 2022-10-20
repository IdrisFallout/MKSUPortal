import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_update import compare_versions
from download_chromedriver import get_chrome_driver

global procees_loading
procees_loading = False


def initialize_selenium():
    try:
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'}

        driver_service = Service(executable_path="chromedriver.exe")

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={headers}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-javascript")
        driver = webdriver.Chrome(service=driver_service, options=options)
        driver.set_page_load_timeout(15)
        procees_loading = True
        return driver
    except:
        output, chrome_version = compare_versions()
        if output == 'UPDATE':
            feedback = get_chrome_driver(chrome_version)
            if feedback == 'Done':
                os.system('python login.py')
            else:
                exit()
        else:
            exit()
