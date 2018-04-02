def settings_launch():
    menu_launch()
    stbt.press('KEY_CHANNELDOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/menu/settings_logo.png")), \
    "Settings not launched"
