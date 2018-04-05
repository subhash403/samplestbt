from Menu_methods import menu_launch
import stbt
from time import sleep
def tv_shows_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*3: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/tv_shows_logo.png")), \
    "TV Shows not launched"
    
def movies_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*4: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/movies_logo.png")), \
    "Movies not launched"
    
def video_store_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*5: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    sleep(2)
    count =0
    while TRUE or count < 15:
        if stbt.ocr(region=stbt.Region(x=508, y=54, width=263, height=64)) == "Video Store":
            break
        else:
            count +=1
   assert stbt.ocr(region=stbt.Region(x=508, y=54, width=263, height=64)) == "Video Store", \
    "Video Store not launched"
