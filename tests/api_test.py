import requests
from requests.auth import HTTPBasicAuth
import stbt

def test_get_auth_token():
     url = "http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
     req = requests.post(url, data={"macAddress":"3438B77F88F8"}, auth=('charternet', 'Chart3rn3t'))
     assert req.status_code == 200
     res=req.text.split("Token")
     r= res[1].decode('utf-8')
     t = str(r)[3:len(str(r))].split(",")
     token = str(t)[0:len(str(t))-1]
     print token
     return r

def test_kandarp():
     nurl = "http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
     headers = {'Content-Type': "application/x-www-form-urlencoded"}
     payload = {"macAddress":"3438B77F88F8"}
     req = requests.post(url = nurl, data=payload, auth=('charternet', 'Chart3rn3t'))

     print req.text


