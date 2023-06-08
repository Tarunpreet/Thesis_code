import random
import time
import matplotlib.pyplot as plt

# Constants for the Next Date problem
MIN_DAY = 1
MAX_DAY = 31
MIN_MONTH = 1
MAX_MONTH = 12
MIN_YEAR = 1900
MAX_YEAR = 2100
POPULATION_SIZE = 500
GENERATIONS = 100
TEST_CASES = 5
# Function to check if a date is valid
def is_valid_date(day, month, year):
    if day < MIN_DAY or day > MAX_DAY:
        return False
    if month < MIN_MONTH or month > MAX_MONTH:
        return False
    if year < MIN_YEAR or year > MAX_YEAR:
        return False
    return True

# Function to calculate the fitness value for a date
def calculate_fitness(day, month, year):
    if is_valid_date(day, month, year):
        return day + month + year
    else:
        return 0

# Function to generate a random date
def generate_date():
    day = random.randint(MIN_DAY, MAX_DAY)
    month = random.randint(MIN_MONTH, MAX_MONTH)
    year = random.randint(MIN_YEAR, MAX_YEAR)
    return day, month, year

# Function to generate initial population
def generate_population():
    return [generate_date() for _ in range(POPULATION_SIZE)]

# Function to perform mutation on an individual with adaptive mutation rate
def mutate(individual, mutation_rate):
    day, month, year = individual
    if random.random() < mutation_rate:
        day = random.randint(MIN_DAY, MAX_DAY)
    if random.random() < mutation_rate:
        month = random.randint(MIN_MONTH, MAX_MONTH)
    if random.random() < mutation_rate:
        year = random.randint(MIN_YEAR, MAX_YEAR)
    return day, month, year

# Function to perform crossover between two individuals
def crossover(parent1, parent2):
    child = []
    for i in range(3):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return tuple(child)

# GenTest with Adaptive Mutation and adaptive mutation
def GenTest_algorithm():
    population = generate_population()
    best_individual = None
    best_fitness = 0
    best_fitnesses = []
    mutation_rate = 0.01
    automated_test_cases = []
    for generation in range(GENERATIONS):
        # Calculate fitness for each individual
        fitness_values = [calculate_fitness(day, month, year) for day, month, year in population]

        # Find the best individual
        max_fitness = max(fitness_values)
        max_index = fitness_values.index(max_fitness)
        if max_fitness > best_fitness:
            best_individual = population[max_index]
            best_fitness = max_fitness

        best_fitnesses.append(best_fitness)

        # Calculate adaptive mutation rate
        mutation_rate = 1 / (best_fitness + 1)

        # Create the next generation
        new_population = []

        

        # Perform crossover and mutation to create the rest of the new population
        while len(new_population) < POPULATION_SIZE-1:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        # Add the best individual to the new population
        new_population.append(best_individual)
        population = new_population
        # Generate automated test cases
        if generation % (GENERATIONS // TEST_CASES) == 0:
            automated_test_cases.append(best_individual)
    return best_fitnesses,automated_test_cases


# Classic Genetic Algorithm
def classic_genetic_algorithm():
    population = generate_population()
    best_fitnesses = []

    for generation in range(GENERATIONS):
        # Calculate fitness for each individual
        fitness_values = [calculate_fitness(day, month, year) for day, month, year in population]

        # Find the best individual
        max_fitness = max(fitness_values)
        max_index = fitness_values.index(max_fitness)
        best_individual = population[max_index]

        best_fitnesses.append(max_fitness)

        # Create the next generation
        new_population = []

        # Perform elitism by adding the best individual to the new population
        new_population.append(best_individual)

        # Perform crossover and mutation to create the rest of the new population
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            child = mutate(child, 0.5)
            new_population.append(child)

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
plt.title("Performance Comparison: GenTest vs. Classic Genetic Algorithm")
plt.legend()
plt.show()

print("Automated Test Cases (GenTest Genetic Algorithm):")
for i, test_case in enumerate(automated_test_cases_modified):
    print("Test Case", i+1, ":", test_case)
