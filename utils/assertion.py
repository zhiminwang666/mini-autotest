def assert_status_code(resp, expected):
    actual = resp.status_code
    assert actual == expected, f"Expected status {expected}, got {actual}. Response: {resp.text}"

def assert_json_has_keys(resp, keys: list):
    data = resp.json()
    for k in keys:
        assert k in data, f"Expected key '{k}' not in response JSON. JSON: {data}"

def assert_json_key(resp, key, expected_value):
    data = resp.json()
    assert key in data, f"Key '{key}' missing in JSON. JSON: {data}"
    assert data[key] == expected_value, f"Expected {key}={expected_value}, got {data[key]}"

