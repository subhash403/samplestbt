import os
IMG_ABS_PATH = "{}/ImageRepo/{}/".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),configuration.img_repo_version)

logo = {
    "image": IMG_ABS_PATH + "MiniGuide/miniguide.png"
}

miniguide_ondemand = {
      "image": IMG_ABS_PATH + "MiniGuide/miniguide_ondemand.png"
}
