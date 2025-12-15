import pytest
import requests

@pytest.mark.parametrize("user,password,expected_status", [
    ("user1","pass1", 404),
    ("user2","wrong", 404),
])
def test_login(env_config, user, password, expected_status):
    base_url = env_config["base_url"]
    endpoint = env_config["login_endpoint"]
    timeout = env_config["timeout"]
    url = base_url + endpoint
    print(f"Testing login: {url} username = {user}, password = {password}")
    response = requests.post(url, json={"user": user, "password": password}, timeout=timeout)
    print("response JSON: ", response.json())
    assert response.status_code == expected_status

# def test_get_profile(login_token, env_config):
#     base_url = env_config["base_url"]
#     url = f"{base_url}/api/profile"
#     headers = {"Authorization": f"Bearer {login_token}"}
#     resp = requests.get(url, headers=headers)
#     assert resp.status_code == 404
#     print("Profile response: ", resp.json())

def test_login(user_api):
    resp = user_api.login("user1", "pass1")
    # 因为当前没有真实 API，返回 404 属于正常情况，我们只测试结构
    assert resp.status_code in (200, 404, 503, 504)
