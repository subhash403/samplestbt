import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

logo = {
    "image": IMG_ABS_PATH + "MyLibrary/my_library_header.png",
    "region": {"x": 502, "y": 57, "width": 277, "height": 62}
}

subtitle = {
    "image": IMG_ABS_PATH + "MyLibrary/subtitle.png",
    "region": {"x": 416, "y": 109, "width": 451, "height": 39}
}