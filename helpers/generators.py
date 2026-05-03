from uuid import uuid4


def generate_email():
    return f"test-user-{uuid4().hex}@example.com"

