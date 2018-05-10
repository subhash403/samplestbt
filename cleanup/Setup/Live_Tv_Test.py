def live_tv_is_playing():
    stbt.press('KEY_CLOSE')  # Close any open menus
    assert stbt.wait_for_motion()
