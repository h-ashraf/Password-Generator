import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password based on user input
def generate_password():
    length = int(length_slider.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_special_chars = special_chars_var.get()

    # Base character set (lowercase letters by default)
    characters = string.ascii_lowercase

    # Add options based on user's selection
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        messagebox.showerror("Error", "Please select at least one character set!")
        return
    
    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display password in the Entry widget
    password_entry.delete(0, tk.END)  # Clear existing text
    password_entry.insert(0, password)  # Insert new password

# Function to reset all fields to their default values
def reset_fields():
    length_slider.set(12)  # Reset slider to default value (12)
    uppercase_var.set(False)  # Uncheck "Include Uppercase Letters"
    numbers_var.set(False)  # Uncheck "Include Numbers"
    special_chars_var.set(False)  # Uncheck "Include Special Characters"
    password_entry.delete(0, tk.END)  # Clear the password entry field

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Labels
tk.Label(root, text="Password Length:").pack(pady=10)

# Password length slider
length_slider = tk.Scale(root, from_=6, to_=32, orient=tk.HORIZONTAL)
length_slider.set(12)  # Default length set to 12
length_slider.pack(pady=10)

# Checkboxes for including options
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var).pack(anchor='w')

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Entry to display the generated password
password_entry = tk.Entry(root, width=30, font=('Arial', 12))
password_entry.pack(pady=10)

# Button to reset all fields
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
