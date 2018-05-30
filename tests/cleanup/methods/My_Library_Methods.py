def my_library_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*2: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/my_library_header.png")), \
    "My Library not launched"
