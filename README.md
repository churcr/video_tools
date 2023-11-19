# video_tools

Python script to maniuplate videos on local and remote drives.  Functions include:

1. A dashboard that uses tkinter and ttkbootstrap to create a button based menu.
2. Main menu has the following functions:
  1. Function to delete videos under a user selected length.
  2. Function to loop through all files in folder and subfolder to remove non-standard characters.
  3. Function to move instead of delete short videos to root.
  4. Function to move instead of delete short videos to subfolder.
  5. Function that opens another dashboard that allows the user to further manipulate video files based on video dimensions.  This new dashboard includes the following functions:
    1. Delete videos based on user inputted video dimensions.
    2. Move remaining videos to folders named square, vert, and horz.
    3. Combines 1 and 2 to delete small dimension files and move the rest to the sqaure, vert, and horz folder.
    4. Move all files to square, vert, horz, and too_small folder

In process.  Not yet in dashboard.
Function that moves all files in subfolder back to parent.  Currently only works with folders that are 3 levels deep.
Function that deletes files my user selected exension.  Helpful if you want to remove pictures from video folder.
