import pandas as pd
def generateNumericSummary(dat, group):
    #write your code
    std = pd.groupby(dat, group).std()
    nums_missing = dat.shape[0] - dat.count()
    means = pd.groupby(dat, group).mean()

    dic = {'std' : std, 'numMissing' : nums_missing, 'mean' : means}
    
    return dic
    
    
#Test Cases    
titanic = pd.read_csv("titanic3.csv")
result1 = generateNumericSummary(titanic['age'],titanic['survived'])
print(result1)

result2 = generateNumericSummary(titanic['fare'],titanic['survived']) 
print("Number of missing values of 'fare' is "+str(result2['numMissing']))
print("mean 'fare' by 'survived':") 
print(result2['mean'])
print("standard deviation of 'fare' by 'survived':") 
print(result2['std'])

result3 = generateNumericSummary(titanic['age'],titanic['pclass'])
print(result3)