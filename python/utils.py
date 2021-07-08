from city import City
from route import Route
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


def generate_population(cities, population_size):
    population = []

    for _ in range(population_size):
        population.append(Route(random.sample(cities, len(cities))))

    return population


def select_parents(population, num_parents):
    ordered_by_distance = sorted(population, key=lambda route: route.distance)
    return ordered_by_distance[:num_parents]
