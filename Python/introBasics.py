# Hello World!
print("Hello World!")
# Numbers
var = 5
# String
coddy = "I am learning to code with Coddy!"
# Boolean
boolean = True

# Challlenge#1
nums = [1, 2, 3]
k = 88
PI = 3.14
name = 'bob'

# Arithmetic operators
a = 5.2
b = 2.6
c = a / b 
# Arithmetic shortcuts
count = 0
count += 4
count *= 2
count -= 1
# Comparison Operators
n1 = 8
n2 = 9
n3 = n1 > n2
# Logical Operators Part 1
b1 = (3 > 1) and (6 < 10)
b2 = not (6 > 10 or 10 < 8)  
b3 = b1 or b2
# Logical Operators Part 2
b1 = 1
b2 = 1
b3 = not (b1 + b2) < (b1 * b2)

# Challenge#1
# You are given a code, initialize the variables a and b so that c will hold 24.
a = 2
b = 12
c = b * a
# Challenge#2
# You are given a code, replace the question marks of the variables b1, b2  and b3 so that b4 will hold True.
b1 = (1 < 2) and (2 > 1)
b2 = (2 > 1) or (1 > 0)
b3 = (2 < 1) and (1 > 2) 
# Don't change the line below
b4 = b1 and b2 and (not b3)

# If statement
a = 12
b = 11
# Don't change below this line
c = 0
if a >= b and not b < 10:
    c = 2
c += 1
# If-else
wind = int(input()) # Don't change this line
status = "unset"
if wind < 8: 
    status = "Calm"
elif wind >= 8 and wind <= 31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

# Recap Challenge#1
# set the variable result based on the conditions:
# if op is '+', set result with n1 + n2.
# if op is '-', set result with n1 - n2.
# if op is '/', set result with n1 / n2.
# if op is '*', set result with n1 * n2.

n1 = int(input()) # Don't change this line
n2 = int(input()) # Don't change this line
op = input() # Don't change this line
result = 0

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '/':
    result = n1 / n2
elif op == '*':
    result = n1 * n2

# Output
print('I love Python programming')
# Output with variables
rnd = input() # Don't change this line
print('The input is: ' + rnd)
# Input
# Write a program that get input from the user (their name), and then outputs Hello,  followed by the user's inputted name.
# For example, if the user inputs Bob, the expected output is Hello, Bob.
# You will need to:
# Use input() to get input from the user.
# Store the input in a variable.
# Print Hello,  and the stored variable in the end.
userName = input()
print(f"Hello, {userName}")

# Cast
var1 = float(input())
var2 = float(input())
print(var1*var2)

# Recap Challenge#1
# Write a program that gets an input from the user, his age.
# The program will output (print), the number of missing years till 120 (In a specific format, shown below)
# For example, for input 25, the expected output is "95 years till 120".
userAge = input('')
age = int(userAge)
missingYears = 120 - age
print(f"{missingYears} years till 120")

# Recap challenge#2
# Write a program that gets an input from the user, a number, 1 or 0.
# The program will output "T" if the input is 1 and "F" otherwise.
number = input()
if int(number) == 1:
    print('T')
else:
    print('F')

# for loop
for i in range (3, 28):
    print(f"Hello Coddy: {i}")    
# rehearsal
# Write a program that get input from the user (their name), and then outputs Hello,  followed by the user's inputted name.
# For example, if the user inputs Bob, the expected output is Hello, Bob.
# You will need to:
# Use input() to get input from the user.
# Store the input in a variable.
# Print Hello,  and the stored variable in the end.
name = input('')
print(f"Hello, {name}")

# Write a program that gets one input, float number.
# Use a while loop to divide the input by 2 as long as the number is bigger or equal to 3.5.
# Print the first number that is smaller than 3.5.
number = float(input())
while number >= 3.5:
    number /= 2
print(number)

# break
# You are given a code that prints the numbers from 1 to 10 (including).
# Your task is to add if and break statements so that only the numbers from 1 to 5 will be printed, the loop will exit before printing the numbers from 6 to 10.
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# continue
# You are given a code which prints the numbers from 1 to 20 (including).
# Your task is to add if and continue statements so that only the even numbers will be printed (2, 4, 6, ...). 
for i in range(1, 21):
    if i % 2 == 1:
        continue
    print(i)