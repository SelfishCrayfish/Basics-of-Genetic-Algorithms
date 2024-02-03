import random

import numpy as np


# Single-point crossover
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


class GeneticAlgorithm:
    def __init__(self, items, population_size=100, elite_threshold=0.25, mutation_probability=0.05):
        self.items = items
        self.population_size = population_size
        self.elite_threshold = elite_threshold
        self.mutation_probability = mutation_probability
        self.population = []

    # Creating a random population
    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            chromosome = np.random.choice([0, 1], len(self.items))
            self.population.append(chromosome)

    # If the weight of items is less or equal to 35, the items' value is returned. Otherwise, the function returns 0
    # (details explained in README)
    def calculate_fitness(self, chromosome):
        total_weight = np.sum(chromosome * [item['weight'] for item in self.items])
        if total_weight <= 35:
            return np.sum(chromosome * [item['value'] for item in self.items])
        else:
            return 0

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

    # Replacement mutation
    def mutate(self, individual):
        mutation_gene = np.random.randint(0, len(individual))
        individual[mutation_gene] = 1 - individual[mutation_gene]
        return individual

    def genetic_algorithm(self, generations=100):
        self.initialize_population()

        for generation in range(generations):
            # Elitism used on 25% of the population
            elite_population = sorted(self.population, key=self.calculate_fitness, reverse=True)
            elite_population = elite_population[:int(self.elite_threshold * self.population_size)]

            temporary_population = self.roulette()

            children = []
            # Crossovers occur between individuals in temporary population
            for i in range(0, len(temporary_population)-1, 2):
                parent1, parent2 = temporary_population[i], temporary_population[i+1]
                child1, child2 = crossover(parent1, parent2)
                children.append(child1)
                children.append(child2)

            # Mutation occurs randomly (5% chance by default)
            for child in children:
                if np.random.rand() < self.mutation_probability:
                    self.mutate(child)

            # Connecting elite population and children of temporary population
            children_point = int(self.population_size - (self.population_size * self.elite_threshold))
            self.population = (elite_population + children[:children_point])

            fitness_values = []
            for ch in self.population:
                fitness_values.append(self.calculate_fitness(ch))
            best_fitness = max(fitness_values)

            print(f"Generation {generation + 1}: Best Fitness - {best_fitness}")
            # Optimal solution is described in README
            if best_fitness == 2222:
                print("Optimal solution found.")
                break

        best_chromosome = max(self.population, key=self.calculate_fitness)

        selected_items = []
        for i, gene in enumerate(best_chromosome):
            # Gene equal to 1 means the item was put in the bag
            if gene == 1:
                selected_items.append(i)

        weights = []
        for i in selected_items:
            weights.append(self.items[i]['weight'])
        total_weight = np.sum(weights)

        values = []
        for i in selected_items:
            values.append(self.items[i]['value'])
        total_value = np.sum(values)

        print(f"Selected items: {selected_items}")
        print(f"Total weight: {total_weight}, Total value: {total_value}")


# Items described as the table in README says
items_data = [
    {'weight': 3, 'value': 266},
    {'weight': 13, 'value': 442},
    {'weight': 10, 'value': 671},
    {'weight': 9, 'value': 526},
    {'weight': 7, 'value': 388},
    {'weight': 1, 'value': 245},
    {'weight': 8, 'value': 210},
    {'weight': 8, 'value': 145},
    {'weight': 2, 'value': 126},
    {'weight': 9, 'value': 322}
]

plecak = GeneticAlgorithm(items_data)
plecak.genetic_algorithm()
