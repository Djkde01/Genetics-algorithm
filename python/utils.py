from city import City
from route import Route
import csv
import random
from copy import deepcopy


def generate_cities(
    city_count, minx, miny, maxx, maxy
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


def _swap_parents(parent1, parent2):
    child = deepcopy(parent2)

    for position_p1, value_p1 in enumerate(parent1):
        position_p2 = child.index(value_p1)
        child[position_p2] = child[position_p1]
        child[position_p1] = value_p1
    return child


def cross(best_parents, population_size):
    missing_childrens = population_size - len(best_parents)
    new_children = []

    for _ in range(missing_childrens):
        parent1, parent2 = random.sample(best_parents, 2)
        new_route = Route(_swap_parents(parent1.cities, parent2.cities))
        new_children.append(new_route)
    return new_children


def mutate(new_childrens):
    mutations = []
    for child in new_childrens:
        cities = deepcopy(child.cities)
        if 0.5 > random.random():
            swap_from = random.randint(0, len(cities) - 1)
            swap_to = random.randint(0, len(cities) - 1)
            while swap_to == swap_from:
                swap_to = random.randint(0, len(cities) - 1)
            aux = cities[swap_to]
            cities[swap_to] = cities[swap_from]
            cities[swap_from] = aux
        mutations.append(Route(cities))
    return mutations
