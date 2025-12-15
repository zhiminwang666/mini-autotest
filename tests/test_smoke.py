import allure
from utils.assertion import assert_status_code, assert_json_has_keys

import sys
print(sys.path)
def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

@allure.feature("Authentication")
@allure.story("User login")
def test_login(user_api):
    resp = user_api.login("user1", "pass1")
    assert_status_code(resp, 200)
    # resp.status_code in (200, 404, 503, 504)
    assert_json_has_keys(resp, ["token","username"])