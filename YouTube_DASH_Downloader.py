from pytube import YouTube
import
url=input("Enter the url: ")
yt=YouTube(url)
print('--------------------')
print(f'Video Title : {yt.title}')
print(f'Video Views : {yt.views}')
print(yt.channel_url)
yt.streams.filter(adaptive=True)