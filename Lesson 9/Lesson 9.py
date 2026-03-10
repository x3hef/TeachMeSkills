import json
import csv
import os

# Задание 1
with open("city.json", "r", encoding="utf-8") as file:
    cities = json.load(file)

print(len(cities))

# Задание 2
count_cities = {}

for city in cities:
    country = city["country"]

    if country in count_cities:
        count_cities[country] += 1
    else:
        count_cities[country] = 1

print(count_cities)

# Задание 3
north = 0
south = 0


for city in cities:
    lat = city["coord"]["lat"]

    if lat > 0:
        north += 1
    else:
        south += 1

print("сереверное", north, "южное", south)

# Задание 4
with open("cities.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["id", "name", "country", "coordinates"])

    for city in cities:
        coord = f"{city['coord']['lon']},{city['coord']['lat']}"

        writer.writerow([
            city["id"],
            city["name"],
            city["country"],
            coord
        ])


ru_cities = []

for city in cities:
    if city["country"] == "RU":
        ru_cities.append(city)

with open("ru_cities.csv", "w", encoding="utf-8") as file:
    json.dump(ru_cities, file, indent = 4)

os.makedirs("country", exist_ok = True)

countries = {}

for city in cities:
    country = city["country"]

    if country not in countries:
        countries[country] = []

    countries[country].append(city)

for country, data in countries.items():
    filename = f"country/{country}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent = 4)

