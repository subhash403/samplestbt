import requests

def test_get_auth_token():
     url = "http://spectrumint.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
     header={'charternet': 'Chart3rn3t'}
     req = requests.request("POST",url, headers=header, params="macAddress=3438B77F88F8")
     res=req.text
     print res
     return res


