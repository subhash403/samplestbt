import stbt
from time import sleep
import itertools

def test_apis():
    stbt.press('KEY_RECORD')
    sleep(3)
    while True:
        stbt.press('KEY_UP')
        if stbt.wait_until(lambda: stbt.match("images/env/ip_video_top_option.png")):
            break
    while True:
        stbt.press('KEY_DOWN')
        if stbt.wait_until(lambda: stbt.match("images/JS_API_Highlight.png")):
            break
    stbt.press('KEY_ENTER')
    sleep(3)
    assert stbt.wait_until(lambda: stbt.match("images/Select_True.png"))
    assert stbt.wait_until(lambda: stbt.match("images/Menu_True.png"))
    assert stbt.wait_until(lambda: stbt.match("images/Right_True.png"))
    assert stbt.wait_until(lambda: stbt.match("images/Left_True.png"))
    assert stbt.wait_until(lambda: stbt.match("images/Led_Down_True.png"))
    assert stbt.wait_until(lambda: stbt.match("images/Led_Up_True.png"))

def test_spectrum_ui():
    stbt.press('KEY_RECORD')
    sleep(3)
    while True:
        stbt.press('KEY_UP')
        if stbt.wait_until(lambda: stbt.match("images/env/ip_video_top_option.png")):
            break
    sleep(3)
    stbt.press('KEY_ENTER')
    sleep(10)
    stbt.press('KEY_1')
    stbt.press('KEY_2')
    count =0
    while True:
        sleep(1)
        count +=1
        if stbt.wait_until(lambda: stbt.wait_for_motion()) or count == 3:
            break
    assert count != 3

    
