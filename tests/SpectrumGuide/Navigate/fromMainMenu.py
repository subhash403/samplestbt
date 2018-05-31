from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import TvShowsScreen
from tests.SpectrumGuide.ObjectRepo import MyLibraryScreen
from tests.SpectrumGuide.ObjectRepo import SettingsAndSupportScreen
from time import sleep


def to_tv_shows(step_name, tester):
    """
    :author: Beau Yoder
    :description: Navigates to and launches TV Shows when Main Menu is already open
    :param step_name:
    :param tester:
    :return:
    """
    tester.remote_control_press('KEY_CHANNELUP')
    if tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.tv_shows["image"], 7, menu_region):
        tester.LogResults.passed("{} : Navigating to TV Shows in Main Menu".format(step_name))
    else:
        tester.LogResults.failed("{} : Navigating to TV Shows in Main Menu".format(step_name))
        return False
    tester.remote_control_press('KEY_ENTER')
    if tester.check_image(TvShowsScreen.logo["image"]):
        tester.LogResults.passed("Expected - TV Shows is Displayed, Actual- Displayed")
        return True
    else:
        tester.LogResults.failed("Expected - TV Shows is Displayed, Actual- Not Displayed")
        return False


def to_my_library(step_name, tester):
    """
    :author: Beau Yoder
    :description: Navigates to and launches My Library when Main Menu is already open
    :param step_name:
    :param tester:
    :return:
    """
    tester.remote_control_press('KEY_CHANNELUP')
    sleep(1)
    if tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.my_library["image"], 7,
                                                     MainMenuScreen.area["region"]):
        tester.LogResults.info("Expected - navigate to my library option, Actual- Displayed")
        tester.LogResults.passed("{} : Navigating to My Library in Main Menu".format(step_name))
    else:
        tester.LogResults.info("Expected - navigate to my library option, Actual- not displayed")
        tester.LogResults.failed("{} : Navigating to My Library in Main Menu".format(step_name))
        return False
    tester.remote_control_press('KEY_ENTER')
    sleep(1)
    if tester.check_image(MyLibraryScreen.logo["image"]) and not \
            tester.check_image(MainMenuScreen.Spectrum_Logo["image"]):
        tester.LogResults.info("Expected - My Library is Displayed, Actual- Displayed")
        tester.LogResults.passed("{} : Reached My Library page".format(step_name))
        return True
    else:
        tester.LogResults.info("Expected - My Library is Displayed, Actual- Not Displayed")
        tester.LogResults.failed("{} : Did not reach My Library page".format(step_name))
        return False


def to_settings(step_name, tester):
    """
    :author: Beau Yoder
    :description: Navigates to and launches Settings when Main Menu is already open
    :param step_name:
    :param tester:
    :return:
    """
    tester.remote_control_press('KEY_CHANNELUP')
    if tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.Settings["image"],
                                                     MainMenuScreen.area["region"], maximum_key_press=7):
        tester.LogResults.passed("{} : Navigating to Settings options in  Main Menu".format(step_name))
    else:
        tester.LogResults.failed("{} : Navigating to TV Settings from Main Menu".format(step_name))
        return False
    tester.remote_control_press('KEY_ENTER', 0)
    if tester.check_image(SettingsAndSupportScreen.logo["image"]):
        tester.LogResults.passed("Expected - Settings & Support is Displayed, Actual- Displayed")
        return True
    else:
        tester.LogResults.failed("Expected - Settings & Support is Displayed, Actual- Not Displayed")
        return False
