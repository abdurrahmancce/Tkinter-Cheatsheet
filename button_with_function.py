import tkinter as tk

def say_hello():
    message_label.config(text="Hello! You clicked the button! 👋", foreground="#0066ff")
    print("Hello!")   # Still prints to console

# Main Window
root = tk.Tk()
root.title("My App")
root.geometry("500x380")
root.configure(bg="#f0f4f8")

# Title
title = tk.Label(root, 
                 text="Button with Function",
                 font=("Arial", 18, "bold"),
                 bg="#f0f4f8",
                 fg="#1e40af")
title.pack(pady=25)

# Button
button = tk.Button(root,
                   text="Click Me",
                   command=say_hello,
                   font=("Arial", 14, "bold"),
                   bg="#3b82f6",
                   fg="white",
                   activebackground="#2563eb",
                   activeforeground="white",
                   padx=30,
                   pady=12)
button.pack(pady=30)

# Message Label (shows feedback inside the window)
message_label = tk.Label(root,
                         text="Click the button to say hello",
                         font=("Arial", 13),
                         bg="#f0f4f8",
                         fg="#555555")
message_label.pack(pady=20)

# Footer
footer = tk.Label(root, 
                  text="Function connected successfully ✅",
                  font=("Arial", 10),
                  bg="#f0f4f8",
                  fg="#777777")
footer.pack(side="bottom", pady=30)

root.mainloop()