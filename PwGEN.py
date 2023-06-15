from tkinter import *
import random
import string

#   UI SETUP

# Create a window
window = Tk()
window.title("OfflinePW_Generator")
window.config(padx=100, pady=10)

# Create a Label for the title
title_label = Label(text="Welcome to the Offline Password generator", font=("Roboto", 20, "bold"))
title_label.grid(row=0)

# Create a Label for the title_text1
title_text1 = Label(text="Please check the boxes below\nand drag the slider in oreder to\ndetermin your passwords format", font=("Roboto", 10))
title_text1.grid(row=1)

# Create a Label for letters, numbers, and symbols
letters = Label(text="Check the box for letters    ", font=("Roboto", 10)) 
letters.grid(column=0, row=2, pady=5)
numbers = Label(text="Check the box for numbers", font=("Roboto", 10))
numbers.grid(column=0, row=3, pady=5)
symbols = Label(text="Check the box for symbols", font=("Roboto", 10))
symbols.grid(column=0, row=4, pady=5)

# Frame for letters
letters_frame = Frame(window)
letters_frame.grid(column=1, row=2, padx=1, sticky=W)

# Create BooleanVar() variables for the checkboxes
is_checked_L = BooleanVar()
is_checked_U = BooleanVar()
is_checked_N = BooleanVar()
is_checked_S = BooleanVar()

# Create Checkbuttons for the letters, uppercase and lowercase
letters_checkbox_L = Checkbutton(letters_frame, text="Lowercase", variable=is_checked_L)
letters_checkbox_L.grid(column=0, row=0)

letters_checkbox_U = Checkbutton(letters_frame, text="Uppercase", variable=is_checked_U)
letters_checkbox_U.grid(column=1, row=0)

# Create Checkbuttons for the numbers
numbers_checkbox = Checkbutton(text="", variable=is_checked_N)
numbers_checkbox.grid(column=1, row=3, padx=1, sticky=W)
# Create Checkbuttons for the symbols
symbols_checkbox = Checkbutton(text="", variable=is_checked_S)
symbols_checkbox.grid(column=1, row=4, padx=1, sticky=W)

# Create scale for letters
letters_scale = Scale(window, from_=0, to=10, orient=HORIZONTAL, width=20, troughcolor="gray", tickinterval=0)
letters_scale.grid(column=2, row=2)

# Create scale for numbers
numbers_scale = Scale(window, from_=0, to=10, orient=HORIZONTAL, width=20, troughcolor="gray", tickinterval=0)
numbers_scale.grid(column=2, row=3)

# Create scale for symbols
symbols_scale = Scale(window, from_=0, to=10, orient=HORIZONTAL, width=20, troughcolor="gray", tickinterval=0)
symbols_scale.grid(column=2, row=4)

new_pass_label = Label(text="New PASSWORD generated is", font=("Roboto", 15, "bold"))
new_pass_label.grid(row=5)

password_generated = Text(window, height=1, width=45)
password_generated.grid(row=6)


def generate_password():
    # create an empty list to store selected options
    options = []
    
    # check the state of each checkbox and add its corresponding options to the list
    if is_checked_L.get():
        options.extend(string.ascii_lowercase)
    if is_checked_U.get():
        options.extend(string.ascii_uppercase)
    if is_checked_N.get():
        options.extend(string.digits)
    if is_checked_S.get():
        options.extend(string.punctuation)
    
    # generate a password using the selected options and scale values
    if options:
        password_length = letters_scale.get() + numbers_scale.get() + symbols_scale.get()
        
        # ensure that the password length is at least 1
        password_length = max(password_length, 1)
        
        password = ''.join(random.choice(options) for _ in range(password_length))
        password_generated.delete('1.0', END)  # clear the existing content of the Text widget
        password_generated.insert(END, password)  # display the generated password in the Text widget
    else:
        password_generated.delete('1.0', END)
        password_generated.insert(END, "Please select at least one option.")

# create a button to generate a password
generate_button = Button(window, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=7)


window.mainloop()
