import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("600x400") 

large_font = ("Arial", 16)

label = tk.Label(root, text="Name", font=large_font)
label.grid(row=0, column=0, padx=20, pady=20)

entry = tk.Entry(root, font=large_font, width=30)
entry.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()