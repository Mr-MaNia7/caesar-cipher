"""Caesar Cipher

A program for demonstrating caesar cipher!

This application allows the user to encrypt alphabetic text
and see the encrypted text in real time.

The app accepts user input through a terminal and it expects
the user to input only alphabetic characters. Otherwise the 
charaters are avoided and hence will not be encrypted!

This program contains the following functions:
    * caesarEnc - encrypts a char shifting it with a key
    * main - the main function of the program
"""

# Import necessary modules
import string

def caesarEnc(char, key):
    """An encrypting function implementing caesar cipher."""
    ascii_number = ord(char)
    skip_number = [10] # tab character
    if ascii_number in skip_number:
        return chr(ascii_number)
    elif (65 <= ascii_number <= 90):
        num = ascii_number - 65
        enc_pos = (num + key) % 26 + 65
        return chr(enc_pos)
    elif (97 <= ascii_number <= 122):
        num = ascii_number - 97
        enc_pos = (num + key) % 26 + 97
        return chr(enc_pos)

def main():
    """The main entry of the program."""
    
    plain_txt = input("Enter a plain text: ")
    key = int(input("Enter a shift key: "))
    
    enc_list = []
    words = plain_txt.split() # removes white space between words
    
    for word in words:
        temp_list=[]
        word = word.translate(str.maketrans("", "", string.punctuation))
        for char in word:
            temp_list.append(caesarEnc(char, key))
        temp_list.append(" ") # undoing the space removal
        enc_list.extend(temp_list)
    
    enc_word = "".join(enc_list)
    print(enc_word.rstrip())

main()
