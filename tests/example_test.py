from time import sleep
import requests
import stbt
import time
import datetime
import os
import sys
import socket
import subprocess
import pexpect

def test_stb_reboot():
    command0 = "osdiag RebootNow"
    timeout = 10.0
    result = ""
    port = 65432
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    try:
        sock.connect_ex("30.255.240.82", port)
        sock.send(command0)          
    except Exception as ex:
        print(ex)
    finally:
        sock.close()
        
def send_command_internal(command, box_ip, timeout=10.0):
        import os
        cwd = os.getcwd()
        print(cwd)
        import socket
        result = ""
        port = 65432
        print('Sending command "%s" to %s:%d' % (command, box_ip, port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        try:
            sock.connect((box_ip, port))
            sock.send(command)
            while True:
                try:
                    data = sock.recv(1024)
                    if len(data) == 0:
                        print('"%s" answer receiving finished' % command)
                        break
                    result += data
                except Exception as ex:
                    print(ex)
                    break
            #print('"%s" command result: %s' % (command, str(result)))
        except Exception as ex:
            print('"%s" command execution failed!' % command)
            print(ex)
        finally:
            sock.close()
        return str(result)

def test_DVR_on_reboot():
    print("TESTEST")
    child = pexpect.spawn('/usr/bin/ssh root@172.30.82.139')
    child.expect('(yes/no)?',timeout=20)
    child.sendline('yes')
    #child.expect('password', timeout=120)
    time.sleep(20)
    child.sendline('Charter1')
    child.expect(r'.*', timeout=120)
    child.sendline('python dvr_status.py 30.255.240.82')
    child.sendline('exit')
    count = 0
    while True:
     if stbt.is_screen_black(): break
     count += 1
     assert count < 10, \
     "STB did not reboot within 30 seconds with osdiag RebootNow"     
    stbt.press('KEY_POWER')
    assert stbt.wait_until(lambda: stbt.match('images/menu/stick_around.png')), \
    "Stick Around screen not found after hard reboot"
    time.sleep(30)
    stbt.press('KEY_EXIT')
    assert stbt.wait_for_motion()
    guide_launch()
    stbt.press('KEY_EXIT')
    mydvr_launch()
    count = 0
    while True:
     if stbt.wait_for_match('images/watch_cta.png'): break
     stbt.press('KEY_ENTER')
     count += 1
     if count > 10: break
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.wait_for_motion()), \
    "DVR asset did not play back"
    stbt.press('KEY_EXIT')
    miniguide_launch()
    stbt.press('KEY_RECORD')
    while True:
     if stbt.wait_for_match('images/edit_ep_rec.png'): break 
     assert stbt.wait_until(lambda: stbt.match("images/miniguide/miniguide_rec_icon.png")), \
     "Recording not set with RECORD press in miniguide"
    stbt.press('KEY_EXIT')  
    guide_launch()
    stbt.press('KEY_RECORD')
    while True:
     if stbt.wait_for_match('images/in_progress.png'): break
     assert stbt.wait_until(lambda: stbt.match("images/guide/guide_rec_icon.png")), \
     "Recording not set with RECORD press in guide"
   
def test_that_live_tv_is_playing():
    stbt.press('KEY_CLOSE')  # Close any open menus
    assert stbt.wait_for_motion()
    
def guide_launch():
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide/guide_options.png")), \
    "Guide not launched"
    
def miniguide_launch():
    stbt.press('KEY_ENTER')
    time.sleep(1.2)
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/miniguide/miniguide.png")), \
    "Miniguide not launched"
    
def mydvr_launch():
    stbt.press('KEY_MYDVR')
    assert stbt.wait_until(lambda: stbt.match("images/dvr/my_dvr.png")), \
    "MyDVR not launched"

def test_VOD_ME_6119_tv_shows_launch():
    init()
    menu_launch()
    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/vod/tv_shows_logo.png")), \
    "TV Shows not launched"
    macAddress = stbt.get_config("sst", "macAddress")
    print (macAddress)
    
def test_VOD_ME_6120_check_tv_shows_filter():
    test_VOD_ME_6119_tv_shows_launch()
    assert stbt.wait_until(lambda: stbt.match("images/vod/included_with.png")), \
    "Included With filter not found in TV Shows"
    
def test_VOD_ME_4434_check_VODpage_not_in_Recently_Watched():
    test_VOD_ME_6119_tv_shows_launch()
    time.sleep(65)
    stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_for_match('images/menu/menu_logo.png')
    stbt.press('KEY_ENTER')
    while True:
     stbt.press('KEY_DOWN')
     if stbt.wait_for_match('images/vod/recently_watched.png'): break      
    stbt.press('KEY_ENTER')

def test_that_stb_tester_logo_is_shown():
    stbt.press('KEY_CHANNELUP')
    assert stbt.wait_for_match('stb-tester-logo.png')
    
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

def test_read_menu():
    stbt.press('KEY_CLOSE')
    sleep(1)
    stbt.press('KEY_MENU')
    sleep(1)
    print stbt.ocr()
             
def test_launch_methods():
    init()
    menu_launch()
    guide_launch()
    my_library_launch()
    tv_shows_launch()
    movies_launch()
    video_store_launch()
    settings_launch()
    stbt.press('KEY_POWER')
               
def init():
    if stbt.match('images/env/user_settings.png'):
        for _ in " "*2: stbt.press('KEY_POWER')
    else:
        stbt.press('KEY_EXIT')
        stbt.press('KEY_EXIT')
        time.sleep(3)
        if stbt.match('images/env/black_screen.png'): stbt.press('KEY_POWER')
        time.sleep(2)
        stbt.press('KEY_MENU')
        if stbt.match('images/env/user_settings.png'):
            for _ in " "*2: stbt.press('KEY_POWER')
        stbt.press('KEY_EXIT')
    
