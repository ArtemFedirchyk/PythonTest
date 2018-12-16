from selenium.webdriver.common.by import By
# from robot_login_pages import WaiterHelper


class LoginPageRobot:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    login_URL = 'http://localhost:8080/login.jsp'

    username_input = (By.ID, "login-form-username")
    password_input = (By.ID, "login-form-password")
    logIn_button = (By.ID, "login-form-submit")

    def first_login(self, driver, username, password):
        driver.get(self.login_URL)
        # WaiterHelper.wait_for_clickable(self.driver, self.username_input)
        # WaiterHelper.wait_for_clickable(self.driver, self.password_input)
        # WaiterHelper.wait_for_clickable(self.driver, self.logIn_button)

        driver.find_element(*self.username_input).send_keys(username)
        driver.find_element(*self.password_input).send_keys(password)
        driver.find_element(*self.logIn_button).click()

    def assert_url(self, driver, url):
        assert driver.current_url == url
