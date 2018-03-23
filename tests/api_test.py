import requests

def test_get_auth_token():
     url = "http://spectrumint.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
     auth=('charternet', 'Chart3rn3t')
     req = requests.request("POST",url, auth=('charternet', 'Chart3rn3t'), params="macAddress=3438B77F88F8")
     res=req.text
     print res
     return res


