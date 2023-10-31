from pytube import YouTube


def download_video(link):
    yt_video = YouTube(link).streams.get_highest_resolution()
    try:
        yt_video.download()
    except:
        print("An error occurred")
    print("Download is completed!!!")


if __name__ == "__main__":
    link = input("Enter the link of the video: ")
    download_video(link)
