import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cnt-10a6fb36-917c-41a3-843b-376e78c58e3d.containerhub.tripleten-services.com")

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()