"""
What is operator?
operators are special symbols that designate that some sort of computation should be performed
What is operands?
The values that an operator acts on are called operands.

example : 
a = 10 
b = 20 
c = a + b .

here's
a, b, c are operands
=, + are operators


Types of Operators: 

1 Arithmetic Operators [ +,-,/,*,%,//,** ]

a = 20
b = 10
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b

h = a // b

i = a ** b

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

2 Comparison Operators [ ==, !=, >=, <=, <, >]

a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

3 Logical Operators [and, or, not]
a = (20 > 10)  # True
b = (20 < 10)  # False
c = a # True
d = b # Fasle

# and/or
# T T = T = T
# T F = F = T
# F T = F = T
# F F = F = F

print(a and b and c and d)
print(a or b or c or d)
print(a and b or c and d)

# not 
x = not a
y = not b 

print(x ,y)


4 Assignment Operators [=, +=, -=, *=, /=, %=, //=, **=]

a = 10
# a = a + 50
a += 50
print(a)

5 Identity Operators [ is, is not ]

x = 10
y = 10
print( x is y)
print( x is not y)

6 Membership Operators [ in, not in]

name = "python"
print('p' in name)
print('P' in name)
print('Py' in name)
print('tho' not in name)

7 Bitwise Operators [&, |, ^, <<, >>]

a b & | ^
0 0 0 0 1
0 1 0 1 0
1 0 0 1 0
1 1 1 1 1

# <<, >>
x = 3
y = x << 2
print(y)
# 0011
# 1100 = 12


"""