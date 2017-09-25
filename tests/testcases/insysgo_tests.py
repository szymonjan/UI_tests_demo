# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore

from tests.pages.insysgo_pages import *
from tests.testdata.settings import *

import unittest
import time


class InsysgoTests(WTFBaseTest):

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get(get_url_address())

    def tearDown(self):
        do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver())

    def UC02(self):
        """ Logout from a service """
        # Actor: Logged in user
        header = Header(self.driver)
        header.select_login_button()
        LoginPage(self.driver).login_to_service(get_vip_login(), get_vip_password())

        # 1. The user selects the logout option
        header.logout_from_service()

        # 2. The system logs out the user
        Header(self.driver).select_login_button()

    def test_UC14(self):
        """ Record material """
        # Logged is user. Ability to record material
        Header(self.driver).select_login_button()
        LoginPage(self.driver).login_to_service(get_vip_login(), get_vip_password())

        # 1. The user selects the record option
        NavBar(self.driver).nowontv.click()
        time.sleep(20)
        Player(self.driver).schedule_recording()

        # Dialog that informs about not enough time before recording
        self.driver.switch_to_active_element()
        # Confirm scheduled recording
        Dialog(self.driver).confirm_recording()

        # Check if recording is scheduled
        self.assertIn("ZLECONE DO NAGRANIA", Player(self.driver).get_recording_status())

    def UC15(self):
        """ Show TV Guide"""
        # 1. The user selects the "TV guide" option
        NavBar(self.driver).select_tvguide()

        # 2. The system presents the "TV guide"
        tvguide = TvGuidePage(self.driver)

        # Check if epg for current day is returned
        self.assertIn(u"Dziś", tvguide.get_day())

        # Check that 4 channels are displayed
        channels_number = tvguide.get_channels_number()
        self.assertEqual(channels_number, 4)

        # The channels are ordered as set up in the Admin Panel
        channels_order = ['AXN BLACK', 'AXN WHITE', '4FUN FIT DANCE', 'BBC HD']

        for i in range(0, channels_number):
            self.assertEqual(channels_order[i], tvguide.get_channel_title(i))

        # Check if any past audition is displayed in EPG
        self.assertTrue(tvguide.get_past_assets_number() > 0)

        # Check if 4 current auditions are displayed in EPG
        self.assertTrue(tvguide.get_current_assets_number() == 4)

        # Check if any next auditions are displayed in EPG
        self.assertTrue(tvguide.get_next_assets_number() > 0)

        # User can open login form by clicking in nonactive play button
        tvguide.select_nonactive_play_button()
        LoginPage(self.driver).login_to_service(get_vip_login(), get_vip_password())

        # Audition can be played
        tvguide = TvGuidePage(self.driver)
        tvguide.select_active_play_button()

        self.assertIsNone(tvguide.find_floating_player())

    def UC16(self):
        """ Display Now on TV page """
        # Actor: Logged in user
        # 1. The user selects the "now on TV" page
        NavBar(self.driver).nowontv.click()

        # 2. The system displays the page "now on TV"
        now_on_tv = NowOnTvPage(self.driver)

        # List with 10 channels is displayed
        self.assertEqual(now_on_tv.get_channels_list_length(), 10)

        # For a logged in user, logging in for the first time,
        # the system displays the player play mode and enables playback of the first channel from the list
        now_on_tv.select_login_button().click()
        LoginPage(self.driver).login_to_service(get_vip_login(), get_vip_password())

        # First audition from a list is displayed on a player
        now_on_tv = NowOnTvPage(self.driver)
        player = Player(self.driver)
        self.assertEqual(now_on_tv.get_current_asset_title(), player.get_asset_title())

        # Player displays a pause button
        self.assertIsNone(player.select_pause_btn().click())

    def UC17(self):
        """Show evening programs"""
        # Preconditions
        # The TV program page is shown, or the page for the specific channel
        NavBar(self.driver).select_tvguide()
        TvGuidePage(self.driver).select_date_filter()

        # 1. The user selects the "show evening programs" option
        DateFilter(self.driver).select_evening()

        # 2. The system presents TV shows available in the evening
        self.assertIn("WIECZOREM", TvGuidePage(self.driver).get_time_of_day())

    def UC18(self):
        """ Show TV guide for one channel"""

        # 1. The user selects the option to display the TV guide for a channel
        mylist = MyListPage(self.driver)
        chosen_channel_title = mylist.get_popular_channel_title()
        mylist.select_popular_channel()

        # 2. The system displays the TV guide for the selected channel
        channelpage = ChannelPage(self.driver)
        player = Player(self.driver)

        # Check correct channel page opened
        self.assertEqual(chosen_channel_title, player.get_channel_name())

        # Check if current asset on PEG and asset on a player are the same
        self.assertEqual(channelpage.get_current_asset_title(), player.get_asset_title())

        # Check if current day is in first column
        self.assertIn(u"Dziś", channelpage.get_weekday())

        # Check if any past audition is displayed in EPG
        self.assertTrue(channelpage.get_past_assets_number() > 0)

        # Check if one current audition is displayed in EPG
        self.assertTrue(channelpage.get_current_assets_number() == 1)

        # Check if any next audition is displayed in EPG
        self.assertTrue(channelpage.get_next_assets_number() > 0)

    def UC19(self):
        """Show programs for specific date"""
        # Preconditions
        # The TV program page is shown, or the page for the specific channel
        NavBar(self.driver).select_tvguide()
        TvGuidePage(self.driver).select_date_filter()

        # 1. The user selects an option to show programs for specific date
        DateFilter(self.driver).select_next_day()

        # 2. The system selects the timetable for the specified date
        tvguide = TvGuidePage(self.driver)

        # Tommorow's date in date filter
        self.assertEqual(tvguide.get_next_day_date(), tvguide.get_date())

        # Check if no past audition is displayed in EPG
        self.assertTrue(tvguide.get_past_assets_number() == 0)

        # Check if no current auditions are displayed in EPG
        self.assertTrue(tvguide.get_current_assets_number() == 0)

        # Check if any next auditions are displayed in EPG
        self.assertTrue(tvguide.get_next_assets_number() > 0)

    def UC20(self):
        """Show channels list"""
        # Preconditions
        # The TV program page is shown, or the page for the specific channel
        NavBar(self.driver).select_tvguide()

        # 1. The user selects the option to show the channel list
        TvGuidePage(self.driver).select_channel_filter()
        channel_filter = ChannelFilter(self.driver)

        # 2. The system presents the channel list, sorted alphabetically

        channels_list = channel_filter.get_channels_names()
        sorted_channels_list = sorted(channels_list)

        def assert_channels_sorted():
            for i in range(len(channels_list)):
                if channels_list[i] != sorted_channels_list[i]:
                    return False
            return True

        self.assertTrue(assert_channels_sorted())

        # Change a channel by channel filter

        channel_filter.select_channel(4)
        channels_epg = TvGuidePage(self.driver).get_channels_titles_list()

        self.assertIn("Cartoon Network", channels_epg)

    def UC25(self):
        """ Log in with correct user credentials """

        # 1. The user selects the login option
        Header(self.driver).select_login_button()

        # 2. The system displays the login screen
        login_page = LoginPage(self.driver)

        # 3. The user enters their credentials - login and password
        login_page.login_to_service(get_vip_login(), get_vip_password())

        # 4. The system checks the credentials and log in user
        MyListPage(self.driver)

    def UC25_4a(self):
        """ Log in with incorrect user credentials """

        # 1. The user selects the login option
        header = Header(self.driver)
        header.select_login_button()

        # 2. The system displays the login screen
        login_page = LoginPage(self.driver)

        # 3. The user enters their credentials - login and password
        login_page.login_to_service("blednylogin", "blednehaslo")

        # 4a1. The system notifies the user regarding incorrect credentials
        self.assertIn("niepoprawne", login_page.get_incorrect_credentials_message().text)

        # Return to step 3 of main scenario
        # 3. The user enters their credentials - login and password
        login_page.login_to_service(get_vip_login(), get_vip_password())

        # 4. The system checks the credentials and log in user
        MyListPage(self.driver)

    def UC26(self):
        """ Display account information """

        # Actor: Logged in user
        Header(self.driver).select_login_button()
        LoginPage(self.driver).login_to_service(get_vip_login(), get_vip_password())

        # 1. The user selects the option to display settings
        Header(self.driver).select_myaccount()

        # 2. The system displays the settings
        MyAccountPage(self.driver)

    def UC32(self):
        """ Display FAQ/Help page"""

        # 1. The user selects the help option
        Footer(self.driver).faq_link.click()

        # 2. The system displays a page with the help content
        self.assertEqual("Pomoc", CmsPage(self.driver).page_title.text)

    def UC36(self):
        """ Display information about the asset"""

        # 1. The user selects the option to view information about the asset
        mylist = MyListPage(self.driver)
        selected_asset_title = mylist.get_recommended_asset_title()
        mylist.select_recommended_asset()

        # 2. The system displays detailed information and photos of the asset
        asset = AssetPage(self.driver)
        player = Player(self.driver)

        # Check if correct audition is selected
        self.assertEqual(selected_asset_title, player.get_asset_title())

        # Open next audition page
        title = asset.get_next_asset_title()
        asset.select_next_asset()
        # Check if correct audition is selected
        self.assertEqual(Player(self.driver).get_asset_title(), title)

    def UC41(self):
        """ Display terms of service page """

        # 1. The user selects the option to display the terms of service
        Footer(self.driver).privacy_policy_link.click()

        # 2. The system displays the page with the terms of service
        self.assertEqual("Regulamin", CmsPage(self.driver).page_title.text)

    def UC42(self):
        """ Display privacy policy """

        # 1. The user selects the option to display the privacy policy
        Footer(self.driver).privacy_policy_link.click()

        # 2. The system displays the page with the privacy policy
        self.assertEqual(u"Polityka Prywatności", CmsPage(self.driver).page_title.text)


if __name__ == '__main__':
    unittest.main()
