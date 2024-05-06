from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import re
import os

from groupCourses import map_course_groupings

FILE_NAME = "output.html"
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)

def extract_courses(course_area: BeautifulSoup) -> list:
    """
    Extracts course information from a specified section of HTML.

    Parameters
    ---
    course_area : BeautifulSoup
        A course row -- the section of HTML to parse, expected to contain divs with class 'courseLine'.

    Returns
    ---
    list
        A list of dictionaries, each containing 'courseNumber', 'courseTitle', and 'courseUnits' for each course.

    """
    courses = course_area.find_all('div', class_='courseLine')
    extracted_courses = []
    for course in courses:
        course_number = course.find('div', class_='prefixCourseNumber').text.strip().replace(" ", "")
        course_title = course.find('div', class_='courseTitle').text.strip()
        course_units = course.find('div', class_='courseUnits').text.strip()
        # remove the "units" at end of unit counts if it is present
        units_index = course_units.find("units")
        course_units = course_units[:units_index] if units_index != -1 else course_units

        extracted_courses.append({
            'courseNumber': course_number,
            'courseTitle': course_title,
            'courseUnits': course_units
        })
    return extracted_courses


try:
    # Initialize the WebDriver with geckodriver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # URL of the webpage
    url = 'https://assist.org/transfer/results?year=74&institution=11&agreement=150&agreementType=from&view=agreement&viewBy=dept&viewSendingAgreements=false&viewByKey=74%2F150%2Fto%2F11%2FAllDepartments'
    url = 'https://assist.org/transfer/results?year=74&institution=11&agreement=10&agreementType=from&view=agreement&viewBy=dept&viewSendingAgreements=false&viewByKey=74%2F10%2Fto%2F11%2FAllDepartments'
    driver.get(url)

    # Wait for the presence of an element specified by XPath
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="view-results"]/app-report-preview/div/awc-agreement/div/div'))
    )
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    course_rows = soup.find_all('div', class_='rowContent')    
    courses = []

    # Get school names and academic year
    institutions = {}
    bold_tags = soup.find_all('b')
    re_year_pattern = r'\b(\d{4})-(\d{4})\b'
    for tag in bold_tags:
        if 'To:' in tag.text:
            institutions['receivingInstitution'] = tag.text.split('To: ')[-1].strip()
        elif 'From:' in tag.text:
            institutions['sendingInstitution'] = tag.text.split('From: ')[-1].strip()
        elif re.search(re_year_pattern, tag.text):
            institutions['academicYear'] = re.search(re_year_pattern, tag.text).group(0)

    # print(bold_tags)
    # print(institutions)

    # Get agreements
    for row in course_rows:
        
        receiving_courses = row.find_all('div', class_='rowReceiving')
        sending_courses = row.find_all('div', class_='rowSending')

        courses_dict = {
            "receiving": {
                "courses": [],
                "conjunctions": []
            },
            'sending': {
                "courses": [],
                "conjunctions": []
            }
        }

        for receiving in receiving_courses:
            courses_dict["receiving"]["courses"] = extract_courses(receiving)
            conjunctions = receiving.find_all('div', class_='conjunction')
            courses_dict["receiving"]["conjunctions"] = [conj.text.strip().upper() for conj in conjunctions]

        for sending in sending_courses:
            courses_dict["sending"]["courses"] = extract_courses(sending)
            conjunctions = sending.find_all('div', class_='conjunction')
            courses_dict["sending"]["conjunctions"] = [conj.text.strip().upper() for conj in conjunctions]

        courses.append(courses_dict)

    # Convert the scraped information to the desired format and group courses appropriately.
    agreements = []
    for course in courses:
        agreements.append(map_course_groupings(course))
    # print(agreements)
    institutions["agreements"] = agreements

except TimeoutException:
    print("Timed out waiting for page to load or element to appear.")
except WebDriverException as e:
    print(f"WebDriver encountered an issue: {e}")
except Exception as e:
    print(f"Unspecified error -- possibly in map_course_groupings: {e}")
finally:
    # Ensure the driver quits no matter what
    driver.quit()

# with open(FILE_PATH, "w", encoding='utf-8') as file:
#     file.write(str(course_rows))