class Algorithm:
    def __init__(self, inputData):
        #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
        #ExampleData = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 234, 1.0, 0.123, 2334] 
        self.Data = inputData
        
    def __InitializePopulation(self):
        return 

    def PerformGeneticAlgorithm(self):
        self.__InitializePopulation()
        #HERE WE WILL PERFORM FURTHER PHASES OF THE ALGORITHM
        return