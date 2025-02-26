from selenium import webdriver

driver = webdriver.Chrome() # create Chrome driver
driver.maximize_window() # Full screen mode

# Open Google
driver.get('https://google.com/')  #navigate to the url
current_url = driver.current_url   # get current url
assert 'google.com' in driver.current_url # verify if google.com in the current url
driver.quit()

# Open TripleTen's Urban Routes Home Page
driver.get(" SERVER URL ") #<- changes

# Check url contains tripleten-services.com
assert "tripleten-services.com" in driver.current_url

# Close the browser
driver.quit()