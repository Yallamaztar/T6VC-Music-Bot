import time
import pygame
import keyboard

from core.track_queue import Queue
from core.wrapper import rcon

class VirtualMic:
    def __init__(self, device_name: str = "Headset Earphone (HyperX Virtual Surround Sound)", vc_key: str = "z") -> None:
        self.vc_key = vc_key
        self.queue  = Queue()

        pygame.init()   
        if pygame.mixer.get_init(): pygame.mixer.quit()
        try: 
            pygame.mixer.init(devicename=device_name)
            print(f"[VirtualMic] Found {device_name}")
        except Exception: print("[VirtualMic] Couldnt find sound device")

        print("[VirtualMic] Initialized")
        
    def play(self, path: str) -> None:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        print(f"[VirtualMic] Playing song {path}")
        rcon.say(f"^7[^5VC^7]: Playing song {path[4:][:-4]}")

        try:
            while self.is_playing():
                keyboard.press(self.vc_key)
                time.sleep(0.1)
        finally: keyboard.release(self.vc_key)

        if not self.queue.empty():
            path = self.queue.next()
            print(f"[VirtualMic] Playing next song {path[4:][:-4]}")
            self.play(path)
        else: 
            print(f"[VirtualMic] All songs finished playing")
            rcon.say("All songs finished playing")

    def pause(self) -> None:
        rcon.say(f"^7[^5VC^7]: Pausing song")
        pygame.mixer.music.pause()

    def unpause(self) -> None:
        rcon.say(f"^7[^5VC^7]: Continuing song")
        pygame.mixer.music.unpause()

    def stop(self) -> None:
        pygame.mixer.music.stop()

    def skip(self, next_path: str) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(next_path)

    def is_playing(self) -> bool:
        return pygame.mixer.music.get_busy()
    
    def cleanup(self) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
        print("[VirtualMic] Clean up successful")