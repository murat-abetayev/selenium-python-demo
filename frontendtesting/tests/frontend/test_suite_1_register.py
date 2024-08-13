import pytest


@pytest.mark.tcid_1_1
def test_case_1_1_register(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
