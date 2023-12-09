"""
A string is a data structure in Python that represents a sequence of characters. 
It is an immutable data type, meaning that once you have created a string, you cannot change it.


Syntax of string: 

str_name = "this is a string"
str_name = 'this is a string'
str_name = '''this is a string'''
str_name = \"\"\"this is a string\"\"\"

print(type(str_name1), type(str_name2), type(str_name3), type(str_name4))
"""

name = "python"
# C P N
# p 0 -6
# y 1 -5
# t 2 -4
# h 3 -3
# o 4 -2
# n 5 -1

# access element using indexing
# positive indexing
# print(name[0])
# print(name[4])

# negetive indexing
# print(name[-2])

# access element using slicing
# str_name[start:stop-1:step-1]
# print(name[2:5])
# print(name[:5])
# print(name[::-1])
# print(name[-2:-5:-1])

# print(name[:2], end="")
# print(name[-1:-3:-1])

# concate two or more string
# print(name[:2] + name[-1:-3:-1])

# replicating python string
# print(name * 2)

# access string using for
# for ch in name:
#     print(ch)

# access string using while
# start = 0
# end = len(name)
# while(start < end):
#     if start % 2 == 0:
#         print(name[start].upper())
#     else:
#         print(name[start].lower())
#     start += 1


# string methods

# password = input("Enter your password : ")

# if len(password) >= 8:
#     if not password.isdigit():
#         print("Now you are logged in")
#     else:
#         print("Enter also alphabet")
# else:
#     print("Your password must be 8 digit atleast")


# print(dir(name))

# name = "    PyTHon PROgrammING    "
name = "pyTHon PROgrammING"
# print(name.lower())
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

# print(name.lower().count("o"))
# print(name.index('m'))
# print(name.title())
print(name.capitalize())