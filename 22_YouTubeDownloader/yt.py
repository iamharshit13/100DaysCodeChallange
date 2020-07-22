from pytube import YouTube

url = input("Enter the link for downloading the video: ")
yt = YouTube(url)
video = yt.streams
i=1

for quality in video:
    print(str(i) +" "+ str(quality))
    i+=1

selected_qual = int(input("Enter the Number: "))
file = video[selected_qual-1]
file.download()
print("File Downloaded")
