str1 = "hellocomputer234"
str2 = "world"
"""print("str1 = ", str1)
print("str2 = ", str2)

print("str1 + str2 = ", str1 + str2)

print("str1**str2 = ", str1*5)

print(" h in str1 = ", 's' in str1)

print("range = ", str1[4:2: -1])

print("slice = ", str2[2:4])

str3 = str2[2:4]
print("str3 = ", str3)"""

# build in functions in string

"""
print("isalpha", str1.isalpha())
str1 = "1234"
print("isdigit", str1.isdigit())
"""

"""
str1 = input("enter any string = ")

if str1.isdigit():
    y = int(str1)
    print("integer")
else:
    y = str1
    print("string")

"""
"""
str1 = "ABCDEF"
print("lower", str1.lower())
"""

# upper
# islower\
# isupper
str1 = "         abcd      "
str2 = "hello"
print("str1+str2=", str1+str2)
print("str1+ str2=", str1.rstrip()+str2)

str3 = "      "
print("isspace", str3.isspace())

# join

str4 = "2345"
s = '-'
print("join", s.join(str4))

str5 = "alp@habeta@gmail.com@puter"
print("partition", str5.partition('@'))


print("split", str5.split('@'))
