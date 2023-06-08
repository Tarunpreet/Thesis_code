import random
import time
import matplotlib.pyplot as plt

# Constants for the triangle problem
MIN_VALUE = 0
MAX_VALUE = 2000
POPULATION_SIZE = 1000
MUTATION_RATE = 0.08
GENERATIONS = 800
TEST_CASES=5
# Function to calculate the fitness value for a triangle
def calculate_fitness(triangle):
    a, b, c = triangle
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    else:
        return 0

# Function to generate a random triangle
def generate_triangle():
    return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(3)]

# Function to generate initial population
def generate_population():
    return [generate_triangle() for _ in range(POPULATION_SIZE)]

# Function to perform mutation on an individual
def mutate(individual):
    for i in range(3):
        if random.random() < MUTATION_RATE:
            individual[i] = random.randint(MIN_VALUE, MAX_VALUE)

# Function to perform crossover between two individuals
def crossover(parent1, parent2):
    child = []
    for i in range(3):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

# GenTest Algorithm
def GenTest_algorithm():
    population = generate_population()
    best_individual = None
    best_fitness = 0
    best_fitnesses = []
    automated_test_cases = []
    for generation in range(GENERATIONS):
        # Calculate fitness for each individual
        fitness_values = [calculate_fitness(individual) for individual in population]

        # Find the best individual
        max_fitness = max(fitness_values)
        max_index = fitness_values.index(max_fitness)
        if max_fitness > best_fitness:
            best_individual = population[max_index]
            best_fitness = max_fitness

        best_fitnesses.append(best_fitness)

        # Create the next generation
        new_population = []

       

        # Perform crossover and mutation to create the rest of the new population
        while len(new_population) < POPULATION_SIZE-1:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        # Perform elitism by adding the best individual to the new population
        new_population.append(best_individual)

        population = new_population
        # Generate automated test cases
        if generation % (GENERATIONS // TEST_CASES) == 0:
            automated_test_cases.append(best_individual)


    return best_fitnesses, automated_test_cases


# Classic Genetic Algorithm
def classic_genetic_algorithm():
    population = generate_population()
    best_fitnesses = []

    for generation in range(GENERATIONS):
        # Calculate fitness for each individual
        fitness_values = [calculate_fitness(individual) for individual in population]

        # Find the best individual
        max_fitness = max(fitness_values)
        max_index = fitness_values.index(max_fitness)
        best_individual = population[max_index]

        best_fitnesses.append(max_fitness)

        # Create the next generation
        new_population = []

        

        # Perform crossover and mutation to create the rest of the new population
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        # Perform elitism by adding the best individual to the new population
        new_population.append(best_individual)
        population = new_population

    return best_fitnesses



best_fitnesses_modified, automated_test_cases_modified = GenTest_algorithm()


best_fitnesses_classic = classic_genetic_algorithm()


# Plot the performance
generations = range(1, GENERATIONS + 1)

plt.plot(generations, best_fitnesses_modified, label="GenTest")
plt.plot(generations, best_fitnesses_classic, label="Classic GA")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Performance Comparison: GenTest vs. Classic Genetic Algorithm(Triangle Problem)")
plt.legend()
plt.show()

print("Automated Test Cases (GenTest Genetic Algorithm):")
for i, test_case in enumerate(automated_test_cases_modified):
    print("Test Case", i+1, ":", test_case)

