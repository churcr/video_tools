import sys
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from actions import orig_remove_short_vids
from actions import move_delete_by_dim
from actions import remove_non_english_char
from actions import move_short_vids_to_root
from actions import move_short_vids_to_subfolder

import subprocess

# import sys
# print(sys.path)

def run_move_short_to_root():
    move_short_vids_to_root.main_script()

def run_move_short_to_sub():
    move_short_vids_to_subfolder.main_script()

def run_remove_short_vids():
    #    subprocess.run(['D:/Python_Scripts/VideoToolsNew/venv/Scripts/python.exe',
    #                    'actions\orig_remove_short_vids.py'])
    orig_remove_short_vids.main_script()

def run_vid_dim_script():
    move_delete_by_dim.main_script()

def remove_non_standard_char():
    remove_non_english_char.main()

mainroot = ttk.Window(themename="superhero")
mainroot.title("Main Menu")
mainroot.geometry("750x400")

label = ttk.Label(mainroot, text="Main Menu")
label.pack()

button1 = ttk.Button(mainroot, text="Delete Short Videos", bootstyle="success, outline",
                     command=run_remove_short_vids)
button2 = ttk.Button(mainroot, text="Move Short Videos to Root", bootstyle="success, outline",
                     command=run_move_short_to_root)
button3 = ttk.Button(mainroot, text="Move Short Videos to Subfolder", bootstyle="success, outline",
                     command=run_move_short_to_sub)

button4 = ttk.Button(mainroot, text="Delete videos by too small dimension in folder", bootstyle="success, outline",
                     command=move_delete_by_dim.delete_too_small_dim)
button4b = ttk.Button(mainroot, text="Delete videos by too small dimension in folder and sub folders", bootstyle="success, outline", command=move_delete_by_dim.delete_too_small_dim_subfolders)
button4c = ttk.Button(mainroot, text="Move videos by too small dimension to root", bootstyle="success, outline", command=move_delete_by_dim.move_too_small_dim)
button4d = ttk.Button(mainroot, text="Move videos to dimensions folder", bootstyle="success, outline", command=move_delete_by_dim.move_by_dim)
button4e = ttk.Button(mainroot, text="Move to dim folder and delete small dimensions", bootstyle="success, outline", command=move_delete_by_dim.both_actions)
button4f = ttk.Button(mainroot, text="Move all files by dimensions", bootstyle="success, outline", command=move_delete_by_dim.move_all)

button5 = ttk.Button(mainroot, text="Remove Non-Standard Characters", bootstyle="success, outline",
                     command=remove_non_standard_char)

button6 = ttk.Button(mainroot, text="Quit", bootstyle="success, outline", command=quit)
# Pack the buttons into the window
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button4b.pack()
button4c.pack()
button4d.pack()
button4e.pack()
button4f.pack()
button5.pack()
button6.pack()

# Start the Tkinter main loop
mainroot.mainloop()