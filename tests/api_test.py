import requests
import urllib2
import json
def test_login_edge():
  endpoint = ".../api/ip"
  data = {"ip":"1.1.2.3"}
  headers = {"Authorization":"Basic MYREALLYLONGTOKENIGOT"}

  print requests.post(endpoint,data=data,headers=headers).json()
def test_get_auth_token()
     req = requests.request("POST",url="http://spectrumint.engprod-charter.net/api/pub/loginedge/login/v1/auth/login", headers=
                             "auth=HTTPBasicAuth('charternet', 'Chart3rn3t'))", payload="macAddress=3438B77F88F8")
     res=req.text
     print res
     return res

def get_response_json_object(url, auth_token)
    auth_token=get_auth_token()
    req=urllib2.Request(url, None, {"Authorization": "Bearer %s" %auth_token})
    response=urllib2.urlopen(req)
    html=response.read()
    json_obj=json.loads(html)
    return json_obj
