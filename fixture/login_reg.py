from selenium.webdriver.remote.webdriver import WebDriver
from fixture.step import StepHelper


class LoginRegister:

    username_field = "#username"
    password_field = "#password"
    login_button = "//button[text()='Log in']"
    error_message = "//ul[@class='woocommerce-error']/li"
    lost_your_password_link = "//a[text()='Lost your password?']"
    login_title = "//h2[text()='Login']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_username(self, username):
        self.step.input_text(self.username_field, username)

    def set_password(self, password):
        self.step.input_text(self.password_field, password)

    def click_login_button(self):
        self.step.click_on_element(self.login_button)

    def get_wrong_password_message_text(self):
        return self.step.get_element_text(self.error_message)

    def click_lost_your_password_link(self):
        self.step.click_on_element(self.lost_your_password_link)

    def lost_you_password_link_visible(self):
        return self.step.specified_element_is_present(self.lost_your_password_link)

    def login_title_visible(self):
        return self.step.specified_element_is_present(self.login_title)
