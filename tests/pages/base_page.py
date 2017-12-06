import time
import datetime

from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from wtframework.wtf.web.page import PageObject

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(PageObject):
    """
    This is a Base Page class that combines custom methods for builiding Page Objects. Every Page Object class
    inherits from Base Page
    """

    def __init__(self, webdriver, *args, **kwargs):
        super(BasePage, self).__init__(webdriver, *args, **kwargs)

    def find_visible_element(self, xpath):
        """Use this method to locate elements that are not visible instantly"""
        try:
            return WebDriverWait(self.webdriver, WTF_TIMEOUT_MANAGER.SHORT).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            msg = "Element located in: '{0}' wasn't found!".format(xpath)
            raise TimeoutException(msg)

    def find_clickable_element(self, xpath):
        """Use this method to locate elements that are not clickable instantly"""

        try:
            return WebDriverWait(self.webdriver, WTF_TIMEOUT_MANAGER.SHORT).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            msg = "Element located in: '{0}' wasn't found!".format(xpath)
            raise TimeoutException(msg)

    def select_submenu_element(self, xpath):
        """Use this methods to select elements in submenu"""

        submenu_element = self.find_clickable_element(xpath)

        # Wait for submenu to show
        time.sleep(WTF_TIMEOUT_MANAGER.BRIEF)

        # Perform chain of actions to find and click on element
        action = ActionChains(self.webdriver)
        # First hooover over an element
        action.move_to_element(submenu_element)
        # Then click on it
        action.click()
        action.perform()

    def find_list_of_elements(self, xpath):
        """ Use this method to locate list of elements """

        # Wait for an element to show
        self.find_clickable_element(xpath)

        # Then return a list of elements
        return self.webdriver.find_elements(By.XPATH, xpath)

    def get_element_from_list(self, xpath, n):
        """This method returns text from element from a list"""
        list = self.find_list_of_elements(xpath)
        return list[n].text

    def select_player_element(self, player, el_xpath):
        """ Use this method to click on elements on a player. This metdod perform move mouse over player
        and then finds an element
        """

        # Perform chain of actions to move over player
        action = ActionChains(self.webdriver)
        # First move to a player
        action.move_to_element(player)
        action.perform()

        # Then return located element
        return self.find_clickable_element(el_xpath)

    def get_alert_text(self):
        """ Returns alert text."""
        i = 1
        while i < 5:
            try:
                return Alert(self.webdriver).text
            except NoAlertPresentException:
                time.sleep(1)
                i+=1

    @staticmethod
    def get_current_date(self):
        """ Returns current date in format 'DD.MM'"""
        return datetime.date.today().strftime("%d.%m")

    @staticmethod
    def get_current_full_date(self):
        """ Returns current date in format 'Thu Jun 08 2017'"""
        return datetime.date.today().strftime("%a %b %d %Y")

    @staticmethod
    def get_next_day_date(self):
        """ Returns next day date in format 'DD.MM'"""
        date = datetime.datetime.now() + datetime.timedelta(days=1)
        return date.strftime("%d.%m")

    @staticmethod
    def get_next_day_full_date(self):
        """ Returns next day date in format 'Thu Jun 08 2017'"""
        date = datetime.datetime.now() + datetime.timedelta(days=1)
        return date.strftime("%a %b %d %Y")

    @staticmethod
    def get_current_hour(self):
        """ Returns current hour in format 'HH:00'"""
        return datetime.datetime.now().strftime("%H:00")
