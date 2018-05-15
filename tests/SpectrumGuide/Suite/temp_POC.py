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


def test_logging():
    Tester.LogResults.passed("Step 1 did a thing")
    Tester.remote_control_press('KEY_MENU')
    sleep(3)
    Tester.check_image(MainMenuScreen.Spectrum_Logo["image"])


def test_page_up_down_nav():
    # Launch guide
    Tester.launch_guide()
    # Verify 'PAGE_DOWN' press shifts down the list by 5, and 'PAGE_UP' shifts back up 5
    last_channel = test.get_text()
    test.press('KEY_PAGEDOWN')
    first_channel = test.get_text()
    assert last_channel == first_channel, \
        "PAGEDOWN press did not shift guide list by 5"
    test.press('KEY_PAGEUP')
