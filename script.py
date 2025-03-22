import os
import time
import requests
from selenium import webdriver

# Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1352103069823008768/QcPEZjYFQp52amD7mr2fA0Jsq5mXT-E4RmRHG9mO_jH0wPQys0UkZjHbkDprSDmallJ4"

# Set up Selenium Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--no-sandbox")  # Required for cloud environments
options.add_argument("--disable-dev-shm-usage")  # Prevent crashes in limited memory
options.add_argument("--disable-gpu")  # Not needed but can improve performance

# Start infinite loop
while True:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    
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

    # Wait 10 seconds before next iteration
    time.sleep(10)
