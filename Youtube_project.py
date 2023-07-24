from pytube import YouTube
link = input("Enter the video link")
youtube_1 = YouTube(link)
# for downloading title of video
# print(youtube_1.title)

# for downloading thumbanil pic of video
# print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.filter(only_audio=True)   for downloading only audio
videos = youtube_1.streams.all()
vi = list(enumerate(videos))
for i in vi:
    print(i)
print()


play = int(input("Enter The Youtube Video Link:>"))
videos[play].download()
print("sucessfully downloaded")

# *note*
# if i want to audio with video than make sure there progressive="True"
# if want to only video than selected type="video/webm"
# if want to only audio than selected type="audio/webm"
