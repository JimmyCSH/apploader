import tkinter as tk
from tkinter import filedialog, Text
import os

# Set TKinter Window Properties
root = tk.Tk()
root.resizable(width = False, height = False)
root.title("App Loader")

addedApps = []

if os.path.isfile('save.txt'):
    with open ('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')

def add():
    # Allow adding of widgets without duplication
    for widget in appFrame.winfo_children():
        widget.destroy()
    
    # Allow adding .exe files to frame
    file = filedialog.askopenfilename(initialdir = "/", title = "Select File", 
        filetypes = (("executables", "*.exe"), ("all files", "*.*")))
    
    addedApps.append(file)

    # Draw added apps
    for app in addedApps:
        label = tk.Label(appFrame, text = app, width = 385)
        label.pack()

def run():
    for app in addedApps:
        os.startfile(app)

def save():
    saveFiles = [('All Files', '*.*'), ('Text Document', '*.txt')]
    saveFile = filedialog.asksaveasfile(filetypes = saveFiles, defaultextension = saveFiles)

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
    bg = "#FFB247", borderwidth = 0, command = add)
openFile.pack(pady = 30)

# Button for Running Files
runFile = tk.Button(logicFrame, text = "Run File(s)", padx = 40, pady = 6, fg = "white", 
    bg = "#FFB247", borderwidth = 0, command = run)
runFile.pack()

# Button for Saving Configuration
saveConfiguration = tk.Button(logicFrame, text = "Save Configuration", padx = 17, pady = 6, 
    fg = "white", bg = "#FFB247", borderwidth = 0, command = save)
saveConfiguration.pack(pady = 30)

# Button for Loading Configuration
loadConfiguration = tk.Button(logicFrame, text = "Load Configuration", padx = 17, pady = 6, 
    fg = "white", bg = "#FFB247", borderwidth = 0)
loadConfiguration.pack()

exit = tk.Button(logicFrame, text = "Exit", padx = 20, pady = 20, 
    fg = "#3D426B", bg = "white", borderwidth = 0)
exit.pack(pady = 30)

# Run Main Loop
root.mainloop()

with open('save.txt', 'w') as f:
    for app in addedApps:
        f.write(app + ',')