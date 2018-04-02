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
    assert stbt.wait_until(lambda: stbt.match("images/vod/video_store_logo.png")), \
    "Video Store not launched"