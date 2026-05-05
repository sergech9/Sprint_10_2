import pytest
from clients.advertisement_client import AdvertisementClient
from clients.user_client import UserClient
from data.test_data import ADVERTISEMENT_PAYLOAD, EDITED_ADVERTISEMENT_PAYLOAD, user_payload
from helpers.response_helpers import auth_headers, extract_object_id, extract_token


@pytest.fixture
def user_client():
    return UserClient()


@pytest.fixture
def advertisement_client():
    return AdvertisementClient()


@pytest.fixture
def new_user_payload():
    return user_payload()


@pytest.fixture
def registered_user(user_client, new_user_payload):
    user_client.register_user(new_user_payload)
    return new_user_payload


@pytest.fixture
def auth_token(user_client, registered_user):
    response = user_client.login_user(
        registered_user["email"],
        registered_user["password"],
    )
    return extract_token(response)


@pytest.fixture
def second_auth_token(user_client):
    second_user = user_payload()
    user_client.register_user(second_user)
    login_response = user_client.login_user(second_user["email"], second_user["password"])
    return extract_token(login_response)


@pytest.fixture
def created_advertisement(advertisement_client, auth_token):
    response = advertisement_client.create_advertisement(
        ADVERTISEMENT_PAYLOAD,
        auth_headers(auth_token),
    )
    return extract_object_id(response)
