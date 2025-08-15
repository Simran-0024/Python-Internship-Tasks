# Number System Converter

while True:
    print("\n Number System Converter ------>")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Octal")
    print("4. Octal to Decimal")
    print("5. Decimal to Hexadecimal")
    print("6. Hexadecimal to Decimal")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        dec = int(input("Enter Decimal number: "))
        print("Binary:", bin(dec)[2:])

    elif choice == "2":
        binary = input("Enter Binary number: ")
        print("Decimal:", int(binary, 2))

    elif choice == "3":
        dec = int(input("Enter Decimal number: "))
        print("Octal:", oct(dec)[2:])

    elif choice == "4":
        octal = input("Enter Octal number: ")
        print("Decimal:", int(octal, 8))

    elif choice == "5":
        dec = int(input("Enter Decimal number: "))
        print("Hexadecimal:", hex(dec)[2:].upper())

    elif choice == "6":
        hexa = input("Enter Hexadecimal number: ")
        print("Decimal:", int(hexa, 16))

    elif choice == "7":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
