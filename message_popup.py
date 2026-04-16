import tkinter as tk
from tkinter import messagebox

def show_msg():
    messagebox.showinfo("Title", "Hello!")

# Create window
root = tk.Tk()
root.title("My App")
root.geometry("400x300")

# Button to show popup
tk.Button(root, text="Show", command=show_msg).pack(pady=50)

# Run app
root.mainloop()