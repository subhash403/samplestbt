import os
import sys
from time import sleep
from tests.SpectrumGuide.ObjectRepo import TvShowsScreen
from tests.SpectrumGuide.ObjectRepo import GuideScreen
from tests.astro.Sampler import UserWrapper
from tests.SpectrumGuide.Navigate import fromLiveTV
from tests.SpectrumGuide.Navigate import fromMainMenuScreen
from tests.SpectrumGuide.Navigate import fromminiguidescreen


# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d


sys.path.insert(0, _get_test_pack_root())


def LiveTV_014_ChannelBarPosition():
    # Initialize test
    user = UserWrapper()
    user.start()
    test_id = "TC6224"
    test_name = "ChannelTune_003_On Demand"
    user.LogResults.info("Test ID : {}, Test Name :{}".format(test_id, test_name))
    assertion_flag = True

    # User should be in Live Tv Initally while starting the Test case
    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return

    user.remote_control_press('KEY_ONDEMAND')

    if not fromMainMenuScreen.to_tvshows("Step 1", user):
        user.clean_up(test_id, test_name)
        return

    if not fromAnyScreen.exit_to_live_tv_screen("Step 2", user, number_of_exit_key=2, wait_after_key_press_secs=5):
       user.clean_up(test_id, test_name)
       return

    user.remote_control_press('KEY_ENTER', 2)

    if not fromminiguidescreen.logo("Step 3", user):
        user.clean_up(test_id, test_name)
        return

    user.remote_control_press('KEY_9', 3)

    if not user.check_text(999):
        user.clean_up(test_id, test_name)
        return

    user.remote_control_press('KEY_ENTER')

    if not fromMainMenuScreen.to_tvshows("Step 4", user):
        user.clean_up(test_id, test_name)
        return

    if not fromAnyScreen.exit_to_live_tv_screen("Step 2", user, number_of_exit_key=2, wait_after_key_press_secs=5):
        user.clean_up(test_id, test_name)
        return

    user.remote_control_press('KEY_GUIDE')

    if not user.check_image(GuideScreen.guide_options):
        user.clean_up(test_id, test_name)
        return

    user.remote_control_press('KEY_9', 3)

    if not fromMainMenuScreen.to_tvshows("Step 1", user):
        user.clean_up(test_id, test_name)
    return













