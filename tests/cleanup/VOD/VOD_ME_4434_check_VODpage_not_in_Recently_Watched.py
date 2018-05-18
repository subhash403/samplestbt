def test_VOD_ME_4434_check_VODpage_not_in_Recently_Watched():
    tv_shows_launch()
    time.sleep(65)
    stbt.press('KEY_EXIT')
    my_library_launch()
    while True:
     stbt.press('KEY_DOWN')
     if stbt.wait_for_match('images/lane/recently_watched.png'): break      
    stbt.press('KEY_ENTER')
