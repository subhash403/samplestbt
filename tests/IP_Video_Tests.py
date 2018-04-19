
import stbt

def test_apis():
    while True:
        stbt.press('KEY_UP')
        if stbt.wait_until(lambda: stbt.match("images/env/ip_video_top_option.png")):
            break
           
    for _ in " "*3: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    stbt.press('KEY_BACK')
