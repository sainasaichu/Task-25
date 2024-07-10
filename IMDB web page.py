from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')


driver = webdriver.Firefox()

try:
    # Navigate to the IMDb search name page
    driver.get("https://www.imdb.com/search/name/")

    # Wait for the search box to be present and visible
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "suggestion-search"))
    )

    # Enter a name to search (e.g., "Tom Hanks")
    search_box.send_keys("Tom Hanks")

    # Wait for the search button to be present and visible
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "suggestion-search-button"))
    )

    # Click the search button
    search_button.click()

    # Wait for the search results to load
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lister-item"))
    )

    # You can now interact with the search results
    print("Search completed successfully.")

finally:
    # Close the browser
    driver.quit()
