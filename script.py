# Remove while True loop

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
