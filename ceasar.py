import string

"""Ceasar Cipher

A program for demonstrating ceasar cipher!
"""

def ceasarEnc(char, key):
    """An encrypting function accepting characters and returning swiched ones."""
    ascii_number = ord(char)
    
    if (65 <= ascii_number <= 90):
        num = ascii_number - 65
        enc_pos = (num + key) % 26 + 65
    elif (97 <= ascii_number <= 122):
        num = ascii_number - 97
        enc_pos = (num + key) % 26 + 97
    return chr(enc_pos)

def main():
    plain_txt = input("Enter a plain text: ")
    key = int(input("Enter a shift key: "))
    
    enc_list = []
    words = plain_txt.split() # removes white space between words
    
    for word in words:
        temp_list=[]
        word = word.translate(str.maketrans("", "", string.punctuation))
        for char in word:
            temp_list.append(ceasarEnc(char, key))
        temp_list.append(" ") # undoing the space removal
        enc_list.extend(temp_list)
    
    enc_word = "".join(enc_list)
    print(enc_word.rstrip())

main()
