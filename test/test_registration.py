from data.test_data import user_payload


class TestUserRegistration:
    def test_register_new_user_with_unique_email(self, user_client, new_user_payload):
        response = user_client.register_user(new_user_payload)

        assert response.status_code == 201

    def test_register_user_with_existing_email_returns_error(self, user_client):
        payload = user_payload()
        first_response = user_client.register_user(payload)
        second_response = user_client.register_user(payload)

        assert first_response.status_code == 201
        assert second_response.status_code == 400
