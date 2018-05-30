
from tests.SpectrumGuide.ObjectRepo import preferencesscreen

def to_guide_settings(step_name,Tester):
    if Tester.remote_control_press_until_image_match('KEY_RIGHT', preferencesscreen.guide_Settings["image"],region=None,maximum_key_press=4) :
        Tester.LogResults.passed("{} : Navigating to Guide_settings in  Preferences".format(step_name))
    else:
        Tester.LogResults.failed("{} : Navigating to Guide settings from preferences ".format(step_name))
        return False
    Tester.remote_control_press('KEY_ENTER')
    if Tester.check_image(preferencesscreen.guidesettings_launched["image"]):
        Tester.LogResults.passed("Expected - guidesettings is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - Guide Setitngs  is Displayed, Actual- Not Displayed")
        return False