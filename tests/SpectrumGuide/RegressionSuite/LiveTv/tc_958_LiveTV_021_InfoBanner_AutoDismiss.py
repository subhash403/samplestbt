import os
import sys
from time import sleep


# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d


sys.path.insert(0, _get_test_pack_root())
from tests.astro.Sampler import UserWrapper
from tests.SpectrumGuide.Navigate import fromAnyScreen
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.Navigate import fromSettings
from tests.SpectrumGuide.Navigate import frompreferences
from tests.SpectrumGuide.Navigate import fromMainMenu
from tests.SpectrumGuide.ObjectRepo import preferencesscreen

"""
======================================================================================================================
Function Test Coverage :  LiveTV_021_InfoBanner_AutoDismiss
Author      : Subhash Boddu
Description : Test to validate the Display Duration (Autodismiss) of Info Banner 
Reviewed By :  
======================================================================================================================
"""

def test_tc_958_LiveTV_021_InfoBanner_AutoDismiss():
    # Initialize test
    test_id = "tc958"
    test_name = "tc_958_LiveTV_021_InfoBanner_AutoDismiss"
    user = UserWrapper(test_name)
    user.start()
    user.LogResults.info("Test ID : {}, Test Name :{}".format(test_id, test_name))
    assertion_flag = True

    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return

    if not fromMainMenu.to_menu("step 2", user):
        assertion_flag = False

    if not fromMainMenu.to_settings("step 3", user):
        assertion_flag = False

    if not fromSettings.to_preference("Step 4", user):
        assertion_flag = False

    if not frompreferences.to_guide_settings("step 5", user):
        assertion_flag = False

    if not frompreferences.to_display_duration("step 6", user):
        assertion_flag = False

    if not frompreferences.info_banner("step 7",user):
        assertion_flag = False

    # Clean up User Wrapper
    user.clean_up(assertion_flag)
