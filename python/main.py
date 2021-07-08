from utils import cross, generate_cities, generate_population, select_parents

all_cities = generate_cities(10, 0, 0, 100, 100)

population = generate_population(all_cities, 50)

selected_parents = select_parents(population, 10)

print(len(selected_parents))

new_childrens = cross(selected_parents, 50)

population = selected_parents + new_childrens

print(len(population))
