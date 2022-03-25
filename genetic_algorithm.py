import random as ra
import numpy as np


class Algorithm:
    def __init__(self, inputData):
        #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
        #ExampleData = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 234, 1.0, 0.123, 2334]
        data = inputData
        self.dimensionality = data[0]
        self.array_of_range = data[1]
        self.matrix_A = data[2]
        self.matrix_B = data[3]
        self.c = data[4]
        self.population_size = data[5]
        self.crossover_param = data[6]
        self.mutation_param = data[7]
        self.iterations = data[8]
        self.population = [
        ]  #Storing current 'x' binary vectors (initialized and then survivors)
        self.populationDecimal = []  #Storing current 'x' decimal vectors
        self.currentMax = []  #Storing the best result
        self.currentMaxIndividuals = []

    def __initializePopulation(self):
        for _ in range(self.population_size):  #Population size
            self.x = []
            for dim in range(self.dimensionality):  #One x for each dimension
                searchedInt = pow(
                    2,
                    self.array_of_range[dim])  #Random values are initialized
                randomInt = (ra.randrange(-1 * searchedInt, searchedInt - 1))
                binary = np.binary_repr(randomInt, self.array_of_range[dim] +
                                        1)  #Conversion into two's compliment
                self.x.append(binary)
            self.population.append(self.x)
        self.__assignFirstMax()
        return

    def __assignFirstMax(self): #To later avoid comparison with nonexistent value
        self.__convertBinaryComplimentToDecimal()
        #Calculate the first value, it will be our first max
        self.currentMax = self.__calculateF(self.populationDecimal[0])
        return

    def __fitness(self):
        '''
        Calculates the fitness function values.

        The best points are those one which are the closest to the maxima - the bigger the better ( ͡°͜ʖ ͡°).
        Hence, in order to give a score first of all values of all x are being calculated, and then the score will
        be given in order of values

        returns the list of [x's, x_{10}, weight] pairs

        x_{10} - is the decimal notation
        '''
        values = []
        self.__convertBinaryComplimentToDecimal(
        )  #We will operate on decimal numbers for function result calculation
        for popCount in range(self.population_size):  #Population size
            dec = self.populationDecimal[popCount]
            values.append(
                [self.population[popCount], dec,
                 self.__calculateF(dec)])
        values.sort(key=lambda l: l[2]
                    )  #sorting [x's, x_{10}, values] pairs ascending by values
        #the better the result, the higher point it gets
        for i in range(len(values)):
            values[i][2] = i
        return values

    def __crossover(self):
        #First we calculate fitness and based on it we do Roulette-wheel selection with scaling
        '''
        Performes the crossover operation in the algorithm.

        Parameter pc is the probability of crossover (??? roulette wheel selection doesn't require such thing I believe).

        Pt - are points selected during the reproduction (selection), better points are selected with higher probability
        p_s - probability of selection of an individual
        q - fitness of the individual
        
        Roulette wheel selection - p_s(Pt_i) = q(Pt_i)/ sum of all q(Pt_k), for all k's
        '''
        fit_function = self.__fitness()
        sum_of_values = 0
        for i in fit_function:
            #            sum_of_values += i  #look out for the case when sum = 0
            sum_of_values += i[2]  #look out for the case when sum = 0
        #important assumption (for now) -> it is assumed, that there are no negative or zero q(Pt_i)
        probability = 0
        p_s = []
        for i in fit_function:
            probability += i[2] / sum_of_values
            p_s.append(probability)

        first = self.__ruletteWheel(p_s, fit_function)
        second = self.__ruletteWheel(p_s, fit_function)
        #Then we perform Single Point crossover for those chosen fit
        new_first, new_second = self.__singlePointCrossover(first, second)
        self.population[self.population.index(first)] = new_first
        self.population[self.population.index(second)] = new_second

        return

    def __ruletteWheel(self, p_s, fit_function):
        '''
        Implementation of the roulette wheel selection.

        It takes the probability of selection of an individual as an input

        returns the points that are chosen
        '''
        new_population = fit_function
        random = ra.random()  #choosing random float between 0 and 1
        selected_points = None
        for i in range(len(p_s)):
            if random <= p_s[i]:
                selected_points = new_population[i][0]
                break
        return selected_points

    def __singlePointCrossover(self, first, second):
        '''
        Performes the single point crossover on the given points
        '''
        new_first = []
        new_second = []
        for dim in range(self.dimensionality):
            swap_range = len(first[dim])
            if len(first[dim]) > len(second[dim]):
                swap_range = len(second[dim])
            point = ra.randint(1, swap_range)
            new_first.append(first[dim][:point] + second[dim][point:])
            new_second.append(second[dim][:point] + first[dim][point:])
        return new_first, new_second

    def __mutation(self):
        #Perform mutation based on probability
        
        for i in range(self.population_size):                                   #Population size
            for j in range(self.dimensionality):
                for k in range(self.array_of_range[j]+1):                       #1 more bit for sign 
                    if(ra.random() > self.mutation_param):                      #choosing random float between 0 and 1
                        '''HERE will be mutation itself
                        print(self.population[i][j][k])
                        self.population[i][j][k] = str(1-int(self.population[i][j][k]))   #Bit swap: 1-0=1, 1-1=0
                        print(self.population[i][j][k]) 
                        '''
                quit()
        
        return

    def __calculateF(self, dec):
        '''
        Calculates the function value at given point

        dec - given population member in the decimal notation
        '''
        result = np.matmul(np.matmul(np.transpose(dec), self.matrix_A), dec)
        result += np.matmul(np.transpose(self.matrix_B), dec) + self.c
        return result

    def __survivorSelection(self):
        self.__convertBinaryComplimentToDecimal(
        )  #We will operate on decimal numbers for function result calculation
        for popCount in range(self.population_size):  #Population size
            dec = self.populationDecimal[popCount]
            #Calculate current value - the higher the better
            result = self.__calculateF(dec)
            #Store the best result
            if(result > self.currentMax):
                self.currentMax = result
                self.currentMaxIndividuals = self.populationDecimal[popCount]
        #FIFO means that we take data generated during mutation and crossover for the next phase

        #self.__returnResultToUser()
        return

    def __returnResultToUser(self):
        print('Maximum value: ', self.currentMax)
        print('X values for maximum F(x): ', self.currentMaxIndividuals)
        return

    def __convertBinaryComplimentToDecimal(self):
        self.populationDecimal = []
        for popCount in range(self.population_size):
            self.x = []
            for dim in range(self.dimensionality):
                decimal = int(self.population[popCount][dim], 2)
                maxInt = pow(2, self.array_of_range[dim])
                if (
                        decimal > maxInt
                ):  #Two's compliment conversion for negative numbers. Honestly, I have no idea if there is a way to do it better.
                    decimal = decimal - maxInt * 2
                self.x.append(decimal)
            self.populationDecimal.append(self.x)
        return

    def __loopUntilTerminationCriterionReached(self):
        for _ in range(self.iterations):
            self.__crossover()
            self.__mutation()
            self.__survivorSelection()
        return

    def performGeneticAlgorithm(self):
        self.__initializePopulation()
        self.__loopUntilTerminationCriterionReached()
        self.__returnResultToUser()
        return
