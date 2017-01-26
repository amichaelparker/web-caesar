""" Encryption helper functions """

def alphabet_position(letter):
    """ Returns index number of entered letter """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()

    return alphabet.index(letter)

def rotate_character(char, rot):
    """ Returns character at rotated position """
    if not char.isalpha():
        return char

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    position = alphabet_position(char)

    if position + rot < 26:
        if char.isupper():
            return alphabet[position + rot].upper()
        else:
            return alphabet[position + rot].lower()
    else:
        if char.isupper():
            return alphabet[(position + rot) % 26].upper()
        else:
            return alphabet[(position + rot) % 26].lower()

