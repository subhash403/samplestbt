from time import sleep
import requests
import stbt
import time
import os

def test_DVR_on_reboot():
    hard_reboot()
    stbt.press('KEY_EXIT')
    assert stbt.wait_for_motion()
    guide_launch()
    stbt.press('KEY_EXIT')
    mydvr_launch()
    stbt.press('KEY_EXIT')
    miniguide_launch()
    stbt.press('KEY_RECORD')
    while True:
     if stbt.wait_for_match('images/edit_ep_rec.png'): break 
     assert stbt.wait_until(lambda: stbt.match("images/miniguide_rec_icon.png")), \
     "Recording not set with RECORD press in miniguide"
    stbt.press('KEY_EXIT')  
    guide_launch()
    stbt.press('KEY_RECORD')
    while True:
     if stbt.wait_for_match('images/in_progress.png'): break
     assert stbt.wait_until(lambda: stbt.match("images/guide_rec_icon.png")), \
     "Recording not set with RECORD press in guide"
   
def hard_reboot():
    os.system("ssh P2729593@olympus.dev-charter.net")
    os.system("Bananadev24.me")
    os.system("ssh seqa@ctec-stb-seqa.enwd.co.sa.charterlab.com")
    os.system("seqa!23")
    os.system("ssh root@30.255.141.82")
    os.system("wb@humax")
    os.system("stbdiag")
    os.system("rebootnow")

def test_that_live_tv_is_playing():
    stbt.press('KEY_CLOSE')  # Close any open menus
    assert stbt.wait_for_motion()
    
def guide_launch():
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide_options.png")), \
    "Guide not launched"
    
def miniguide_launch():
    stbt.press('KEY_ENTER')
    time.sleep(1.2)
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/miniguide.png")), \
    "Miniguide not launched"
    
def mydvr_launch():
    stbt.press('KEY_MYDVR')
    assert stbt.wait_until(lambda: stbt.match("images/my_dvr.png")), \
    "MyDVR not launched"
    
def init():
    for _ in " "*3: stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
    if stbt.is_screen_black(): stbt.press('KEY_POWER')
    stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
    if stbt.is_screen_black(): stbt.press('KEY_POWER')
    stbt.press('KEY_EXIT')

def test_VOD_ME_6119_tv_shows_launch():
    init()
    stbt.press('KEY_MENU')
    assert stbt.wait_for_match('images/menu_logo.png')
    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/tv_shows_logo.png")), \
    "TV Shows not launched"
    macAddress = stbt.get_config("sst", "macAddress")
    print (macAddress)
    
def test_VOD_ME_6120_check_tv_shows_filter():
    test_VOD_ME_6119_tv_shows_launch()
    assert stbt.wait_until(lambda: stbt.match("images/included_with.png")), \
    "Included With filter not found in TV Shows"
    
def test_VOD_ME_4434_check_VODpage_not_in_Recently_Watched():
    test_VOD_ME_6119_tv_shows_launch()
    time.sleep(65)
    stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_for_match('images/menu_logo.png')
    stbt.press('KEY_ENTER')
    while True:
     stbt.press('KEY_DOWN')
     if stbt.wait_for_match('images/recently_watched.png'): break      
    stbt.press('KEY_ENTER')

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
