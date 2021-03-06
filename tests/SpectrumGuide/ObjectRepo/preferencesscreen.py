import os

IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
area = {
"region": {"x": 501, "y": 400, "width": 120, "height": 52}
}

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
    "image": IMG_ABS_PATH +"/ImageRepo/preferences/Infobanner.png"
}
info_banner_time = {
    "region": {"x": 420, "y": 405, "width": 80, "height": 37}
}