# Create a button
import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("480x300")

button = tk.Button(root, text="Click Me")
button.pack()

root.mainloop()