import os
import sys


# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    print "dirName : %s" %d
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
        print "dirName : %s" %d
    return d


sys.path.insert(0, _get_test_pack_root())

from tests.SpectrumGuide.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen

#IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_tc01_demo_framework():
    """ This is a simple test to illustrate the how the framework structure works """
    Tester.press("KEY_MENU")
    print MainMenuScreen.Spectrum_Logo["logo"]
    Tester.check_image(MainMenuScreen.Spectrum_Logo["logo"])