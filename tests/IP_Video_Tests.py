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
    stbt.press('KEY_RECORD')
    sleep(3)
    while True:
        stbt.press('KEY_UP')
        if stbt.wait_until(lambda: stbt.match("images/env/ip_video_top_option.png")):
            break
    stbt.press('KEY_DOWN')
    sleep(1)
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/JS_SDK_Page_Loaded.png"))
    for _ in itertools.repeat(None, 8):
        stbt.press('KEY_LAST')
        sleep(1)
    for _ in itertools.repeat(None, 7):
        stbt.press('KEY_ENTER')
        sleep(1)
        stbt.press('KEY_LAST')
