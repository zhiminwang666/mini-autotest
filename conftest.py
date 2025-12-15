import pytest
import yaml
from pathlib import Path
from api.client import APIClient
from api.user_api import UserAPI

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev or test"
    )

@pytest.fixture(scope="session")
def env_config(request):
    env = request.config.getoption("--env")
    config_file = Path(__file__).parent / "config" / f"{env}.yaml"
    with open(config_file) as f:
        data = yaml.safe_load(f)
    return data

@pytest.fixture(scope="session")
def client(env_config):
    """返回全局 API client"""
    return APIClient(env_config["base_url"])


@pytest.fixture(scope="session")
def user_api(client):
    """用户相关 API 封装"""
    return UserAPI(client)


@pytest.fixture(scope="session")
def login_token(client, env_config):
    """
    登录并返回 token
    当前阶段使用 fake token，等 Day5 再接真实 API
    """
    # 先用模拟 token
    fake_token = "fake-token-123"
    client.set_token(fake_token)
    return fake_token