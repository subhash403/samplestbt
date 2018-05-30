import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

Logo = {"image": IMG_ABS_PATH + "AppsScreen/Apps_Logo.png",
        "region": {"x": 5, "y": 4, "width": 10, "height": 4}
    }

Subtitle = {"image": IMG_ABS_PATH + "AppsScreen/Apps_Logo.png",
            "region": {"x": 5, "y": 4, "width": 10, "height": 4}
    }

Apps = {
    "netflix": "AppsScreen/Netflix.png"
}