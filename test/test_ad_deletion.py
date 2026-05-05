from helpers.response_helpers import auth_headers


class TestAdvertisementDeletion:
    def test_delete_own_advertisement(self, advertisement_client, auth_token, created_advertisement):
        response = advertisement_client.delete_advertisement(
            created_advertisement,
            auth_headers(auth_token),
        )

        assert response.status_code == 200
        body = response.json()
        assert body

