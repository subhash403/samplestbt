import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)
watchlist_overlay = {
    "ok": IMG_ABS_PATH + "GenericButtons/ok.png",
    "asset_name": {"x": 614, "y": 265, "width": 266, "height": 78}
}