from pytube import YouTube
import tkinter
#url=input("Enter the url: ")
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = (total_size - bytes_remaining)
    bytes_remaining_MB = round(bytes_remaining*0.000001,1)
    done_size = round((total_size - bytes_remaining)*0.000001,1)
    percentage_of_completion = round(bytes_downloaded / total_size * 100, 1)

    print(f'{percentage_of_completion}%, {done_size}MB/{bytes_remaining_MB}MB')

url='https://www.youtube.com/watch?v=6I5nor_880M' #For test
yt=YouTube(url)
print('--------------------')
print(f'Video Title : {yt.title}')
print(f'Video Views : {yt.views}')
print(f'Video Thumbnail : {yt.thumbnail_url}')
print(f'Channel URL : {yt.channel_url}')
print('--------------------')
print(yt.streams.filter().order_by('resolution'))
stream = yt.streams.filter(adaptive=True).order_by('resolution').last()
print(f'Video Quality : {stream.resolution}')
print(f'Video Size : {round((stream.filesize)*0.000001,2)}MB')
print(f'Video Type : {stream.mime_type}')
print('--------------------')
yt.register_on_progress_callback(on_progress)
stream.download()
print('finish')