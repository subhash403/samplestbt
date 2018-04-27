import requests

response = requests.post(
    "https://charter.stb-tester.com/api/v2/run_tests",
    headers={"Authorization": "token W7rfXCJfEIlk1eeVywNmBfPvSGYYt_2l"},
    data=json.dumps({
        "node_id": "stb-tester-00044b80f5f9",
        "test_pack_revision": "147b7d7",
        "test_cases": ["tests/example_test.py::test_VOD_ME_6119_tv_shows_launch"],
        "remote_control": "roku",
        }))
print response.json()
