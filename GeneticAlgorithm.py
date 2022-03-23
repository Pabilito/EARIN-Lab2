import random as ra

class Algorithm:
    def __init__(self, inputData):
        #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
        #ExampleData = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 234, 1.0, 0.123, 2334] 
        self.Data = inputData
        self.population = []
        
    def __InitializePopulation(self):
        for _ in range(self.Data[5]):                     #Population size
            self.x = []
            for dim in range(self.Data[0]):                 #One x for each dimension
                searchedInt = pow(2, self.Data[1][dim])
                self.x.append(ra.randrange(-1*searchedInt, searchedInt-1))
            self.population.append(self.x)
        return 

    def PerformGeneticAlgorithm(self):
        self.__InitializePopulation()
        print(self.population)
        #HERE WE WILL PERFORM FURTHER PHASES OF THE ALGORITHM
        return