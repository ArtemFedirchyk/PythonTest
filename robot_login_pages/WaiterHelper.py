import sys
# sys.path.append('c:\\Users\\afedirchyk\\Projects\\first_test\\robot\\waiter_helper.py')
# sys.path.append('/Users/anastasia/PycharmProjects/first/robot/robot_login_pages/login_pages/waiter_helper.py')
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WaiterHelper:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def wait_for_visible(driver, element):
        return WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(element))

    def wait_for_clickable(driver, element):
        return WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(element))

    def wait_for_present(driver, element):
        return WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(element))
