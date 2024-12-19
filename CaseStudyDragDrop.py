from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(5)

# Step 2: Switch to the iframe where the draggable and droppable elements are located
driver.switch_to.frame(0)

# Step 3: Locate the draggable and droppable elements
fromElement = driver.find_element(By.ID, "draggable")
toElement = driver.find_element(By.ID, "droppable")
time.sleep(5)

# Step 4: Perform drag and drop
try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement, toElement).perform()  # Drag the element to the drop target
    time.sleep(5)
    actions.drag_and_drop(toElement, fromElement).perform()  # Drag it back again

    print("Drag and drop is Successful")

except Exception as e:
    print(f"Drag and drop failed due to: {e}")

# Close the browser
driver.quit()
