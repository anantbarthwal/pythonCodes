tup1 = (2, 3, 4, 5)

""""
for i in range(0, len(tup1)):
    print(tup1[i]*2)
"""
"""
print(tup1[1:4])

list1 = list(tup1)

print(list1)

list1[1] = 10

print(list1)

tup2 = tuple(list1)

print(tup2)
"""
"""
rollNumbers = [1, 2, 3, 4]
print("rollNumbers", rollNumbers)

"""

rollNumbers = [1, 2, 3, 4]

newRollNumber = 5

flag = False

for i in range(0, len(rollNumbers)):
    if(rollNumbers[i] == newRollNumber):
        flag = True
        break

if flag == False:
    rollNumbers.append(newRollNumber)
print("rollNumbers = ", rollNumbers)
