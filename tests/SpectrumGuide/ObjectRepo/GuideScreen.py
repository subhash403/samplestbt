import os

IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Guide_Options = {
    "image": IMG_ABS_PATH + "/ImageRepo/Guide/guide_options.png",
    "region": {"x": 2, "y": 5, "width": 10, "height": 10}
}

First_Channel = {
    "region": {"x": 100, "y": 309, "width": 76, "height": 31}
}

Last_Channel = {
    "region": {"x": 100, "y": 668, "width": 76, "height": 31}
}
