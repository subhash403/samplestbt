import requests

response = requests.post(
    "https://charter.stb-tester.com/api/v2/run_tests",
    headers={"Authorization": "token BP7BxqZvuZPGeQRBuG6fxh7S_B1iWmS9"},
    data=json.dumps({
        "node_id": "stb-tester-abcdef123456",
        "test_pack_revision": "c2c82cad",
        "test_cases": ["tests/menu.py::test_that_menu_appears_when_menu_key_is_pressed"],
        "remote_control": "roku",
        }))
print response.json()
