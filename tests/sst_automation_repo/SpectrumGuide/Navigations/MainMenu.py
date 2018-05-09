from charter_automation_repo.Astro import Video
from charter_automation_repo.SpectrumGuide.ObjectRepo import  MainMenuScreen
def got_to_search():
    Video.check(MainMenuScreen.Search_Menu["selected"])