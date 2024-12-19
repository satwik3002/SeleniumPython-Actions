from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Launch the Rajasthan Royals website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://www.easycalculation.com/index.php")
driver.maximize_window()
time.sleep(8)

# Step 2: Define the element to hover over
element = driver.find_element(By.CLASS_NAME, "icon-earth3")
itemToclickLocator = "/html[1]/body[1]/div[1]/header[1]/div[1]/div[2]/div[1]/span[2]/div[1]/ul[1]/li[3]/a[1]/span[1]/img[1]"

try:
    # Step 3: Perform mouse hover action
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print("Mouse hover on 'Deutschland' element performed.")
    time.sleep(5)

    # Step 4: Click on the 'Squad' item
    topLink = driver.find_element(By.XPATH, itemToclickLocator)
    actions.move_to_element(topLink).click().perform()
    print("Item clicked.")
except Exception as e:
    # Catch any exception and print the error
    print("Mouse hover failed on element. Error:", str(e))
