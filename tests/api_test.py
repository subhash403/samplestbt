import requests

def test_get_auth_token():
     url = "http://spectrumint.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
     auth=('charternet', 'Chart3rn3t')
     req = requests.post(url, data={"macAddress":"3438B77F88F8"}, auth=('charternet', 'Chart3rn3t'))
     res=req.text
     print res
     return res


