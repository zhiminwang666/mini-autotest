import pytest

def test_base_url(env_config):
    assert "http" in env_config["base_url"]

@pytest.mark.parametrize("user,password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
])
def test_login(user, password):
    # 示例：这里可以用 config 里的 base_url 去做接口请求
    print(f"Testing login for {user}/{password}")
    assert isinstance(user, str)
