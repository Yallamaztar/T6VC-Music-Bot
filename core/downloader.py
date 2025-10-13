import re
import yt_dlp

def download_audio(url: str) -> str | None:
    try:
        title, filesize = get_info(url)
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
            "max_filesize": 2500 * 1024 * 1024,
            "concurrent_fragment_downloads": 5
        }

        if filesize and filesize > opts["max_filesize"]:
            print(f"^7[^5VC^7]: Too large file for {sanitized}")
            return None

        print(f"^7[^5VC^7]: Started new download for {sanitized}")

        with yt_dlp.YoutubeDL(opts) as yt:
            yt.download([url])

        return sanitized

    except Exception as e:
        print(f"^7[^5VC^7]: Download failed for {url}: {e}")
        return None

def get_info(url: str) -> str:
    print(f"^7[^5VC^7]: validating {url}")
    with yt_dlp.YoutubeDL() as yt:
        info = yt.extract_info(url, download=False)
        return info.get("title"), info.get("filesize") or info.get("filesize_approx")


def sanitize_filename(name):
    name = name.replace("｜", "|")
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    return name.strip()
