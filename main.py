from read_data_from_user import ReadData
from genetic_algorithm import Algorithm
#import numpy as np

def Main():

    '''
    ### Test data ###
    #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
    DataFromUser = [
        2, [5, 6],
        np.array([[-1., -2.], [-3., -4.]]),
        np.array([[1.], [2.]]), 435.0, 100, 0.6, 0.123, 212
    ]
    # Exemplary data - uncomment numpy import to use
    '''

    DataFromUser = ReadData().performReadingSequence()
    Algorithm(DataFromUser).performGeneticAlgorithm()

    return

Main()
