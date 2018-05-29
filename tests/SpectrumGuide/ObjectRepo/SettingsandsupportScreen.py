import os

IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

area = {
    "region": {"x": 1, "y": 1, "width": 312, "height": 715}
}

logo = {
    "image": IMG_ABS_PATH + "/ImageRepo/Settings/settingslaunched.png"
}

preference = {
    "selected": IMG_ABS_PATH +"/ImageRepo/Settings/preferences.png",
    "launched": IMG_ABS_PATH +"/ImageRepo/Settings/preferences_launched.png"
}

