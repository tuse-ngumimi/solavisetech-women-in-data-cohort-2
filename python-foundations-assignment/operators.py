import math 
# Exercise 1 - Simple Calculator

print("\n" + "*" * 30)
print("    SIMPLE ARITHMETIC CALCULATOR")
print("*" * 30)


print("Choose an operation:")
print("1 or + : Addition")
print("2 or - : Subtraction") 
print("3 or x : Multiplication")
print("4 or / : Division")
print("*" * 30)


operation_choice: str = input("\nEnter your choice (1, 2, 3, 4 or +, -, x, /): ")

print(f"\nYou selected: {operation_choice}")
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))


print(f"\n CALCULATING...")

if operation_choice == "1" or operation_choice == "+":
    result: float = num1 + num2
    print(f"\n RESULT: {num1} + {num2} = {result}")

elif operation_choice == "2" or operation_choice == "-":
    result: float = num1 - num2
    print(f"\n RESULT: {num1} - {num2} = {result}")

elif operation_choice == "3" or operation_choice == "x":
    result: float = num1 * num2
    print(f"\n RESULT: {num1} × {num2} = {result}")

elif operation_choice == "4" or operation_choice == "/":
    if num2 == 0:
        print(f"\n ERROR: Cannot divide by zero!")
    else:
        result: float = num1 / num2
        print(f"\n RESULT: {num1} ÷ {num2} = {result:.2f}")

else:
    print(f"\n ERROR: '{operation_choice}' is not a valid choice!")

print("\nThank you for using Simple Calculator! ")

# Exercise 2: Area of Shapes

print("\n" + "*" * 30)
print("    AREA OF SHAPE CALCULATOR")
print("*" * 30)

print("What shape are you working with today :")
print("1 for Circle")
print("2 for Triangle") 
print("3 for Rectangle")
print("Enter 4 to Exit")
print("*" * 30)

PI = 3.14
shape_choice: str = input("\nEnter your choice (1, 2, 3, : ")


print(f"\nYou selected: {operation_choice}")

if shape_choice == 1:
    radius = input("Enter the value of the radius: ")
    area = PI * radius ** 2
    print(f"\nThe area of the circle with radius {radius} is: {area}")
elif shape_choice == 2:
    base = input("Enter the value of the base: ")
    height = input("Enter the value of the height: ")
    area = 0.5 * base * height
    print(f"\nThe area of the triangle with base {base} and height {height} is: {area}")
elif shape_choice == 3:
    length = input("Enter the value of the length: ")
    width = input("Enter the value of the width: ")
    area = length * width
    print(f"\nThe area of the rectangle with length {length} and width {width} is: {area}")
elif shape_choice == 4:
    print("\nExiting the Area of Shape Calculator. Goodbye!")
else:
    print(f"\n ERROR: '{shape_choice}' is not a valid choice!")
    
# Exercise 3: Even or Odd Number Checker
print("\n" + "*" * 30)
print("    EVEN OR ODD NUMBER CHECKER")

sample_number: int = int(input("Enter any whole number: "))  

if sample_number % 2 == 0:
    print(f"\n{sample_number} is an even number.")          
    print(f"It is divisible by 2, and the result is a whole number.")
else:                                                        
    print(f"\n{sample_number} is an odd number.")           
    print(f"It is NOT divisible by 2. The result would be a decimal.")

# Exercise 4: Student Grade Percentage Calculator
print("\n" + "*" * 30)
print("    GRADE PERCENTAGE CALCULATOR")
print("*" * 30)

total_marks: float = float(input("Enter the total marks for the course: "))
marks_obtained: float = float(input("Enter the marks obtained by the student: "))
if total_marks <= 0:
    print("\nERROR: Total marks must be greater than zero.")
else:
    percentage: float = (marks_obtained / total_marks) * 100
    print(f"\nThe student's grade percentage is: {percentage:.2f}%")

# Exercise 4: BMI Calculator
print("\n" + "*" * 30)
print("    BMI CALCULATOR")
print("*" * 30)

user_height = float(input("Enter height (in metres): "))
user_weight = float(input("Enter weight (in kg): "))

bmi = user_weight / user_height * 2
if bmi < 18.5:
    print(f"\n Your Body Mass Index (BMI) is {bmi:.2f}")
    print(f"You're underweight!")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"\n Your Body Mass Index (BMI) is {bmi:.2f}")
    print(f"Your current body weight is healthy!")
elif bmi >= 25.0 and bmi <= 29.9:
    print(f"\n Your Body Mass Index (BMI) is {bmi:.2f}")
    print(f"Based on your current body weight, you are overweight.")
elif bmi > 30.0:
    print(f"\n Your Body Mass Index (BMI) is {bmi:.2f}")
    print(f"Based on your current body weight, you are obese.")

# Exercise 6: Power and Modulus
print("\n" + "*" * 30)
print("    POWER & MODULUS")
print("*" * 30)

base_val  = int(input("  Enter base number     : "))
exp_val   = int(input("  Enter exponent        : "))
divisor   = int(input("  Enter divisor (for %) : "))
 
power     = base_val ** exp_val
remainder = base_val % divisor
 
print(f"\n  {base_val} ^ {exp_val}  = {power}")
print(f"  {base_val} mod {divisor}  = {remainder}")