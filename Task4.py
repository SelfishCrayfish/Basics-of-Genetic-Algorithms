import random
import numpy as np


# Two-point crossover, necessary for the traveling salesman problem as the cities shouldn't appear more than once
# in the solution
def order_crossover(parent1, parent2):
    point1 = random.randint(0, len(parent1) - 1)
    point2 = random.randint(point1 + 1, len(parent1))

    child1, child2 = [-1] * len(parent1), [-1] * len(parent2)

    child1[point1:point2] = parent1[point1:point2]
    child2[point1:point2] = parent2[point1:point2]

    cities1 = []
    for city in parent2:
        if city not in child1:
            cities1.append(city)

    cities2 = []
    for city in parent1:
        if city not in child2:
            cities2.append(city)

    index1 = 0
    index2 = 0
    for i in range(len(parent1)):
        if child1[i] == -1:
            child1[i] = cities1[index1]
            index1 += 1
        if child2[i] == -1:
            child2[i] = cities2[index2]
            index2 += 1

    return child1, child2


class GeneticAlgorithm:
    def __init__(self, cities, population_size=100, elite_threshold=0.2, mutation_probability=0.01):
        self.cities = cities
        self.population_size = population_size
        self.elite_threshold = elite_threshold
        self.mutation_probability = mutation_probability
        self.population = []

    # Creating a random population
    def initialize_population(self):
        self.population = []
        for i in range(self.population_size):
            chromosome = np.random.permutation(len(self.cities))
            self.population.append(chromosome)

    # Function calculates the total distance between each city in the order that chromosome describes
    # and returns the chromosome's fitness (1/total_distance)
    def calculate_fitness(self, chromosome):
        total_distance = 0
        for i in range(len(chromosome) - 1):
            city1, city2 = chromosome[i], chromosome[i + 1]
            total_distance += np.sqrt((self.cities[city2]['x'] - self.cities[city1]['x']) ** 2 +
                                      (self.cities[city2]['y'] - self.cities[city1]['y']) ** 2)
        total_distance += np.sqrt((self.cities[chromosome[-1]]['x'] - self.cities[chromosome[0]]['x']) ** 2 +
                                  (self.cities[chromosome[-1]]['y'] - self.cities[chromosome[0]]['y']) ** 2)
        return 1 / total_distance

    # Roulette method for determining a temporary population
    def roulette(self):
        fitness_values = []
        for chromosome in self.population:
            fitness_values.append(self.calculate_fitness(chromosome))

        normalised_fitness = []
        for fitness in fitness_values:
            normalised_fitness.append(fitness / np.sum(fitness_values))

        temporary_population = []
        for i in random.choices(range(len(self.population)), weights=normalised_fitness, k=len(self.population)):
            temporary_population.append(self.population[i])
        return temporary_population

    # Swap mutation
    def mutate(self, chromosome):
        index1 = random.randint(0, len(chromosome) - 1)
        index2 = random.randint(0, len(chromosome) - 1)
        temp = chromosome[index1]
        chromosome[index1] = chromosome[index2]
        chromosome[index2] = temp

    def genetic_algorithm(self, generations=4000):
        self.initialize_population()

        for generation in range(generations):
            # Elitism used on 20% of the population
            elite_population = sorted(self.population, key=self.calculate_fitness, reverse=True)
            elite_population = elite_population[:int(self.elite_threshold * self.population_size)]

            temporary_population = self.roulette()

            children = []
            # Crossovers occur between individuals in temporary population
            for i in range(0, len(temporary_population) - 1, 2):
                parent1, parent2 = temporary_population[i], temporary_population[i+1]
                child1, child2 = order_crossover(parent1, parent2)
                children.append(child1)
                children.append(child2)

            # Mutation occurs randomly (1% chance by default)
            for child in children:
                if np.random.rand() < self.mutation_probability:
                    self.mutate(child)

            # Connecting elite population and children of temporary population
            children_point = int(self.population_size - (self.population_size * self.elite_threshold))
            self.population = (elite_population + children[:children_point])

            fitness_values = []
            for i in self.population:
                fitness_values.append(self.calculate_fitness(i))
            best_fitness = max(fitness_values)

            print(f"Generation {generation + 1}: Best Fitness - {(1 / best_fitness):.2f}")
            # Optimal (though the program occasionally finds a shorter route) solution is described in README
            # if (1/best_fitness) <= 869:
            #     print("Optimal solution found.")
            #     break

        best_chromosome = max(self.population, key=self.calculate_fitness)

        print(f"Best route found: {best_chromosome}")
        total_distance = 1 / self.calculate_fitness(best_chromosome)
        print(f"Total distance: {total_distance:.2f}")


# Cities described as the table in README says
cities_data = [
    {'x': 119, 'y': 38},
    {'x': 37, 'y': 38},
    {'x': 197, 'y': 55},
    {'x': 85, 'y': 165},
    {'x': 12, 'y': 50},
    {'x': 100, 'y': 53},
    {'x': 81, 'y': 142},
    {'x': 121, 'y': 137},
    {'x': 85, 'y': 145},
    {'x': 80, 'y': 197},
    {'x': 91, 'y': 176},
    {'x': 106, 'y': 55},
    {'x': 123, 'y': 57},
    {'x': 40, 'y': 81},
    {'x': 78, 'y': 125},
    {'x': 190, 'y': 46},
    {'x': 187, 'y': 40},
    {'x': 37, 'y': 107},
    {'x': 17, 'y': 11},
    {'x': 67, 'y': 56},
    {'x': 78, 'y': 133},
    {'x': 87, 'y': 23},
    {'x': 184, 'y': 197},
    {'x': 111, 'y': 12},
    {'x': 66, 'y': 178},
]

salesman = GeneticAlgorithm(cities_data)
salesman.genetic_algorithm()
