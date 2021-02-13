b = 20


def func(a):
    #b = 10
    a = a + 1
    a = a * b
    print("a inside function = ", a)


#list1 = [10, 20, 30, 40]
a = 10
func(a)

print("a outside function = ", a)
