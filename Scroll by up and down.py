from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
time.sleep(8)

# Scroll Down
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(5)

# Scroll Up
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(5)

# Scroll to the element with ID "mousehover"
element = driver.find_element(By.ID, "mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(5)

# Adjust scroll position slightly upwards
driver.execute_script("window.scrollBy(0, -150);")  # Fixed syntax
time.sleep(5)


