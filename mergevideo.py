import os
list = os.listdir()
for item in list:
    print(item)

os.system('ffmpeg -i video.webm -i audio.webm -c:v copy -c:a copy merged.webm')
