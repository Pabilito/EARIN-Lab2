import numpy as np
#For aesthetic purposes
line = "-------------------------------------------------------------------"

class ReadData:
    def __init__(self):
        self.data = []
        self.maxD = 100             #I assume that 2^100 is enough range
        self.maxPop = 10000         #Max population and max number of iteration can be easilly changed here if needed.
        self.maxIter = 10000

    def ReadInt(self, message):
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

    def ReadIntWithRange(self, message, min, max):
        while(1):
            print(line)
            print(message)
            retVal = input()
            try: # Is the input an int?
                retVal = int(retVal)
                if(retVal<min or retVal>max): #Check if number is in specified range
                    print('Number out of range, choose again!')
                    continue 
                self.data.append(retVal) 
                return
            except:
                print('Number could not be accepted, choose again!')
                continue

    def ReadFloat(self, message):
        while(1):
            print(line)
            print(message)
            retVal = input()
            try: # Is the input a float?
                retVal = float(retVal) 
                self.data.append(retVal)
                return
            except:
                print('Number could not be accepted, choose again!')
                continue
    
    def ReadFloatWithRange(self, message, min, max):
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

    def PerformReadingSequence(self):
        self.ReadInt("Please provide dimensionality [int].")
        self.ReadIntWithRange("Please provide d>=1 [restricted int].\nProgram will not accept d greater than {}. If you need larger range, edit _init_.".format(self.maxD), 1, self.maxD)
        #Read A
        #Read b
        self.ReadFloat("Please provide 'c' parameter [float]")
        self.ReadIntWithRange("Please provide population size [restricted int].\nProgram will not accept population greater than {}. If you need larger range, edit _init_.".format(self.maxPop), 1, self.maxPop)
        self.ReadFloatWithRange("Please provide crossover probability in range [0,1] [restricted float]", 0, 1)
        self.ReadFloatWithRange("Please provide mutation probability in range [0,1] [restricted float]", 0, 1)
        self.ReadIntWithRange("Please provide number of iterations [restricted int].\nProgram will not accept number greater than {}. If you need larger range, edit _init_.".format(self.maxIter), 1, self.maxIter)
        return self.data

D = ReadData()
D.PerformReadingSequence()