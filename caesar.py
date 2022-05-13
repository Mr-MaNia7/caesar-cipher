"""Caesar Cipher

A program for demonstrating caesar cipher!

This application allows the user to encrypt alphabetic text
and see the encrypted text in real time. The program allows 
two types of encryptions right shift with a positive key and
left shift with a negative key. It also allows decryption in 
such a way that you will decrypt using left shift on the cipher
text encrypted with a right shift and using the same key.

The app accepts user input through a text box and it expects
the user to input only alphabetic characters along with tab 
and new-line characters. Otherwise the charaters are avoided
and hence will not be encrypted!

This program requires that `tkinter` will be installed within 
the Python environment you are running this code in.

This program contains the following functions:
    * caesarEnc - encrypts a char shifting it with a key
    * main - the main function of the program
    * processInput - accepts, parses and processes user input
    * clear - clears text-box widgets
"""

# Import necessary modules
import string
import tkinter as tk
from tkinter import messagebox

def caesarEnc(char, key):
    """An encrypting function implementing caesar cipher."""
    ascii_number = ord(char)
    skip_number = [9, 10] # new line and tab characters
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
    def processInput():
        """A function to process user input."""
        txt = plain_txt.get(1.0, "end-1c")
        try:
            key = int(key_txt.get(1.0, "end-1c"))
            enc_list = []
            words = txt.split(" ") # removes blank-space between words

            for word in words:
                temp_list = []
                remove_chars = string.punctuation + "1234567890"
                word = word.translate(str.maketrans("", "", remove_chars))
                for char in word:
                    temp_list.append(caesarEnc(char, key))
                temp_list.append(" ") # undoing the space removal
                enc_list.extend(temp_list)
    
            # removing the last trailing space
            enc_word = "".join(enc_list).rstrip()         
            encrypt_txt.delete(1.0, "end")
            encrypt_txt.insert(1.0, enc_word)
        
        except:
            messagebox.showwarning(title = "Warning", message = "Please enter an integer value for the key field!")
    
    def clear():
        """A function to clear text-box widgets."""
        plain_txt.delete(1.0, "end")
        encrypt_txt.delete(1.0, "end")

    # Initialize tkinter window
    root = tk.Tk()
    root.title("Caesar's cipher")
    # Get screen size information
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    win_width = 600
    win_height = 570

    x_begin = int((screen_width/2)-(win_width/2))
    y_begin = int((screen_height/2)-(win_height/2))
   
    root.geometry('{}x{}+{}+{}'.format(
        win_width, win_height, x_begin, y_begin
    ))
    root.resizable(1, 0)
    root.configure(bg = "#e1f2f2")

    # Configuring rows and columns
    root.rowconfigure(1, weight = 1)
    root.rowconfigure(2, weight = 2)
    root.rowconfigure(4, weight = 1)
    root.rowconfigure(5, weight = 2)
 
    root.columnconfigure(1, weight = 5)    
    root.columnconfigure(2, weight = 1)
    root.columnconfigure(3, weight = 1)
    
    # Widgets to accept user input
    plain_lbl = tk.Label(root, text = "Input the plain text to be encrypted below", bg = "#e1f2f2", fg = "#000", font = (14))
    plain_lbl.grid(row = 0, column = 0, columnspan = 7, sticky = tk.EW, padx = 5, pady = 5)

    plain_txt = tk.Text(root)
    plain_txt.grid(row = 1, column = 0, columnspan = 7, sticky = tk.EW, padx = 5, pady = 5)

    key_lbl = tk.Label(root, text = "Key", bg = "#e1f2f2", fg = "#000")
    key_lbl.grid(row = 2, column = 3, pady = 5)

    key_txt = tk.Text(root, width = 10)
    key_txt.grid(row = 2, column = 4, pady = 5)

    clear_btn = tk.Button(root, text = "Clear", command = clear, bg = "#FF0000", fg = "#F5F5F5",
        highlightbackground = "#FF0000", activebackground = "#F5F5F5", activeforeground = "#FF0000")
    clear_btn.grid(row = 2, column = 5, pady = 5, padx = 5)

    submit_btn = tk.Button(root, text = "Encrypt", command = processInput, bg = "#0000FF", fg = "#F5F5F5", 
       highlightbackground = "#0000FF", activebackground = "#F5F5F5", activeforeground = "#0000FF")
    submit_btn.grid(row = 2, column = 6, padx = 5, pady = 5)

    # Widget to display output
    encrypt_lbl = tk.Label(root, text = "Encrypted Text", bg = "#e1f2f2", fg = "#000", font = (14))
    encrypt_lbl.grid(row = 3, column = 0, columnspan = 7, sticky = tk.EW, padx = 5, pady = 5)
    
    encrypt_txt = tk.Text(root)
    encrypt_txt.grid(row = 4, column = 0, columnspan = 7, sticky = tk.EW, padx = 5, pady = 5)
    
    root.mainloop()

main()