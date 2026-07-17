#Tracking individual letters

#name = "Python"
#print(name[0]) # 'P'
#print(name[-1]) # 'n'
#print(name[2]) # 't'


# Using string methods

#town = "  Johannesburg  "
#print(town.upper())
#print(town.strip())

# creating a professional system email generator

#first_name = input("Enter your first name: ").strip()
#last_name = input("Enter your last name: ").strip()

#username = f"{first_name[0]}{last_name}"
#print(f"Your email is: {username.lower()}@university.co.za")

#message = "Hello World"
#print(message)

message = 'Bobby\'s world'
print(message)

message = """Bobby's World was a good show in the 1990s"""
print(message)

# slicing strings

message = 'Hello World'
print(message[0:5]) # print all the characters between the beginning and up to but not including the 5th index

message = 'Hello World'
print(message[6:]) # print all the characters from the 6th index to the end of the string 


message = 'Hello World'
print(message.lower()) # convert all the characters in the string to lowercase

message = 'Hello World'
print(message.upper()) # convert all the characters in the string to uppercase

message = 'Hello World'
print(message.count('Hello')) # count the number of times a substring appears in the string

message = 'Hello World'
print(message.find('World')) # find the index of the first occurrence of a substring in the string

message = 'Hello World'
new_message = message.replace('World', 'Universe') # replace a substring with another substring in the string
print(new_message)

# concatenation of strings
greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {name}. Welcome!'
print(message) 






