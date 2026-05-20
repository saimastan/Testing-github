# BASIC LEVEL (Foundation Building)

# Variables

'''1. Create variables to store:
Your name
Age
Height
Is_student (True/False)'''

# name = "Sai Mastan"
# age = 20
# height = 5.8
# is_student = True

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Is Student:", is_student)


'''2. Swap two numbers without using a third variable.'''

# a,b = 10, 20
# print("Before swapping: a =", a, "b =", b)
# a,b = b,a
# print("After swapping: a =", a, "b =", b)


# Data Types

'''1. Identify the datatype
10            # int
10.5          # float
3+4j          # complex
True          # boolean
"Python"      # string
'''

# Operators

'''1. Perform 
Addition
Subtraction
Multiplication
Division
Floor division
Modulus
Exponent
'''

# a = 10
# b = 20

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Exponent:", a ** 2)

# Type Conversion
'''
Convert:
int → float
float → int
string → int
int → string
'''

# num_int = 10
# print("Integer to Float:", float(num_int))

# num_float = 10.5
# print("Float to Integer:", int(num_float))

# num_str = "20"
# print("String to Integer:", int(num_str))

# num_int = 30
# print("Integer to String:", str(num_int))


# INTERMEDIATE LEVEL (Logic Building)

# Variables + Operators

''' 1. Calculate area of rectangle.'''

# length = 10
# breadth = 5

# area = length * breadth
# print("Area of rectangle:", area)

'''2. Calculate the average of three numbers.'''

# num1 = 10
# num2 = 20
# num3 = 30

# avg = num1 + num2 + num3 / 3
# print("Average of three numbers:", avg)

'''3. Calculate area of circle.'''

# radius = 5
# pi = 3.14

# circle = pi * radius ** 2
# print("Area of circle:", circle)

''' 4. Convert kilometers to meters.'''

# km = 5
# m = km * 1000
# print("Kilometers to Meters:", m)

''' 5. Convert Celsius to Fahrenheit.'''

# celsius = 25
# fahrenheit = (celsius * 9/5) + 32
# print("Celsius to Fahrenheit:", fahrenheit)

''' 6. Calculate simple interest.'''

# p = 1000
# t = 2
# r = 5

# si = (p * t * r) / 100
# print("Simple Interest:", si)


'''7. Calculate compound interest.'''

# p = 1000
# t = 2
# r = 5

# ci = p * (1 + r/100) ** t - p
# print("Compound Interest:", ci)


# Input + Type Conversion

'''1. Take marks of 5 subjects and calculate total + percentage.'''

# sub1 = int(input("Enter marks for subject 1: "))
# sub2 = int(input("Enter marks for subject 2: "))
# sub3 = int(input("Enter marks for subject 3: "))
# sub4 = int(input("Enter marks for subject 4: "))
# sub5 = int(input("Enter marks for subject 5: "))

# total = sub1 + sub2 + sub3 + sub4 + sub5
# percentage = (total / 500) * 100
# print("Total Marks:", total)
# print("Percentage:", percentage)


''' 2. Convert minutes into hours and minutes.'''

# min = int(input("Enter minutes: "))
# hours = min // 60
# remaining_minutes = min % 60
# print("Hours:", hours)
# print("Remaining Minutes:", remaining_minutes)


# Operators

''' 1. Check if a number is divisible by both 5 and 7.'''

# num = int(input("Enter a number: "))
# if num % 5 == 0 and num % 7 == 0:
#     print(num, "is divisible by both 5 and 7.") 
# else:
#     print(num, "is not divisible by both 5 and 7.")    

''' 2. Reverse a 2-digit number.'''

# num = int(input("Enter a 2-digit number: "))
# if 10 <= num <= 99:
#     tens = num // 10
#     units = num % 10
#     reversed_num = (units * 10) + tens
#     print("Reversed number:", reversed_num)


#  ADVANCED LEVEL (Problem Solving + Interview Style)

# Variables + Operators

'''1. Swap 3 variables cyclically.'''

# a, b, c = 1, 2, 3
# print("Before swapping: a =", a, "b =", b, "c =", c)
# a, b, c = c, a, b
# print("After swapping: a =", a, "b =", b, "c =", c)

'''2. Calculate electricity bill:
Rules:
First 100 units → ₹5/unit
Next 100 → ₹7/unit
Remaining → ₹10/unit'''

# units = int(input("Enter electricity units consumed: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + ((units - 100) * 7)
# else:
#     bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
# print("Electricity Bill: ₹", bill)    


''' 3. Salary calculation:
Input:
Basic salary

Calculate:

HRA = 20%
DA = 10%
Total salary'''

# basic_salary = float(input("Enter basic salary: "))
# hra = 0.20 * basic_salary
# da = 0.10 * basic_salary    
# total_salary = basic_salary + hra + da
# print("HRA: ₹", hra)
# print("DA: ₹", da)
# print("Total Salary: ₹", total_salary)



'''4. BMI Calculator
Classify:

Underweight
Normal
Overweight
Obese'''

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")      
          