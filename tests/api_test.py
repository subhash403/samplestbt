import requests

def test_get_auth_token():
     req = requests.request("POST",url="http://spectrumint.engprod-charter.net/api/pub/loginedge/login/v1/auth/login", headers=
                             "auth=HTTPBasicAuth('charternet', 'Chart3rn3t'))", payload="macAddress=3438B77F88F8")
     res=req.text
     print res
     return res


