"""
Range function:
syntax: 
range(start:end-1:step-1)

Example :
numbers =  list(range(1,111,3))
print(numbers)

syntax of for loop
for iter_var in sequesnce:
    # block of code

Example : 
name = "Python code"
for ch in name:
    print(ch)

Example : 
numbers =  list(range(1,21))
for num in numbers:
    print(num)

Example : 
num = 6
for row in range(1, num):
    # print(row)
    for col in range(1, num):
        print("*", end=" ")
    print("\n")

Ans:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

# print("brijesh", end="")
# print(" gondaliya")

Example : 
num = 6
for row in range(1, num):
    # print(row)
    for col in range(1, row+1):
        print("*", end=" ")
    print("\n")

Ans :
*
* *
* * *
* * * *
* * * * *

num = 6
for row in range(1, num):
    # print(row)
    for col in range(1, num-row+1):
        print("*", end=" ")
    print("\n")

Ans:
* * * * *
* * * *
* * *
* *
*

Example :
num = 6
for row in range(1, num):
    # print(row)
    for col in range(1, row+1):
        print(" ", end=" ")
    
    for col in range(1, num-row+1):
        print("*", end=" ")
    print("\n")
Ans:
  * * * * *
    * * * *
      * * *
        * *
          *

Syntax of while loop
while():
    # block of code

Example : 
# use while for limitation
start = 1
end = 20
while(start <= end):
    print(start, end= "-")
    start = start + 1
Ans: 1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-

Example :
# use without limitation

while(1):
    age = input("Enter your age : ")
    age = int(age)

    if(age >= 18):
        weight = input("Enter your weight : ")
        weight = float(weight)
        if(weight>= 50):
            print("You can donate")
        else:
            print(f"You can not donate because of your weight is less than 50 : {weight}")
    else:
        print(f"You can not donate because of your age is less 18: {age} ")

Example :
num = 5
start = 1


while(start <= num):
    cstart = 1
    while(cstart <= num):
        print("*", end=" ")
        cstart += 1
    print("\n")
    start += 1
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *


Assignment :

* * * * * * *
*   *   *   *
* * *   *   *
*       *   *
* * * * *   *
*           *
* * * * * * *

"""
num = 10
for r in range(1,num):
    
    if r % 2 == 0:
        # print("Even")
        print("*")
    else:
        # print(f"row - ", r)
        # print("Odd")
        for co in range(1, r+1):
            print("*", end=" ")
    print("\n")