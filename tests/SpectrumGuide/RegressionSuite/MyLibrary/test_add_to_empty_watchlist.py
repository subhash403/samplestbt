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
from tests.SpectrumGuide.Navigate import fromMainMenu


def test_add_to_empty_watchlist():
    # Initialize test
    user = UserWrapper()
    user.start()
    test_id = "TCxyz"
    test_name = "test_add_to_empty_watchlist"
    user.LogResults.info("Test ID : {}, Test Name :{}".format(test_id, test_name))
    assertion_flag = True

    # We can also check if there are any action panels and see if we can get out it to a Live channel, for now we will
    # exit the test.
    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, number_of_exit_key=2,wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return

    # Step 2 : Hide Adult OFF and Empty Watchlist (use API?)

    # Step 3 : Get to TV Shows
    if not fromLiveTV.to_main_menu("Step 3", user):
        user.clean_up(test_id, test_name)
        return

    if not fromMainMenu.to_tv_shows("Step 3", user):
        user.clean_up((test_id, test_name))
        return



    # Clean up User Wrapper
    user.clean_up(assertion_flag, test_name)
