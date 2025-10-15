import time
import pygame
import keyboard

from core.wrapper import rcon

class VirtualMic:
    def __init__(self, queue, device_name: str = "CABLE Input (VB-Audio Virtual Cable)", vc_key: str = "z") -> None:
        self.vc_key    = vc_key
        self.is_paused = False
        self.queue     = queue

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
            while True:
                if not self.is_playing(): break
                keyboard.press(self.vc_key)
                time.sleep(0.1)
                if self.is_paused: 
                    while self.is_paused and self.is_playing():
                        keyboard.press(self.vc_key)
                        time.sleep(0.1)
        finally: keyboard.release(self.vc_key)

        if not self.queue.is_empty():
            path = self.queue.next()
            print(f"[VirtualMic] Playing next song {path[4:][:-4]}")
            self.play(path)
        else: 
            print(f"[VirtualMic] All songs finished playing")
            rcon.say("All songs finished playing")

    def pause(self) -> None:
        if self.is_playing() and not self.is_paused:
            self.is_paused = True
            rcon.say("^7[^5VC^7]: Pausing song")
            pygame.mixer.music.pause()

    def unpause(self) -> None:
        if not self.is_playing() and self.is_paused:
            self.is_paused = False
            rcon.say("^7[^5VC^7]: Continuing song")
            pygame.mixer.music.unpause()

    def stop(self) -> None:
        pygame.mixer.music.stop()

    def skip(self) -> None:
        if not self.queue.is_empty():
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.queue.next())

    def is_playing(self) -> bool:
        return pygame.mixer.music.get_busy()
    
    def cleanup(self) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
        print("[VirtualMic] Clean up successful")