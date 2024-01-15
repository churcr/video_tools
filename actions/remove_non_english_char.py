import os
import re
import tkinter as tk
from tkinter import filedialog

def remove_non_english_chars(input_string):
    # pattern = r'[^a-zA-Z0-9()-.]'
    # pattern = r'[^a-zA-Z0-9_()-\.]'
    # pattern = r'[^a-zA-Z0-9_()\-.\']'
    # pattern = r'[^a-zA-Z0-9_()\-.\' ]'
    pattern = r'[^a-zA-Z0-9_()\-.\' ]+'
    cleaned_string = re.sub(pattern, ' ', input_string)
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)  # Collapse multiple spaces
    cleaned_string = cleaned_string.strip()  # Remove leading/trailing spaces

    # Remove trailing spaces before the extension
    base, extension = os.path.splitext(cleaned_string)
    cleaned_string = base.rstrip() + extension

    return cleaned_string
    # return cleaned_string
    # return cleaned_string.strip()  # Remove leading/trailing spaces
def process_files_in_directory(directory_path, extensions):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                original_file_path = os.path.join(root, file)
                cleaned_file_name = remove_non_english_chars(file)
                cleaned_file_path = os.path.join(root, cleaned_file_name)
                if original_file_path == cleaned_file_path:
                    continue
                else:
                    counter = 1
                    while os.path.exists(cleaned_file_path):
                        base, extension = os.path.splitext(cleaned_file_name)
                        cleaned_file_name = f"{base}{counter}{extension}"
                        cleaned_file_path = os.path.join(root, cleaned_file_name)
                        counter += 1

                    print(f'{original_file_path} RENAMED TO {cleaned_file_path}')
                    os.rename(original_file_path, cleaned_file_path)

def main():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")

    if folder_path:
        extensions = [('.mp4', '.avi', '.mkv', '.mov', '.mpg', '.m4p', '.wmv', '.ts', '.vob', '.mpeg', '.3gp', '.m4v', '.m2ts')]  # Add the desired file extensions
        process_files_in_directory(folder_path, extensions)
        print("File names cleaned successfully!")

if __name__ == "__main__":
    main()
