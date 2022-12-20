from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.google.cl")

#Código
driver.find_element(By.NAME, 'q')

time.sleep(10)
driver.close()
