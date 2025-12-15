import requests
import logging
import allure

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def set_token(self, token):
        """设置 token（用于后续接口请求自动带上 Authorization 头）"""
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        logging.info("Token set")

    @allure.step("POST {path}")
    def post(self, path, json=None):
        url = f"{self.base_url}{path}"
        logging.info(f"POST {url}")
        if json:
            allure.attach(
                str(json), name="Request JSON",
                attachment_type=allure.attachment_type.JSON
            )
        resp = self.session.post(url, json=json)
        allure.attach(
            resp.text[:1000], name=f"Response {resp.status_code}",
            attachment_type=allure.attachment_type.TEXT
        )
        return resp

    @allure.step("GET {path}")
    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        logging.info(f"GET {url}")
        resp = self.session.get(url, params=params)
        allure.attach(
            resp.text[:1000], name=f"Response {resp.status_code}",
            attachment_type=allure.attachment_type.TEXT
        )
        return resp