import requests

status = requests.get(
    "https://charter.stb-tester.com/api/v2/nodes/stb-tester-00044b80f5f9/job",
    headers={"Authorization": "token W7rfXCJfEIlk1eeVywNmBfPvSGYYt_2l"}
    )
response =status.json()
print response["status"]
