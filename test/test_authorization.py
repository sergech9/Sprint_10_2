from helpers.response_helpers import extract_token


class TestUserAuthorization:
    def test_login_registered_user(self, user_client, registered_user):
        response = user_client.login_user(
            registered_user["email"],
            registered_user["password"],
        )

        assert response.status_code == 201
        assert extract_token(response)
