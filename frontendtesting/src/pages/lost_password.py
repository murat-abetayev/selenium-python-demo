from selenium.webdriver.remote.webdriver import WebDriver

from frontendtesting.src.pages.step import StepHelper


class LostPassword:

    lost_password_title = "//h1[text()='Lost password']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def lost_password_title_visible(self):
        return self.step.specified_element_is_present(self.lost_password_title)
