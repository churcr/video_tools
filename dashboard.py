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
mainroot.geometry("750x250")

label = ttk.Label(mainroot, text="Main Menu")
label.pack()

button1 = ttk.Button(mainroot, text="Delete Short Videos", bootstyle="success, outline",
                     command=run_remove_short_vids)
button2 = ttk.Button(mainroot, text="Modify Videos Based on Dimensions", bootstyle="success, outline",
                     command=run_vid_dim_script)
button3 = ttk.Button(mainroot, text="Remove Non-Standard Characters", bootstyle="success, outline",
                     command=remove_non_standard_char)
button4 = ttk.Button(mainroot, text="Move Short Videos to Root", bootstyle="success, outline",
                     command=run_move_short_to_root)
button5 = ttk.Button(mainroot, text="Move Short Videos to Subfolder", bootstyle="success, outline",
                     command=run_move_short_to_sub)
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