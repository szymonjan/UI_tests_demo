# -*- coding: utf-8 -*-

from tests.pages.base_page import BasePage


class Header(BasePage):

    """This is a header of a webpage."""

    # Login button in the upper right page corner
    _login_btn_xpath = "//a[@class='theme__button___1iKuo RTButton__raised___z9-mt theme__raised___ONZv6 theme__accent___3MS_k']"

    # Account submenu button in the upper right page corner
    _submenu_btn_xpath = "//button[@class='ContextMenu__trigger___3_fvu']"

    # 'My account' lbutton in submenu
    _my_account_btn_xpath = "//ul[@class='ContextMenu__menuInner___GRiWG']/li[1]"

    # Logout button in submenu
    _logout_btn_xpath = "//ul[@class='ContextMenu__menuInner___GRiWG']/li[2]"

    # App logo
    _logo_xpath = "//img[@alt='Logo']"


    def __init__(self, webdriver, *args, **kwargs):
        # Initialise static elements of a webpage
        super(Header, self).__init__(webdriver, *args, **kwargs)

        self.find_clickable_element(self._logo_xpath)

    def logout_from_service(self):
        # Open context menu
        self.find_clickable_element(self._submenu_btn_xpath).click()

        # Click [LOGOUT] button in submenu
        self.select_submenu_element(self._logout_btn_xpath)

    def select_login_button(self):
        # Click on the login button that shows if user isn't logged in
        self.find_clickable_element(self._login_btn_xpath).click()

    def select_myaccount(self):
        # Open context menu
        self.find_clickable_element(self._submenu_btn_xpath).click()

        # Click on 'My account' button in submenu
        self.select_submenu_element(self._my_account_btn_xpath)


class NavBar(BasePage):
    """ This is menu that allows for navigation between 'My lists', 'tv guide', 'mow on tv' pages"""

    # 'My lists' link
    _mylists_xpath = "//a[@class='MainMenu__active___1zVLb']"

    # 'Now on tv' link
    _nowontv_xpath = "//a[@href='/epg/teraz-w-tv']"

    # 'TV guide' link
    _tvguide_xpath = "//a[@href='/epg']"

    def __init__(self, webdriver, *args, **kwargs):
        # Initialise static elements of a webpage
        super(NavBar, self).__init__(webdriver, *args, **kwargs)

        self.mylists = self.find_clickable_element(self._mylists_xpath)
        self.nowontv = self.find_clickable_element(self._nowontv_xpath)
        self.tvguide = self.find_clickable_element(self._tvguide_xpath)

    def select_mylists(self):
        return self.mylists.click()

    def select_nowontv(self):
        return self.nowontv.click()

    def select_tvguide(self):
        return self.tvguide.click()


class MyListPage(BasePage):

    """
    This is a main page of an application. It combines information about auditions and
    user recordings.
    """

    # 'Recommended for you' banner title
    _recommended_title_xpath = "//h2[@class='Recommendations__title___2dm8p']"

    # 'Most popular channels' carousel title
    _popular_channels_title_xpath = "//h2[@class='TilesList__title___3zHwQ']"

    # Current audition in popular channels
    _asset_xpath = "//div[@data-index=0]//h1[@class='MostPopularChannelsTile__title___1K_e3']/a"

    # First popular channel link
    _channel_link_xpath = "//div[@data-index=0]//div[@class='MostPopularChannelsTile__imgSpace___2TOjJ']//a"

    # First popular channel title
    _channel_title_xpath = "//div[@data-index=0]//div[@class='MostPopularChannelsTile__imgSpace___2TOjJ']/h1"

    # Recommendated auditions title
    _recommended_asset_title = "//h1[@class='Recommendations__auditionTitle___2kt9E']"

    # Recommended audition tile
    _recommended_asset = "//a[@class='Recommendations__link___1Zsnz']"

    def __init__(self, webdriver, *args, **kwargs):
        # Initialise static elements of a webpage
        super(MyListPage, self).__init__(webdriver, *args, **kwargs)

        self.find_visible_element(self._recommended_title_xpath)
        self.find_visible_element(self._popular_channels_title_xpath)
        self.recommended_assets_list = self.find_list_of_elements(self._recommended_asset)
        self.recommended_assets_titles_list = self.find_list_of_elements(self._recommended_asset_title)
        self.channel_link = self.find_clickable_element(self._channel_link_xpath)
        self.channel_title = self.find_visible_element(self._channel_title_xpath)

    def select_recommended_asset(self, n=0):
        return self.recommended_assets_list[n].click()

    def get_recommended_asset_title(self, n=0):
        return self.recommended_assets_titles_list[n].text

    def get_popular_channel_title(self):
        return self.channel_title.text

    def select_popular_channel(self):
        return self.channel_link.click()

    def select_current_asset(self, n=0):
        return self.find_clickable_element(self._asset_xpath).click()

class LoginPage(BasePage):

    """This is user login page. On this page user can log in to a serivce"""

    # Login form title
    _login_form_title_xpath = "//h1[@class='LoginForm__title___8wMlp']"

    # Login field
    _login_field_xpath = "//input[@name='Login']"

    # Password field
    _password_field_xpath = "//input[@name='Password']"

    # 'Fill login credentials' message displayed if login form is empty
    _fill_credentials_xpath = "//div[@class='LoginForm__messageContent___GadUf']"

    # 'Trouble logging in?' message
    _login_help_xpath = "//div[@class='LoginForm__loginProblems___3MlT8']/a"

    # Login button displayed if user filled credetials
    _login_btn_xpath = "//div[@class='LoginForm__submit___1Tali']"

    # incorrect credentials message
    _incorrect_credentials_message_xpath = "//div[@class='LoginForm__message___2WWbV LoginForm__error___3LgxU']/div"

    def __init__(self, webdriver, *args, **kwargs):
        # Initialise static elements of a webpage
        super(LoginPage, self).__init__(webdriver, *args, **kwargs)

        self.find_visible_element(self._login_form_title_xpath)
        self.login_field = self.find_clickable_element(self._login_field_xpath)
        self.password_field = self.find_clickable_element(self._password_field_xpath)
        self.fill_data_message = self.find_visible_element(self._fill_credentials_xpath)
        self.login_help = self.find_clickable_element(self._login_help_xpath)

    def login_to_service(self, login, password):
        # Clear login form before entering credentials
        self.login_field.clear()
        self.password_field.clear()

        # Enter login credentials
        self.login_field.send_keys(login)
        self.password_field.send_keys(password)

        # Press login button
        self.find_clickable_element(self._login_btn_xpath).click()

    def get_incorrect_credentials_message(self):
        # "Indcorrect credentials" message displayed if user enters incorrect login ot password
        return self.find_visible_element(self._incorrect_credentials_message_xpath)


class MyAccountPage(BasePage):

    """ This is user account page. On this page user can check information about his account. """

    # My account age name
    _myaccount_name_xpath = "//h1[@class='AccountProfile__title___3_g5M']"

    # Label of username data
    _username_label_xpath = "//ul[@class='AccountProfile__list___1WPGg']/li[1]/h2"

    # Usernaname
    _username_xpath = "//ul[@class='AccountProfile__list___1WPGg']/li[1]/div/p"

    # Label of user active package
    _package_label_xpath = "//li[@class='AccountProfile__list___1WPGg']/ul/li[2]/h2"

    # User package name
    _package_name_xpath = "//h3[@class='AccountProfile__productName___vCamV']"

    def __init__(self, webdriver, *args, **kwargs):
        super(MyAccountPage, self).__init__(webdriver, *args, **kwargs)

        self.find_visible_element(self._myaccount_name_xpath)
        self.find_visible_element(self._username_label_xpath)
        self.find_visible_element(self._username_xpath)
        self.find_visible_element(self._package_label_xpath)
        self.find_visible_element(self._package_name_xpath)


class CmsPage(BasePage):

    """ This is a represantation of any of static pages """

    # CMS page title
    _cms_page_title_xpath = "//h1[@class='StaticPage__title___2rfzS']"

    def __init__(self, webdriver, *args, **kwargs):
        super(CmsPage, self).__init__(webdriver, *args, **kwargs)

        self.page_title = self.find_visible_element(self._cms_page_title_xpath)

class Dialog(BasePage):

    """ This object contains all types of dialogs """

    #Button that schedules recording
    _recording_button_xpath = "//button[contains(text(), 'Zleć nagranie')]"

    def confirm_recording(self):
        recording_button = self.find_clickable_element(self._recording_button_xpath)
        recording_button.click()

class Player(BasePage):

    """ In this class all of player elements and methods are defined"""

    # Floating player location
    _player_xpath = "//div[@class='FloatingPlayer__playerPlaceholder___3YApl']"

    # Login button on a player
    _login_button_xpath = "//button[contains(@class,'1RNEb')]"

    # Poster behind player
    _poster_xpath = "//div[@class='FloatingPlayer__posterBg___3_sQN']"

    # Audition displayed on a player title
    _audition_title_xpath = "//h1[@class='AuditionAside__title___3nZMu']"

    # Channel logo
    _channel_logo_xpath = "//img[@class='AuditionAside__channelLogo___eOmau']"

    # Pause button on a player
    _pause_player_xpath = "//button[@title='Pause']"

    # Fullscreen button on a player
    _fullscreen_player_xpath = "//button[@title='Fullscreen']"

    # Schedule recording button
    _recording_button_xpath = "//button[contains(@class,'FloatingAuditionAsideRecording__schedule___1YkZB')]"

    # Recording recording is scheduled dialog
    _recording_status_xpath = "//button[contains(@class, 'theme__button___1iKuo RTButton')]"

    def __init__(self, webdriver, *args, **kwargs):
        super(Player, self).__init__(webdriver, *args, **kwargs)

        try:
            self.find_visible_element(self._poster_xpath)
            self.player = self.find_clickable_element(self._player_xpath)
        except:
            pass

        self.asset_title = self.find_visible_element(self._audition_title_xpath)
        self.channel_logo = self.find_clickable_element(self._channel_logo_xpath)

    def select_pause_btn(self):
        """ Search for pause button. Pause is displayed when video is playing"""
        return self.select_player_element(self.player, self._pause_player_xpath)

    def select_fullscreen_btn(self):
        """ Search for fulscreen button. Fullscreen button is displayed when video is playing"""
        return self.select_player_element(self.player, self._fullscreen_player_xpath)

    def get_asset_title(self):
        return self.asset_title.text

    def get_channel_name(self):
        channel = self.find_clickable_element(self._channel_logo_xpath)
        return channel.get_attribute("alt")

    def schedule_recording(self):
        recording_button = self.find_clickable_element(self._recording_button_xpath)
        recording_button.click()

    def get_recording_status(self):
        return self.find_clickable_element(self._recording_status_xpath).text

class AssetPage(BasePage):

    """ This is asset details page"""

    # 'Next on this channel' carousel title
    _carousel_title_xpath = "//h2[@class='TilesList__title___3zHwQ']"

    # 'Next on this channel' asset title
    _next_assets_title_xpath = "//h1[@class='AuditionTile__title___1xOB0']/a"

    # Current asset title
    _asset_title_xpath = "//h1[@class='Asset__title___HittY']"

    def __init__(self, webdriver, *args, **kwargs):
        super(AssetPage, self).__init__(webdriver, *args, **kwargs)

        self.find_visible_element(self._carousel_title_xpath)
        self.next_assets_list = self.find_list_of_elements(self._next_assets_title_xpath)
        self.audition_title = self.find_visible_element(self._asset_title_xpath)

    def select_next_asset(self, n=0):
        """ Click on the audition from 'Next audtion..' carousel """
        return self.next_assets_list[n].click()

    def get_next_asset_title(self, n=0):
        """ Click on the audition from 'Next audtion..' carousel """
        return self.next_assets_list[n].text

class ChannelPage(BasePage):

    """ This is one channel page. On this page EPG for a chosen channel is displayed"""

    # Current audition title in EPG
    _current_asset_epg_xpath = "//a[@class='EpgAudition__root___k0Ucz EpgAudition__isCurrent___2DzTZ']/div/h2"

    # Past audtion title
    _past_asset_epg_xpath = "//a[@class='EpgAudition__root___k0Ucz EpgAudition__isPast___1S8qs']/div/h2"

    # Next audition title
    _next_asset_epg_xpath = "//a[@class='EpgAudition__root___k0Ucz EpgAudition__isNext___1wUkI']/div/h2"

    # Weekday header
    _weekday_header_xpath = "//div[@class='Channel__weekday___IHpH5']"

    # Channel filter button
    _channel_filter_xpath = "//button[@class='ContextMenu__trigger___3_fvu ChannelPicker__trigger___2fRYo']"

    def __init__(self, webdriver, *args, **kwargs):
        super(ChannelPage, self).__init__(webdriver, *args, **kwargs)

        self.weekdays_list = self.find_list_of_elements(self._weekday_header_xpath)
        self.current_asset = self.find_clickable_element(self._current_asset_epg_xpath)

    def get_current_asset_title(self):
        return self.current_asset.text

    def get_weekday(self, n=0):
        return self.weekdays_list[n].text

    def get_past_assets_number(self):
        try:
            return len(self.find_list_of_elements(self._past_asset_epg_xpath))
        except:
            return 0

    def get_current_assets_number(self):
        try:
            return len(self.find_list_of_elements(self._current_asset_epg_xpath))
        except:
            return 0

    def get_next_assets_number(self):
        try:
            return len(self.find_list_of_elements(self._next_asset_epg_xpath))
        except:
            return 0


class NowOnTvPage(BasePage):

    """ This is "Now on tv" page that shows current auditions from every channel """

    # Now on tv page title
    _nowontv_title_xpath = "//h2[@class='NowOnTv__title___1oKrn']/span"

    # Every channel logo
    _channels_logos_xpath = "//a[@class='NowOnTv__imageHolder___16JPI']"

    # Every current audition
    _current_auditions_xpath = "//div[@class='Audition__current___2Tz2E']//a"

    # Every next audtion
    _next_auditions_xpath = "//div[@class='Audition__next___2_Jx-']//a"

    # Login button on a player
    _login_button_xpath = "//button[contains(@class,'1RNEb')]"

    # Poster behind player
    _poster_xpath = "//div[@class='FloatingPlayer__posterBg___3_sQN']"


    def __init__(self, webdriver, *args, **kwargs):
        super(NowOnTvPage, self).__init__(webdriver, *args, **kwargs)

        try:
            self.find_visible_element(self._nowontv_title_xpath)
        except:
            pass

        self.channels_list = self.find_list_of_elements(self._channels_logos_xpath)
        self.current_assets_list = self.find_list_of_elements(self._current_auditions_xpath)
        self.next_assets_list = self.find_list_of_elements(self._next_auditions_xpath)

    def select_login_button(self):
        return self.find_clickable_element(self._login_button_xpath)

    def get_channels_list_length(self):
        return len(self.channels_list)

    def get_current_asset_title(self, n=0):
        """ Returns n-th audition from a list title """
        return self.current_assets_list[n].text


class TvGuidePage(BasePage):

    """ This is the TV guide pgae. It shows EPG in vertical layout"""

    # Channel logo in column header
    _channel_logo_xpath = "//div[@class='Channel__logo___2_Ybt']"

    # Channel title
    _channel_title_xpath = "//div[@class='Channel__info___11Qvy']/p"

    # Play button unavialable for not logged in user
    _play_button_nonactive_xpath = "//span[@class='material-icons PlayButton__playButton___3r3zC Channel__playButton___EDEcX PlayButton__isUnavailable___-NL1K']"

    # Play button available for logged user with channels in his package
    _play_button_active_xpath = "//span[@class='material-icons PlayButton__playButton___3r3zC Channel__playButton___EDEcX']"

    # Current audition title in column header
    _current_asset_header_xpath = "//p[@class='Channel__title___3RoeD']"

    # Current audition title in EPG
    _current_asset_epg_xpath = "//a[@class='EpgAudition__root___k0Ucz EpgAudition__isCurrent___2DzTZ']/div/h2"

    # Past audtion title
    _past_asset_epg_xpath = "//a[@class='EpgAudition__root___k0Ucz EpgAudition__isPast___1S8qs']/div/h2"

    # Next audition title
    _next_asset_epg_xpath = "//a[@class='EpgAudition__root___k0Ucz EpgAudition__isNext___1wUkI']/div/h2"

    # Date filter button
    _date_filter_xpath = "//div[contains(@class,'ContextMenu__contextMenu___2bj_E DropdownDateTimePicker__contextMenu___2pJdc')]/button"

    # Day in date filter
    _day_xpath = "//time[@class='DropdownDateTimePicker__triggerDay___2ShwM']"

    # Date in date filter
    _date_xpath = "//time[@class='DropdownDateTimePicker__triggerDate___3If9W']"

    # Time of day label
    _time_label_xpath = "//time[@class='DropdownDateTimePicker__triggerTime___3dbnk']"

    # Channel filter button
    _channel_filter_xpath = "//button[@class='ContextMenu__trigger___3_fvu ChannelPicker__trigger___2fRYo']"

    # Navigation arrow to move carousel to the next channels
    _next_channels_xpath = "//button[contains(@class, 'buttonNext')]"

    # Context menu button
    _context_menu_button_xpath = "//span[contains(text(),'more_vert')]"

    # Floatin player
    _floating_player_xpath = "//div[@class='FloatingPlayer__playerPlaceholder___3YApl']"


    def __init__(self, webdriver, *args, **kwargs):
        super(TvGuidePage, self).__init__(webdriver, *args, **kwargs)
        self.channel_logos_list = self.find_list_of_elements(self._channel_logo_xpath)

    def select_channel_filter(self):
        self.find_clickable_element(self._channel_filter_xpath).click()

    def select_date_filter(self):
        self.find_clickable_element(self._date_filter_xpath).click()

    def get_current_audition_epg_title(self, n=0):
        return self.get_element_from_list(self._current_asset_epg_xpath, n)

    def get_current_audition_header_title(self, n=0):
        return self.get_element_from_list(self._current_asset_header_xpath, n)

    def get_channel_title(self, n=0):
        return self.get_element_from_list(self._channel_title_xpath, n)

    def get_channels_titles_list(self):
        channels_titles_list = []
        for i in range(self.get_channels_number()):
            channels_titles_list.append(self.get_channel_title(i))
        return channels_titles_list

    def get_channels_number(self):
        return len(self.channel_logos_list)

    def get_past_assets_number(self):
        try:
            return len(self.find_list_of_elements(self._past_asset_epg_xpath))
        except:
            return 0

    def get_current_assets_number(self):
        try:
            return len(self.find_list_of_elements(self._current_asset_epg_xpath))
        except:
            return 0

    def get_next_assets_number(self):
        try:
            return len(self.find_list_of_elements(self._next_asset_epg_xpath))
        except:
            return 0

    def get_time_of_day(self):
        return self.find_visible_element(self._time_label_xpath).text

    def get_day(self):
        return self.find_visible_element(self._day_xpath).text

    def get_date(self):
        return self.find_visible_element(self._date_xpath).text

    def select_nonactive_play_button(self):
        self.find_clickable_element(self._play_button_nonactive_xpath).click()

    def select_active_play_button(self):
        self.find_clickable_element(self._play_button_active_xpath).click()

    def find_floating_player(self):
        self.find_visible_element(self._floating_player_xpath)

class DateFilter(BasePage):
    """ This is a date filter popup. It's displayed on Tv Guide and lets user choose date of EPG"""

    # Now button
    _now_button_xpath = "//button[contains(.,'Teraz')]"

    # Evening button
    _evening_button_xpath = "//button[contains(.,'Wieczorem')]"

    # Filter button
    _filter_button_xpath = "//button[contains(.,'Filtruj')]"

    # Cancel button
    _cancel_button_xpath = "//button[contains(.,'Anuluj')]"

    # Common date picker xpath
    _daypicker_xpath = "//div[@aria-label='{0}']"

    def __init__(self, webdriver, *args, **kwargs):
        super(DateFilter, self).__init__(webdriver, *args, **kwargs)

        self.now_btn = self.find_clickable_element(self._now_button_xpath)
        self.evening_btn = self.find_clickable_element(self._evening_button_xpath)
        self.filter_btn = self.find_clickable_element(self._filter_button_xpath)
        self.cancel_btn = self.find_clickable_element(self._cancel_button_xpath)

    def select_next_day(self):
        next_day = self._daypicker_xpath.format(self.get_next_day_date_format())
        self.find_visible_element(next_day).click()
        self.filter_btn.click()

    def select_current_day(self):
        current_day = self._daypicker_xpath.format(self.get_current_date_format())
        self.find_visible_element(current_day).click()
        self.filter_btn.click()

    def select_evening(self):
        self.evening_btn.click()
        self.filter_btn.click()


class ChannelFilter(BasePage):

    """ This is a channel filter, displayed on TvGuide page and channel page"""

    # Channel grouping letter
    _channel_letter_xpath = "//h3[@class='ChannelPicker__channelLetter___3WGqn']"

    # Channel name
    _channel_name_xpath = "//button[@class='ChannelPicker__channel___2_Y1N']"

    def __init__(self, webdriver, *args, **kwargs):
        super(ChannelFilter, self).__init__(webdriver, *args, **kwargs)

        self.groups_list = self.find_list_of_elements(self._channel_letter_xpath)
        self.channels_list = self.find_list_of_elements(self._channel_name_xpath)

    def get_channels_names(self):
        channels_names_list = []
        for i in range(len(self.channels_list)):
            channels_names_list.append(
                self.get_element_from_list(self._channel_name_xpath, i))

        return channels_names_list

    def get_channel_name(self, n=0):
        return self.get_element_from_list(self._channel_name_xpath, n)

    def select_channel(self, n=0):
        self.channels_list[n].click()


class Footer(BasePage):
    """This ia a webpage footer."""

    # Insys logo that links to insysgo webpage
    _insys_logo_xpath = "//a[@class='Footer__logo___11qYZ']"

    # Contact page link
    _contact_xpath = "//div[@class='Footer__contact___3IZDh']/a"

    # Privacy policy link
    _privacy_policy_xpath = "//a[@href='/page/polityka-prywatnosci']"

    # Terms of service link
    _terms_of_service_xpath = "//a[@href='/page/regulamin']"

    # FAQ/help page link
    _faq_xpath = "//a[@href='/faq']"

    def __init__(self, webdriver, *args, **kwargs):
        super(Footer, self).__init__(webdriver, *args, **kwargs)

        self.insys_logo = self.find_clickable_element(self._insys_logo_xpath)
        self.contact_link = self.find_clickable_element(self._contact_xpath)
        self.privacy_policy_link = self.find_clickable_element(self._privacy_policy_xpath)
        self.terms_of_service_link = self.find_clickable_element(self._terms_of_service_xpath)
        self.faq_link = self.find_clickable_element(self._faq_xpath)

