import numpy as np
def findOL(arryMatx):
    
    median = np.median(arryMatx, axis = 1)
    median_array = median.reshape(len(arryMatx), 1)
    element_comparision_with_median = np.absolute(arryMatx - median_array)
    outlier = np.argmax(element_comparision_with_median, axis = 1)
    
    return outlier

def main():    
    firstMatx = np.array([[10,3,2],[1,2,6]])   
    print(findOL(firstMatx))   
    
    thirdMatx = np.array([[1,10,2,8,5],[2,7,3,9,11],[19,2,1,1,5]])    
    print(findOL(thirdMatx))

main()

