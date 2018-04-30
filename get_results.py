import requests, subprocess
import json

response = requests.get(
    "https://charter.stb-tester.com/api/v2/results",
    headers={"Authorization": "token W7rfXCJfEIlk1eeVywNmBfPvSGYYt_2l"},
    params={"filter": "job:/stb-tester-00044b80f5f9/74Vf/3747"})
print response.json()["result"]
