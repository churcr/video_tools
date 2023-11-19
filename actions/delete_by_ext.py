import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def remove_files_by_ext(directory, extensions):
    for ext in extensions:
        for root, dirs, files in os.walk(directory):
            for file in files:
                # print(f"{files}")
                if file.endswith(ext):
                    file_path = os.path.join(root, file)
                    print(f"Removing {file_path} with {ext} extension")
                    os.remove(file_path)

# Get the directory using filedialog.askdirectory
root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory(title="Select Directory")

if directory:
    # Get the extension using simpledialog.askstring
    # extension = simpledialog.askstring("Input", "Enter file extension (e.g., .jpg):")
    extension = ".jpg"
    if extension:
        # Remove files with the specified extension
        remove_files_by_ext(directory, [extension])
        # print(f"Removed {file} with {extension} files from {directory}")
    else:
        print("Extension not provided.")
else:
    print("Directory not selected.")
