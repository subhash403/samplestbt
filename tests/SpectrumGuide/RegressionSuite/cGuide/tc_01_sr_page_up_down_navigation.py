
import os
import sys

# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d

sys.path.insert(0,_get_test_pack_root())

from tests.astro.Sampler import UserWrapper
from tests.SpectrumGuide.Navigate import fromLiveTV
from tests.SpectrumGuide.Navigate import fromAnyScreen
from tests.SpectrumGuide.Navigate import fromCloudGuide


"""
======================================================================================================================
Function Test Coverage : <ALM_Functional_Test_Name>
Author      : Beau Yoder 
Description : Test to check page up and pae down functions of a silver remote in cloud guide screen.
Reviewed By : SivaRam Kumar Mani
======================================================================================================================
"""


def test_01_sr_page_up_down_navigation():
    # Initialize test
    test_name = "01_sr_page_up_down_navigation"
    user = UserWrapper(test_name)
    user.start()
    user.LogResults.info("Test Name :{}".format(test_name))
    assertion_flag = True

    # Pre-Requisites
    # Check if STB is ON <TODO>

    # Step 1 : Check if STB is in live TB
    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(assertion_flag)
        return

    # Step 2 : Navigate to guide screen from Live TV
    if not fromLiveTV.to_guide("Step 2", user):
        # call any other teardown if necessary
        assertion_flag = False
        user.clean_up(assertion_flag)
        return

    # Event if this step fails proceed to check if Page down works.
    fromCloudGuide.check_page_down_channel_scrolling("Step 3", user)

    # Event if this step fails proceed to check if Page up works.
    fromCloudGuide.check_page_up_channel_scrolling("Step 4", user)

    # Verify "RIGHT KEY" action to select future program
    if not fromCloudGuide.select_future_program_using_right_arrow("Step 5", user):
        # call any other teardown if necessary
        assertion_flag = False
        # clean up user object
        user.clean_up(assertion_flag)
        return

    # Event if this step fails proceed to check if Page down works.
    if not fromCloudGuide.check_page_down_channel_scrolling("Step 6", user):
        assertion_flag = False

    # Event if this step fails proceed to check if Page up works.
    if not fromCloudGuide.check_page_up_channel_scrolling("Step 7", user):
        assertion_flag = False

    # Check page up/down from center of guide, no return value
    if not fromCloudGuide.move_in_guide_using_down_arrow("Step 8",user, number_of_times_to_move_down=3):
        assertion_flag = False

    # Event if this step fails proceed to check if Page down works.
    if not fromCloudGuide.check_page_down_channel_scrolling("Step 9", user):
        assertion_flag = False

    # Event if this step fails proceed to check if Page up works.
    if not fromCloudGuide.check_page_up_channel_scrolling("Step 10", user):
        assertion_flag = False

    # Clean up User Wrapper
    user.clean_up(assertion_flag)
