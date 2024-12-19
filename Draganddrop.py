from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("http://admin:admin@the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()
time.sleep(5)

fromElement = driver.find_element(By.ID, "column-a")
toElement = driver.find_element(By.ID, "column-b")
time.sleep(5)

try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement, toElement).perform()
    time.sleep(5)
    actions.drag_and_drop(toElement, fromElement).perform()

    print("Drag and drop is Successful")

except Exception as e:
    print(f"Drag and drop failed due to: {e}")
