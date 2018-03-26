from time import sleep
import requests
import stbt
import time
import datetime
import os
import sys
import socket
import subprocess

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
    p1 = subprocess.Popen(["echo", "osdiag rebootnow"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["./mototerm", "30.255.240.82"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    output,err = p2.communicate()
    count = 0
    while True:
     if stbt.is_screen_black(): break
     count += 1
     assert count < 10, \
     "STB did not reboot within 30 seconds with osdiag RebootNow"     
    stbt.press('KEY_POWER')
    assert stbt.wait_until(lambda: stbt.match('images/stick_around.png')), \
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
     assert stbt.wait_until(lambda: stbt.match("images/miniguide_rec_icon.png")), \
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
    #init()
    stbt.press('KEY_EXIT')
    stbt.press('KEY_EXIT')
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
    assert stbt.wait_until(lambda: stbt.match("images/vod/included_with.png")), \
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
