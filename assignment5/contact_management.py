import json
import os

# Initialize the contact list
contacts = []

# Load contacts from file if it exists
if os.path.exists('contacts.json'):
    with open('contacts.json', 'r') as file:
        contacts = json.load(file)

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    save_contacts()
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contacts():
    search_term = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]

    if not results:
        print("No contacts found.")
        return

    print("\nSearch Results:")
    for contact in results:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}\n")

def update_contact():
    search_term = input("Enter name or phone number to search for update: ")
    results = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]

    if not results:
        print("No contacts found.")
        return

    contact = results[0]
    print("\nUpdating Contact:")
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}\n")

    name = input("Enter new name (leave blank to keep current): ")
    phone = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    address = input("Enter new address (leave blank to keep current): ")

    if name:
        contact['name'] = name
    if phone:
        contact['phone'] = phone
    if email:
        contact['email'] = email
    if address:
        contact['address'] = address

    save_contacts()
    print("Contact updated successfully.")

def delete_contact():
    search_term = input("Enter name or phone number to search for deletion: ")
    results = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]

    if not results:
        print("No contacts found.")
        return

    contact = results[0]
    contacts.remove(contact)
    save_contacts()
    print("Contact deleted successfully.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
