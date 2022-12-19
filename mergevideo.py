import ffmpeg
import os
list = os.listdir()
for item in list:
    print(item)

input = ffmpeg.input('video.mp4')
ainput = ffmpeg.input('audio.mp3')
audio = ainput.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
video = input.video.hflip()
out = ffmpeg.output(audio, video, 'out.mp4')
