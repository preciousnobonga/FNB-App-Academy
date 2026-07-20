# ask the user for their password
password = input("Enter your secret password: ").strip()

# extract the first and last letters of the password
first_letter = password[0]
last_letter = password[-1]

# print a hint using an f-string that forces the letters into uppercase so they stand out 
print(f"Your password hint: starts with '{first_letter.upper()}' and ends with '{last_letter.upper()}'")


