import os
import sys


# # Workaround for import path behaviour; can be removed once stb-tester v29 is released.
# def _get_test_pack_root():
#     d = os.path.dirname(os.path.abspath(__file__))
#     print ("Absolute Path : {}".format(d))
#     while not os.path.exists(os.path.join(d, ".stbt.conf")):
#         d = os.path.dirname(d)
#         sys.path.insert(0, d)
#         # Add the module directory to sys.path
#         #sys.path.append(d)
#         print "Info : Appending Module Path : {} to path".format(d)
#     return d
# sys.path.insert(0, _get_test_pack_root())

from tests.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import GuideScreen


def to_main_menu():
    Tester.LogResults.info("Navigating to Main Menu from Live TV")
    Tester.remote_control_press("KEY_MENU")
    if Tester.check_image(MainMenuScreen.Spectrum_Logo["image"]):
        Tester.LogResults.passed("Expected - Main Menu is Displayed, Actual- Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - Main Menu is Displayed, Actual- Not Displayed")
        return False

def to_guide():
    Tester.LogResults.info("Navigating to Guide from Live TV")
    Tester.remote_control_press("KEY_GUIDE")
    if Tester.check_image(GuideScreen.guide_options["image"]):
        Tester.LogResults.passed("Expected - Guide is Displayed, Actual - Displayed")
        return True
    else:
        Tester.LogResults.failed("Expected - Guide is Displayed, Actual - Not Displayed")
        return False

