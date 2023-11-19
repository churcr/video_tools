import os
import cv2
# import moviepy
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import pandas as pd
from datetime import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
saved_files = []

def get_minimum_duration():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    entered_value = simpledialog.askstring("Minimum Duration", "Enter the minimum video duration (in seconds):")

    try:
        minimum_duration = float(entered_value)
        return minimum_duration
    except (ValueError, TypeError):
        return None

# Function to get the video duration using moviepy
def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        duration = clip.duration
        clip.close()
        return duration
    except Exception as e:
        print(f"Error getting duration for {file_path}: {str(e)}")
        return None

# Function to delete video files under a specified duration
def delete_short_videos(root_directory, threshold_duration):
    deleted_files = []
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4', '.m4v')):  # Adjust the extensions as needed
                video_path = os.path.join(root, filename)
                video_duration = get_video_duration(video_path)
                # print(threshold_duration, video_duration)
                if video_duration is not None and video_duration < threshold_duration:
                    print(f"Deleting {video_path} (Duration: {video_duration} seconds)...")
                    os.remove(video_path)
                    deleted_files.append((video_path, video_duration))
                else:
                    saved_files.append((video_path, video_duration))
                    print(f"Saving {video_path} (Duration: {video_duration} seconds)... ")
    return deleted_files


# if __name__ == "__main__":
    # This block will only run if the script is executed directly, not when imported as a module
def main_script():
    # Create a folder dialog to select the root directory
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root_directory = filedialog.askdirectory(title="Select the root directory to search for video files")

    if root_directory:
        # threshold_duration = float(input("Enter the video length threshold (in seconds): "))
        threshold_duration = get_minimum_duration()
        print(f"Searching for videos in {root_directory} and its subdirectories...")
        print(threshold_duration)
        deleted_files = delete_short_videos(root_directory, threshold_duration)

        if deleted_files:
            # Create a timestamp for the Excel file name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            use_path = f"{root_directory}/"
            # excel_file_name = f"S:\deleted_files_{timestamp}.xlsx"
            excel_file_name = f"{use_path}deleted_files_{timestamp}.xlsx"
            saved_excel_file_name = f"{use_path}saved_files_{timestamp}.xlsx"

            # Convert the list of deleted files to a DataFrame
            df = pd.DataFrame(deleted_files, columns=["File Path", "Duration (seconds)"])

            # Convert the list of saved files to a DataFrame
            df2 = pd.DataFrame(saved_files, columns=["File Path", "Duration (seconds)"])

            # Save the DataFrames to an Excel file
            df.to_excel(excel_file_name, index=False, engine="openpyxl")
            df2.to_excel(saved_excel_file_name, index=False, engine="openpyxl")
            print(f"Deleted files and their durations saved to {excel_file_name}")
            print(f"Saved files and their durations saved to {saved_excel_file_name}")
        else:

            print("No files were deleted.")
    else:
        print("No directory selected. Script terminated.")