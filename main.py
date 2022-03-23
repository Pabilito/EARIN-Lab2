from ReadDataFromUser import ReadData
from GeneticAlgorithm import Algorithm
import numpy as np

def Main():
    ### Test data ###
    #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
    DataFromUser = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 10, 1.0, 0.123, 2334] 
    # Exeplary data - uncomment numpy import to use

    # DataFromUser = ReadData().PerformReadingSequence()   #Uncomment later
    Algorithm(DataFromUser).PerformGeneticAlgorithm()

    return

Main()