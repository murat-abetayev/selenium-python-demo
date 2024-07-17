from selenium.webdriver.remote.webdriver import WebDriver
from fixture.step import StepHelper


class MyAccount:

    greeting = "//p[contains(text(),'Hello')]"
    log_out_link = "//nav//a[text()='Log out']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def account_greeting_is_visible(self):
        return self.step.specified_element_is_present(self.greeting)

    def click_on_log_out_link(self):
        self.step.click_on_element(self.log_out_link)
