# string and Numeric values can Operate Together with *

A,B = 2, 3
Txt = "@"
print(2*Txt*3)


#String & String can operate with +

A,B = "2", 3
Txt = "@"
print((A+Txt)*B) 


# Numeric values can operate with all arithmetic operators

A,B = 10, 5
c = 5
print (A + B *c)

# Arithmetic expression with integer and float will result in float

A,B = 10, 5.0
C = A * B
print(C)

# Result of division operator with two integers will be float 

A , B = 1,2
c = A/B
print(C)

# Integer division with float and int give int displayed as float

a,b = 1.5, 3
c = a//b 
print(c, a/b)

# Floor gives closest integer , which is lesser than or equal to the float value

A,B = 12,5
C = A// B
print (C)

A,B = -12,5
C = A// B
print (C)

A,B = 12,-5
C = A// B
print (C)

# Remainder is negative when denominator is negative

A,B = 12,5
C = A%B
print (C)

A,B = 12,-5
C = A % B
print (C)

# Single line comment

"""
Multi line

comment
write anything
"""
