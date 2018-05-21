
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

from tests.SpectrumGuide.Navigate import fromLiveTV
from tests.SpectrumGuide.Navigate import fromAnyScreen
from tests.SpectrumGuide.Navigate import fromCloudGuide


def test_record_in_guide():
    # Initialize test
    user = UserWrapper()
    user.start()
    test_id = "TCxyz"
    test_name = "test_record_in_guide"
    user.LogResults.info("Test ID : {}, Test Name :{}".format(test_id, test_name))
    assertion_flag = True

    # We can also check if there are any action panels and see if we can get out it to a Live channel, for now we will
    # exit the test.
    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, number_of_exit_key=2,wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return

    if not fromLiveTV.to_guide("Step 2 - 3", user):
        # call any other teardown if necessary
        user.clean_up(test_id, test_name)
        return

    # Event if this step fails proceed to check if Page down works.
    if not fromCloudGuide.record_in_program_cell("Step 4", user):
        assertion_flag = False

    # Event if this step fails proceed to check if Page up works.
    if not fromCloudGuide.error_check_for_record("Step 5", user):
        assertion_flag = False

    # Clean up User Wrapper
    user.clean_up(assertion_flag, test_name)
