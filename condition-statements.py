"""
1] if
syntax: 
    if (condition):
        block of code

Example : 
    score = 15
    if (score >= 30):
        print("pass")


2] if...else
syntax:
    if(condition):
        # code of block
    else:
        # default statments

    score = 15
    if (score >= 30):
        print("pass")
    else:
        print("failed")

3] if...elif ladder

syntax: 
if( condition - 1 ):
    # block of statment
elif (condition - 2): 
    # block of statment
elif (condition - 3): 
    # block of statment
elif (condition - 4): 
    # block of statment
else:
    # default statments

score = -20
if score >= 0 and score <= 100:
    if (score >= 80):
        print("First-class")
    elif (score >= 60):
        print("Second-class")
    elif (score >= 40):
        print("Third-class")
    else:
        print("Sorry, You are failed")
else:
    print("Please enter your score between 0 to 100")

4] nested if/if..else
while(1):
    age = input("Enter your age: ")
    age = int(age)

    if (age >= 18):
        weight = input("Enter your weight: ")
        weight = int(weight)
        if (weight >= 50):
            print("You can donate")
        else:
            print("You can not donate")
    else:
        print("You can not donate")

"""
