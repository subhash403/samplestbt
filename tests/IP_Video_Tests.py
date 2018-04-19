import stbt
from time import sleep

def test_apis():
    stbt.press('KEY_REPLAY')
    stbt.press('KEY_REPLAY')
    sleep(3)
    while True:
        stbt.press('KEY_UP')
        if stbt.wait_until(lambda: stbt.match("images/env/ip_video_top_option.png")):
            break
           
    for _ in " "*3: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    stbt.press('KEY_REPLAY')
