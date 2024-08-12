'''
import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestrailApiClient :
    def __init__(self, base_url, user, password):
        self.base_url = base_url.rstrip('/')
        self.user = user
        self.password = password

    def send_post(self, uri, data):
        url = f"{self.base_url}/{uri}"
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data), auth=(self.user, self.password))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send POST request to TestRail: {e}")
            return None

    def add_result_for_case(self, run_id, case_id, status_id, comment):
        uri = f"index.php?/api/v2/add_result_for_case/{run_id}/{case_id}"
        data = {
            "status_id": status_id,
            "comment": comment
        }
        return self.send_post(uri, data)

    def get_tests(self, run_id):
        uri = f"index.php?/api/v2/get_tests/{run_id}"
        return self.send_post(uri, {})
'''