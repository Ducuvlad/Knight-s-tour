# Knight-s-tour
Knight's tour problem solved with an evolutionary algorithm

Individuals are possible solutions to the problem and are represented here as permutations of tuples 
containing the possition of the chess board square ( X , Y ).
Individuals can generate two new offsprings by applying an ordered crossover on two individuals or mutate.
Each Individual has a fitness equal to the number of correct moves on the chess board pressent in the permutation.

The Population is a list of Individuals.The population multiplies and then executes a ranked select to return to original size.
This process repeats until a suitable answer is found.

The initial population is randomly generated.
Statistics show the number of iterations of the evolution process and the best Individual of each iteration.
