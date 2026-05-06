import time
from api.api_client import APIClient


def test_api_response_time():

    api = APIClient()

    start = time.time()

    response = api.get_notes()

    end = time.time()

    response_time = end - start

    assert response.status_code == 200

    assert response_time < 2