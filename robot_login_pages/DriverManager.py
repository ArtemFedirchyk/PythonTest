from selenium import webdriver


class DriverManager:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def create_driver(self):
        self.driver = webdriver.Chrome(r'/Users/appleteam/PycharmProjects/PythonRobot/venv/lib/chromedriver')
        return self.driver

    def close_driver(self, driver):
        driver.close
