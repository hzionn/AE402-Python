from pytubefix import YouTube
# yt = YouTube("你想要的影片網址")
yt = YouTube("https://youtu.be/yG60SUkxVX0")

# 初探Pytube
stream = yt.streams.first()
stream.download()

# 更改下載位置
stream = yt.streams.first()
stream.download("youtube影片", "我下載的影片-1")

# 顯示串流資料
stream = yt.streams.first()
print(stream)

# 篩選串流格式
stream = yt.streams.filter(res="720p").first()
stream.download()

# 篩選串流格式
stream = yt.streams.filter(res="360p").first()
stream.download("youtube影片", yt.title+"360p")

# 增加篩選條件
stream = yt.streams.filter(res="720p", fps=30).first()
stream.download("youtube影片", yt.title+"720p"+"30fps")

# 增加篩選條件
stream = yt.streams.filter(only_audio=True).first()
stream.download("youtube影片", yt.title+"music only")