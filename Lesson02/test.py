from pytubefix import YouTube
from pytubefix.cli import on_progress

progress = 0


def showProgress(stream,chunk,bytes_remaining):
    size = stream.filesize
    global progress
    preProgress = progress
    currentProgress = (size - bytes_remaining)*100 // size
    progress = currentProgress
    
    if progress == 100:
        print("下載完成！")
        # return
    if preProgress != progress:
        print("目前進度： " + str(progress) + "%")


yt = YouTube(
    "https://youtu.be/A5RfSftJRw8",
    # on_progress_callback=showProgress
    on_progress_callback=on_progress
)
# stream = yt.streams.first()
stream = yt.streams.filter().first()
stream.download("")
