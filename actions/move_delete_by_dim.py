import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from moviepy.editor import VideoFileClip
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
import pandas as pd
import cv2
# Start of main code
# Declare variables
min_width = 0
min_height = 0
video_directory = ""
output_directories = ""
destination_directory = ""
deleted_files = []

def save_file(dir):
    # Create a timestamp for the Excel file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    use_path = f"{dir}/"
    # excel_file_name = f"S:\deleted_files_by_dim{timestamp}.xlsx"
    excel_file_name = f"{use_path}deleted_files_{timestamp}.xlsx"
    saved_excel_file_name = f"{use_path}saved_files_{timestamp}.xlsx"

    # Convert the list of deleted files to a DataFrame
    df = pd.DataFrame(deleted_files, columns=["File Name", "Width", "Length"])

    # Save the DataFrames to an Excel file
    df.to_excel(excel_file_name, index=False, engine="openpyxl")
    print(f"Deleted files and their dimensions saved to {excel_file_name}")

def get_dir():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()
    # Ask the user to select a directory using a file dialog
    video_directory = filedialog.askdirectory(title="Select the directory containing your video files")
    # print(video_directory)
    # Check if the user canceled the file dialog
    if not video_directory:
        print("Directory selection canceled. Exiting.")
    else:
        return video_directory

def get_min_width():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    width_value = simpledialog.askstring("Minimum Width", "Enter the minimum video width:/t/t/t", initialvalue=480)

    try:
        min_width = float(width_value)
        return min_width
    except (ValueError, TypeError):
        return None

def get_min_height():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    height_value = simpledialog.askstring("Minimum Height", "Enter the minimum video height:/t/t/t", initialvalue=480)

    try:
        min_height = float(height_value)
        return min_height
    except (ValueError, TypeError):
        return None

def both_actions():
    video_directory = get_dir()
    # Create the output directories for different dimensions
    output_directories = {
        'vert': os.path.join(video_directory, 'vert'),
        'horz': os.path.join(video_directory, 'horz'),
        'square': os.path.join(video_directory, 'square')
    }
    # Ensure the output directories exist, and if not, create them
    for output_dir in output_directories.values():
        os.makedirs(output_dir, exist_ok=True)

    # Get min dimensions
    min_width = get_min_width()
    min_height = get_min_height()
    # List all files in the selected directory
    # print(video_directory)
    files_deleted = False
    video_files = [f for f in os.listdir(video_directory) if f.endswith((('.mp4', '.avi', '.mkv', '.mov', '.mpg', '.m4p', '.wmv', '.ts', '.vob', '.mpeg', '.3gp', '.m4v', '.m2ts')))]
    # Loop through each video file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        # Load the video file using MoviePy
        video = VideoFileClip(video_path)
        # Get the video dimensions (resolution)
        video_width, video_height = video.size
        # Determine the dimensions category (vertical, horizontal, or square)
        if video_width < video_height:
            dimensions = 'vert'
        elif video_width > video_height:
            dimensions = 'horz'
        else:
            dimensions = 'square'
        # Close the video file
        video.close()
        # Print the video name, size, and dimensions
        # print(f"Video Name: {video_file} Dimensions {video_width}x{video_height} pixels: Category: {dimensions}")
        # print(f"Video Width is {video_width} and Minimum Width is {min_width}, Video Height is {video_height} and Minimum Height is {min_height}")
        # Check if the width is less than the minimum width and delete the video
        if (video_width < min_width) or (video_height < min_height):
            os.remove(video_path)
            deleted_files.append((video_file, video_width, video_height))
            print(f"Deleted {video_file} for small dimensions.")
            files_deleted = True
        else:
            # Move the video to the appropriate output directory
            destination_dir = output_directories.get(dimensions)
            if destination_dir:
                destination_path = os.path.join(destination_dir, video_file)
                os.rename(video_path, destination_path)
                print(f"Moved {video_file} to '{dimensions}' folder.")
                # print()
    print("All Done Deleting and Moving Files!")
    print(files_deleted)
    if files_deleted:
        save_file(video_directory)
    else:
        print("No files deleted by dim")

def move_all():
    video_directory = get_dir()
    # Create the output directories for different dimensions
    output_directories = {
        'vert': os.path.join(video_directory, 'vert'),
        'horz': os.path.join(video_directory, 'horz'),
        'square': os.path.join(video_directory, 'square'),
        'too_small': os.path.join(video_directory, 'too_small')
    }
    # Ensure the output directories exist, and if not, create them
    for output_dir in output_directories.values():
        os.makedirs(output_dir, exist_ok=True)

    # Get min dimensions
    min_width = get_min_width()
    min_height = get_min_height()
    # List all files in the selected directory
    # print(video_directory)
    files_deleted = False
    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4', '.3gp', '.m4v'))]
    # Loop through each video file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        # Load the video file using MoviePy
        video = VideoFileClip(video_path)
        # Get the video dimensions (resolution)
        video_width, video_height = video.size
        # Determine the dimensions category (vertical, horizontal, or square)
        if (video_width < min_width) or (video_height < min_height):
            dimensions = 'too_small'
        elif video_width < video_height:
            dimensions = 'vert'
        elif video_width > video_height:
            dimensions = 'horz'
        else:
            dimensions = 'square'
        # Close the video file
        video.close()
        # Print the video name, size, and dimensions
        # print(f"Video Name: {video_file} Dimensions {video_width}x{video_height} pixels: Category: {dimensions}")
        # print(f"Video Width is {video_width} and Minimum Width is {min_width}, Video Height is {video_height} and Minimum Height is {min_height}")
        # Check if the width is less than the minimum width and delete the video
        # Move the video to the appropriate output directory
        destination_dir = output_directories.get(dimensions)
        if destination_dir:
            destination_path = os.path.join(destination_dir, video_file)
            os.rename(video_path, destination_path)
            print(f"Moved {video_file} to '{dimensions}' folder.")
            # print()
    print("All Done Moving Files!")

def delete_by_dim():
    video_directory = get_dir()
    # Create the output directories for different dimensions
    # Get min dimensions
    min_width = get_min_width()
    min_height = get_min_height()
    files_deleted = False
    # List all files in the selected directory
    print(video_directory)
    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4','.m4v'))]
    # Loop through each video file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        # Load the video file using MoviePy
        video = VideoFileClip(video_path)
        # Get the video dimensions (resolution)
        video_width, video_height = video.size
        # Determine the dimensions category (vertical, horizontal, or square)
        if video_width < video_height:
            dimensions = 'vert'
        elif video_width > video_height:
            dimensions = 'horz'
        else:
            dimensions = 'square'
        # Close the video file
        video.close()

        # Print the video name, size, and dimensions
        # print(f"Video Name: {video_file} Dimensions {video_width}x{video_height} pixels: Category: {dimensions}")
        # print(f"Video Width is {video_width} and Minimum Width is {min_width}, Video Height is {video_height} and Minimum Height is {min_height}")
        # Check if the width is less than the minimum width and delete the video
        if (video_width < min_width) or (video_height < min_height):
            os.remove(video_path)
            deleted_files.append((video_file, video_width, video_height))
            print(f"Deleted {video_file} for small dimensions.")
            # print()
            files_deleted = True

    print("All Done Deleting Files!")
    if files_deleted:
        save_file(video_directory)
    else:
        print("No files deleted by dim")

def move_by_dim():
    video_directory = get_dir()
    # Create the output directories for different dimensions
    output_directories = {
        'vert': os.path.join(video_directory, 'vert'),
        'horz': os.path.join(video_directory, 'horz'),
        'square': os.path.join(video_directory, 'square')
    }
    # Ensure the output directories exist, and if not, create them
    for output_dir in output_directories.values():
        os.makedirs(output_dir, exist_ok=True)
    # List all files in the selected directory
    # print(video_directory)
    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4', '.m4v'))]
    # Loop through each video file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        # Load the video file using MoviePy
        video = VideoFileClip(video_path)
        # Get the video dimensions (resolution)
        video_width, video_height = video.size
        # Determine the dimensions category (vertical, horizontal, or square)
        if video_width < video_height:
            dimensions = 'vert'
        elif video_width > video_height:
            dimensions = 'horz'
        else:
            dimensions = 'square'
        # Close the video file
        video.close()
        # Print the video name, size, and dimensions
        # print(f"Video Name: {video_file} Dimensions {video_width}x{video_height} pixels: Category: {dimensions}")
        # print(f"Video Width is {video_width} and Minimum Width is {min_width}, Video Height is {video_height} and Minimum Height is {min_height}")
        # Check if the width is less than the minimum width and delete the video
        # Move the video to the appropriate output directory
        destination_dir = output_directories.get(dimensions)
        if destination_dir:
            destination_path = os.path.join(destination_dir, video_file)
            os.rename(video_path, destination_path)
            print(f"Moved {video_file} to '{dimensions}' folder.")
            # print()
    print("All Done Moving Files!")

def main_script():
    mainroot = ttk.Window(themename="superhero")
    mainroot.title("Choose Video Move and Delete Actions")
    mainroot.geometry("750x250")
    label = ttk.Label(mainroot, text="What do you want to do?")
    label.pack()
    button1 = ttk.Button(mainroot, text="Delete videos by dimension", bootstyle="success, outline",
                         command=delete_by_dim)
    button2 = ttk.Button(mainroot, text="Move videos to dimensions folder", bootstyle="sucess, outline",
                         command=move_by_dim)
    button3 = ttk.Button(mainroot, text="Move to dim folder and delete small", bootstyle="sucess, outline",
                         command=both_actions)
    button4 = ttk.Button(mainroot, text="Move all files by dimensions", bootstyle="sucess, outline",
                         command=move_all)
    button5 = ttk.Button(mainroot, text="Quit", bootstyle="sucess, outline", command=quit)
    # Pack the buttons into the window
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    # Start the Tkinter main loop
    mainroot.mainloop()

if __name__ == "__main__":
    # This block will only run if the script is executed directly, not when imported as a module
    main_script()