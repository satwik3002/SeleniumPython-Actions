
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(8)

# Step 2: Perform Scroll
driver.execute_script("window.scrollTo(0, 500);")  # Scroll down by 500px


# Step 3: Locate the draggable and droppable elements
drag_element = driver.find_element(By.ID, "draggable")
drop_element = driver.find_element(By.ID, "droppable")


# Step 4: Perform drag and drop
try:
    actions = ActionChains(driver)
    actions.drag_and_drop(drag_element, drop_element).perform()  # Drag the element to the target

    print("Drag and drop is Successful")
except Exception as e:
    print(f"Drag and drop failed due to: {e}")