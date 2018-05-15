import os

IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

guide_Options = {
    "image": IMG_ABS_PATH + "/ImageRepo/Guide/guide_options.png",
    "region": {"x": 2, "y": 5, "width": 10, "height": 10}
}

first_Channel = {
    "region": {"x": 100, "y": 309, "width": 71, "height": 29}
}

last_Channel = {
    "region": {"x": 96, "y": 669, "width": 76, "height": 27}
}
