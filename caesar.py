""" Caesar cipher implementation """
from sys import argv, exit
from helpers import rotate_character

def encrypt(text, rot):
    """ Encrypt message using rot13 """
    encrypted_message = ''
    for i in text:
        if not i.isalpha():
            encrypted_message += i
        else:
            encrypted_message += rotate_character(i, rot)

    return encrypted_message

def user_input_is_valid(cl_args):
    """ Check for appropriate command line argument """
    if len(cl_args) == 1 or not cl_args[1].isdigit():
        return False

    return True

def main():
    """ Main program function """

    if user_input_is_valid(argv) is False:
        print("usage: python3 caesar.py n")
        exit()

    answer = input("Type a message to encrypt:\n")

    print(encrypt(answer, int(argv[1])))


if __name__ == "__main__":
    main()
