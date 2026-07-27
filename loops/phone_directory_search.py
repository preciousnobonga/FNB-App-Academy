# create a mini data directory using a List and a Dictioanry combined

# 1. Create a dictionary called contacts where the Keys are friend names
# and the values are their phone numbers (keep phone numbers as strings so the leading 0 doesn't drop off).
# fill it with 3 people
# 2. ask the user to input the name of the friend they want to look up.
# 3. use a conditional check to see if the name matches a key.
# if it exists, pull out and print their number: "Found! [Name]'s number is [Number]".
# 4. otherwise, print "Contact not found."


# create a dictionary
contacts = {
    "Potso": "0795412236",
    "Tiisetso": "0839781474",
    "Kagiso": "0669821345"}

# ask the user to input name of the friend they want to look up
friend_name = input("Enter the name of the friend you want to look up: ")

# use a conditional check to see if the name matches a key
if friend_name in contacts:
    print(f"Found! {friend_name}'s number is {contacts[friend_name]}")
else:
    print("Contact not found.")
