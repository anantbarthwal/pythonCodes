def addition(num1, num2):
    return product(num1, num2)
    # return num1 + num2


def subtraction(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


def product(num1, num2):
    return num1*num2


number1 = int(input("enter first number= "))
number2 = int(input("enter second number= "))

print("addition", addition(number1, number2))
print("subtraction", subtraction(number1, number2))
