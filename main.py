def encode(encoder):
    i = 0
    encoded = ""
    while i < len(encoder):
        if encoder[i] == "0":
            encoded += "3"
        if encoder[i] == "1":
            encoded += "4"
        if encoder[i] == "2":
            encoded += "5"
        if encoder[i] == "3":
            encoded += "6"
        if encoder[i] == "4":
            encoded += "7"
        if encoder[i] == "5":
            encoded += "8"
        if encoder[i] == "6":
            encoded += "9"
        i += 1

    return encoded

def main():
    x = 0
    while x != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        u_input = int(input("Please enter an option: "))

        if u_input == 1:
            encoder = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print("")

        if u_input == 2:
            encoded = encode(encoder)
            print(f"The encoded password is {encoded}, and the original password is {encoder}.")
            print("")

        if u_input == 3:
            break


if __name__ == '__main__':
    main()
