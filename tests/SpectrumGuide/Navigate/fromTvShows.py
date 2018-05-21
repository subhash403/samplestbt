from time import sleep

from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.ObjectRepo import GuideScreen
from tests.SpectrumGuide.ObjectRepo import Overlays
from tests.SpectrumGuide.ObjectRepo import CTA


def add_to_watchlist_with_a(step_name, tester):
    tester.remote_control_press('KEY_A')
    return True


def get_added_asset_name(step_name, tester):
    """ Returns name of asset added to watchlsit, as seen in Added/Removed Watchlist overlay """
    if not tester.check_image(CTA.ok["image"]):
        return None
    asset = tester.get_text(Overlays.watchlist_overlay["asset_name"])
    assetstrip()
    return asset