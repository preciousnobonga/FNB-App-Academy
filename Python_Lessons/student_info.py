# Write a Python script called student_info.py that collects personal information
# from the user and displays it in a formatted profile card. The program must 
# demonstrate correct use of all four data types, string manipulation, arithmetic,
# and the f-string output format.


first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))
full_name = first_name + " " + surname

# Formatted greeting
print(f"Welcome, {full_name}!")

# Display name in Uppercase using .upper() and Title Case using .title()
print("Name in UPPERCASE:", full_name.upper())
print("Name in Title Case:", full_name.title())

# Calculate and display the age in months (age x 12)
age_in_months = age * 12
print("Your age in months is:", age_in_months)

# Round the favourite number to 2 decimal pplaces using round()
rounded_favourite_number = round(favourite_number, 2)
print("Your favourite number rounded to 2 decimal places is:", rounded_favourite_number)

# Print the data type of each collected value using type()
print("Data type of first name:", type(first_name))
print("Data type of surname:", type(surname))
print("Data type of age:", type(age))
print("Data type of favourite number:", type(favourite_number))


