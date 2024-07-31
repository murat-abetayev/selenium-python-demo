import pytest


@pytest.mark.tc_id_2_1
@pytest.mark.uitests
def test_login_with_valid_credentials(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
    app.qaDemo.loginReg.set_username('democustomer')
    app.qaDemo.loginReg.set_password('dEmOcstmr546')
    app.qaDemo.loginReg.click_login_button()
    app.assert_that(app.qaDemo.myAccount.account_greeting_is_visible()).is_true()


@pytest.mark.tc_id_2_2
def test_login_with_valid_username_and_invalid_password(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
    app.qaDemo.loginReg.set_username('democustomer')
    app.qaDemo.loginReg.set_password('dEmOcstmr547')
    app.qaDemo.loginReg.click_login_button()
    app.assert_that(app.qaDemo.loginReg.get_wrong_password_message_text()).is_equal_to(
        "Error: The password you entered for the username democustomer is incorrect. Lost your password?")


@pytest.mark.tc_id_2_3
def test_login_with_invalid_credentials(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
    app.qaDemo.loginReg.set_username('democustomer1')
    app.qaDemo.loginReg.set_password('dEmOcstmr547')
    app.qaDemo.loginReg.click_login_button()
    app.assert_that(app.qaDemo.loginReg.get_wrong_password_message_text()).contains(
        "Error: The username democustomer1 is not registered on this site.")


@pytest.mark.tc_id_2_4
def test_login_without_credentials(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
    app.qaDemo.loginReg.set_username('')
    app.qaDemo.loginReg.set_password('')
    app.qaDemo.loginReg.click_login_button()
    app.assert_that(app.qaDemo.loginReg.get_wrong_password_message_text()).is_equal_to(
        "Error: Username is required.")


@pytest.mark.tc_id_2_5
def test_lost_your_password_link_present_and_working(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
    app.assert_that(app.qaDemo.loginReg.lost_you_password_link_visible()).is_true()
    app.qaDemo.loginReg.click_lost_your_password_link()
    app.assert_that(app.qaDemo.lostPassword.lost_password_title_visible()).is_true()


@pytest.mark.tc_id_2_6
def test_user_not_logged_out_when_pressing_browser_back_button(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
    app.qaDemo.loginReg.set_username('democustomer')
    app.qaDemo.loginReg.set_password('dEmOcstmr546')
    app.qaDemo.loginReg.click_login_button()
    app.assert_that(app.qaDemo.myAccount.account_greeting_is_visible()).is_true()
    app.step.click_browser_back_btn()
    app.assert_that(app.qaDemo.myAccount.account_greeting_is_visible()).is_true()


@pytest.mark.tc_id_2_7
def test_user_not_logged_in_when_pressing_browser_back_button(app):
    app.qaDemo.open_url()
    app.qaDemo.click_my_account_link()
    app.qaDemo.loginReg.set_username('democustomer')
    app.qaDemo.loginReg.set_password('dEmOcstmr546')
    app.qaDemo.loginReg.click_login_button()
    app.assert_that(app.qaDemo.myAccount.account_greeting_is_visible()).is_true()
    app.qaDemo.myAccount.click_on_log_out_link()
    app.assert_that(app.qaDemo.loginReg.login_title_visible()).is_true()
    app.step.click_browser_back_btn()
    app.assert_that(app.qaDemo.loginReg.login_title_visible()).is_true()
