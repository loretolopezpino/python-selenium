from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selenium():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    wait = WebDriverWait(driver, 20)
    driver.maximize_window()
    driver.get("https://www.google.cl")
    driver.find_element(By.NAME, 'q').send_keys('28 USD to CLP')
    wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
    driver.find_element(By.NAME, 'btnK').click()

    assert len(driver.find_elements(By.ID, 'knowledge-currency__updatable-chart-column')) == 0
    driver.close()


test_selenium()
