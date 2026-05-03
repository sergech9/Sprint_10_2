from data.test_data import advertisement_payload
from helpers.response_helpers import auth_headers


class TestAdvertisementCreation:
    def test_create_advertisement_in_category(self, advertisement_client, auth_token):
        payload = advertisement_payload()
        response = advertisement_client.create_advertisement(payload, auth_headers(auth_token))

        assert response.status_code == 201

