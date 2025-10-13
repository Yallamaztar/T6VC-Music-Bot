import pygame

class VirtualMic:
    def __init__(self, device_name: str = "Headset Earphone (HyperX Virtual Surround Sound)") -> None:
        pygame.init()   
        if pygame.mixer.get_init(): pygame.mixer.quit()
        try: pygame.mixer.init(devicename=device_name)
        except Exception as e: print("Couldnt find sound device")
        
    def play(self, track: str) -> None:
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(start=20)

    def pause(self) -> None:
        pygame.mixer.music.pause()

    def unpause(self) -> None:
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