import re
import yt_dlp
from core.wrapper import rcon

def download_audio(url: str) -> str | None:
    MAX_SIZE: int = 10000 * 1024 * 1024 # 250 MB
    
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

def search_song(query: str) -> str | None:
    print(f"[Downloader]: Searching for: {query}")
    rcon.say(f"^7[^5VC^7]: Searching for ^5{query}")
    
    try:
        opts = {
            "quiet": True,
            "noplaylist": True,
            "extract_flat": True,
            "default_search": "ytsearch1"
        }
        
        with yt_dlp.YoutubeDL(opts) as ydl:
            search_results = ydl.extract_info(f"ytsearch1:{query}", download=False)
            
            if not search_results or 'entries' not in search_results:
                print(f"[Downloader]: No results found for: {query}")
                rcon.say(f"^7[^5VC^7]: ^1No results ^7found for {query}")
                return
                
            first_result = search_results['entries'][0]
            video_url = first_result.get('url') or f"https://www.youtube.com/watch?v={first_result.get('id')}"
            video_title = first_result.get('title', 'Unknown Title')
            
            print(f"[Downloader]: Found: {video_title}")
            rcon.say(f"^7[^5VC^7]: Found ^5{video_title}")
            
            return video_url
            
    except Exception as e:
        print(f"[Downloader]: Search failed for {query}: {e}")
        rcon.say(f"^7[^5VC^7]: ^1Search failed ^7for {query}")
        return

def sanitize_filename(name):
    name = name.replace("｜", "|")
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    return name.strip()
