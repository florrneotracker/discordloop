import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")  
options.add_argument("--disable-dev-shm-usage")  
options.add_argument("--disable-gpu")  

# Initialize WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Remove while True loop

# Open webpage
driver.get("https://guestydaysreal.pythonanywhere.com/super?pretty=true&judgement=true")

# Apply zoom effect (optional)
driver.execute_script("document.body.style.zoom='.5'")

# Save screenshot
screenshot_path = "screenshot.png"
driver.save_screenshot(screenshot_path)

# Close WebDriver
driver.quit()

# Send screenshot to Discord
with open(screenshot_path, "rb") as file:
    response = requests.post(WEBHOOK_URL, files={"file": file})

# Delete screenshot after sending
os.remove(screenshot_path)

# Print status
if response.status_code == 204:
    print("✅ Screenshot sent to Discord successfully!")
else:
    print(f"❌ Failed to send screenshot! Status Code: {response.status_code}")
