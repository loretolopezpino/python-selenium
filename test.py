from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture
def browser():
    s = Service(GeckoDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=s, options=options)
    driver.maximize_window()
    yield driver
    driver.close()


def test_selenium(browser):
    wait = WebDriverWait(browser, 20)
    browser.maximize_window()
    browser.get("https://www.google.cl")
    browser.find_element(By.NAME, 'q').send_keys('28 USD to CLP')
    wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
    browser.find_element(By.NAME, 'btnK').click()

    assert len(browser.find_elements(By.ID, 'knowledge-currency__updatable-chart-column')) == 0
