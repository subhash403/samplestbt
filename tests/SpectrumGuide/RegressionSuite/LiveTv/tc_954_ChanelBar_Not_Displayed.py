import os
import sys


# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d
sys.path.insert(0, _get_test_pack_root())

from time import sleep
import stbt
from tests.astro.Sampler import UserWrapper
from tests.SpectrumGuide.Navigate import fromLiveTV
from tests.SpectrumGuide.Navigate import fromAnyScreen
from tests.SpectrumGuide.ObjectRepo import MyDVRScreen
from tests.SpectrumGuide.ObjectRepo import LiveTV
from tests.SpectrumGuide.MicroService import make_api_call
from tests.SpectrumGuide.Navigate import fromMainMenu
"""
======================================================================================================================
Function Test Coverage : <ALM_Functional_Test_Name>
Author      : Kavitha.Pasupuleti
Description : To check whether the Channel Banner is not displayed
Reviewed By :
======================================================================================================================
"""

def test_tc_954_ChanelBar_Not_Displayed():
    # Initialize test
    test_name = "ChanelBar_Not_Displayed"
    user = UserWrapper( test_name)
    user.start()
    user.LogResults.info("Test Name :{}".format( test_name))
    assertion_flag = True
    # Pre-Requisites
    # Check if STB is ON <TODO>
    #method to navigate from live tv to mydvr
    def LiveTV_to_MyDVR(step_name, user):
        """ Returns true or false based on navigation from LiveTV in to my DVR Screen """
        user.remote_control_press('KEY_MYDVR',0)
        # wait for 3 seconds for mydvr screen to launch
        sleep(3)
        if user.check_image(MyDVRScreen.MyDVR_logo["image"]):
            user.LogResults.passed("{} : Navigating to MyDVR from Live TV".format(step_name))
            user.LogResults.info("Expected - MyDVR <MyDVR logo> should be displayed, Actual - Displayed")
            return True
        else:
            user.LogResults.failed("{} : Navigating to MyDVR from Live TV".format(step_name))
            user.LogResults.info("Expected - MyDVR <MyDVR logo> should be displayed, Actual - Not Displayed")
            return False

        ##method to navigate from live tv to tvshows using on demand method
    def LiveTV_to_Tvshows(step_name, user):
        """Returns true or false based on navigation from liveTV into Tvshows"""
        user.remote_control_press('KEY_ONDEMAND',0)
        # wait for 3 seconds for tvshows page
        sleep(3)
        if user.check_image(TvShowsScreen.Tv_Shows_Logo["image"]):
            user.LogResults.passed("{} : Navigating to tvshows from Live TV".format(step_name))
            user.LogResults.info("Expected - TvShows <Tv_Shows_Logo> should be displayed, Actual - Displayed")
            return True
        else:
            user.LogResults.failed("{} : Navigating to tvshows from Live TV".format(step_name))
            user.LogResults.info("Expected - TvShows <Tv_Shows_Logo> should be displayed, Actual - Not Displayed")
            return False
    make_api_call.parental_pin(off)
    ######Verify mydvr box is dvr box or not
    if not LiveTV_to_MyDVR("Step2", user):
        assertion_flag = False

    ######Check if STB is in live TB and verify if channel bar is displayed on live tv
    if not fromAnyScreen.exit_to_live_tv_screen("Step 3", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(assertion_flag)
        return
    user.remote_control_press('KEY_ENTER',0)
    if not user.check_image(LiveTV.ChannelBar_validation["image"]):
        assertion_flag = False

  #########Step 3: Press "Guide",Guide Screen should be displayed without displaying the channel bar
    if not fromLiveTV.to_guide("Step 4", user):
        assertion_flag = False
  ######Navigate to LIVE TV
    if not fromAnyScreen.exit_to_live_tv_screen("Step 3", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(assertion_flag)
        return
    user.remote_control_press('KEY_ENTER',0)
    if not user.check_image(LiveTV.ChannelBar_validation["image"]):
        assertion_flag = False

###########Step 4: Press "MYDVR",DVRScreen should be displayed without displaying the channel bar.
    if not LiveTV_to_MyDVR("Step6", user):
        assertion_flag = False
        ######Navigate to LIVE TV
        if not fromAnyScreen.exit_to_live_tv_screen("Step 3", user, number_of_exit_key=2, wait_after_key_press_secs=5):
            user.clean_up(assertion_flag)
            return
        user.remote_control_press('KEY_ENTER', 0)
        if not user.check_image(LiveTV.ChannelBar_validation["image"]):
            assertion_flag = False

    ## Step 5: Press "MENU",menu Screen should be displayed without displaying the channel bar.
    if not fromMainMenu.to_menu("Step5",user):
        assertion_flag = False
        ######Navigate to LIVE TV
        if not fromAnyScreen.exit_to_live_tv_screen("Step 3", user, number_of_exit_key=2, wait_after_key_press_secs=5):
            user.clean_up(assertion_flag)
            return
        user.remote_control_press('KEY_ENTER', 0)
        if not user.check_image(LiveTV.ChannelBar_validation["image"]):
            assertion_flag = False

    # Step 6: Press "on demand",on demand Screen should be displayed without displaying the channel bar.
    if not LiveTV_to_Tvshows("Step8", user):
        assertion_flag = False
        ######Navigate to LIVE TV
        if not fromAnyScreen.exit_to_live_tv_screen("Step 3", user, number_of_exit_key=2, wait_after_key_press_secs=5):
            user.clean_up(assertion_flag)
            return
        user.remote_control_press('KEY_ENTER', 0)
        if not user.check_image(LiveTV.ChannelBar_validation["image"]):
            assertion_flag = False

    ########## Press "POWER",System should be turned 'OFF' without displaying the channel bar
    user.remote_control_press('KEY_POWER',0)
    if not stbt.is_screen_black:
        user.clean_up(test_id, test_name)
        return
    user.remote_control_press('KEY_POWER', 0)
    sleep(3)


# Clean up User Wrapper
    user.clean_up(assertion_flag, test_name)
