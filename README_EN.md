## Task 1  
Assume that we have a set of 10 genes, each of which can take a binary value (0 or 1). The fitness function is calculated as the number of genes with a value of 1 present in the chromosome. The greater the number of genes with a value of 1, the higher the level of fitness. Implement a genetic algorithm that will strive to maximize the fitness level of individuals in the population. Assume a population size of 10. In each generation, the two best-fit individuals from the entire population are selected and subjected to crossover operation, resulting in two offspring. They replace the two least fit individuals in the population. Additionally, with a 60% probability, a mutation may occur that involves changing the value of a random gene to the opposite, among the two best individuals.

## Task 2  
Write a program that uses a genetic algorithm to solve the equation $2a^2 + b = 33$, where $a, b ∈< 0, 15 >$. The chromosome should consist of 8 bits (4 bits each occupied by the value of variable a and b). The calculation of the fitness function should be based on the phenotype (values of variables a and b). Assume a population size of 10 individuals, in each generation a new population is selected using the roulette method, and then 50% of the individuals of this population undergo crossover, the offspring replaces one of the parents in the population. Each of the individuals of the new population can undergo mutation with a probability of 10%.

## Task 3 - Knapsack problem  
Write a program that will solve the knapsack problem using a genetic algorithm. The knapsack problem is often presented as a problem of a thief robbing a store - he found 10 items; the j-th item is worth vj and weighs wj. The thief strives to take with him the most valuable loot, but he cannot take more than 35 kilograms. He also cannot take a fractional part of the items (this would be possible in the continuous knapsack problem). The value of the fitness function will be calculated according to the following formula:  

![image](https://github.com/SelfishCrayfish/Basics-of-Genetic-Algorithms/assets/137427463/d5b37774-5f34-4c90-a5b5-041f8037a606)

where:  
• $n$ - length of the chromosome (corresponds to the number of all items in the store),  
• $c_i$ - value of the i-th gene (1 means that the item is packed into the bag, 0 that it is not),  
• $w_i$ - weight of the i-th item,  
• $v_i$ - value of the i-th item.  

Assume a population size of 8. During the implementation of the algorithm, use the principle of elitism, as a threshold assume 25% of individuals in the population. From the entire population, a temporary population is selected using the roulette method, and then there are crossovers between individuals, and the newly created individuals go to the new population. Additionally, each gene of each of the new individuals can undergo mutation with a probability of 5%. This means that the new population will consist of 25% of individuals from the previous population and 75% of offspring who can undergo mutation.  
Test the operation of your algorithm on a set of data presented in table 1. The optimal (probably) solution for this example is to choose things with numbers:
$0, 2, 3, 4, 5, 8$, the weight of the selected things is 32, and the value is 2222.  
| ID | Weight | Value |
| -- | ---- | ------- |
| 0 | 3 | 266 |
| 1 | 13 | 442 |
| 2 | 10 | 671 |
| 3 | 9 | 526 |
| 4 | 7 | 388 |
| 5 | 1 | 245 |
| 6 | 8 | 210 |
| 7 | 8 | 145 |
| 8 | 2 | 126 |
| 9 | 9 | 322 |
