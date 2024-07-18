# HOW TO FIND LENGTH OF STRING

name = "this is python program"
result = len(name)
print("the length of the string is ",+result)

# SUM OF 10 NATURAL NUMBERS

numbers = 0
for num in range (1,11):
    numbers += num
print("the sum of first 10 naturak numbers is ",+numbers)

# READING INTEGER NUMBERS AND CONVERTING INTO FLOAT

num = int(input("enter a number"))
for i in range(1,6):
    num = float(i)
    print("the integer number and converted in to float are ",+num)

# GREATER OF 2 NUMBERS

num1 = int(input("enter the number 1"))
num2 = int(input("enter the number 2"))
if num1 > num2:
    print("number 1 is greater than number 2")
else:
    print("number 2 is reater than number 1")

# MAXIMUM OF 2 NUMBERS

num1 = int(input("enter the first nnumber"))
num2 = int(input("enter the secomd number"))

if num1 < num2:
    print("number2 is greater than number 1")
else:
    print("number1 is greater than number 2")

# TO CHECK THE GIVEN NUMBER IS EVEN OR ODD

num = int(input("enter a number"))
if num%2==0:
    print("it is even number")
else:
    print("it is odd number")

# GREATEST AMOUNG 2 STRINGS

first_string = input("enter the first string")
second_string = input("enter the second string")

if first_string > second_string:
    print("first string is greater than the second string")
else:
    print("second string is greater than the first string")

# to check the given integer is positive or negative

num = int(input("enter the integer"))
if num < 0:
    print("it is negative integer")
else :
    print("it is positive integer")