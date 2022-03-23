import random as ra
import numpy as np


class Algorithm:
    def __init__(self, inputData):
        #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
        #ExampleData = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 234, 1.0, 0.123, 2334]
        self.Data = inputData
        self.population = [
        ]  #Storing current 'x' binary vectors (initialized and then survivors)
        self.populationDecimal = []  #Storing current 'x' decimal vectors
        self.currentMax = []  #Storing the best result
        self.currentMaxIndividuals = []

    def __initializePopulation(self):
        for _ in range(self.Data[5]):  #Population size
            self.x = []
            for dim in range(self.Data[0]):  #One x for each dimension
                searchedInt = pow(
                    2, self.Data[1][dim])  #Random values are initialized
                randomInt = (ra.randrange(-1 * searchedInt, searchedInt - 1))
                binary = np.binary_repr(randomInt, self.Data[1][dim] +
                                        1)  #Conversion into two's compliment
                self.x.append(binary)
            self.population.append(self.x)
        return

    def __crossover(self):
        #First we calculate fitness and based on it we do Roulette-wheel selection with scaling
        '''
        Performes the crossover operation in the algorithm.

        Pt - are points selected during the reproduction (selection), better points are selected with higher probability
        p_s - probability of selection of an individual
        q - fitness of the individual
        
        Roulette wheel selection - p_s(Pt_i) = q(Pt_i)/ sum of all q(Pt_k), for all k's
        '''
        sum_of_values = 0
        for i in self.population:
            #            sum_of_values += i  #look out for the case when sum = 0
            sum_of_values += 1  #look out for the case when sum = 0
        #important assumption (for now) -> it is assumed, that there are no negative or zero q(Pt_i)
        p_s = []  #table of all p_s(Pt_i)
        probability = 0
        for i in self.population:
            probability = 0  #just for dbg
            #            probability += i / sum_of_values #i is the vector:( of binary number - fix that
            p_s.append(probability)

        self.__ruletteWheel(
            p_s
        )  #I have no idea how many times we should choose, thus for now it will be just once

        #Then we perform Single Point crossover for those chosen fit
        self.__ruletteWheel(p_s)
        return

    def __ruletteWheel(self, p_s):
        '''
        Implementation of the roulette wheel selection.

        It takes the probability of selection of an individual as an input
        '''
        random = ra.random()  #choosing random float between 0 and 1
        selected_points = None
        for i in p_s:
            if random <= i:
                selected_points = self.population[p_s.index(i)]
                break
        return selected_points

    def __singlePointCrossover(self, selected_points):
        '''
        Performes the single point crossover on the given points
        '''
        pass

    def __mutation(self):
        #Perform mutation based on probability
        return

    def __survivorSelection(self):
        self.__convertBinaryComplimentToDecial(
        )  #We will operate on decimal numbers for function result calculation
        for popCount in range(self.Data[5]):  #Population size
            dec = self.populationDecimal[popCount]
            #Calculate current value - the higher the better
            result = np.matmul(np.matmul(np.transpose(dec), self.Data[2]), dec)
            result = result + np.matmul(np.transpose(self.Data[3]),
                                        dec) + self.Data[4]

            #DELETE THIS 2 LINES LATER - now just for testing
            self.currentMax = result
            self.currentMaxIndividuals = self.populationDecimal[popCount]
        #FIFO ???
        return

    def __returnResultToUser(self):
        print('Maximum value: ', self.currentMax)
        print('X values for maximum F(x): ', self.currentMaxIndividuals)
        return

    def __convertBinaryComplimentToDecial(self):
        self.populationDecimal = []
        for popCount in range(self.Data[5]):
            self.x = []
            for dim in range(self.Data[0]):
                decimal = int(self.population[popCount][dim], 2)
                maxInt = pow(2, self.Data[1][dim])
                if (
                        decimal > maxInt
                ):  #Two's compliment conversion for negative numbers. Honestly, I have no idea if there is a way to do it better.
                    decimal = decimal - maxInt * 2
                self.x.append(decimal)
            self.populationDecimal.append(self.x)
        return

    def __loopUntilTerminationCriterionReached(self):
        for _ in range(self.Data[8]):
            self.__crossover()
            self.__mutation()
            self.__survivorSelection()
        return

    def performGeneticAlgorithm(self):
        self.__initializePopulation()
        #print(self.population)
        self.__loopUntilTerminationCriterionReached()
        self.__returnResultToUser()
        return
