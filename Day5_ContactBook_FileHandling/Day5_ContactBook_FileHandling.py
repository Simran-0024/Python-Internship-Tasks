import csv
import os

FILE_NAME = "contacts.csv"

# make file if not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])  # header


def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
    print("Contact added!")


def view_contacts():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            print(row)


def search_contact():
    name = input("Enter name to search: ").lower()
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0].lower() == name:
                print("Found:", row)
                return
    print("Not found.")


def delete_contact():
    name = input("Enter name to delete: ").lower()
    contacts = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[0].lower() != name:
                contacts.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(contacts)

    print("Deleted (if existed).")


while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
