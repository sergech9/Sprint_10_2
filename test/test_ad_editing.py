from data.test_data import edited_advertisement_payload
from helpers.response_helpers import auth_headers


class TestAdvertisementEditing:
    def test_edit_own_advertisement_field(self, advertisement_client, auth_token, created_advertisement):
        payload = edited_advertisement_payload()
        response = advertisement_client.edit_advertisement(
            created_advertisement,
            payload,
            auth_headers(auth_token),
        )

        assert response.status_code == 200

    def test_edit_foreign_advertisement_returns_forbidden(
        self,
        advertisement_client,
        second_auth_token,
        created_advertisement,
    ):
        response = advertisement_client.edit_advertisement(
            created_advertisement,
            edited_advertisement_payload(),
            auth_headers(second_auth_token),
        )

        assert response.status_code == 401
