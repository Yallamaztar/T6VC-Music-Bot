import time, os

from collections import deque
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

from core.track_queue import TrackQueue
from core.virtual_mic import VirtualMic
from core.downloader import download_audio
from core.wrapper import server, rcon

class VCMusicBot:
    def __init__(self) -> None:
        self.queue      = TrackQueue()
        self.last_seen  = deque(maxlen=50)
        self.vm         = VirtualMic()

        self.lock     = Lock()
        self.executor = ThreadPoolExecutor(max_workers=20)

        print("[VCMusicBot] Starting To Listen For Commands")
        self.run()

    def is_valid_audit_log(self, audit_log: dict[str, str]) -> bool:
        if (audit_log["origin"], audit_log["data"], audit_log["time"]) in self.last_seen: return False
        if (audit_log["origin"]) == server.logged_in_as(): return False
        return True
    
    def handle_command(self, data: str) -> None:
        parts = data.strip().split()
        if not parts: return

        command = parts[0].lower()
        if command.startswith("!play") or command.startswith("!ply"):
            url = " ".join(parts[1:]) if len(parts) > 1 else None
            if not url:
                print("[VCMusicBot] No URL provided")
                rcon.say("^7[^5VC^7]: Please provide a YouTube link"); return
            
            if self.queue.is_full():
                print("[VCMusicBot] Queue is full")
                rcon.say("^7[^5VC^7]: Queue is full, please try again after this song"); return
            
            if self.queue.is_empty(): self.executor.submit(self.start, url)
            else: self.queue.add(url)

        elif command.startswith("!pause") or command.startswith("!pa"): pass
        elif command.startswith("!next") or command.startswith("!nxt"): pass

    def start(self, url: str) -> None:
        if url.startswith("https://"): url = url[8:]
        elif url.startswith("http://"): url = url[7:]
        rcon.say(f"^7[^5VC^7]: Started processing {url}")
            
        title = download_audio(url)
        path  = os.path.join("tmp", title + ".wav")
        if title: self.vm.play(path)
        else: rcon.say("^7[^5VC^7]: Failed to download {url}")

    def run(self):
        while True:
            audit_log = server.get_recent_audit_log()
            if audit_log is None: time.sleep(0.1); continue
            if not self.is_valid_audit_log(audit_log): time.sleep(.01); continue
            
            self.last_seen.append((audit_log["origin"], audit_log['data'], audit_log['time']))
            self.executor.submit(self.handle_command, audit_log['data']) 
            time.sleep(.01)

if __name__ == '__main__':
    VCMusicBot().run()