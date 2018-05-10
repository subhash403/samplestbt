import os
import sys

# Workaround for import path behaviour; can be removed once stb-tester v29 is
# released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    print "dirName : %s" %d
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
        #print "dirName : %s" %d
    return d
sys.path.insert(0, _get_test_pack_root())
IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.SpectrumGuide.astro.Video import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen

def test_demo_framework():
    test = Tester()
    test.press("KEY_MENU")
    #print "Full Path : {}".format(fullpath)
    #test.check_image("{}/ImageRepo/MainMenu/Spectrum_Logo.png".format(fullpath))
    test.check_image(IMG_ABS_PATH + MainMenuScreen.Spectrum_Logo["logo"])
    #test.check_text(MainMenuScreen.Spectrum_Logo["ocr"])
