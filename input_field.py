import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("My App")
root.geometry("400x300")

# Create the Input Field (Entry widget)
entry = tk.Entry(root)
entry.pack(pady=10)  # Added a little padding for better looks

# Optional: Function to print the input to the console
def get_input():
    user_text = entry.get()
    print(f"User entered: {user_text}")

# Optional: Button to trigger the 'get' action
button = tk.Button(root, text="Submit", command=get_input)
button.pack()

# Start the application loop
root.mainloop()