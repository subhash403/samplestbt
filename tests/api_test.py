import requests
from requests.auth import HTTPBasicAuth

def test_get_auth_token():
     url = "http://spectrumint.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
     auth=('charternet', 'Chart3rn3t')
     req = requests.post(url, data={"macAddress":"3438B77F88F8"}, auth=('charternet', 'Chart3rn3t'))
     res=req.text
     print res
     return res

def test_kandarp():
nurl = "http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
headers = {
    'Content-Type': "application/x-www-form-urlencoded"}
payload = {"macAddress":"3438B77F88F8"}
req = requests.post(url = nurl, data=payload, auth=('charternet', 'Chart3rn3t'))

print req.text


