from pytube import YouTube
import tkinter
import sys
#url=input("Enter the url: ")
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = (total_size - bytes_remaining)
    bytes_remaining_MB = round(bytes_remaining*0.000001,1)
    done_size = round((total_size - bytes_remaining)*0.000001,1)
    percentage_of_completion = round(bytes_downloaded / total_size * 100, 1)
    print(f'{percentage_of_completion}%, {done_size}MB/{bytes_remaining_MB}MB')
    
    '''global filesize
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳  |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()'''

url='https://www.youtube.com/watch?v=6qTghUgMOeY' #For test
yt=YouTube(url)
print('--------------------')
print(f'Video Title : {yt.title}')
print(f'Video Views : {yt.views}')
print('--------------------')
stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first().download()
yt.register_on_progress_callback(on_progress)
print(f'Video Quality : {stream.resolution}')
print(f'Video Size : {round((stream.filesize)*0.000001,2)}MB')
print(f'Video Type : {stream.mime_type}')
print('--------------------')
stream.download()
print('finish')