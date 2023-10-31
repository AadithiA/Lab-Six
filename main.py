# Aadithi Arjun
def encode(password):
    encoded_password = ''
    for digit in str(password):
        new_digit = int(digit) + 3
        encoded_password += str(new_digit)
    return encoded_password


# main function
def main():
    while True:
        # menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option:")

        # option1 -> get input password
        if option == '1':
            UserChoice1 = int(input("Please enter your password to encode:"))
            print(UserChoice1)
            print("Your password has been encoded and stored!")

            x = encode(UserChoice1)

        # option2 -> encode and decode password
        elif option == '2':
            print("a")

            # print("The encoded password is", encoded_password, "and the original password is", UserChoice1)

        # option3 -> quit
        elif option == '3':
            False


if __name__ == "__main__":
    main()