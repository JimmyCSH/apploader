import tkinter as tk
from tkinter import filedialog, Text
import os

# Set TKinter Window Properties
root = tk.Tk()
root.resizable(width = False, height = False)
root.title("App Loader")

# Create Canvas
screen = tk.Canvas(root, height = 400, width = 700, bg="#FFB247")
screen.pack()

# Add Frame for Buttons/Logic
frame = tk.Frame(root, bg="#3D426B")
frame.place(relwidth = 0.3, relheight = 0.80, rely = 0.1, relx = 0.05)

# Add Frame for Applications
frame = tk.Frame(root, bg="white")
frame.place(relwidth = 0.55, relheight = 0.80, rely = 0.1, relx = 0.4)

# Run Main Loop
root.mainloop()