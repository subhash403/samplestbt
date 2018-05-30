import os

IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

guide_Settings = {
    "image": IMG_ABS_PATH +"/ImageRepo/preferences/guide_settings.png"
}

guidesettings_launched = {
    "image": IMG_ABS_PATH +"/ImageRepo/preferences/Guide_settings_launched.png"
}

display_duration = {
    "image": IMG_ABS_PATH +"/ImageRepo/preferences/Display_Duration.png"
}

displayduration_launched = {
    "image": IMG_ABS_PATH +"/ImageRepo/preferences/displayduration_launched.png"
}

infobanner = {
    "image": IMG_ABS_PATH +"/ImageRepo/preferences/infobanner.png"
    "region": {"x": 504, "y": 404, "width": 65, "height": 39}
}
info_banner_time = {
    "region": {"x": 420, "y": 405, "width": 80, "height": 37}
}