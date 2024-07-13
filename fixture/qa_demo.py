from fixture.step import StepHelper


class QaDemo:

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd

    def open_url(self, url='https://abetayev.me/qa-demo/'):
        self.wd.get(url)
