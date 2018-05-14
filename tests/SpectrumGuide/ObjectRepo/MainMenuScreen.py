import os
IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print IMG_ABS_PATH

Spectrum_Logo = {
    "image": IMG_ABS_PATH + "/ImageRepo/MainMenu/Spectrum_Logo.png",
    "region" : {"x" : 2,"y" : 5 ,"width" : 10,"height" : 10}
}
Search = {
    "selected": IMG_ABS_PATH +"/ImageRepo/MainMenu/Search_Menu_Selected.png",
    "not_selected": IMG_ABS_PATH + "/ImageRepo/MainMenu/Search_Menu_Not_Selected.png"
}
Guide = {
    "selected": IMG_ABS_PATH + "/ImageRepo/MainMenu/Guide_Selected.png",
    "not_selected": IMG_ABS_PATH + "/ImageRepo/MainMenu/Guide_Not_Selected.png"
}
My_Library = {
    "selected": IMG_ABS_PATH +"/ImageRepo/MainMenu/My_Library_Selected.png",
    "not_selected": IMG_ABS_PATH +"/ImageRepo/MainMenu/My_Library_Not_Selected.png"
}
TV_Shows = {
    "selected": IMG_ABS_PATH +"/ImageRepo/MainMenu/TV_Shows_Selected.png",
    "not_selected": IMG_ABS_PATH +"/ImageRepo/MainMenu/TV_Shows_Not_Selected.png"
}
Movies = {
    "selected": IMG_ABS_PATH +"/ImageRepo/MainMenu/Movies_Selected.png",
    "not_selected": IMG_ABS_PATH + "/ImageRepo/MainMenu/Movies_Not_Selected.png"
}
Video_Store = {
    "selected": "/SpecGuide/ImageRepo/MainMenu/Video_Store_Selected.png",
    "not_selected": "SpecGuide/ImageRepo/MainMenu/Video_Store_Not_Selected.png"
}
Apps = {
    "selected": "/SpecGuide/ImageRepo/MainMenu/Apps_Selected.png",
    "not_selected": "SpecGuide/ImageRepo/MainMenu/Apps_Not_Selected.png"
}
Settings = {
    "selected": "/SpecGuide/ImageRepo/MainMenu/Settings_Selected.png",
    "not_selected": "SpecGuide/ImageRepo/MainMenu/Settings_Not_Selected.png"
}