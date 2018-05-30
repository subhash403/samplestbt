from tests.SpectrumGuide.ObjectRepo import SettingsAndSupportScreen


def to_preference(step_name, tester):
    if tester.remote_control_press_until_image_match('KEY_DOWN', SettingsAndSupportScreen.preference["selected"],
                                                     SettingsAndSupportScreen.area["region"], maximum_key_press=5):
        tester.LogResults.passed("{} : Navigating to Preferences options in  Settings & Support".format(step_name))
    else:
        tester.LogResults.failed("{} : Navigating to Preferences options in  Settings & Support".format(step_name))
        return False
    tester.remote_control_press('KEY_ENTER', 0)
    if tester.check_image(SettingsAndSupportScreen.preference["launched"]):
        tester.LogResults.passed("Expected - Preferences is Displayed, Actual- Displayed")
        return True
    else:
        tester.LogResults.failed("Expected - Preferences is Displayed, Actual- Not Displayed")
        return False
