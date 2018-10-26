x = input("Enter the file name:")
y = input("Enter the manager name:")
f = open(x, 'r')
salary_file = f.read()
person_split = salary_file.split("\n")
text_split = []
for row in person_split:
    row = row.split(" ")
    text_split.append(row)
print("Month", "Qty", "Price", "Revenue")
count = 0
Manager_in = False
for i in range(len(text_split) - 1):
    if text_split[i][1] == y:
        Manager_in = True
        revenue = int(text_split[i][2]) * float(text_split[i][3])
        count += revenue
        print(text_split[i][0], text_split[i][2], text_split[i][3], str(revenue))
        
if Manager_in:
    print("Total revenue is", count)
else:
    print("N/A   N/A N/A  N/A")

     
    
