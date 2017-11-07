# -*- coding: utf-8 -*-
# This file contains all of the pages used in tests. Every page should consist of loctors (e.g. Xpath)
# and methods used to interact with an webpage elements.

from tests.pages.base_page import BasePage


class LoginPage(BasePage):

    """ This is login page designed specifically for practice. Login form
        consist of three fields and a button. """

    #All locators are specified by XPATH
    LOGIN_FIELD = "//input[@name='userid']"
    PASS_FIELD = "//input[@name='passid']"
    REPEAT_PASS_FIELD = "//input[@name='repeatpassid']"
    LOGIN_BTN = "//input[@name='submit']"

    def __init__(self, webdriver, *args, **kwargs):
        super().__init__(webdriver, *args, **kwargs)

        #Login form elements are located during page initailiztion.
        self.login_field = self.find_clickable_element(self.LOGIN_FIELD)
        self.pass_field = self.find_clickable_element(self.PASS_FIELD)
        self.repeat_pass_field = self.find_clickable_element(self.REPEAT_PASS_FIELD)
        self.login_btn = self.find_clickable_element(self.LOGIN_BTN)

    def set_login(self, text):
        "This method first clears login field then enters the username"
        self.login_field.clear()
        self.login_field.send_keys(text)

    def set_password(self, text):
        "This method first clears password field then enters the password"
        self.pass_field.clear()
        self.pass_field.send_keys(text)

    def set_repeat_password(self, text):
        "This method first cleats repeat password field then enters the repeated password"
        self.repeat_pass_field.clear()
        self.repeat_pass_field.send_keys(text)

    def submit_form(self):
        "Submit login form by clicking on a login button"
        self.login_btn.click()
