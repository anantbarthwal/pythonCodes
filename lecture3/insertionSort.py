a = [7, 4, 3, 6, 8, 2]
print("original list: ", a)
for i in a:
    j = a.index(i)
    while j > 0:
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
        j = j - 1
print("sorted list: ", a)
print("type(a) : ", type(a))
