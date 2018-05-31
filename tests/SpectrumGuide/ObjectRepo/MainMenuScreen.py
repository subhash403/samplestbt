import os
from tests import configuration

IMG_ABS_PATH = "{}/ImageRepo/{}/".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        configuration.img_repo_version)

area = {
    "region": {"x": 1, "y": 1, "width": 312, "height": 715}
}

Spectrum_Logo = {
    "image": IMG_ABS_PATH + "MainMenu/Spectrum_Logo.png",
    "region": {"x": 27, "y": 52, "width": 252, "height": 98}
}

search_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Search_Menu_Selected.png",
    "region": {"x": 38, "y": 194, "width": 153, "height": 53}
}

search_not_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Search_Menu_Not_Selected.png",
    "region": {"x": 38, "y": 194, "width": 153, "height": 53}
}

guide_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Guide_Selected.png",
    "region": {"x": 38, "y": 251, "width": 146, "height": 58}
}

guide_not_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Guide_Not_Selected.png",
    "region": {"x": 38, "y": 251, "width": 146, "height": 58}
}
my_library = {
    "image": IMG_ABS_PATH +"/ImageRepo/MainMenu/my_library_selected.png",
    #"not_selected": IMG_ABS_PATH +"/ImageRepo/MainMenu/My_Library_Not_Selected.png"
}
my_library_selected = {
    "image": IMG_ABS_PATH + "MainMenu/My_Library_Selected.png",
    "region": {"x": 48, "y": 317, "width": 173, "height": 58}
}

my_library_not_selected = {
    "image": IMG_ABS_PATH + "MainMenu/My_Library_Not_Selected.png",
    "region": {"x": 48, "y": 317, "width": 173, "height": 58}
}

tv_shows_selected = {
    "image": IMG_ABS_PATH + "MainMenu/TV_Shows_Selected.png",
    "region": {"x": 26, "y": 368, "width": 208, "height": 67}
}

tv_shows_not_selected = {
    "image": IMG_ABS_PATH + "MainMenu/TV_Shows_Not_Selected.png",
    "region": {"x": 26, "y": 368, "width": 208, "height": 67}
}

movies_selected = {
    "selected": IMG_ABS_PATH + "MainMenu/Movies_Selected.png",
    "region": {"x": 49, "y": 434, "width": 140, "height": 52}
}

movies_not_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Movies_Not_Selected.png",
    "region": {"x": 49, "y": 434, "width": 140, "height": 52}
}

video_store_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Video_Store_Selected.png",
    "region": {"x": 31, "y": 489, "width": 198, "height": 56}
}

video_store_not_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Video_Store_Not_Selected.png",
    "region": {"x": 31, "y": 489, "width": 198, "height": 56}
}
apps_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Apps_Selected.png",
    "region": {"x": 34, "y": 553, "width": 162, "height": 58}
}

apps_not_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Apps_Not_Selected.png",
    "region": {"x": 34, "y": 553, "width": 162, "height": 58}
}

settings_selected = {
    "image": IMG_ABS_PATH + "MainMenu/Settings_Selected.png",
    "region": None
}

settings_not_seleted = {
    "image": IMG_ABS_PATH + "MainMenu/Settings_Not_Selected.png",
    "region": None
}
