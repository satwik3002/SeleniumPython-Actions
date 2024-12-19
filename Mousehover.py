from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Launch the Rajasthan Royals website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://www.rajasthanroyals.com/login")
driver.maximize_window()
time.sleep(8)

# Step 2: Define the element to hover over
element = driver.find_element(By.CLASS_NAME, "nav-anchor")
itemToclickLocator = "//span[normalize-space()='Squad']"

try:
    # Step 3: Perform mouse hover action
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print("Mouse hover on 'Squad' element performed.")
    time.sleep(5)

    # Step 4: Click on the 'Squad' item
    topLink = driver.find_element(By.XPATH, itemToclickLocator)
    actions.move_to_element(topLink).click().perform()
    print("Item clicked.")
except Exception as e:
    # Catch any exception and print the error
    print("Mouse hover failed on element. Error:", str(e))
