"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules
# Create a window object
window = Tk()     # Create a window object

# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
number1 = simpledialog.askinteger('Infuriating Calculator', "Enter a number")
# Ask the user for the second number
number2 = simpledialog.askinteger('Infuriating Calculator', "Enter a second number")
# Ask the user for the math operation
operation = simpledialog.askstring('Infuriating Calculator', "Type an operation(multiply, divide, add, subtract)")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == 'multiply':
    messagebox.showinfo('Infuriating Calculator', number1 * number2)

elif operation == 'divide':
    messagebox.showinfo('infuriating Calculator', number1 / number2)

elif operation == 'add':
    messagebox.showinfo('Infuriating Calculator', number1 + number2)

elif operation == 'subtract':
    messagebox.showinfo('Infuriating Calculator', number1 - number2)
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
else:
    messagebox.showerror('error', "type an operation")
# Keep the window open
window.mainloop()