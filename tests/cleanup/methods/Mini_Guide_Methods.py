def miniguide_launch():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_ENTER')
    time.sleep(1.2)
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/miniguide/miniguide.png")), \
    "Miniguide not launched"
