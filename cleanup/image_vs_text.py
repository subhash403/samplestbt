from VOD_methods import tv_shows_launch
from VOD_methods import video_store_launch
from Menu_methods import menu_launch
from stbt/tests/methods/VOD_Methods import tv_shows_launch
import stbt
import api_test

def test_run():
    tv_shows_launch()
    video_store_launch()
