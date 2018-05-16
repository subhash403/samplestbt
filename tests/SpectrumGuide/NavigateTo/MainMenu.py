from tests.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import TvShowsScreen
from tests.SpectrumGuide.ObjectRepo import MyLibraryScreen


def to_tv_shows():
    Tester.LogResults.info("Navigating to TV Shows from Main Menu")
    Tester.remote_control_press('KEY_CHANNELUP')
    Tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.tv_shows["image"], 7)
    Tester.remote_control_press('KEY_ENTER')
    if Tester.check_image(TvShowsScreen.logo["image"])
        Tester.LogResults.passed("Expected - TV Shows is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - TV Shows is Displayed, Actual- Not Displayed")
        return False


def to_my_library():
    Tester.LogResults.info("Navigating to My Library from Main Menu")
    Tester.remote_control_press('KEY_CHANNELUP')
    Tester.remote_control_press_until_image_match('KEY_DOWN', MainMenuScreen.my_library["image"], 7)
    Tester.remote_control_press('KEY_ENTER')
    if Tester.check_image(MyLibraryScreen.logo["image"]) and not Tester.check_image(MainMenuScreen.Spectrum_Logo["image"])
        Tester.LogResults.passed("Expected - My Library is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - My Library is Displayed, Actual- Not Displayed")
        return False