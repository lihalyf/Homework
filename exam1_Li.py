# Question 1

lyst = ['THE',  'ITEM',  'THE',  'THAT',  'THE',  'ITEM',  'ITEM',  'IN',  'THIS',  'LINE', 'OF', 'THE',  'IS',  'ITEM',  'THIS',  'THIS',  'OUTPUT',  'CONSISTS',  'OF', 'ITEM']

k = str(input("Enter k: "))

theDictionary = {}
for word in lyst:
    freq = theDictionary.get(word, None)
    if freq == None:    # number entered for the first time
        theDictionary[word] = 1
    else:	        # number already seen, increment its freq
        theDictionary[word] = freq + 1

freqList = theDictionary.values()
freqList = sorted(freqList)
kFreqList = []
lastIndex = min(int(k) + 1, len(freqList) + 1)
for i in range(1, lastIndex):
    kFreqList.append(freqList[-i])

kFreqDictionary = {}
for key in theDictionary:
    if theDictionary[key] in kFreqList:
        kFreqDictionary[key] = theDictionary[key]
 
print("words with the "+k+" highest frequencies;")
print(kFreqDictionary)



# Question 2

# x is a list of values.
# s is the number of smallest values to be trimmed
# l is the number of largest values to be trimmed
 

def trimmedMean(x, s, l): 
  # Write your code here
    if len(x) < s + l + 1:
        return("Not enough observations. The data can't be trimmed as requested")
    sorted_list = sorted(x)
    for i in range(s):
        sorted_list.pop(0)
    for j in range(l):
        sorted_list.pop()
    result = sum(sorted_list) / len(sorted_list)
    return result
    
# Test Case for Question 2
lyst = [1, 7, 3, 2, 5, 0.5, 9, 10]
print(trimmedMean(lyst,1,2))

lystNone = [0,1]
print(trimmedMean(lystNone,1,1))


