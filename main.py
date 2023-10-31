# Aadithi Arjun
def main():
  while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = input("Please enter an option:")

    if option == '1':
      global UserChoice1
      UserChoice1 = int(input("Please enter your password to encode:"))
      print(UserChoice1)
      print("Your password has been encoded and stored!")

    elif option == '2':
      print("a")
    elif option == '3':
      False

if __name__ == "__main__":
    main()
    