from city import City
import csv
import random


def generate_cities(
    city_count: int, minx: int, miny: int, maxx: int, maxy: int
):
    cities = set()
    with open("cities.csv", encoding="utf8") as readable:
        reader = csv.reader(readable)
        for raw_city in reader:
            x = random.randint(minx, maxx)
            y = random.randint(miny, maxy)
            cities.add(City(name=raw_city[0], x=x, y=y))

    return set(random.sample(cities, city_count))
