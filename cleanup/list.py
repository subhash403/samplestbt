import requests, subprocess

my_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
tests = requests.get(
    "https://company.stb-tester.com/api/v2/test_pack/%s/test_case_names" % my_sha,
    headers={"Authorization": "token BP7BxqZvuZPGeQRBuG6fxh7S_B1iWmS9"}
    ).json()
for test_name in tests:
    print test_name