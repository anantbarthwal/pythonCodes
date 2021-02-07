dict1 = {'Subject': 'computer science', 'class': 12}

"""
print(dict1['Subject'])

print("dic1[class]", dict1['class'])


student1 = {'name': 'abhishek', 'class': 12, 'school': 'DIS'}

print(student1['school'])

schoolName = student1['school']
print(schoolName)"""

for i in dict1:
    print(dict1[i])


dict1['class'] = 11

print("dict1['class'] = ", dict1['class'])


print("len(dict1)= ", len(dict1))

str1 = str(dict1)

print(str1)

print(str1[2])

print(dict1.items())

print(dict1.values())

print(dict1.keys())
