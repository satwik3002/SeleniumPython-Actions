import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

# Step 2: Perform Scroll
driver.execute_script("window.scrollTo(0, 1500);")  # Scroll down by 1500px
time.sleep(5)

# Upload file using forward slashes in the file path
driver.find_element(By.ID, 'singleFileInput').send_keys("C:/Users/SATWIK/Downloads/Satwik.jpeg")
time.sleep(5)

# Step 3: Validation - Check if the file name is displayed after upload
try:
    # Find the element where the uploaded file name appears
    uploaded_file_name = driver.find_element(By.ID, "singleFileInput")
    if uploaded_file_name.is_displayed():
        print("File uploaded successfully.")
    else:
        print("File upload failed: File name not displayed.")
except Exception as e:
    print(f"File upload failed: {e}")

# Close the browser
driver.quit()
