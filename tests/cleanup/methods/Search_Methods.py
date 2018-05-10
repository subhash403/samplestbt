def search_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/menu/search_logo.png")), \
    "Search not launched"
