from time import sleep

import stbt


def test_that_live_tv_is_playing():
    stbt.press('KEY_CLOSE')  # Close any open menus
    assert stbt.wait_for_motion()

def test_VOD_ME_6119_tv_shows_launch():
    for _ in " "*3: stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_for_match('images/menu_logo.png')
    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_for_match('images/tv_shows_logo.png')
    
def test_VOD_ME_6120_check_tv_shows_filter():
    test_VOD_ME_6119_tv_shows_launch()
    assert stbt.wait_for_match('images/included_with.png')
    
def test_VOD_ME_4434_check_VODpage_not_in_Recently_Watched():
    test_VOD_ME_6119_tv_shows_launch()
    time.sleep(65)
    stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_for_match('images/menu_logo.png')
    stbt.press('KEY_ENTER')
    while True:
     stbt.press('KEY_DOWN')
     if stbt.wait_for_match('images/recently_watched.png')
        break
    stbt.press('KEY_ENTER')
    assert not stbt.wait_for_match('images/VOD_page.png')

def test_that_stb_tester_logo_is_shown():
    stbt.press('KEY_CHANNELUP')
    assert stbt.wait_for_match('stb-tester-logo.png')

def test_that_menu_launches():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_for_match('images/menu_logo.png')

def test_read_menu():
    stbt.press('KEY_CLOSE')
    sleep(1)
    stbt.press('KEY_MENU')
    sleep(1)
    print stbt.ocr()
