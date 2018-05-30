import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

area = {
    "region": {"x": 1, "y": 1, "width": 312, "height": 715}
}

logo = {
    "image": IMG_ABS_PATH + "Settings/settings_header.png"
}

preference = {
    "selected": IMG_ABS_PATH + "Settings/preferences_selected.png",
    "launched": IMG_ABS_PATH + "Settings/preferences_launched.png"
}

