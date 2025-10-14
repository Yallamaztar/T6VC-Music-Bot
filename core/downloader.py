import re
import yt_dlp
from core.wrapper import rcon

def download_audio(url: str) -> str | None:
    MAX_SIZE: int = 100 * 1024 * 1024 # 100 MB
    
    print(f"[Downloader]: Trying to download: {url}")
    try:
        with yt_dlp.YoutubeDL({"quiet": True, "noplaylist": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        title = info.get("title") or "unknown_title"
        filesize = info.get("filesize") or info.get("filesize_approx")
        sanitized = sanitize_filename(title)

        if filesize and filesize > MAX_SIZE:
            msg = f"Too large file - {sanitized}"
            print(f"[Downloader]: {msg}")
            rcon.say(f"^7[^5VC^7]: ^1Too large ^7file - {sanitized}")
            return
        
        sanitized = sanitize_filename(title)
        opts = {
            "format": "bestaudio/best",
            "outtmpl": rf"tmp\{sanitized}.%(ext)s",
            "noplaylist": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }],
            "max_filesize": MAX_SIZE, # 50 MB
            "concurrent_fragment_downloads": 5
        }

        print(f"[Downloader]: Started new download for {sanitized}")
        rcon.say(f"^7[^5VC^7]: Started ^5new ^7download for {sanitized}")

        with yt_dlp.YoutubeDL(opts) as yt:
            yt.download([url])

        return sanitized

    except Exception:
        print(f"[Downloader]: Download failed for {sanitized}")
        rcon.say(f"^7[^5VC^7]: Download ^1failed ^7for {sanitized}"); return

def sanitize_filename(name):
    name = name.replace("｜", "|")
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    return name.strip()
