import os
webm = input("webm file name : ")
os.system("ffmpeg -i "+webm+".webm -c:v libx264 -c:a aac output.mp4")