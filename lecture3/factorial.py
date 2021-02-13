"""num = 5
fact = 1
while num > 0:
    fact = fact * num
    num -= 1
print("fact = ", fact)"""


def factorail(num):
    if num == 0:
        return 1
    else:
      #  print("num in else = ", num)
        return num * factorail(num-1)


print("fact = ", factorail(5))
