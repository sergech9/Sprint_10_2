def extract_token(response):
    body = response.json()
    return body["token"]["access_token"]


def extract_object_id(response):
    body = response.json()
    return body["id"]


def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}
