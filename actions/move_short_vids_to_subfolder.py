import os
import cv2
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from datetime import datetime
import shutil


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


# Function to move video files under a specified duration to a 'too_short' folder
def move_short_videos(root_directory, threshold_duration):
    for root, dirs, files in os.walk(root_directory):
        too_short_folder = os.path.join(root, 'too_short')

        # Create 'too_short' folder if it doesn't exist in the current subfolder
        if not os.path.exists(too_short_folder):
            os.makedirs(too_short_folder)

        for filename in files:
            if filename.endswith(('.mp4', '.avi', '.mkv', '.mpg', '.wmv', '.mk4', '.m4v')):
                video_path = os.path.join(root, filename)
                video_duration = get_video_duration(video_path)
                if video_duration is not None and video_duration < threshold_duration:
                    print(f"Moving {video_path} to 'too_short' folder (Duration: {video_duration} seconds)...")
                    new_path = os.path.join(too_short_folder, filename)
                    shutil.move(video_path, new_path)
                else:
                    print(f"Not moving {video_path} (Duration: {video_duration} seconds)... ")


def main_script():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root_directory = filedialog.askdirectory(title="Select the root directory to search for video files")

    if root_directory:
        threshold_duration = get_minimum_duration()
        print(f"Searching for videos in {root_directory} and its subdirectories...")
        print(threshold_duration)
        move_short_videos(root_directory, threshold_duration)
        print("Video processing complete.")
    else:
        print("No directory selected. Script terminated.")


if __name__ == "__main__":
    main_script()
