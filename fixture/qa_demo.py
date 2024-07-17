from fixture.login_reg import LoginRegister
from fixture.lost_password import LostPassword
from fixture.my_account import MyAccount
from fixture.step import StepHelper


class QaDemo:
    my_account_link = "//ul[@id='primary-menu']//a[text()='My account']"

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd
        self.loginReg = LoginRegister(self.step, self.wd)
        self.myAccount = MyAccount(self.step, self.wd)
        self.lostPassword = LostPassword(self.step, self.wd)

    def open_url(self, url='https://abetayev.me/qa-demo/'):
        self.wd.get(url)

    def click_my_account_link(self):
        self.step.click_on_element(self.my_account_link)
