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
from pexpect import pxssh
import getpass
import shutil
import example_test

def mydvr_launch():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_MYDVR')
    assert stbt.wait_until(lambda: stbt.match("images/dvr/my_dvr.png")), \
    "MyDVR not launched"

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
    stbt.wait_for_motion(timeout_secs=600)
    sleep(60)
    stbt.press('KEY_RECORD')
    sleep(1)
    if not stbt.match('images/dvr/edit_ep_rec.png') and not stbt.match('images/dvr/ch_bar_rec.png'):
        sleep(120)
    stbt.press('KEY_EXIT')
    stbt.press('KEY_RECORD')
    assert stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_rec.png") or stbt.match("images/dvr/ch_bar_rec.png")), \
    "RECORD press after 60 seconds on live TV did not set recording, or prompt for edit recording"
    mydvr_launch()
    sleep(60)
    count = 0
    while True:
        stbt.press('KEY_ENTER')
        if stbt.match('images/cta/watch.png'): break
        count += 1
        assert count < 16, \
        "Could not find recording to play in DVR page"
    stbt.press('KEY_ENTER')
    assert stbt.wait_for_motion(timeout_secs=20)
