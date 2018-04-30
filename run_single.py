import requests, subprocess
import json
import job_init
my_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
response = requests.post(
    "https://charter.stb-tester.com/api/v2/run_tests",
    headers={"Authorization": "token W7rfXCJfEIlk1eeVywNmBfPvSGYYt_2l"},
    data=json.dumps({
        "node_id": "stb-tester-00044b80f5f9",
        "test_pack_revision": my_sha,
        "test_cases": ["tests/example_test.py::test_VOD_ME_6119_tv_shows_launch"],
        "remote_control": "Moto_Worldbox1",
        }))
job_init.myJob = response.job_uid
print response.json()
