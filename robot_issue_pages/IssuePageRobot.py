from selenium.webdriver.common.by import By
# from jira_testing_ui.utils.waiter_helper import *
from selenium.webdriver.common.keys import Keys


class IssuePage:
    def __init__(self, driver):
        self.driver = driver

    search_value = ""
    # str(search_value)

    # issue creation
    create_button_header = (By.ID, "create_link")
    summary_field = (By.ID, "summary")
    create_button = (By.ID, "create-issue-submit")
    search_input = (By.ID, "quickSearchInput")
    task_found_link = (By.XPATH, "//a[contains(@data-issue-key,'TES-" + search_value + "')]")

    def open_dashboard_page(self):
        self.driver.get("http://localhost:8080/secure/Dashboard.jspa")

    def create_issue(self, summary):
        WaiterHelper.wait_for_clickable(self.driver, self.create_button_header)
        self.driver.find_element(*self.create_button_header).click()
        WaiterHelper.wait_for_visible(self.driver, self.summary_field)
        WaiterHelper.wait_for_visible(self.driver, self.create_button)
        self.driver.find_element(*self.summary_field).click()
        self.driver.find_element(*self.summary_field).send_keys(summary)
        self.driver.find_element(*self.create_button).click()

    def search_issue(self, search_value):
        WaiterHelper.wait_for_clickable(self.driver, self.search_input)
        self.driver.find_element(*self.search_input).click()
        self.driver.find_element(*self.search_input).send_keys(search_value, Keys.ENTER)
        WaiterHelper.wait_for_visible(self.driver, self.task_found_link)
