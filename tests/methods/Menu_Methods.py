def menu_launch():
    for _ in " "*2: stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_until(lambda: stbt.match("images/menu/menu_logo.png")), \
    "Menu not launched"
