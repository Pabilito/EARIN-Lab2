import numpy as np
#For aesthetic purposes
line = "-------------------------------------------------------------------"


class ReadData:
    def __init__(self):
        self.data = []
        self.range = []  #Integer range for each dimension
        self.maxD = 100  #I assume that 2^100 is enough range
        self.maxPop = 10000  #Max population and max number of iteration can be easilly changed here if needed.
        self.maxIter = 10000

    def __readInt(
            self, message
    ):  #This method should not be needed elswere, so it is private
        while (1):
            print(line)
            print(message)
            retVal = input()
            try:  # Is the input an int?
                retVal = int(retVal)
                self.data.append(retVal)  #Store data to return
                return
            except:
                print('Number could not be accepted, choose again!')
                continue

    def __readIntWithRange(self, message, min, max, returnMode):
        while (1):
            print(line)
            print(message)
            retVal = input()
            try:  # Is the input an int?
                retVal = int(retVal)
                if (retVal < min or
                        retVal > max):  #Check if number is in specified range
                    print('Number out of range, choose again!')
                    continue
                if (returnMode):
                    self.data.append(retVal)
                    return
                else:
                    return retVal
            except:
                print('Number could not be accepted, choose again!')
                continue

    def __readFloat(self, message, returnMode):
        while (1):
            print(line)
            print(message)
            retVal = input()
            try: # Is the input a float?
                retVal = float(retVal)
                if(returnMode): 
                    self.data.append(retVal)
                    return
                else:
                    return retVal
            except:
                print('Number could not be accepted, choose again!')
                continue
    
    def __readFloatWithRange(self, message, min, max):
        while(1):
            print(line)
            print(message)
            retVal = input()
            try: # Is the input a float?
                retVal = float(retVal)
                if(retVal<min or retVal>max):
                    print('Number out of range, choose again!')
                    continue 
                self.data.append(retVal)
                return
            except:
                print('Number could not be accepted, choose again!')
                continue
    
    def __readMatrixFromUser(self, message, rows, columns):   
        mat = np.empty([rows, columns])
        print(line)
        print(message)
        for i in range(rows):
            for j in range(columns):
                mat.itemset((i, j), self.__readFloat("Please write value for cell: [{}][{}].".format(i, j), 0))
        self.data.append(mat)

    def performReadingSequence(self):
        #Order is: Dimensionality, Array of Range, Matrix A, Matrix B, c, Population size, Crossover, Mutation, Iterations
        self.__readInt("Please provide dimensionality 'i' [int].")
        for dimension in range(self.data[0]):
            self.range.append(self.__readIntWithRange("Dimension {}. Please provide d>=1 [restricted int].\nProgram will not accept d greater than {}. If you need larger range, edit _init_.".format(dimension+1, self.maxD), 1, self.maxD, 0))
        self.data.append(self.range)
        self.__readMatrixFromUser("Reading matrix 'A'.", self.data[0], self.data[0])
        self.__readMatrixFromUser("Reading matrix 'b'.", self.data[0], 1)
        self.__readFloat("Please provide 'c' parameter [float].", 1)
        self.__readIntWithRange("Please provide population size [restricted int].\nProgram will not accept population greater than {}. If you need larger range, edit _init_.".format(self.maxPop), 1, self.maxPop, 1)
        self.__readFloatWithRange("Please provide crossover probability in range [0,1] [restricted float].", 0, 1)
        self.__readFloatWithRange("Please provide mutation probability in range [0,1] [restricted float].", 0, 1)
        self.__readIntWithRange("Please provide number of iterations [restricted int].\nProgram will not accept number greater than {}. If you need larger range, edit _init_.".format(self.maxIter), 1, self.maxIter, 1)
        return self.data
