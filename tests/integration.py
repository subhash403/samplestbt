from charter_automation_repo.Astro.Video import Tester
from charter_automation_repo.SpectrumGuide.ObjectRepo import AppsScreen

def test_demo_framework():
    Tester.press("KEY_MENU")
    Tester.check_image(AppsScreen.Apps_Logo["image"])
    Tester.check_text(AppsScreen.Apps_Logo["ocr"])
