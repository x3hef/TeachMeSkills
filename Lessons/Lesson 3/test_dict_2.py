fr = {
    "name": "France",
    "capital": "Paris",
    "population": 67364357,
    "area": 551695,
    "currency": "Euro",
    "languages": ["French"],
    "region": "Europe",
    "subregion": "Western Europe",
    "flag": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg"
}

print("name", type(fr["name"]))
print("capital", type(fr["capital"]))
print("population", type(fr["population"]))

print("area", type(fr["area"]))
print("currency", type(fr["currency"]))

print("Страна:", fr["name"])
print("Основной язык:", fr['languages'])

user_profile = {
    "firstName": "Jane",
    "lastName": "Doe",
    "birthDate": "1992-04-12",
    "gender": "female",
    "avatarUrl": "https://example.com/avatars/janedoe.jpg",
    "bio": "Digital marketer and blogger."
}

user = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": user_profile
}

# user = {
# "userId": 2,
# "username": "janedoe",
# "email": "janedoe@example.com",
# "profile": user_profile
# }

# CTRL + ALT + L

# user = {
#     "userId": 2,
#     "username": "janedoe",
#     "email": "janedoe@example.com",
#     "profile": user_profile
# }


user = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    }
}

print(user)

# Пустой словарь
user['profile'] = {}

print(user)

notifications = {
    "email": False,
    "sms": True,
    "push": True
}

user['notifications'] = notifications

print(user)

print("Оповещения через почту:", user["notifications"]["email"])