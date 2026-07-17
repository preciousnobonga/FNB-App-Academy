# write a Python script called string_formatter.py 
# that takes a user's first name, last name, and a short bio
# message as input, then applies multiple string transformations
# to produce a formatted user profile output. This simulates how
# a real app backend processes user-submitted text. 


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio message about yourself: ").strip()

# create a username
username = f"{first_name[0]}{last_name}".lower()

# full name in Title Case
full_name = f"{first_name} {last_name}".title()

# count and display the number of characters in the bio using len()
bio_length = (len(bio))

# replace any occurrence of 'I am' in the bio with 'I'm' using .replace()
updated_bio = bio.replace("I am", "I'm")


# display the formatted user profile
print(f"\n--- User Profile ---")
print(f"Username: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {updated_bio}")
print(f"Bio Character Count: {bio_length}")

