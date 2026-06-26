def validate_user(user: dict):
    if "@" not in user.get("email", ""):
        raise ValueError("email is not valid")
    if not user.get("username"):
        raise ValueError("username is not valid")
    if not user.get("password"):
        raise ValueError("password is not valid")


def create_user(username: str, password: str, email: str) -> dict:
    user = {
        "username": username,
        "password": password,
        "email": email,
    }

    try:
        validate_user(user)
        return user
    except ValueError as exc:
        raise TypeError(exc) from exc

    finally:
        user["email"] = ""



user1 = create_user("user1", "", "")