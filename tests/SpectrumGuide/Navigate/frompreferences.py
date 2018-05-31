
from tests.SpectrumGuide.ObjectRepo import preferencesscreen

def to_guide_settings(step_name,Tester):
    if Tester.remote_control_press_until_image_match('KEY_RIGHT', preferencesscreen.guide_Settings["image"],region=None,maximum_key_press=4) :
        Tester.LogResults.passed("{} : Navigating to Guide_settings in  Preferences".format(step_name))
    else:
        Tester.LogResults.failed("{} : Navigating to Guide settings from preferences ".format(step_name))
        return False
    Tester.remote_control_press('KEY_ENTER',0)
    if Tester.check_image(preferencesscreen.guidesettings_launched["image"]):
        Tester.LogResults.passed("Expected - guidesettings is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - Guide Setitngs  is Displayed, Actual- Not Displayed")
        return False

def to_display_duration(step_name, Tester):
    if Tester.check_image(preferencesscreen.guidesettings_launched["image"]):
        Tester.remote_control_press('KEY_DOWN')
        if Tester.check_image(preferencesscreen.display_duration["image"]):
            Tester.remote_control_press('KEY_RIGHT', 0)
        else:
            Tester.LogResults.failed("{} : Navigating to Display_Duration from Guide Settings".format(step_name))
            return False
        Tester.remote_control_press('KEY_ENTER', 0)
        if Tester.check_image(preferencesscreen.displayduration_launched["image"]):
            Tester.LogResults.passed("Expected - displayDuration is Displayed, Actual- Displayed")
            return True
        else:
            Tester.LogResults.failed("Expected - Display Duration is Displayed, Actual- Not Displayed")
            return False

def info_banner(step_name, Tester):
    preferences_region= preferencesscreen.area["region"]
    #Tester.remote_control_press('KEY_DOWN', 0)
    Tester.remote_control_press_until_image_match('KEY_DOWN', preferencesscreen.infobanner["image"], maximum_key_press=1,region=preferences_region)
    Tester.remote_control_press('KEY_ENTER', 0)
    Tester.get_text(preferencesscreen.info_banner_time["region"])