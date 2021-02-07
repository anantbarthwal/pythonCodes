list1 = [10, 8, 12, 2]
length = len(list1)

print("list1 = ", list1)

for i in range(length-1):
    for j in range(length - i - 1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print("list after sorting= ", list1)
