"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

# Create a window object
window = Tk()     # Create a window object

# Hide the window, hint: use the withdraw method
window = Tk()     # Create a window object

# Ask the user for the first number   
number1 = simpledialog.askinteger('Simple Adder', "Enter a number")
# Ask the user for the second number
number2 = simpledialog.askinteger('Simple Adder', "Enter a second number")
# Display the sum of the two numbers 
messagebox.showinfo('Simple Adder', number1 + number2)
# Keep the window open
window.mainloop()
