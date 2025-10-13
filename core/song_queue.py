import time
from queue import Queue

from core.wrapper import rcon
from core.downloader import get_info

class TrackQueue:
    def __init__(self) -> None:
        self.queue = Queue(maxsize=5)

    def add(self, url: str) -> None:
        if self.queue.full(): return
        
        self.queue.put(url)
        title, _ = get_info(url)
        
    def clear(self) -> None:
        while not self.queue.empty():
            self.queue.get_nowait()
            self.queue.task_done()

    def next(self) -> None:
        if self.queue.empty(): return None
        return self.queue.get_nowait()

    def status(self) -> None:
        if self.queue.empty(): return
        
        songs = list(self.queue.queue)
        for i, song in enumerate(songs, start=1):
            rcon.say(f"^7[^5VC^7]: #{i} - {song}")
            time.sleep(0.5)

    def is_empty(self) -> bool:
        return self.queue.empty()
    
    def is_full(self) -> bool:
        return self.queue.full()