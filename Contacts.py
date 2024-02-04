#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

def display_menu():
    print("---------------------------------------")
    print("           CONTACT MANAGEMENT          ")
    print("---------------------------------------")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("---------------------------------------")

def add_contact(contacts):
    print("---------------------------------------")
    print("            ADD CONTACT                 ")
    print("---------------------------------------")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = Contact(name, phone, email, address)
    contacts.append(contact)

    print("\nContact added successfully!\n")

def view_contact_list(contacts):
    print("---------------------------------------")
    print("         CONTACT LIST                  ")
    print("---------------------------------------")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact.name} | {contact.phone}")
    print("---------------------------------------")

def search_contact(contacts):
    print("---------------------------------------")
    print("         SEARCH CONTACT                ")
    print("---------------------------------------")
    search_term = input("Enter Name or Phone Number: ").lower()

    matching_contacts = [contact for contact in contacts if search_term in (contact.name.lower() or contact.phone.lower())]

    if matching_contacts:
        print_contacts(matching_contacts)
    else:
        print("No matching contacts found.")
    print("---------------------------------------")

def update_contact(contacts):
    print_contact_list(contacts)
    selection = int(input("Select Contact to Update: ")) - 1

    if 0 <= selection < len(contacts):
        contact = contacts[selection]
        print_contact(contact)

        print("\nEnter New Details:")
        contact.name = input("Enter New Name: ")
        contact.phone = input("Enter New Phone Number: ")
        contact.email = input("Enter New Email: ")
        contact.address = input("Enter New Address: ")

        print("\nContact updated successfully!\n")
    else:
        print("Invalid selection. Please try again.")

def delete_contact(contacts):
    print_contact_list(contacts)
    selection = int(input("Select Contact to Delete: ")) - 1

    if 0 <= selection < len(contacts):
        contact = contacts.pop(selection)
        print_contact(contact)
        print("\nContact deleted successfully!\n")
    else:
        print("Invalid selection. Please try again.")

def print_contact(contact):
    print(f"\nName: {contact.name}")
    print(f"Phone: {contact.phone}")
    print(f"Email: {contact.email}")
    print(f"Address: {contact.address}\n")

def print_contacts(contacts):
    for contact in contacts:
        print_contact(contact)

def main():
    contacts = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact_list(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    


# In[ ]:





# In[ ]:




