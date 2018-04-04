def tv_shows_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*3: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/tv_shows_logo.png")), \
    "TV Shows not launched"
