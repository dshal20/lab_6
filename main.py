def main():
    while True:
        option = int(input('Menu:\n1. Encoder\n2. Decoder\n3. Quit\n'))
        if option == 1:
            password = input('Please enter an eight digit number: ')
            digits = len(password)

            if digits == 8:
                print(encoder(password))
            else:
                print('Please enter an eight digit password.')
        if option == 2:
            password = input('Please enter an eight digit number: ')
            digits = len(password)

            if digits == 8:
                print(decoder(password))
            else:
                print('Please enter an eight digit password.')
        else:
            break


def encoder(password):
    epassword = ''
    for i in password:
        encoding = (int(i) + 3) % 10
        epassword += str(encoding)
    return epassword


def decoder(password):
    dpassword = ''
    for i in password:
        encoding = (int(i) - 3) % 10
        dpassword += str(encoding)
    return dpassword


if __name__ == "__main__":
    main()
