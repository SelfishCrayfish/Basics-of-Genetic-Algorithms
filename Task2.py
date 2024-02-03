import numpy as np


# 8 bits per chromosome - 4 reserved for 'a', 4 reserved for 'b'
def decode_chromosome(chromosome):
    # Function decodes and returns 'a' and 'b' in decimal
    a_bits = chromosome[:4]
    b_bits = chromosome[4:]
    a = int(''.join(map(str, a_bits)), 2)
    b = int(''.join(map(str, b_bits)), 2)
    return a, b


def calculate_fitness(chromosome):
    # Function calculates fitness based on the solution of quadratic equation 2a^2 + b = 33
    a, b = decode_chromosome(chromosome)
    equation_result = 2 * a ** 2 + b
    fitness = 1 / (abs(equation_result - 33) + 1)  # +1 to avoid dividing by zero
    return fitness


class GeneticAlgorithm:
    def __init__(self, gene_count_arg, population_size_arg, generations_arg, mutation_probability_arg):
        self.gene_count = gene_count_arg
        self.population_size = population_size_arg
        self.generations = generations_arg
        self.mutation_probability = mutation_probability_arg
        self.population = self.initialize_population()

    # Creating a random population
    def initialize_population(self):
        return np.random.randint(0, 2, size=(self.population_size, self.gene_count))

    # Choosing two best fit individuals for crossover
    def select_parents(self):
        fitness_values = []
        for individual in self.population:
            fitness_values.append(calculate_fitness(individual))
        sorted_indices = np.argsort(fitness_values)[::-1]
        return self.population[sorted_indices[:2]]

    # Single-point crossover, but with only one offspring
    def crossover(self, parent1, parent2):
        crossover_point = np.random.randint(1, self.gene_count - 1)
        child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        return child

    # Replacement mutation
    def mutate(self, individual):
        mutation_gene = np.random.randint(0, self.gene_count)
        individual[mutation_gene] = 1 - individual[mutation_gene]
        return individual

    # Roulette method
    def roulette(self):
        fitness_values = np.empty(self.population_size)
        for i, chromosome in enumerate(self.population):
            fitness_values[i] = calculate_fitness(chromosome)
        fitness_values = np.array(fitness_values)
        normalized_fitness = fitness_values / np.sum(fitness_values)
        selected = np.random.choice(range(self.population_size), p=normalized_fitness)

        return self.population[selected]

    def genetic_algorithm(self):
        for generation in range(self.generations):
            new_population = np.zeros_like(self.population)

            # Using roulette method for determining new population
            for i in range(self.population_size):
                individual = self.roulette()
                new_population[i] = individual

            # Choosing 50% of the population to be crossovererd
            to_be_crossovered = np.random.choice([0, 1], self.population_size, replace=True, p=[0.5, 0.5])
            for i in range(self.population_size):
                if to_be_crossovered[i] == 1:
                    parents = self.select_parents()
                    offspring = self.crossover(parents[0], parents[1])

                    # Offspring replaces one of the parents (50/50)
                    if np.random.rand() < 0.5:
                        parents[0] = offspring
                    else:
                        parents[1] = offspring

                # Mutation occurs randomly (10% chance by default)
                if np.random.rand() < self.mutation_probability:
                    new_population[i] = self.mutate(new_population[i])

            self.population = new_population

            fitness_values = []
            for chromosome in self.population:
                fitness_values.append(calculate_fitness(chromosome))
            best_fitness = max(fitness_values)
            print(f"Generation {generation + 1}: Best fitness: {best_fitness}")

            if best_fitness == 1:
                a, b = decode_chromosome(
                    self.population[np.argmax([calculate_fitness(ch) for ch in self.population])])
                print(f"Solution found: a = {a}, b = {b}")
                break


if __name__ == "__main__":
    gene_count = 8
    population_size = 10
    generations = 100
    mutation_probability = 0.1

    equation_solver = GeneticAlgorithm(gene_count, population_size, generations, mutation_probability)
    equation_solver.genetic_algorithm()
