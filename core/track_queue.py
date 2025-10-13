import os
from queue import Queue

from core.downloader import download_audio
from core.wrapper import rcon

class TrackQueue:
    def __init__(self) -> None:
        self.queue = Queue(maxsize=5)
        print("[TrackQueue] Initialized")

    def add(self, url: str) -> None:
        if self.queue.full(): return

        if url.startswith("https://"): url = url[8:]
        elif url.startswith("http://"): url = url[7:]
            
        title = download_audio(url)
        if title: 
            self.queue.put(os.path.join("tmp", title + ".wav"))
            print(f"[TrackQueue] Added {title} - {url}")
            rcon.say(f"^7[^5VC^7]: Added ^5{title} ^7to queue")
        
    def clear(self) -> None:
        while not self.queue.empty():
            self.queue.get_nowait()
            self.queue.task_done()

    def next(self) -> None:
        if self.queue.empty(): return None
        return self.queue.get_nowait()

    def is_empty(self) -> bool:
        return self.queue.empty()
    
    def is_full(self) -> bool:
        return self.queue.full()