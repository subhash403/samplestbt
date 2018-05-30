import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}/".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

guide_options = {
    "image": IMG_ABS_PATH + "Guide/guide_options.png",
    "region": {"x": 2, "y": 5, "width": 10, "height": 10}
}

first_cell_selected = {
    "image": IMG_ABS_PATH + "Guide/first_cell_selected.png",
    "region": {"x": 244, "y": 292, "width": 56, "height": 10}
}

first_cell_not_selected = {
    "image": IMG_ABS_PATH + "Guide/first_cell_not_selected.png",
    "region": {"x": 271, "y": 295, "width": 66, "height": 13}
}

first_channel = {
    "image": None,
    "region": {"x": 100, "y": 309, "width": 71, "height": 29}
}

last_channel = {
    "image": None,
    "region": {"x": 96, "y": 669, "width": 76, "height": 27}
}

record_in_cell = {
    "image": IMG_ABS_PATH + "Guide/record_in_cell.png",
    "region": {"x": 220, "y": 302, "width": 1059, "height": 54}
}

edit_episode_recording = {
    "image": IMG_ABS_PATH + "Guide/edit_episode_recording.png",
    "region": {"x": 220, "y": 302, "width": 1059, "height": 54}
}