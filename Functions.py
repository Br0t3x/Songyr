import urllib.request as request
import re


def download_ytvid_as_mp3(url: str):
    video_info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f"Download of {filename} completed")


def search_songs(input: str, options: dict):
    if options.get("type") == "all":
        video_urls = []
        html = request.urlopen(f"https://www.youtube.com/results?search_query={input}")
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        for identifier in video_ids:
            video_urls.append("https://www.youtube.com/watch?v=" + identifier)

# <h1>This is the password!</h1>
