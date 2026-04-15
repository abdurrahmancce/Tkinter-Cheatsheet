import tkinter as tk

# Create window
root = tk.Tk()
root.title("My App")
root.geometry("400x300")

# Placeholder text
PLACEHOLDER = "Type your message here..."

# Create Text widget
text = tk.Text(root, height=5, width=30, fg="gray")
text.pack(pady=20)

# Insert placeholder initially
text.insert("1.0", PLACEHOLDER)

# Functions to handle placeholder behavior
def on_focus_in(event):
    if text.get("1.0", "end-1c") == PLACEHOLDER:
        text.delete("1.0", "end")
        text.config(fg="black")

def on_focus_out(event):
    if text.get("1.0", "end-1c") == "":
        text.insert("1.0", PLACEHOLDER)
        text.config(fg="gray")

# Bind events
text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)

# Run app
root.mainloop()