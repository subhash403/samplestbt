import os
import sys


# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    print "dirName : %s" % d
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
        print "dirName : %s" % d
    return d

sys.path.insert(0, _get_test_pack_root())

from tests.SpectrumGuide.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen


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
