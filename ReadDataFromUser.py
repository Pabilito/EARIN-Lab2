import numpy as np
#For aesthetic purposes
line = "-------------------------------------------------------------------"

class ReadData:
    def __init__(self):
        self.data = []
        self.range = []             #Integer range for each dimension
        self.maxD = 100             #I assume that 2^100 is enough range
        self.maxPop = 10000         #Max population and max number of iteration can be easilly changed here if needed.
        self.maxIter = 10000

    def __ReadInt(self, message):   #This method should not be needed elswere, so it is private
        while(1):
            print(line)
            print(message)
            retVal = input()
            try: # Is the input an int?
                retVal = int(retVal)
                self.data.append(retVal) #Store data to return
                return
            except:
                print('Number could not be accepted, choose again!')
                continue

    def __ReadIntWithRange(self, message, min, max, returnMode):
        while(1):
            print(line)
            print(message)
            retVal = input()
            try: # Is the input an int?
                retVal = int(retVal)
                if(retVal<min or retVal>max): #Check if number is in specified range
                    print('Number out of range, choose again!')
                    continue 
                if(returnMode): 
                    self.data.append(retVal) 
                    return
                else:
                    return retVal
            except:
                print('Number could not be accepted, choose again!')
                continue

    def __ReadFloat(self, message, returnMode):
        while(1):
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
    
    def __ReadFloatWithRange(self, message, min, max):
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
    
    def __ReadMatrixFromUser(self, message, rows, columns):   
        mat = np.empty([rows, columns])
        print(line)
        print(message)
        for i in range(rows):
            for j in range(columns):
                mat.itemset((i, j), self.__ReadFloat("Please write value for cell: [', i, '][', j, ']", 0))
        self.data.append(mat)

    def PerformReadingSequence(self):
        self.__ReadInt("Please provide dimensionality 'i' [int].")
        for dimension in range(self.data[0]):
            self.range.append(self.__ReadIntWithRange("Dimension {}. Please provide d>=1 [restricted int].\nProgram will not accept d greater than {}. If you need larger range, edit _init_.".format(dimension+1, self.maxD), 1, self.maxD, 0))
        self.data.append(self.range)
        self.__ReadMatrixFromUser("Reading matrix 'A'.", self.data[0], self.data[0])
        self.__ReadMatrixFromUser("Reading matrix 'b'.", self.data[0], 1)
        self.__ReadFloat("Please provide 'c' parameter [float]", 1)
        self.__ReadIntWithRange("Please provide population size [restricted int].\nProgram will not accept population greater than {}. If you need larger range, edit _init_.".format(self.maxPop), 1, self.maxPop, 1)
        self.__ReadFloatWithRange("Please provide crossover probability in range [0,1] [restricted float]", 0, 1)
        self.__ReadFloatWithRange("Please provide mutation probability in range [0,1] [restricted float]", 0, 1)
        self.__ReadIntWithRange("Please provide number of iterations [restricted int].\nProgram will not accept number greater than {}. If you need larger range, edit _init_.".format(self.maxIter), 1, self.maxIter, 1)
        return self.data