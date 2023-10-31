# Aadithi Arjun
# Lab partner: Isabella Marin

def encode(password):
    encoded_password = ''
    for digit in str(password):
        new_digit = int(digit) + 3
        encoded_password += str(new_digit)
    return encoded_password

# decode function done by lab partner, Isabella Marin
def decode(encoded_password):
    # initialize empty string for decoded password
    decoded_password = ""
    # loop through the digits in the string encoded password
    for digit in str(encoded_password):
        new_password = int(digit) - 3               # convert characters in string to integers & subtract 3 from each
        decoded_password += str(new_password)       # convert the new password back to a string and add to empty string

    return decoded_password

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
            global x
            x = encode(UserChoice1)

        # option2 -> encode and decode password
        elif option == '2':
            decoded_password = decode(x)
            print(f"The encoded password is {x}, and the original password is {decoded_password}.")

        # option3 -> quit
        elif option == '3':
            False


if __name__ == "__main__":
    main()