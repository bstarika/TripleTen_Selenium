import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cnt-d0cdd3d5-5100-4ec9-b6be-9044762008a8.containerhub.tripleten-services.com")

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()