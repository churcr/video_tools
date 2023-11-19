import os
import tkinter as tk
from tkinter import filedialog
import shutil

# Move files to parent - Only works if 3 levels deep.
def move_files(parent_folder):
    # Get a list of all second-level subfolders in the specified folder
    second_level_subfolders = [subfolder for subfolder in os.listdir(parent_folder) if
                               os.path.isdir(os.path.join(parent_folder, subfolder))]

    # Loop through each second-level subfolder
    for second_level_subfolder in second_level_subfolders:
        second_level_subfolder_path = os.path.join(parent_folder, second_level_subfolder)

        # Get a list of all third-level subfolders in the second-level subfolder
        third_level_subfolders = [subfolder for subfolder in os.listdir(second_level_subfolder_path) if
                                  os.path.isdir(os.path.join(second_level_subfolder_path, subfolder))]

        # Loop through each third-level subfolder
        for third_level_subfolder in third_level_subfolders:
            third_level_subfolder_path = os.path.join(second_level_subfolder_path, third_level_subfolder)

            # Get a list of all files in the third-level subfolder
            files = [file for file in os.listdir(third_level_subfolder_path) if
                     os.path.isfile(os.path.join(third_level_subfolder_path, file))]

            # Loop through each file and move it to the second-level subfolder
            for file in files:
                file_path = os.path.join(third_level_subfolder_path, file)
                new_path = os.path.join(second_level_subfolder_path, file)
                shutil.move(file_path, new_path)
                print(f"Moved {file} in {file_path } to {new_path}")

            # Remove the empty third-level subfolder
            os.rmdir(third_level_subfolder_path)
            print(f"Removed {third_level_subfolder_path}")
    print("All done moving files to parent")

# Get the directory using filedialog.askdirectory
root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory(title="Select Directory")

if directory:
    # Move files to parent
    move_files(directory)
else:
    print("Directory not selected")
