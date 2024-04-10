#Jake Drummond
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == "2":
            print("Decode function will be implemented later.\n")

        elif option == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
