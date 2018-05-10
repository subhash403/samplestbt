import os
import sys

# Workaround for import path behaviour; can be removed once stb-tester v29 is
# released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d
sys.path.insert(0, _get_test_pack_root())

from tests.SpecGuide.astro.Video import Tester
from tests.SpecGuide.ObjectRepo import MainMenuScreen

def test_demo_framework():
    test = Tester()
    test.press("KEY_MENU")
    test.check_image(MainMenuScreen.Spectrum_Logo["logo"])
    #test.check_text(MainMenuScreen.Spectrum_Logo["ocr"])
