"""
What is a function?
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

Syntax : 
def function_name(para1, para2, ... , paran): function defination
    # block of statments

function_name(value1, value2, ... , valuen) // function call

"""
# a = 10
# b = 20
# c = 10
# d = 20

# print(a + b)
# print(c + d)

# def add(a, b):
#     print(a + b)

# add(10, 50)

# positional
def add(a,b,c):
    print(a + b + c)

# add(10,20, 20)
# default
def car(color="red"):
    print(color)

# car()
# car(color="blue")

# keyword
def bill(tomato, potato):
    sum = 0
    sum = tomato + potato
    # print(sum)

# bill(20, 30)

# variable length
def bill(**products):
    sum = 0
    for k, v in products.items():
        sum += v
        print(k, ":", v)
    print("Total amount : ", sum)

bill(pen=20, book=30, laptop=45000)
# 1] inbuilt function
# 2] user defined function

# from datetime import datetime, timedelta
# import time

# def current_datetime():
#     return datetime.now()

# # print(current_datetime() + timedelta(days=1, minutes=2, hours=2))

# import random


# while(True):
#     s = random.randint(1, 5)
#     time.sleep(s)
#     print("python")