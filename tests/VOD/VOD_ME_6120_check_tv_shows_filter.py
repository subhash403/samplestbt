def test_VOD_ME_6120_check_tv_shows_filter():
    tv_shows_launch()
    assert stbt.wait_until(lambda: stbt.match("images/vod/included_with.png")), \
    "Included With filter not found in TV Shows"
