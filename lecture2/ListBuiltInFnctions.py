list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4, 5]

print("len(list1)=", len(list1))
print("max(list1)=", max(list1))
print("min(list2)= ", min(list2))

# list(seq) used in tuple

sum1 = 0
for i in range(0, len(list1)):
    sum1 = sum1 + list1[i]
print("sum of list1 = ", sum1)

print("sum(lsit1) = ", sum(list1))

# index

print("list1.index(30) =", list1.index(30))


# sort in ascending order
list3 = [5, 1, 8, 4, 6]
print("list3.sort()=", list3.sort())

print("list3=", list3)

# sort in descinding order
list3 = [5, 1, 8, 4, 6]
print("list3.sort() desc=", list3.sort(reverse=True))

print("list3 after dec sort=", list3)

list3.remove(1)

print("list3=", list3)

# reverse

list3.reverse()

print("list3=", list3)
