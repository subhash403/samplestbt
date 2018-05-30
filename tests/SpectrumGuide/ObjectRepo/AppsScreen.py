import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}/".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

logo = {"image": IMG_ABS_PATH + "AppsScreen/Apps_Logo.png",
        "region": {"x": 5, "y": 4, "width": 10, "height": 4}
    }

subtitle = {"image": IMG_ABS_PATH + "AppsScreen/Apps_Logo.png",
            "region": {"x": 5, "y": 4, "width": 10, "height": 4}
    }

apps = {
    "netflix": "AppsScreen/Netflix.png"
}