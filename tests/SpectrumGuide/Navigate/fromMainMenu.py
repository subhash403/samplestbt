from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import TvShowsScreen
from tests.SpectrumGuide.ObjectRepo import MyLibraryScreen
from time import sleep

menu_region = MainMenuScreen.area["region"]


def to_menu(step_name, Tester):
    Tester.remote_control_press('KEY_MENU')
    if Tester.check_image(MainMenuScreen.Spectrum_Logo["image"]):
        Tester.LogResults.passed("Expected - MENU is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - MENU is Displayed, Actual- Not Displayed")
        return False

def to_tv_shows(step_name,Tester):
    Tester.remote_control_press('KEY_CHANNELUP')
    if Tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.tv_shows["image"], 7, menu_region) :
        Tester.LogResults.passed("{} : Navigating to TV Shows options in  Main Menu".format(step_name))
    else:
        Tester.LogResults.failed("{} : Navigating to TV Shows from Main Menu".format(step_name))
        return False
    Tester.remote_control_press('KEY_ENTER')
    if Tester.check_image(TvShowsScreen.logo["image"]):
        Tester.LogResults.passed("Expected - TV Shows is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - TV Shows is Displayed, Actual- Not Displayed")
        return False


def to_my_library(step_name,Tester):
    Tester.LogResults.info("Navigating to My Library from Main Menu")
    Tester.remote_control_press('KEY_CHANNELUP')
    sleep(1)
    if Tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.my_library["image"], 7, menu_region):
        Tester.LogResults.passed("Expected - navigate to my library option, Actual- Displayed")
    else:
        Tester.LogResults.passed("Expected - navigate to my library option, Actual- not displayed")
        return False
    Tester.remote_control_press('KEY_ENTER')
    sleep(1)
    if Tester.check_image(MyLibraryScreen.logo["image"]) and not Tester.check_image(MainMenuScreen.Spectrum_Logo["image"]):
        Tester.LogResults.passed("Expected - My Library is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - My Library is Displayed, Actual- Not Displayed")
        return False

def to_settings(step_name, Tester):
    Tester.remote_control_press('KEY_CHANNELUP')
    if Tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.Settings["selected"], 7, menu_region):
        Tester.LogResults.passed("{} : Navigating to Settings options in  Main Menu".format(step_name))
    else:
        Tester.LogResults.failed("{} : Navigating to TV Settings from Main Menu".format(step_name))
        return False
    Tester.remote_control_press('KEY_ENTER')
    if Tester.check_image(SettingsandsupportScreen.logo["image"]):
        Tester.LogResults.passed("Expected - Settings&Support is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - Settings&Support is Displayed, Actual- Not Displayed")
        return False

