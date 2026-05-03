from helpers.generators import generate_email


DEFAULT_PASSWORD = "ABOBAPASS"


def user_payload():
    password = DEFAULT_PASSWORD
    return {
        "email": generate_email(),
        "password": password,
        "submitPassword": password,
    }


def advertisement_payload():
    return {
        "name": "Test advertisement",
        "description": "Created by API autotest",
        "price": 1500,
        "category": "Авто",
        "condition": "Новый",
        "city": "Москва",
    }


def edited_advertisement_payload():
    payload = advertisement_payload()
    payload["name"] = "Updated test advertisement"
    return payload
