import requests

status = requests.get(
    "https://charter.stb-tester.com/api/v2/nodes/stb-tester-00044b80f5f9/job",
    headers={"Authorization": "token BP7BxqZvuZPGeQRBuG6fxh7S_B1iWmS9"}
    ).json()
print status
