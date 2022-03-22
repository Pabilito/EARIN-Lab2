from ReadDataFromUser import ReadData
#import numpy as np

def Main():
    A = ReadData().PerformReadingSequence()
    #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
    # A = [2, [4, 5], np.array([[1., 2.],[3., 4.]]), np.array([[1.],[2.]]), 435.0, 234, 1.0, 0.123, 2334] 
    # Exeplary data - uncomment numpy import to use
    print(A)
    return

Main()

#TO DO
#Sprawdzić czy A musi być Positive Definite