from charter_test_repo.Coop import ImageCompare
from charter_test_repo.SpectrumGuide.ObjectRepo import  MainMenuScreen
def got_to_search():
    ImageCompare.check(MainMenuScreen.Search_Menu["selected"])