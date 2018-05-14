#from tests.stbtwrapper.key_press import press
from time import sleep
import requests
import stbt
import time
import datetime
import os
import sys
import socket
import subprocess
import getpass
import shutil

def test_press_check():
    stbt.press('KEY_MENU')

def test_DVR_on_reboot():
    count = 0
    while True:
     if stbt.is_screen_black(): break
     count += 1
     sleep(3)
     assert count < 10, \
     "STB did not reboot within 30 seconds with osdiag RebootNow"  
    count = 0
    while True:
     stbt.press('KEY_POWER')
     sleep(5)
     if stbt.match('images/menu/stick_around.png') or stbt.match('images/menu/reboot_logo.png'): break
     sleep(5)
     count += 1
     assert count < 18, \
     "Stick Around screen is not shown after reboot within 3 minutes"
    stbt.wait_for_motion(timeout_secs=300)
    stbt.press('KEY_RECORD')
    assert stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_rec.png") or stbt.match("images/dvr/ch_bar_rec.png")), \
    "RECORD press on live TV did not set recording, or prompt for edit recording"
    mydvr_launch()
    count = 0
    while True:
        stbt.press('KEY_ENTER')
        if stbt.match('images/cta/watch.png'): break
        count += 1
        assert count < 16, \
        "Could not find recording to play in DVR page"
    stbt.press('KEY_ENTER')
    assert stbt.wait_for_motion(timeout_secs=20)
    
def guide_launch():
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide/guide_options.png")), \
    "Guide not launched"
    
def miniguide_launch():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_ENTER')
    time.sleep(1.2)
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/miniguide/miniguide.png")), \
    "Miniguide not launched"
    
def test_mydvr_launch():
    f = open("testFile.txt","w+")
    stbt.press('KEY_EXIT')
    f.write("Step 1: press exit: Passed")
    stbt.press('KEY_MYDVR')
    f.write("Step 2: press MyDVR: Passed")
    f.close()
    assert stbt.wait_until(lambda: stbt.match("images/dvr/my_dvr.png")), \
    "MyDVR not launched"

def test_VOD_ME_6119_tv_shows_launch():
    init()
    tv_shows_launch()
    
def test_VOD_ME_6120_check_tv_shows_filter():
    tv_shows_launch()
    assert stbt.wait_until(lambda: stbt.match("images/vod/included_with.png")), \
    "Included With filter not found in TV Shows"
    
def test_VOD_ME_4434_check_VODpage_not_in_Recently_Watched():
    tv_shows_launch()
    time.sleep(65)
    stbt.press('KEY_EXIT')
    my_library_launch()
    while True:
     stbt.press('KEY_DOWN')
     if stbt.wait_for_match('images/lane/recently_watched.png'): break      
    stbt.press('KEY_ENTER')
    
def my_library_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*2: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/my_library_logo.png")), \
    "My Library not launched"
    
def tv_shows_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*3: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/tv_shows_logo.png")), \
    "TV Shows not launched"
    
def movies_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*4: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/movies_logo.png")), \
    "Movies not launched"
    
def video_store_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    for _ in " "*5: stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/video_store_logo.png")), \
    "Video Store not launched"
    
def settings_launch():
    menu_launch()
    stbt.press('KEY_CHANNELDOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/menu/settings_logo.png")), \
    "Settings not launched"
    
def search_launch():
    menu_launch()
    stbt.press('KEY_CHANNELUP')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/menu/search_logo.png")), \
    "Search not launched"

def menu_launch():
    for _ in " "*2: stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_until(lambda: stbt.match("images/menu/menu_logo.png")), \
    "Menu not launched"
    
def guide_launch():
    for _ in " "*2: stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide/guide_options.png")), \
    "Guide not launched"
             
def test_launch_methods():
    init()
    menu_launch()
    guide_launch()
    miniguide_launch()
    my_library_launch()
    tv_shows_launch()
    movies_launch()
    video_store_launch()
    settings_launch()
               
def init():
    if stbt.match('images/env/user_settings.png'):
        for _ in " "*2: stbt.press('KEY_POWER')
    else:
        stbt.press('KEY_EXIT')
        stbt.press('KEY_EXIT')
        guide_launch()
        stbt.press('KEY_EXIT')

def test_read_menu():
    stbt.press('KEY_CLOSE')
    sleep(1)
    stbt.press('KEY_MENU')
    sleep(1)
    print stbt.ocr()

def test_that_live_tv_is_playing():
    stbt.press('KEY_CLOSE')  # Close any open menus
    assert stbt.wait_for_motion()
    
def test_that_stb_tester_logo_is_shown():
    stbt.press('KEY_CHANNELUP')
    assert stbt.wait_for_match('stb-tester-logo.png')
