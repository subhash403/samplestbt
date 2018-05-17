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

from tests.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.NavigateTo import LiveTV
from tests.SpectrumGuide.ObjectRepo import GuideScreen
from tests.SpectrumGuide.NavigateTo import MainMenu
from time import sleep

def test_logging():
    Tester.LogResults.passed("Step 1 did a thing")
    Tester.remote_control_press('KEY_MENU')
    sleep(3)
    Tester.check_image(MainMenuScreen.Spectrum_Logo["image"])


def test_add_adult_and_nonadult_to_watchlist():
    # Turn off 'Hide Adult Content'
    # Clear Watchlist
    # Press 'A'/'Settings' on non-adult asset
    assert LiveTV.to_main_menu(), \
        "Main Menu not launched from Live TV"
    assert MainMenu.to_tv_shows(), \
        "TV Shows not launched from Main Menu"
    Tester.remote_control_press('KEY_EXIT')
    sleep(2)
    assert LiveTV.to_main_menu(), \
        "check 1"
    assert MainMenu.to_my_library(), \
        "check 2"
    # Exit session, re-open, verify in Watchlist
    # Press 'A'/'Settings' on adult asset
    # Exit session, re-open, verify in Watchlist



def test_page_up_down_nav():
    start_time = time.time()
    Tester.LogResults.info("Test beginning at " + start_time)
    Tester.remote_control_press('KEY_EXIT')
    Tester.LogResults.passed("Step 1: Live TV reached")
    sleep(4)
    # Launch guide
    assert LiveTV.to_guide(), \
        "Guide not reached from Live TV"
    Tester.LogResults.passed("Step 2: Guide launched")
    # Verify 'PAGE_DOWN' press shifts down the list by 5, and 'PAGE_UP' shifts back up 5
    last_channel = Tester.get_text(GuideScreen.last_channel["region"])
    # Tester.LogResults.info("Channel " + last_channel + " is at bottom of guide")
    Tester.remote_control_press('KEY_PAGEDOWN')
    sleep(2)
    first_channel = Tester.get_text(GuideScreen.first_channel["region"])
    # Tester.LogResults.info("After PAGEDOWN press, " + first_channel + " is at top of guide")
    assert last_channel == first_channel, \
        "PAGEDOWN press did not shift guide list by 5"
    Tester.LogResults.passed("Step 3: Page_Down press moves down the guide by 5 channels")
    Tester.remote_control_press('KEY_PAGEUP')
    sleep(2)
    last_channel = Tester.get_text(GuideScreen.last_channel["region"])
    # Tester.LogResults.info("After PAGEUP press, " + last_channel + " is at bottom of guide")
    assert last_channel == first_channel, \
        "PAGEUP press did not shift guide list by 5"
    Tester.LogResults.passed("Step 4: Page_Up press moves up the guide by 5 channels")
    Tester.remote_control_press('KEY_RIGHT')
    sleep(2)
    assert Tester.check_image(GuideScreen.first_cell_not_selected["image"],
                              GuideScreen.first_cell_not_selected["region"]), \
        "RIGHT press in guide did not move highlight to future program"
    Tester.LogResults.passed("Step 5: Right press moves to next future program in guide")
    # Checking page up/down from future program cell
    last_channel = Tester.get_text(GuideScreen.last_channel["region"])
    # Tester.LogResults.info("Channel " + last_channel + " is at bottom of guide")
    Tester.remote_control_press('KEY_PAGEDOWN')
    sleep(2)
    first_channel = Tester.get_text(GuideScreen.first_channel["region"])
    # Tester.LogResults.info("After PAGEDOWN press, " + first_channel + " is at top of guide")
    assert last_channel == first_channel, \
        "PAGEDOWN press did not shift guide list by 5"
    Tester.LogResults.passed("Step 6: Page_Down press moves down the guide by 5 channels on future program cell")
    Tester.remote_control_press('KEY_PAGEUP')
    sleep(2)
    last_channel = Tester.get_text(GuideScreen.last_channel["region"])
    # Tester.LogResults.info("After PAGEUP press, " + last_channel + " is at bottom of guide")
    assert last_channel == first_channel, \
        "PAGEUP press did not shift guide list by 5"
    Tester.LogResults.passed("Step 7: Page_Up press moves up the guide by 5 channels on future program cell")
    # Check page up/down from center of guide
    Tester.remote_control_press('KEY_DOWN', 2)
    last_channel = Tester.get_text(GuideScreen.last_channel["region"])
    # Tester.LogResults.info("Channel " + last_channel + " is at bottom of guide")
    Tester.remote_control_press('KEY_PAGEDOWN')
    sleep(2)
    first_channel = Tester.get_text(GuideScreen.first_channel["region"])
    # Tester.LogResults.info("After PAGEDOWN press, " + first_channel + " is at top of guide")
    assert last_channel == first_channel, \
        "PAGEDOWN press did not shift guide list by 5"
    Tester.LogResults.passed("Step 8: Page_Down press moves down the guide by 5 channels from center of guide")
    Tester.remote_control_press('KEY_PAGEUP')
    sleep(2)
    last_channel = Tester.get_text(GuideScreen.last_channel["region"])
    # Tester.LogResults.info("After PAGEUP press, " + last_channel + " is at bottom of guide")
    assert last_channel == first_channel, \
        "PAGEUP press did not shift guide list by 5"
    Tester.LogResults.passed("Step 9: Page_Up press moves up the guide by 5 channels from center of guide")
    end_time = time.time()
    Tester.LogResults.info("Test ending at " + end_time)
