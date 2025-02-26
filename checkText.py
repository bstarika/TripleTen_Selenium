from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# Replace our link with your own server link here
driver.get("https://cnt-a946de49-7a04-4edd-a3d6-9d49e3977dcb.containerhub.tripleten-services.com")

time.sleep(2)

# Gets the element's text
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Assert that the text of the discalimer variable is "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()