import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# List of IDs to visit
ids = []
# Initialize the WebDriver (you might need to specify the path to your WebDriver executable)
driver = webdriver.Chrome()

# Open a new tab
driver.execute_script("window.open('about:blank', 'new_tab')")
driver.switch_to.window("new_tab")

try:
    for id in ids:
        url = f'https://ad-archive.nexxxt.cloud/#{id}'
        # Open the webpage in the new tab
        driver.get(url)

        # Wait for the "Toggle preview" button to become clickable (up to 10 seconds)
        wait = WebDriverWait(driver, 10)
        toggle_preview_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(., 'Toggle preview')]")))

        # Click the button
        toggle_preview_button.click()
        time.sleep(3)  # Add a 3-second delay

except TimeoutException:
    print("Timeout waiting for 'Toggle preview' button to become clickable on", url)

# Close the WebDriver when done
driver.quit()
