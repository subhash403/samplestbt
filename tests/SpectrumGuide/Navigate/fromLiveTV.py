from time import sleep

from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import GuideScreen


def to_main_menu(step_name, tester):
    """ Returns true or false based on navigation from LiveTv into Main Menu Screen """
    tester.remote_control_press("KEY_MENU")
    if tester.check_image(MainMenuScreen.Spectrum_Logo["image"]):
        tester.LogResults.passed("{} : Navigate to Main Menu from Live TV".format(step_name))
        tester.LogResults.info("Expected - Main Menu is Displayed, Actual- Displayed")
        return True
    else:
        tester.LogResults.failed("{} : Navigating to Main Menu from Live TV".format(step_name))
        tester.LogResults.info("Expected - Main Menu is Displayed, Actual- Not Displayed")
        return False


def to_guide(step_name, tester):
    """ Returns true or false based on navigation from LiveTV into Guide Screen """
    tester.remote_control_press("KEY_GUIDE")
    # wait for 3 seconds for guide screen to launch
    sleep(3)
    if tester.check_image(GuideScreen.guide_options["image"]):
        tester.LogResults.passed("{} : Navigating to Guide from Live TV".format(step_name))
        tester.LogResults.info("Expected - Guide <guide-options> should be displayed, Actual - Displayed")
        return True
    else:
        tester.LogResults.failed("{} : Navigating to Guide from Live TV".format(step_name))
        tester.LogResults.info("Expected - Guide <guide-options> should be displayed, Actual - Not Displayed")
        return False
