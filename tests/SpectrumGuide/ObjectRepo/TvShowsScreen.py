import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

logo = {
    "image": IMG_ABS_PATH + "TvShows/tv_shows_header.png",
    "region": {"x": 473, "y": 50, "width": 321, "height": 70}
}

subtitle = {
    "image": IMG_ABS_PATH + "TvShows/subtitle.png",
    "region": {"x": 428, "y": 110, "width": 419, "height": 39}
}