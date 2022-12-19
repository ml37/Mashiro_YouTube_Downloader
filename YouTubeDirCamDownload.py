from pytube import YouTube
import sys
import os


def urldownload(url):
    def on_progress(stream, chunck, bytes_remaining):
        global filesize
        filesize = stream.filesize
        current = ((filesize - bytes_remaining)/filesize)
        percent = ('{0:.1f}').format(current*100)
        progress = int(50*current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write(' ↳  |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()
    yt=YouTube(url)
    yt.register_on_progress_callback(on_progress)
    print('--------------------')
    print(f'Video Title : {yt.title}')
    print(f'Video Views : {yt.views}')
    print('--------------------')
    stream_video = yt.streams.filter(adaptive=True, res='2160p')
    stream_audio = yt.streams.filter(only_audio=True, abr="160kbps")
    stream_webm = stream_video.get_by_itag(313)
    stream_audio_160 = stream_audio.get_by_itag(251)
    print(stream_webm)
    print(stream_audio_160)
    #stream_audio_160.download()
    #stream_webm.download()
    print('dl finish')
    os.system('ffmpeg -i {yt.title}.webm -i {yt.title}.webm -c:v copy -c:a copy {yt.title}merged.webm')

while True :
    url = input('url : ')
    urldownload(url)

#ffmpeg -i video.webm -i audio.webm -c:v copy -c:a copy output.webm