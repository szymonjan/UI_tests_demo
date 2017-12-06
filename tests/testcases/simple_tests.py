# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER

from tests.pages.simple_page import LoginPage
import tests.testdata.settings as data

import unittest

class LoginTests(WTFBaseTest):

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get(data.url_address())

    def tearDown(self):
        WTF_WEBDRIVER_MANAGER.close_driver()

    def test_valid_data(self):
        """ Test that a user with a valid login data can login """

        #Login page intitialization.
        #If some elements aren't displayed an exception is thrown.
        login_page = LoginPage(self.driver)

        #Fill the login form
        login_page.set_login(data.login())
        login_page.set_password(data.password())
        login_page.set_repeat_password(data.password())

        #Submit filled form
        login_page.submit_form()

        #Assert that user is logged in and correct message is displayed
        self.assertEqual("Succesful login!", login_page.get_alert_text())


if __name__ == '__main__':
    unittest.main()
