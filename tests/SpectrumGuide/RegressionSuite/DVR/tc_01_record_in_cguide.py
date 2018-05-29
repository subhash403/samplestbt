
import os
import sys

# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d

sys.path.insert(0, _get_test_pack_root())

from tests.astro.Sampler import UserWrapper
from tests.SpectrumGuide.Navigate import fromLiveTV
from tests.SpectrumGuide.Navigate import fromAnyScreen
from tests.SpectrumGuide.Navigate import fromCloudGuide

"""
======================================================================================================================
Function Test Coverage : <ALM_Functional_Test_Name> 
Author      : Beau Yoder    
Description : In Cloud Guide, Check if 
Reviewed By : 
======================================================================================================================
"""


def test_01_record_in_cguide():
    # Initialize test
    test_name = "01_record_in_guide"
    user = UserWrapper(test_name)
    user.start()
    user.LogResults.info("Test Name :{}".format(test_name))
    assertion_flag = True

    # We can also check if there are any action panels and see if we can get out it to a Live channel, for now we will
    # exit the test.
    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, number_of_exit_key=2,wait_after_key_press_secs=5):
        user.clean_up(False)
        return

    if not fromLiveTV.to_guide("Step 2", user):
        # call any other teardown if necessary
        # <TODO> Check If cloud guide is available.
        user.clean_up(False)
        return

    # Event start a recording using record button
    if not fromCloudGuide.record_in_program_cell("Step 3", user):
        assertion_flag = False

    # Check if Record panel is displayed
    if not fromCloudGuide.error_check_for_record("Step 4", user):
        assertion_flag = False

    # Clean up User Wrapper
    user.clean_up(assertion_flag)
