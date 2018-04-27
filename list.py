import requests, subprocess
import json
my_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
tests = requests.get(
    "https://charter.stb-tester.com/api/v2/test_pack/%s/test_case_names" % my_sha,
    headers={"Authorization": "token W7rfXCJfEIlk1eeVywNmBfPvSGYYt_2l"}
    ).json()
for test_name in tests:
    print test_name
