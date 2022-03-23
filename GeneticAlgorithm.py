import random as ra
import numpy as np

class Algorithm:
    def __init__(self, inputData):
        #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
        #ExampleData = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 234, 1.0, 0.123, 2334] 
        self.Data = inputData
        self.population = []
        
    def __InitializePopulation(self):
        for _ in range(self.Data[5]):                               #Population size
            self.x = []
            for dim in range(self.Data[0]):                         #One x for each dimension
                searchedInt = pow(2, self.Data[1][dim])
                randomInt = (ra.randrange(-1*searchedInt, searchedInt - 1))
                binary = np.binary_repr(randomInt, self.Data[1][dim]+1)     #Conversion into two's compliment          
                self.x.append(binary)
            self.population.append(self.x)
        return 

    def __Crossover(self):
        return

    def __Mutation(self):
        return

    def __SurvivorSelection(self):
        return

    def __ReturnResultToUser(self):
        return

    def __LoopUntilTerminationCriterionReached(self):
        for _ in range(self.Data[8]):
            self.__Crossover()
            self.__Mutation()
            self.__SurvivorSelection()
        return

    def PerformGeneticAlgorithm(self):
        self.__InitializePopulation()
        print(self.population)
        self.__LoopUntilTerminationCriterionReached()
        self.__ReturnResultToUser()
        return