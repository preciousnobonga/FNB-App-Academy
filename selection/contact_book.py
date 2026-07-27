# store contacts as a list of dictionaries, each with keys: name, phone, email
# implement an add_contact() function that appends a new dictionary to the list
# implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
# implement a delete_contact(name) function that removes a contact by name
# implement a view_all() function that displays all contacts in a formatted layout
# use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)


# list of dictionaries for contacts
contacts = []

# add_contact() function
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email }
    contacts.append(contact)
    print("contacts added successfully.\n")


# search_contact(name) function
def search_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None

# delete_contact(name) function
def delete_contact(name):
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.\n")

# view_all() function
def view_all():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 25)
    print()

        
# while loop to let user choose an action
while True:
    print("=== Contacy Book ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter name to search: ")
        result = search_contact(name)
        if result:
            print("\nContact Found:")
            print(f"Name : {result['name']}")
            print(f"Phone : {result['phone']}")
            print(f"Email : {result['email']}")
        else:
            print("Contact not found.\n")
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.\n")

