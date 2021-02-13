"""def subtraction(a, b=20, c=20):
    return a - b + c


a = 10
c = 20

print("sub = ", subtraction(a=10, c=30, b=50))"""

# variable length arguments


def func1(*n):
    sum = 0
    for i in n:
        sum = sum + i
    return sum


print("sum1 = ", func1(10, 20))
print("sum2= ", func1(10, 20, 30, 40, 50, 1, 2, 4, 5, 65, 6))
