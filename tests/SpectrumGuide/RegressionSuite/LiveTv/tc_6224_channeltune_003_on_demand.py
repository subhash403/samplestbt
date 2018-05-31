import os
import sys
from time import sleep
#Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d
sys.path.insert(0, _get_test_pack_root())

from tests.SpectrumGuide.ObjectRepo import TvShowsScreen
from tests.SpectrumGuide.ObjectRepo import GuideScreen
from tests.astro.Sampler import UserWrapper
from tests.SpectrumGuide.Navigate import fromLiveTV
from tests.SpectrumGuide.Navigate import fromAnyScreen
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import MiniGuideScreen

"""
======================================================================================================================
Function Test Coverage : ChannelTune_003_On_Demand
Author      : Subhash Boddu
Description : Test to Launch Ondemand channel from Live Tv & MiniGuide & CloudGuide  
Reviewed By :  
======================================================================================================================
"""


def test_tc_6224_channel_tune_003_on_demand():
    # Initialize test
    test_id = "tc6224"
    test_name = "tc_6224_ChannelTune_003_On Demand"
    user = UserWrapper()
    user.start()
    user.LogResults.info("Test ID : {}, Test Name :{}".format(test_id, test_name))
    assertion_flag = True

    def ondemand_to_tv_shows(step_name, Tester):
        if Tester.remote_control_press_until_image_match('KEY_ONDEMAND', TvShowsScreen.logo["image"]):
            Tester.LogResults.passed("Expected - TV Shows is Displayed, Actual- Displayed")
            return True
        else:
            Tester.LogResults.failed("Expected - TV Shows is Displayed, Actual- Not Displayed")
            return False

    def miniguidelaunch(step_name, Tester):
        if Tester.remote_control_press_until_image_match('KEY_ENTER', MiniGuideScreen.logo["image"], maximum_key_press=2):
            Tester.LogResults.passed("Expected - MiniGuide is Displayed, Actual- Displayed")
            return True
        else:
            Tester.LogResults.failed("Expected - MiniGuide is Displayed, Actual- Not Displayed")
            return False

    def checkchannelnumberinminiguide(key,number_of_times,channelnumber):
        user.remote_control_press(key,number_of_times)
        sleep(5)
        if user.check_image(MiniGuideScreen.miniguide_ondemand["image"]):
            user.LogResults.passed("Expected - MiniGuide 999 is Displayed, Actual- Displayed")
            return True
        else:
            user.LogResults.failed("Expected - MiniGuide 999 is Displayed, Actual- Not Displayed")
            assertion_flag = False
            user.clean_up(test_id, test_name)
            return False

    def Guidelaunch(step_name, Tester):
        if Tester.remote_control_press_until_image_match('KEY_Guide', GuideScreen.guide_options["image"],region=None, maximum_key_press=1):
            Tester.LogResults.passed("Expected - Guide is Displayed, Actual- Displayed")
            return True
        else:
            Tester.LogResults.failed("Expected - Guide is Displayed, Actual- Not Displayed")
            assertion_flag = False
            return False
#Step-1
#Launch the ondemand channel using Ondemand key
# User should be in Live Tv Initally while starting the Test case
    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return

    if not ondemand_to_tv_shows("Step 2", user):
        assertion_flag = False
#Step-2
#Launch the ondemand channel from Guide 
    
    if not fromAnyScreen.exit_to_live_tv_screen("Step 2", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return

    if not fromLiveTV.to_guide("Step 4", user):
        # call any other teardown if necessary
        assertion_flag = False

#if we press 999 from the guide it directly launches the Tvshows page'''
    user.remote_control_press('KEY_9', 2)
    sleep(10)
    if user.check_image(TvShowsScreen.logo["image"]):
        user.LogResults.passed("Expected - TV Shows is Displayed, Actual- Displayed")
    else:
        user.LogResults.failed("Expected - TV Shows is Displayed, Actual- Not Displayed")
            
#Step-3
#Launch the ondemand channel from Miniguide 
    if not fromAnyScreen.exit_to_live_tv_screen("Step 3", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return
    
    if not miniguidelaunch("Step 4", user):
        assertion_flag = False

    if not checkchannelnumberinminiguide('KEY_9',number_of_times=2,channelnumber=999):
        assertion_flag = False

#if 999 channel we got in miniguide then we need to select that to launch the ondemand channel
    user.remote_control_press('KEY_ENTER')
    sleep(10)
    if user.check_image(TvShowsScreen.logo["image"]):
        user.LogResults.passed("Expected - TV Shows is Displayed, Actual- Displayed")
        return True
    else:
        user.LogResults.failed("Expected - TV Shows is Displayed, Actual- Not Displayed")
        assertion_flag = False
    user.clean_up(assertion_flag, test_name)


