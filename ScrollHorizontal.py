from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(8)

driver.switch_to.frame(0)
element = driver.find_element(By.XPATH, "//body/div[@id='slider']/span[1]")

try:
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(element, 400, 0).perform()  # Correct syntax
    print("Sliding Element Successful")
except Exception as e:
    print(f"Sliding failed on element: {e}")  # Corrected string formatting
