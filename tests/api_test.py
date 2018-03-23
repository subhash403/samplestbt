import requests
from requests.auth import HTTPBasicAuth
import stbt
import numpy as np

def get_auth_token():
     url = "http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
     req = requests.post(url, data={"macAddress":"3438B77F88F8"}, auth=('charternet', 'Chart3rn3t'))
     assert req.status_code == 200
     res=req.text.split("Token")
     r= res[1].decode('utf-8')
     t = str(r)[3:len(str(r))].split(",")
     token = str(t[0])[0:len(str(t[0]))-1]
     return token

def HDAT_setting(value):
	token = get_auth_token()
	if value == "Off":
		newAcctJson ='{"settings":{"groups":[{"id":"STB3438B77F88F8","type":"device-stb","options":[{"name":"HD Auto Tune","value":["Off"]}]}]}}'
	elif value == "On":
		newAcctJson ='{"settings":{"groups":[{"id":"STB3438B77F88F8","type":"device-stb","options":[{"name":"HD Auto Tune","value":["On"]}]}]}}'
	url = "http://spectrum.engprod-charter.net/api/pub/networksettingsedge/v1/settings"
	headers={'X-CHARTER-SESSION':token, 'Content-Type':'application/json'}
	req = requests.post(url, data=newAcctJson, auth=('charternet', 'Chart3rn3t'),headers=headers)
	print req
	assert req.status_code == 200
	
def moviescatalog():
	token = get_auth_token()
	url = "http://spectrum.engprod-charter.net/api/pub/videocatalogedge/services/v1/vod/ctec_c3h2/features/movie_vod/catalog?depth=20&folderContentLimit=100&channelLineupId=CC32-1&folderId=0&startIndex=0&maxResults=100"
	headers={'X-CHARTER-SESSION':token, 'Content-Type':'application/json'}
	req = requests.get(url, auth=('charternet', 'Chart3rn3t'),headers=headers)
	assert req.status_code == 200
	assets = movies_parser(req.text)
	return assets

def movies_parser(string):
	assert string
	m = string.split("TitleId")
	assets = []
	for num in m:
		str = num[3:-1]
		id = str.split("'")
		st= id[0][0:13]
		if 'ctec' not in st and 'exit' not in st:
			assets.append(st)
	asset = np.unique(assets)
	return asset

	
def Add_watchlist():
	assets = moviescatalog()
	token = get_auth_token()
	url = "http://spectrum.engprod-charter.net/api/pub/watchlistedge/watchlist"
	headers={'X-CHARTER-SESSION':token, 'Content-Type':'application/json'}
	newAcctJson ='{"TitleId":"'+assets[0]+'"}'
	print newAcctJson
	req = requests.post(url, data=newAcctJson,auth=('charternet', 'Chart3rn3t'),headers=headers)
	print req.text
	assert req.status_code == 200 or req.status_code == 201
	
def test_parser():
	HDAT_setting("On")
	HDAT_setting("Off")
	Add_watchlist()

