import os

IMG_ABS_PATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

play = {
    "image": IMG_ABS_PATH + "/ImageRepo/LiveTV/play.png"
}

pause = {
    "image": IMG_ABS_PATH + "/ImageRepo/LiveTV/pause.png"
}

fastforward = {
    "image": IMG_ABS_PATH + "/ImageRepo/LiveTV/fastforward.png"
}

rewind = {
    "image": IMG_ABS_PATH + "/ImageRepo/LiveTV/rewind.png"
}