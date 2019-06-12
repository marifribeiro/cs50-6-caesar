from cs50 import get_string
from sys import argv

# if argument is not valid, exit
if len(argv) != 2:
    exit("Usage: python caesar.py key")
elif not argv[1].isdigit():
    exit("Usage: python caesar.py key")

# declaration of variables key and plaintext, for users input
key = int(argv[1])
plaintext = get_string("Plaintext: ")

# beggining of printing encrypted text
print("ciphertext: ", end="")

# if the inputed key is > than 26, use the remainter to keep inside the alphabet
if (key >= 26):
    key = key % 26

# for each char in the plaintext, do the following:
for i in plaintext:

    # declaration of ciphertext variable
    ciphertext = ord(i) + key

    # if the char is upper case, keep upercase going through the alphabet
    if i.isupper() and ciphertext > 90:
        ciphertext = ciphertext - 26

    # if the char is lower case, keep lower case going through the alphabet
    elif i.islower() and ciphertext > 122:
        ciphertext = ciphertext - 26

    # if is an alphabet letter, encrypt it
    if i.isalpha():
        print(chr(ciphertext), end="")

    # if not, leave as it is
    else:
        print(i, end="")

# jump a line at the end
print("")
