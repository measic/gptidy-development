import random

def compute_fitness(solution):
    """
        This function returns the total distance traveled on the current road trip.
        
        The genetic algorithm will favor road trips that have shorter
        total distances traveled.
    """
    solution_fitness = 0.0
    for index in range(len(solution)):
        waypoint1 = solution[index - 1]
        waypoint2 = solution[index]
        solution_fitness += waypoint_distances[frozenset([waypoint1, waypoint2])]
    return solution_fitness

def generate_random_agent():
    """
        Creates a random road trip from the waypoints.
    """
    new_random_agent = list(all_waypoints)
    random.shuffle(new_random_agent)
    return tuple(new_random_agent)

def mutate_agent(agent_genome, max_mutations=3):
    """
        Applies 1 - `max_mutations` point mutations to the given road trip.
        
        A point mutation swaps the order of two waypoints in the road trip.
    """
    agent_genome = list(agent_genome)
    num_mutations = random.randint(1, max_mutations)
    for mutation in range(num_mutations):
        swap_index1 = random.randint(0, len(agent_genome) - 1)
        swap_index2 = swap_index1
        while swap_index1 == swap_index2:
            swap_index2 = random.randint(0, len(agent_genome) - 1)
        agent_genome[swap_index1], agent_genome[swap_index2] = (agent_genome[swap_index2], agent_genome[swap_index1])
    return tuple(agent_genome)

def function_def(agent_genome):
    """
        Applies a single shuffle mutation to the given road trip.
        
        A shuffle mutation takes a random sub-section of the road trip
        and moves it to another location in the road trip.
    """
    agent_genome = list(agent_genome)
    start_index = random.randint(0, len(agent_genome) - 1)
    length = random.randint(2, 20)
    genome_subset = agent_genome[start_index:start_index + length]
    agent_genome = agent_genome[:start_index] + agent_genome[start_index + length:]
    insert_index = random.randint(0, len(agent_genome) + len(genome_subset) - 1)
    agent_genome = agent_genome[:insert_index] + genome_subset + agent_genome[insert_index:]
    return tuple(agent_genome)

def generate_random_population(pop_size):
    """
        Generates a list with `pop_size` number of random road trips.
    """
    random_population = []
    for agent in range(pop_size):
        random_population.append(generate_random_agent())
    return random_population

def run_genetic_algorithm(generations=5000, population_size=100):
    """
        The core of the Genetic Algorithm.
        
        `generations` and `population_size` must be a multiple of 10.
    """
    population_subset_size = int(population_size / 10.0)
    generations_10pct = int(generations / 10.0)
    population = generate_random_population(population_size)
    for generation in range(generations):
        population_fitness = {}
        for agent_genome in population:
            if agent_genome in population_fitness:
                continue
            population_fitness[agent_genome] = compute_fitness(agent_genome)
        new_population = []
        for rank, agent_genome in enumerate(sorted(population_fitness, key=population_fitness.get)[:population_subset_size]):
            if (generation % generations_10pct == 0 or generation == generations - 1) and rank == 0:
                print('Generation %d best: %d | Unique genomes: %d' % (generation, population_fitness[agent_genome], len(population_fitness)))
                print(agent_genome)
                print('')
            new_population.append(agent_genome)
            for offspring in range(2):
                new_population.append(mutate_agent(agent_genome, 3))
            for offspring in range(7):
                new_population.append(function_def(agent_genome))
        for i in range(len(population))[::-1]:
            del population[i]
        population = new_population