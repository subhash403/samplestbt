from tests.sst_automation_repo.astro.Video import Tester
from tests.sst_automation_repo.SpectrumGuide.ObjectRepo import AppsScreen

def test_demo_framework():
    test = Tester()
    test.press("KEY_MENU")
    test.check_image(AppsScreen.Logo["image"])
    test.check_text(AppsScreen.Logo["ocr_region"])
