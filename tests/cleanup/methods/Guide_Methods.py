def guide_launch():
    for _ in " "*2: stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide/guide_options.png")), \
    "Guide not launched"
