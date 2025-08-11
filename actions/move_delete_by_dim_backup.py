import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from moviepy.editor import VideoFileClip
import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
from datetime import datetime
import pandas as pd
import shutil
# from shutil import copy
# from os import remove
# import cv2
# Start of main code
# Declare variables
min_width = 0
vert_min_width = 0
horz_min_width = 0
square_min_width_height = 0
min_height = 0
vert_min_height = 0
horz_min_height = 0
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

def get_vert_min_width():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    vert_width_value = simpledialog.askstring("Minimum Vertical Width", "Enter the minimum vertical video width:", initialvalue=480)

    try:
        vert_min_width = float(vert_width_value)
        return vert_min_width
    except (ValueError, TypeError):
        return None

def get_horz_min_width():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    horz_width_value = simpledialog.askstring("Minimum Horizontal Width", "Enter the minimum horizontal video width:", initialvalue=720)

    try:
        horz_min_width = float(horz_width_value)
        return horz_min_width
    except (ValueError, TypeError):
        return None

def get_vert_min_height():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    vert_height_value = simpledialog.askstring("Minimum Vertical Height", "Enter the minimum vertical video height:", initialvalue=720)

    try:
        vert_min_height = float(vert_height_value)
        return vert_min_height
    except (ValueError, TypeError):
        return None
def get_horz_min_height():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    horz_height_value = simpledialog.askstring("Minimum Horizontal Height", "Enter the minimum horizontal video height:", initialvalue=480)

    try:
        horz_min_height = float(horz_height_value)
        return horz_min_height
    except (ValueError, TypeError):
        return None

def get_square_min_width_height():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    square_min_value = simpledialog.askstring("Minimum Square Width and Height", "Enter the minimum square video width and height:", initialvalue=480)

    try:
        square_min_width_height = float(square_min_value)
        return square_min_width_height
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
    vert_min_width = get_vert_min_width()
    vert_min_height = get_vert_min_height()
    horz_min_width = get_horz_min_width()
    horz_min_height = get_horz_min_height()
    square_min_width_height = get_square_min_width_height()
    # List all files in the selected directory
    # print(video_directory)
    files_deleted = False
    video_files = [f for f in os.listdir(video_directory) if f.endswith((('.mp4', '.avi', '.mkv', '.mov', '.mpg', '.m4p', '.wmv', '.ts', '.vob', '.mpeg', '.3gp', '.m4v', '.m2ts')))]
    # Loop through each video file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        # Load the video file using MoviePy
        video = VideoFileClip(video_path)
        video_length = video.duration
        if video_length > 0:
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
            print(f"Video Name: {video_file} Dimensions {video_width}x{video_height} pixels: Category: {dimensions}")
            print(f"Video Width is {video_width} and Minimum Width is {min_width}, Video Height is {video_height} and Minimum Height is {min_height}")
            # Check the dimensions
            if (video_width < vert_min_width) and (video_height < vert_min_height):
                # Video is smaller then the minimum vertical dimensions
                os.remove(video_path)
                deleted_files.append((video_file, video_width, video_height))
                print(f"Deleted {video_file} for small dimensions.")
                files_deleted = True
            elif (video_width < horz_min_width) and (video_height < horz_min_height):
                # Video is smaller then the minimum horizontal dimensions
                os.remove(video_path)
                deleted_files.append((video_file, video_width, video_height))
                print(f"Deleted {video_file} for small dimensions.")
                files_deleted = True
            elif (video_width < square_min_width_height) and (video_height < square_min_width_height):
                # Video is smaller then the minimum square dimensions
                os.remove(video_path)
                deleted_files.append((video_file, video_width, video_height))
                print(f"Deleted {video_file} for small dimensions.")
                files_deleted = True
            else:
                # Video passed all dimension tests so move the video to the appropriate output directory
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
    vert_min_width = get_vert_min_width()
    vert_min_height = get_vert_min_height()
    horz_min_width = get_horz_min_width()
    horz_min_height = get_horz_min_height()
    square_min_width_height = get_square_min_width_height()
    # List all files in the selected directory
    # print(video_directory)
    files_deleted = False
    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4', '.3gp', '.m4v'))]
    # Loop through each video file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        # Load the video file using MoviePy
        video = VideoFileClip(video_path)
        vid_length = video.duration
        if vid_length > 0:
            # Get the video dimensions (resolution)
            video_width, video_height = video.size
            # Determine the dimensions category (vertical, horizontal, or square)
            if ((video_width < vert_min_width) and (video_height < vert_min_height)) or \
            ((video_width < horz_min_width) and (video_height < horz_min_height)) or \
            ((video_width < square_min_width_height) and (video_height < square_min_width_height)):
                dimensions = 'too small'
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

def delete_too_small_dim():
    video_directory = get_dir()
    # Create the output directories for different dimensions
    # Get min dimensions
    vert_min_width = get_vert_min_width()
    vert_min_height = get_vert_min_height()
    horz_min_width = get_horz_min_width()
    horz_min_height = get_horz_min_height()
    square_min_width_height = get_square_min_width_height()
    files_deleted = False
    # List all files in the selected directory
    print(video_directory)
    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4','.m4v'))]
    # Loop through each video file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        # Load the video file using MoviePy
        video = VideoFileClip(video_path)
        vid_length = video.duration
        if vid_length > 0:
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
        if ((video_width < vert_min_width) and (video_height < vert_min_height)) or \
                ((video_width < horz_min_width) and (video_height < horz_min_height)) or \
                ((video_width < square_min_width_height) and (video_height < square_min_width_height)):
            os.remove(video_path)
            deleted_files.append((video_file, video_width, video_height))
            print(f"Deleted {video_path} for small dimensions.")
            # print()
            files_deleted = True
        else:
            print(f"Kept {video_path}")

    print("All Done Deleting Files!")
    if files_deleted:
        save_file(video_directory)
    else:
        print("No files deleted by dim")

def move_too_small_dim():
    video_directory = get_dir()

    # Create the output directory for videos with small dimensions
    small_dim_dir = os.path.join(video_directory, 'too_small_dim')
    os.makedirs(small_dim_dir, exist_ok=True)

    # Get min dimensions
    vert_min_width = get_vert_min_width()
    vert_min_height = get_vert_min_height()
    horz_min_width = get_horz_min_width()
    horz_min_height = get_horz_min_height()
    square_min_width_height = get_square_min_width_height()

    files_moved = False

    # Recursively list all files in the selected directory and its subdirectories
    for root, dirs, files in os.walk(video_directory):
        for filename in files:
            if filename.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4', '.m4v')):
                video_path = os.path.join(root, filename)

                try:
                    # Load the video file using MoviePy
                    video = VideoFileClip(video_path)
                    vid_length = video.duration

                    if vid_length > 0:
                        # Get the video dimensions (resolution)
                        video_width, video_height = video.size

                    # Determine the dimensions category (vertical, horizontal, or square)
                    if video_width < video_height:
                        dimensions = 'vert'
                    elif video_width > video_height:
                        dimensions = 'horz'
                    else:
                        dimensions = 'square'

                    # Check if the video dimensions are less than the minimum dimensions
                    if ((video_width < vert_min_width) and (video_height < vert_min_height)) or \
                        ((video_width < horz_min_width) and (video_height < horz_min_height)) or \
                        ((video_width < square_min_width_height) and (video_height < square_min_width_height)):

                        # Move the video to the small_dim_dir
                        # Close the video file
                        video.close()
                        newpath = os.path.join(small_dim_dir,filename)
                        shutil.move(video_path, newpath)
                        print(f"Moved {video_path} for small dimensions.")
                        files_moved = True
                    else:
                        print(f"Not moving {video_path} for small dimensions")


                except Exception as e:
                    print(e)
                    continue

    print("All Done Processing Files!")

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
        vid_length = video.duration
        if vid_length > 0:
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
        print(f"Video Name: {video_file} Dimensions {video_width}x{video_height} pixels: Category: {dimensions}")
        print(f"Video Width is {video_width} and Minimum Width is {min_width}, Video Height is {video_height} and Minimum Height is {min_height}")
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
    button1 = ttk.Button(mainroot, text="Delete videos by too small dimension", bootstyle="success, outline",
                         command=delete_too_small_dim)
    button2 = ttk.Button(mainroot, text="Move videos by too small dimension to root", bootstyle="success, outline",
                         command=move_too_small_dim)
    button3 = ttk.Button(mainroot, text="Move videos to dimensions folder", bootstyle="success, outline",
                         command=move_by_dim)
    button4 = ttk.Button(mainroot, text="Move to dim folder and delete small dimensions", bootstyle="success, outline",
                         command=both_actions)
    button5 = ttk.Button(mainroot, text="Move all files by dimensions", bootstyle="success, outline",
                         command=move_all)
    button6 = ttk.Button(mainroot, text="Quit", bootstyle="success, outline", command=quit)
    # Pack the buttons into the window
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    # Start the Tkinter main loop
    mainroot.mainloop()

if __name__ == "__main__":
    # This block will only run if the script is executed directly, not when imported as a module
    main_script()