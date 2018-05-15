import os

IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

guide_options = {
    "image": IMG_ABS_PATH + "/ImageRepo/Guide/guide_options.png",
    "region": {"x": 2, "y": 5, "width": 10, "height": 10}
}

first_cell_selected = {
    "image": IMG_ABS_PATH + "/ImageRepo/Guide/first_cell_selected.png",
    "region": {"x": 244, "y": 292, "width": 56, "height": 10}
}

first_cell_not_selected = {
    "not_selected": IMG_ABS_PATH + "/ImageRepo/Guide/first_cell_not_selected.png",
    "region": {"x": 271, "y": 295, "width": 66, "height": 13}
}

first_channel = {
    "region": {"x": 100, "y": 309, "width": 71, "height": 29}
}

last_channel = {
    "region": {"x": 96, "y": 669, "width": 76, "height": 27}
}
