from time import sleep
import requests
import stbt
import time
import requests
from requests.auth import HTTPBasicAuth
from http.client import HTTPSConnection
from base64 import b64encode
def test_that_live_tv_is_playing():
    stbt.press('KEY_CLOSE')  # Close any open menus
    assert stbt.wait_for_motion()
    
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
    assert stbt.wait_for_match('images/tv_shows_logo.png')
    print stbt.get_config("sst", "macAddress")
    
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
    
def test_login_edge():
    #r = requests.post('http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login')
    #r.text()
    #url = "http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
    #r = requests.get('http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login', auth=HTTPBasicAuth('charternet', 'Chart3rn3t'))
    #print r
    #uri = urlparse("http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login")
    #http = http.client.HTTPConnection(uri.host, uri.port)
    #This sets up the https connection
    c = HTTPSConnection("http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login")
    #we need to base 64 encode it 
    #and then decode it to acsii as python 3 stores it as a byte string
    userAndPass = b64encode(b"charternet:Chart3rn3t").decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    #then connect
    c.request('GET', '/', headers=headers)
    #get the response back
    res = c.getresponse()
    # at this point you could check the status etc
    # this gets the page text
    data = res.read() 
