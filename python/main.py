from utils import generate_cities, generate_population, select_parents

all_cities = generate_cities(10, 0, 0, 100, 100)

population = generate_population(all_cities, 50)

print(len(population))

selected_parents = select_parents(population, 10)

print(len(selected_parents))
