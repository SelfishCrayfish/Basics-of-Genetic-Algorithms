import numpy as np


# The more genes equal to 1, the better the fitness
def calculate_fitness(individual):
    return np.sum(individual)


class GeneticAlgorithm:
    def __init__(self, gene_count_arg, population_size_arg):
        self.gene_count = gene_count_arg
        self.population_size = population_size_arg
        self.population = self.initialize_population()

    # Creating a random population
    def initialize_population(self):
        return np.random.choice([0, 1], size=(self.population_size, self.gene_count))

    # Choosing two best fit individuals for crossover
    def select_parents(self):
        fitness_values = []
        for individual in self.population:
            fitness_values.append(calculate_fitness(individual))
        sorted_indices = np.argsort(fitness_values)[::-1]
        return self.population[sorted_indices[:2]]

    # Single-point crossover
    def crossover(self, parent1_arg, parent2_arg):
        crossover_point = np.random.randint(1, self.gene_count - 1)
        child1 = np.concatenate((parent1_arg[:crossover_point], parent2_arg[crossover_point:]))
        child2 = np.concatenate((parent2_arg[:crossover_point], parent1_arg[crossover_point:]))
        return child1, child2

    # Replacement mutation
    def mutate(self, individual):
        mutation_gene = np.random.randint(0, self.gene_count)
        individual[mutation_gene] = 1 - individual[mutation_gene]
        return individual

    def genetic_algorithm(self, generations_arg):
        for generation in range(generations_arg):
            parents = self.select_parents()
            offspring1, offspring2 = self.crossover(parents[0], parents[1])

            # 60% mutation chance
            if np.random.rand() < 0.6:
                offspring1 = self.mutate(offspring1)
            if np.random.rand() < 0.6:
                offspring2 = self.mutate(offspring2)

            # Calculating fitness for each individual
            fitness_values = []
            for individual in self.population:
                fitness_values.append(calculate_fitness(individual))

            # Two individuals with the worst fitness are replaced by the two offsprings
            least_fit_indices = np.argsort(fitness_values)[:2]
            self.population[least_fit_indices[0]] = offspring1
            self.population[least_fit_indices[1]] = offspring2

            best_fitness = max(fitness_values)
            print(f"Generation {generation + 1}: Best Fitness - {best_fitness}")
            if best_fitness == 10:
                break


if __name__ == "__main__":
    gene_count = 10
    population_size = 10
    generations = 50

    genetic_algorithm = GeneticAlgorithm(gene_count, population_size)
    genetic_algorithm.genetic_algorithm(generations)
