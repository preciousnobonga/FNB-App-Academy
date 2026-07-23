# Build a Python calculator called calculator.py that takes two
# numbers as input and performs all four basic arithmetic operations
# plus two advanced operations. The calculator must handle user input
# safely using type casting and display results clearly using f-strings. 

# enter two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# calculate and display using all four basic arithmetic operations
addition = round(num1 +  num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# handle division by zero 
if num2 == 0:
    division = "Error (division by zero)"
    floor_division = "Error (division by zero)"
    modulus = "Error (division by zero)"
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

# display results in a formatted table using f-strings
print("\n=== Calculator Results ===")
print(f"{'Operation':<20}{'Result':<20}")
print("-" * 40)
print(f"{'Addition (+)':<20}{addition:<20}")
print(f"{'Subtraction (-)':<20}{subtraction:<20}")
print(f"{'Multiplication (*)':<20}{multiplication:<20}")
print(f"{'Division (/)':<20}{division:<20}")
print(f"{'Floor Division (//)':<20}{floor_division:<20}")
print(f"{'Modulus (%)':<20}{modulus:<20}")
