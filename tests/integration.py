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

from charter_automation_repo.Astro.Video import Tester
from charter_automation_repo.SpectrumGuide.ObjectRepo import AppsScreen

def test_demo_framework():
    test = Tester()
    test.press("KEY_MENU")
    test.check_image(AppsScreen.Apps_Logo["image"])
    test.check_text(AppsScreen.Apps_Logo["ocr"])
