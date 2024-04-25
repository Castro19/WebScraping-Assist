from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

try:
    # Initialize the WebDriver with geckodriver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # URL of the webpage
    url = 'https://assist.org/transfer/results?year=74&institution=11&agreement=150&agreementType=from&view=agreement&viewBy=dept&viewSendingAgreements=false&viewByKey=74%2F150%2Fto%2F11%2FAllDepartments'
    driver.get(url)

   # Wait for the presence of an element specified by XPath
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="view-results"]/app-report-preview/div/awc-agreement/div/div'))
    )
    
    # If the element is found, print its text (or handle it as needed)
    print("Element found: ", element.text)

except TimeoutException:
    print("Timed out waiting for page to load or element to appear.")
except WebDriverException as e:
    print(f"WebDriver encountered an issue: {e}")
finally:
    # Ensure the driver quits no matter what
    driver.quit()