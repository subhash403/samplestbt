from time import sleep

from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import GuideScreen
from tests.SpectrumGuide.ObjectRepo import LiveTV


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


def pause_for_num_seconds(step_name, tester, num_seconds):
    tester.remote_control_press('KEY_PLAYPAUSE')
    if tester.check_image(LiveTV.pause["image"]):
        tester.LogResults.info("Expected - Live TV should be paused, Actual - Live TV is paused")
    else:
        return False
    sleep(num_seconds)
    if tester.check_image(LiveTV.pause["image"]):
        tester.LogResults.passed("{} : Live TV was successfully paused for {} seconds".format(step_name, num_seconds))
        tester.LogResults.info("Expected - Live TV stays paused for {} seconds, "
                               "Actual - Live TV stayed paused for {} seconds".format(num_seconds, num_seconds))
        return True
    else:
        tester.LogResults.failed("{} : Pausing Live TV for {} seconds".format(step_name, num_seconds))
        tester.LogResults.info("Expected - Live TV stays paused for {} seconds, "
                               "Actual - Live TV did not stay paused for {} seconds".format(num_seconds, num_seconds))
        return False

def cycle_trickplay_from_pause(step_name, tester, num_times):
    if tester.check_image(LiveTV.pause["image"]):
        tester.LogResults.info("Expected - Live TV should be paused, Actual - Live TV is paused")
    else:
        return False
    for _ in range(num_times):
        tester.remote_control_press('KEY_PLAYPAUSE')
        if tester.check_image(LiveTV.play["image"]):
            tester.LogResults.info("Expected - Live TV should be played, Actual - Live TV is played")
        else:
            tester.LogResults.failed("{} : Expected - Live TV should be played,"
                                     " Actual - Live TV is not played".format(step_name))
            return False
        tester.remote_control_press('KEY_LEFT')
        if tester.check_image(LiveTV.rewind["image"]):
            tester.LogResults.info("Expected - Live TV should be rewound, Actual - Live TV is rewound")
        else:
            tester.LogResults.failed("{} : Expected - Live TV should be rewound, "
                                     "Actual - Live TV is not rewound".format(step_name))
            return False
        tester.remote_control_press('KEY_RIGHT')
        if tester.check_image(LiveTV.fastforward["image"]):
            tester.LogResults.info("Expected - Live TV should be forwarded, Actual - Live TV is forwarded")
        else:
            tester.LogResults.failed("{} : Expected - Live TV should be forwarded, "
                                     "Actual - Live TV is not forwarded".format(step_name))
            return False
        tester.remote_control_press('KEY_PLAYPAUSE')
        if tester.check_image(LiveTV.play["image"]):
            tester.LogResults.info("Expected - Live TV should be resumed, Actual - Live TV is resumed")
        else:
            tester.LogResults.failed("{} : Expected - Live TV should be resumed, "
                                     "Actual - Live TV is not resumed".format(step_name))
            return False
        tester.remote_control_press('KEY_PLAYPAUSE')
        if tester.check_image(LiveTV.pause["image"]):
            tester.LogResults.info("Expected - Live TV should be paused, Actual - Live TV is paused")
        else:
            tester.LogResults.failed("{} : Expected - Live TV should be paused, "
                                     "Actual - Live TV is not paused".format(step_name))
            return False
    return True