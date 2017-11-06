# -*- coding: utf-8 -*-
# This file contains all of the pages used in tests. Every page should consist of loctors (e.g. Xpath)
# and methods used to interact with an webpage elements.

from tests.pages.base_page import BasePage


class MainPage(BasePage):

    """This is a main page. It opens when user visit youtube.com page. On this page most popular videos,
    search bar and navigation buttons are displayed"""

    _login_btn = "(//paper-button[@id='button'])[1]"


    def __init__(self, webdriver, *args, **kwargs):
        super(MainPage, self).__init__(webdriver, *args, **kwargs)
