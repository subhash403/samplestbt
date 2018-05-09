from charter_automation_repo.Astro.Video import Tester
from charter_automation_repo.SpectrumGuide.ObjectRepo import AppsScreen

def test_demo_framework():
    test = Tester()
    test.press("KEY_MENU")
    test.check_image(MainMenuScreen.Spectrum_Logo["logo"])
    #test.check_text(AppsScreen.Apps_Logo["ocr"])
