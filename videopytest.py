from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("ale1.mp4")
clip1_resized = clip1.resize(720,1280)
clip2 = VideoFileClip("ale2.mp4")
clip3 = VideoFileClip("ale3.mp4")
final_clip = concatenate_videoclips([clip1_resized,clip2,clip3])
final_clip.write_videofile("my_concatenation_resized.mp4")