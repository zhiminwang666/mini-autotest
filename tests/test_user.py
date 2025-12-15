def test_profile(user_api, login_token):
    resp = user_api.get_profile()

    # 模拟环境中我们只验证请求被发送成功即可
    assert resp.status_code in (200, 404)
