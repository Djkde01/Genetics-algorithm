from utils import cross, generate_cities, generate_population, mutate, select_parents

n_cities = 20
population_size = 100
parents_size = 50
max_generations = 500

all_cities = generate_cities(n_cities, 0, 0, 100, 100)

population = generate_population(all_cities, population_size)

for generator_id in range(max_generations):
    best_route = sorted(population, key=lambda route: route.distance)[0]
    print(f"{generator_id}: {best_route.distance}")
    selected_parents = select_parents(population, parents_size)

    new_childrens = cross(selected_parents, population_size)

    mutated_childrens = mutate(new_childrens)

    population = selected_parents + mutated_childrens
