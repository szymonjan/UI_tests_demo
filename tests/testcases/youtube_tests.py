# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore

import unittest


class YoutubeTests(WTFBaseTest):

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get("http://youtube.com")

    def tearDown(self):
        do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver())

    def UC02(self):
        pass

if __name__ == '__main__':
    unittest.main()
