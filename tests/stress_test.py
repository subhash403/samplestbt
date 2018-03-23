import stbt

def test_weekend_run():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide_options.png")), \
    "Guide not launched"
    stbt.press('KEY_SELECT')
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_SELECT')
    stbt.press('KEY_OPTIONS')
