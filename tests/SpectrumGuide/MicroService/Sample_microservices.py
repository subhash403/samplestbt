
import configparser
import requests

config = configparser.ConfigParser()
configFilePath = r'C:\Users\Sindhushree.V\PycharmProjects\stb-tester-test-pack-charter\config\stbt.conf'
config.read(configFilePath)
Env=config.get('sst','test_env')
print (Env)

url ="http://spectrum.engprod-charter.net/api/pub/loginedge/login/v1/auth/login"
payload ="macAddress=0000071CE4AE"
headers = {'Content-Type':"application/x-www-form-urlencoded",'Authorization':"Basic Y2hhcnRlcm5ldDpDaGFydDNybjN0",'Cache-Control':"no-cache"}
response = requests.request("POST", url,data=payload,headers=headers)
print(response)

url = "http://charternet:Chart3rn3t@spectrum.engprod-charter.net/api/pub/watchlistedge/watchlist"

payload = "{\"settings\":{\"groups\":[{\"id\":\"STB0000071CE4AE\",\"type\":\"device-stb\",\"options\":[{\"name\":\"WATCHLIST\",\"value\":[\"Clear\"]}]}]}}"
headers = {
    'Content-Type': "application/json",
    'X-CHARTER-SESSION': "ccb2ce27-2e0e-4431-830d-1ecc9852c4ac",
    'Cache-Control': "no-cache",
    'Postman-Token': "4f40f70e-642e-4411-bb7f-54e41f359562"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import requests

url = "http://charternet:Chart3rn3t@spectrum.engprod-charter.net/api/pub/networksettingsedge/v1/settings"

payload = "{\"settings\":{\"groups\":[{\"id\":\"STB0000071CE4AE\",\"type\":\"device-stb\",\"options\":[{\"name\":\"Hide Adult Content\",\"value\":[\"Off\"]}]}]}}"
headers = {
    'Content-Type': "application/json",
    'X-CHARTER-SESSION': "ccb2ce27-2e0e-4431-830d-1ecc9852c4ac",
    'Cache-Control': "no-cache",
    'Postman-Token': "93278838-1482-41ae-830d-b44828f49092"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)