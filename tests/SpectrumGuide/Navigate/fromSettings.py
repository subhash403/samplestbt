from tests.SpectrumGuide.ObjectRepo import SettingsandsupportScreen

def to_preference(step_name,Tester):
    if Tester.remote_control_press_until_image_match('KEY_DOWN', SettingsandsupportScreen.preferences["selected"], menu_region,maximum_key_press=5):
        Tester.LogResults.passed("{} : Navigating to Preferences options in  Settings & Support".format(step_name))
    else:
        Tester.LogResults.failed("{} : Navigating to Preferences options in  Settings & Support".format(step_name))
        return False
    Tester.remote_control_press('KEY_ENTER')
    if Tester.check_image(SettingsandsupportScreen.preferences["launched"]):
        Tester.LogResults.passed("Expected - Preferences is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - Preferences is Displayed, Actual- Not Displayed")
        return False