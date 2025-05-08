import random

# Parameters
POP_SIZE = 50
GENES = 3
GENERATIONS = 20
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 3

# Fitness Function: minimize sum of squares
def evaluate(individual):
    return sum(x ** 2 for x in individual)

# Create a random individual
def create_individual():
    return [random.uniform(-5, 5) for _ in range(GENES)]

# Tournament selection
def select(population):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    return min(tournament, key=evaluate)

# Crossover (blend)
def crossover(parent1, parent2):
    alpha = 0.5
    return [(1 - alpha) * p1 + alpha * p2 for p1, p2 in zip(parent1, parent2)]

# Mutation (Gaussian)
def mutate(individual):
    return [
        gene + random.gauss(0, 1) if random.random() < MUTATION_RATE else gene
        for gene in individual
    ]

# Initialize population
population = [create_individual() for _ in range(POP_SIZE)]

# Evolve over generations
for gen in range(GENERATIONS):
    new_population = []
    for _ in range(POP_SIZE):
        parent1 = select(population)
        parent2 = select(population)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population

# Get best result
best_individual = min(population, key=evaluate)
best_fitness = evaluate(best_individual)

print("Best individual:", best_individual)
print("Best fitness:", best_fitness)
