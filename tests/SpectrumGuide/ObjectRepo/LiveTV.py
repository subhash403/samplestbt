import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}/".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

play = {
    "image": IMG_ABS_PATH + "LiveTV/play.png",
    "region": {"x": 209, "y": 551, "width": 132, "height": 123}
}

pause = {
    "image": IMG_ABS_PATH + "LiveTV/pause.png",
    "region": {"x": 209, "y": 551, "width": 132, "height": 123}
}

fastforward = {
    "image": IMG_ABS_PATH + "LiveTV/fastforward.png",
    "region": {"x": 209, "y": 551, "width": 132, "height": 123}
}

rewind = {
    "image": IMG_ABS_PATH + "LiveTV/rewind.png",
    "region": {"x": 209, "y": 551, "width": 132, "height": 123}
}