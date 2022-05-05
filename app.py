import tkinter as tk
from tkinter import filedialog, Text
import os

# Set TKinter Window Properties
root = tk.Tk()
root.resizable(width = False, height = False)
root.title("App Loader")

# Create Canvas
screen = tk.Canvas(root, height = 400, width = 700, bg = "#FFB247")
screen.pack()

# Add Frame for Buttons/Logic
logicFrame = tk.Frame(root, bg = "#3D426B")
logicFrame.place(relwidth = 0.3, relheight = 0.80, rely = 0.1, relx = 0.05)

# Add Frame for Applications
appFrame = tk.Frame(root, bg = "white")
appFrame.place(relwidth = 0.55, relheight = 0.80, rely = 0.1, relx = 0.4)

# Button for Opening Files
openFile = tk.Button(logicFrame, text = "Open File", padx = 40, pady = 6, fg = "white", 
    bg = "#FFB247", borderwidth = 0)
openFile.pack(pady = 30)

# Button for Running Files
runFile = tk.Button(logicFrame, text = "Run File(s)", padx = 40, pady = 6, fg = "white", 
    bg = "#FFB247", borderwidth = 0)
runFile.pack()

# Button for Saving Configuration
saveConfiguration = tk.Button(logicFrame, text = "Save Configuration", padx = 17, pady = 6, 
    fg = "white", bg = "#FFB247", borderwidth = 0)
saveConfiguration.pack(pady = 30)

# Button for Loading Configuration
loadConfiguration = tk.Button(logicFrame, text = "Load Configuration", padx = 17, pady = 6, 
    fg = "white", bg = "#FFB247", borderwidth = 0)
loadConfiguration.pack()

# Run Main Loop
root.mainloop()