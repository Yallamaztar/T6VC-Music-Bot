import yt_dlp
from .wrapper import rcon

def download_audio(url: str, ) -> None:
    opts = {
        "format": "bestaudio/best",
        "outtmpl": r"tmp\%(title)s.%(ext)s",
        "noplaylist": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }],
        "max_filesize": 25 * 1024 * 1024, # 25MB
        "concurrent_fragment_downloads": 5
    }

    with yt_dlp.YoutubeDL(opts) as yt:
        try:
            title, filesize = get_info(url)
            if filesize and filesize > opts["max_filesize"]:
                rcon.say(f"^7[^5VC^7]: Too large file for {title}")
                return
        
            rcon.say(f"^7[^5VC^7]: Started new download for {title}")
            yt.download(url)

        except Exception as e: rcon.say(f"^7[^5VC^7]: Download failed for {title}")

def get_info(url: str) -> str:
    rcon.say(f"^7[^5VC^7]: validating {url}")
    with yt_dlp.YoutubeDL() as yt:
        info = yt.extract_info(url, download=False)
        return info.get("title"), info.get("filesize") or info.get("filesize_approx")