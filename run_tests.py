import requests, subprocess
import json

test_array = ["tests/example_test.py::test_VOD_ME_6119_tv_shows_launch","tests/example_test.py::test_VOD_ME_6120_check_tv_shows_filter"]
node = "stb-tester-00044b80f5f9"
remote = "Moto_Worldbox1"
my_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()

response = requests.post(
    "https://charter.stb-tester.com/api/v2/run_tests",
    headers={"Authorization": "token W7rfXCJfEIlk1eeVywNmBfPvSGYYt_2l"},
    data=json.dumps({
        "node_id": node,
        "test_pack_revision": my_sha,
        "test_cases": test_array,
        "remote_control": remote,
        }))
print response.json()
