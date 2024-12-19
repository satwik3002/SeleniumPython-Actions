from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the SpiceJet website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://www.spicejet.com/")
driver.maximize_window()
time.sleep(8)

# Scroll Down
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(5)

# Scroll Up
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(5)

# Scroll to the element with ID "cargo"
element = driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[@id='main-container']/div[@class='css-1dbjc4n r-1niwhzg r-1jgb5lz r-r0h9e2 r-13qz1uu']/div[@class='css-1dbjc4n r-14lw9ot']/div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n r-1kihuf0 r-tvv088 r-13qz1uu']/div[@class='css-1dbjc4n r-18u37iz r-1wtj0ep r-15d164r r-1qxgc49']/div[1]/div[2]/div[4]/div[1]")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(5)


# Adjust scroll position slightly upwards
driver.execute_script("window.scrollBy(0, -150);")
time.sleep(5)



