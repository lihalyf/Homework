# -*- coding: utf-8 -*-
def naivePrediction(lyst, k):
    # If the number of observations is less than or equal to k, return error message.
    if len(lyst) <= k:
        return str("Error: k should be less than the number of observations.")
    
    result = []     # result list to store absolute error of each case
    rain = 0 
    
    for i in range(len(lyst)):
        if i + k >= len(lyst):
            break     #break loop when i + k is out of index, which means all cases have been considered
        
        # Naïve time series forecasting
        sample = sum(lyst[i:i+k])  
        if sample >= k / 2:
            rain = 1
        else:
            rain = 0
        
        # Forecasting error
        absolute_error = abs(rain - lyst[i + k])
        result.append(absolute_error)
    
    MAE = sum(result) / len(result)
    
    return MAE

def main():    
    print(naivePrediction([1,0,1,0,1],2))    
    print(naivePrediction([1,0,1,0,1],3))    
    print(naivePrediction([1,0,1,0,1],5))    
    print(naivePrediction([1,0,1,0,1,1,1],3))    
    print(naivePrediction([1,0,1,0,1,1,1],4))
    
main()
    
        
            