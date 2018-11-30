import pandas as pd
import numpy as np

class dataByGroup(object):
    
    def __init__(self, dat, group):
        #write your code
        # __init__ should initialize three object attributes      
        # _dat, _group, _isBinary
        self._dat = dat
        self._group = group
    
    def __str__(self):
        #write your code
        return str(pd.concat([self._dat, self._group], axis=1))
    
    def isBinary(self):
        isBin = True
        for i in range(0,len(self._dat)):
            if self._dat[i] not in [0,1] and np.isnan(self._dat[i]) == False:
                isBin = False
                break
        return isBin
        
    
    def getNumMissings(self):
        return (self._dat.shape[0] - self._dat.count())

class numericDataByGroup(dataByGroup):    
    def __init__(self,dat, group):        
        #write your code  
        super(numericDataByGroup,self).__init__(dat, group)
    
    def getMeans(self):
        #write your code
        return self._dat.groupby(self._group).mean()
    
    def getSTD(self):
        #write your code
        return self._dat.groupby(self._group).std()

class categoricalDataByGroup(dataByGroup):    
    def __init__(self,dat, group):        
        #write your code
        super(categoricalDataByGroup,self).__init__(dat, group)
    
    def getTallies(self):
        #write your code
        return self._dat.groupby(self._group).value_counts()
        

#Testing Case
def main():       
    titanic = pd.read_csv("titanic3.csv")        
    survivedByPclass = categoricalDataByGroup(titanic['survived'],titanic['pclass'])   
    print("Data and Group: ")     
    print(survivedByPclass)   
    ## __str__  is invoked    
    print("Is the data binary? : "+str(survivedByPclass.isBinary()))     
    print("The number of missing values : "+str(survivedByPclass.getNumMissings()))      
    print("Tallies: ")     
    print(survivedByPclass.getTallies()) 
    
def main2():  
    titanic = pd.read_csv("titanic3.csv")      
    ageBySurvived = numericDataByGroup(titanic['age'],titanic['survived'])    
    print("Data and Group: ")     
    print(ageBySurvived)  ## __str__  is invoked    
    print("Is the data binary? : "+str(ageBySurvived.isBinary()))     
    print("The number of missing values : "+str(ageBySurvived.getNumMissings()))      
    print("Means: ")     
    print(ageBySurvived.getMeans())    
    print("Standard Deviations: ")         
    print(ageBySurvived.getSTD())    

main()
main2()