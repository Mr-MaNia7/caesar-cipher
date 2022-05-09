"""Ceasar Cipher

A program for demonstrating ceasar cipher!
"""

# Importing modules
import string
import tkinter as tk

def ceasarEnc(char, key):
    """An encrypting function implementing ceasar cipher."""
    ascii_number = ord(char)
    
    if (65 <= ascii_number <= 90):
        num = ascii_number - 65
        enc_pos = (num + key) % 26 + 65
    elif (97 <= ascii_number <= 122):
        num = ascii_number - 97
        enc_pos = (num + key) % 26 + 97
    return chr(enc_pos)

def main():
    """The main entry of the program."""
    def getInput():
        """A function to process user input."""
        txt = plain_txt.get(1.0, "end-1c")
        key = int(key_txt.get(1.0, "end-1c"))
        
        enc_list = []
        words = txt.split() # removes white space between words

        for word in words:
            temp_list=[]
            word = word.translate(str.maketrans("", "", string.punctuation))
            for char in word:
                temp_list.append(ceasarEnc(char, key))
            temp_list.append(" ") # undoing the space removal
            enc_list.extend(temp_list)
    
        enc_word = "".join(enc_list)
        encrypt_txt.insert(1.0, enc_word)
    
    # Initialize tkinter window
    root = tk.Tk()
    root.title("Ceasar's cipher")
    root.geometry('600x570')
    root.resizable(1, 1)
    
    # Configuring rows and columns
    root.rowconfigure(1, weight = 1)
    root.rowconfigure(2, weight = 2)
    root.rowconfigure(4, weight = 1)
    root.rowconfigure(5, weight = 2)
 
    root.columnconfigure(1, weight = 5)    
    root.columnconfigure(2, weight = 1)
    root.columnconfigure(3, weight = 1)
    
    # Widgets to accept user input
    plain_lbl = tk.Label(root, text = "Input the plain text to be encrypted below")
    plain_lbl.grid(row = 0, column = 0, columnspan = 6, sticky = tk.EW, padx = 5, pady = 5)

    plain_txt = tk.Text(root)
    plain_txt.grid(row = 1, column = 0, columnspan = 6, sticky = tk.EW, padx = 5, pady = 5)

    key_lbl = tk.Label(root, text = "Shifting Key: ")
    key_lbl.grid(row = 2, column = 3, pady = 5)

    key_txt = tk.Text(root, width = 10)
    key_txt.grid(row = 2, column = 4, pady = 5)

    submit = tk.Button(root, text = "Encrypt", command = getInput)
    submit.grid(row = 2, column = 5, padx = 5, pady = 5)

    # Widget to display output
    encrypt_lbl = tk.Label(root, text = "Encrypted Text")
    encrypt_lbl.grid(row = 3, column = 0, columnspan = 6, sticky = tk.EW, padx = 5, pady = 5)
    
    encrypt_txt = tk.Text(root)
    encrypt_txt.grid(row = 4, column = 0, columnspan = 6, sticky = tk.EW, padx = 5, pady = 5)
    
    root.mainloop()

main()
