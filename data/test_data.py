from helpers.generators import generate_email


DEFAULT_PASSWORD = "ABOBAPASS"


def user_payload():
    email = generate_email()
    return {
        "email": email,
        "password": DEFAULT_PASSWORD,
        "submitPassword": DEFAULT_PASSWORD,
    }


ADVERTISEMENT_PAYLOAD = {
    "name": "Test advertisement",
    "description": "Created by API autotest",
    "price": 1500,
    "category": "Авто",
    "condition": "Новый",
    "city": "Москва",
}

EDITED_ADVERTISEMENT_PAYLOAD = {**ADVERTISEMENT_PAYLOAD, "name": "Updated test advertisement"}
