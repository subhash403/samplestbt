from charter_automation_repo.Astro import Video
from charter_automation_repo.SpectrumGuide.ObjectRepo import GuideScreen
def got_to_search():
    Video.check(GuideScreen.Search_Menu["selected"])