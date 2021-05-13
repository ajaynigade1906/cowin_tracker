import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError


class CallApi:

    def _api_call(self, url) -> [HTTPError, dict]:
        user_agent = UserAgent()
        headers = {'User-Agent': user_agent.random}
        response = requests.get(url, headers=headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e

        return response.json()
