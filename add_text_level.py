import tkinter as tk

# Create window
root = tk.Tk()
root.title("My App")
root.geometry("400x300")

# Add text (Label)
label = tk.Label(root, text="Hello, World! Welcome to Tkinter. This is a simple label using Tkinter.")
label.pack()

# Run the application
root.mainloop()