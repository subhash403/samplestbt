import stbt
from time import sleep

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
        if stbt.wait_until(lambda: stbt.match("images/env/ip_video_top_option.png")):
            break
        else:
            stbt.press('KEY_UP')
    sleep(3)
    stbt.press('KEY_ENTER')
    sleep(10)
    stbt.press('KEY_1')
    stbt.press('KEY_2')
    sleep(2)
    assert stbt.wait_until(lambda: stbt.wait_for_motion()), \
    "Video not displayed within time constrant on channel 12"
    stbt.press('KEY_1')
    stbt.press('KEY_7')
    sleep(2)
    assert stbt.wait_until(lambda: stbt.wait_for_motion()), \
    "Video not displayed within time constrant on channel 17"
    count =0
    while True:
        sleep(1)
        count +=1
        if stbt.wait_until(lambda: stbt.wait_for_motion()) or count == 3:
            break
    assert count != 3
    stbt.press('KEY_MENU')
    assert stbt.wait_until(lambda: stbt.match("images/IP_Video_Menu.png")), \
    "Menu not launched"
    stbt.press('KEY_DOWN')
    assert stbt.wait_until(lambda: stbt.match("images/Lib_Highlight.png")), \
    "Scrolling down on the main menu failed"
    stbt.press('KEY_DOWN')
    assert stbt.wait_until(lambda: stbt.match("images/TV_highlight.png")), \
    "Scrolling down on the main menu failed"
    stbt.press('KEY_UP')
    assert stbt.wait_until(lambda: stbt.match("images/Lib_Highlight.png")), \
    "Scrolling up on the main menu failed"
    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/IP_Video_TV_Shows.png")), \
    "TV Shows not launched"
    stbt.press('KEY_UP')
    stbt.press('KEY_RIGHT')
    assert stbt.wait_until(lambda: stbt.match("images/hbo_highlighted.png")), \
    "Scrolling right inside of TV Shows failed"
    stbt.press('KEY_LEFT')
    assert stbt.wait_until(lambda: stbt.match("images/all_sub_highlighted.png")), \
    "Scrolling left inside of TV Shows failed"
