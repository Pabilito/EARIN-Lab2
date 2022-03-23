import random as ra
import numpy as np

class Algorithm:
    def __init__(self, inputData):
        #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
        #ExampleData = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 234, 1.0, 0.123, 2334] 
        self.Data = inputData
        self.population = []                #Storing current 'x' binary vectors
        self.populationDecimal = []         #Storing current 'x' decimal vectors
        self.currentMax = []                #Storing the best result
        self.currentMaxIndividuals = []
        
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
        #First we calculate fitness and based on it we do Roulette-wheel selection with scaling


        #Then we perform Single Point crossover for those chosen fit
        return

    def __Mutation(self):
        return

    def __SurvivorSelection(self):
        self.__ConvertBinaryComplimentToDecial()                           #We will operate on decimal numbers for function result calculation
        for popCount in range(self.Data[5]):                               #Population size
            dec = self.populationDecimal[popCount]
            #Calculate current value - the higher the better
            result = np.matmul(np.matmul(np.transpose(dec), self.Data[2]), dec)
            result = result + np.matmul(np.transpose(self.Data[3]), dec) + self.Data[4] 

            #DELETE THIS 2 LINES LATER
            self.currentMax = result   
            self.currentMaxIndividuals = self.populationDecimal[popCount] 
        #FIFO ???
        return

    def __ReturnResultToUser(self):
        print('Maximum value: ', self.currentMax)
        print('X values for maximum F(x): ', self.currentMaxIndividuals)
        return

    def __ConvertBinaryComplimentToDecial(self):
        self.populationDecimal = []
        for popCount in range(self.Data[5]):
            self.x = []
            for dim in range(self.Data[0]):
                decimal = int(self.population[popCount][dim], 2)
                maxInt = int(pow(2, self.Data[1][dim]))
                if(decimal > maxInt):   #Two's compliment conversion. Honestly, I have no idea how to do it better.
                    decimal = decimal - maxInt*2            
                self.x.append(decimal)
            self.populationDecimal.append(self.x)    
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