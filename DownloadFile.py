import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, 'textbox').send_keys("Hi I'm Satwik")
driver.find_element(By.ID, 'createTxt').click()
driver.find_element(By.ID, 'link-to-download').click()
time.sleep(5)

driver.find_element(By.ID, 'textbox').send_keys("Hi I'm Satwik")
driver.find_element(By.ID, 'createPdf').click()
driver.find_element(By.ID, 'pdf-link-to-download').click()
time.sleep(5)