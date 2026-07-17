# Create a program that acts as a digital ticket counter.
# 1. Ask the user for their name
# 2. Ask them for the name of the band/artist they want to see
# 3. Print a personalised confirmation message usiing an f-string
# that says something like: "Hey, [Name]! Your tickets to see [Artist] are booked successfully!"

name = input("Enter your name: ")
artist = input("Enter the name of the band/artist you want to see: ")
print(f"Hey, {name}! Your tickets to see {artist} are booked successfully!")