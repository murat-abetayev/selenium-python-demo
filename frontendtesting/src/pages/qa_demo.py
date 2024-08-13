from frontendtesting.src.pages.login_reg import LoginRegister
from frontendtesting.src.pages.lost_password import LostPassword
from frontendtesting.src.pages.my_account import MyAccount
from frontendtesting.src.pages.step import StepHelper


class QaDemo:
    my_account_link = "//ul[@class='nav-menu']//a[text()='My account']"

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd
        self.loginReg = LoginRegister(self.step, self.wd)
        self.myAccount = MyAccount(self.step, self.wd)
        self.lostPassword = LostPassword(self.step, self.wd)

    def open_url(self, url='http://192.168.110.155/demostore/'):
        self.wd.get(url)

    def click_my_account_link(self):
        self.step.click_on_element(self.my_account_link)
