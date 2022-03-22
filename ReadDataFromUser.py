#For aesthetic purposes
line = "-------------------------------------------------------------------"

class ReadData:
    def __init__(self):
        self.data = []

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

#D = ReadData()
#D.ReadFloatWithRange("test", 1, 2)