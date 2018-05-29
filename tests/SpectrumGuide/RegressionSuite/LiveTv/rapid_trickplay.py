
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
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from time import sleep

"""
======================================================================================================================
Function Test Coverage : <ALM_Functional_Test_Name>
Author      : Beau Yoder 
Description : Test pressing many trickplay functions in rapid succession on Live TV, after 60 sec pause.
Reviewed By : --- TBD ---
======================================================================================================================
"""


def test_many_trickplay_presses_on_tsb():
    test_name = "rapid_trickplay_presses_on_paused_live_tv"
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

    # Step 2 : Pause Live for 60 seconds
    if not fromLiveTV.pause_for_num_seconds("Step 2", user, 60):
        assertion_flag = False

    # Step 3 : Perform a number of iterations of trickplay functions
    if not fromLiveTV.cycle_trickplay_from_pause("Step 3", user, 5):
        assertion_flag = False

    # Clean up User Wrapper
    user.clean_up(assertion_flag)


def test_time_to_get_text():
    test_name = "checking_get_text_time"
    user = UserWrapper(test_name)
    user.start()
    user.LogResults.info("Test Name :{}".format(test_name))
    #assertion_flag = True
    fromAnyScreen.exit_to_live_tv_screen("Step 0", user, number_of_exit_key=1)
    fromLiveTV.to_main_menu("Step 1", user)
    sleep(5)
    my_text = user.get_text(MainMenuScreen.Spectrum_Logo["region"])
    print my_text
