from data.test_data import ADVERTISEMENT_PAYLOAD
from helpers.response_helpers import auth_headers


class TestAdvertisementCreation:
    def test_create_advertisement_in_category(self, advertisement_client, auth_token):
        response = advertisement_client.create_advertisement(ADVERTISEMENT_PAYLOAD, auth_headers(auth_token))

        assert response.status_code == 201
        body = response.json()
        assert body["name"] == ADVERTISEMENT_PAYLOAD["name"]
        assert body["description"] == ADVERTISEMENT_PAYLOAD["description"]
        assert body["price"] == ADVERTISEMENT_PAYLOAD["price"]

