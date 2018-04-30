import requests, subprocess
import json

def list_tests_in_branch(my_branch)
  tests = requests.get(
      "https://charter.stb-tester.com/api/v2/test_pack/%s/test_case_names" % my_branch,
      headers={"Authorization": "token W7rfXCJfEIlk1eeVywNmBfPvSGYYt_2l"}
      ).json()
  for test_name in tests:
      print test_name
