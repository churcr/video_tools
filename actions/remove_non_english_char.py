import os
import re
import tkinter as tk
from tkinter import filedialog

def remove_non_english_chars(input_string):
    # pattern = r'[^a-zA-Z0-9()-.]'
    # pattern = r'[^a-zA-Z0-9_()-\.]'
    # pattern = r'[^a-zA-Z0-9_()\-.\']'
    pattern = r'[^a-zA-Z0-9_()\-.\' ]!'
    cleaned_string = re.sub(pattern, ' ', input_string)
    return cleaned_string

def process_files_in_directory(directory_path, extensions):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                original_file_path = os.path.join(root, file)
                cleaned_file_name = remove_non_english_chars(file)
                cleaned_file_path = os.path.join(root, cleaned_file_name)
                os.rename(original_file_path, cleaned_file_path)
                if original_file_path == cleaned_file_path:
                    continue
                print(f"{original_file_path} has been renamed to {cleaned_file_path}")


def main():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")

    if folder_path:
        extensions = ['.mp4', '.mkv']  # Add the desired file extensions
        process_files_in_directory(folder_path, extensions)
        print("File names cleaned successfully!")

if __name__ == "__main__":
    main()
