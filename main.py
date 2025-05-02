from abc import ABC, abstractmethod

# Target interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, file):
        pass

# Adaptee 1
class MP3Player:
    def play_mp3(self, filename):
        print(f"Playing MP3 file: {filename}")

# Adaptee 2
class FLACDecoder:
    def decode_flac(self, filepath):
        print(f"Decoding FLAC file: {filepath}")

# Adaptee 3
class AVIPlayer:
    def play_avi(self, avi_file):
        print(f"Playing AVI video: {avi_file}")

# Adapter for MP3
class MP3Adapter(MediaPlayer):
    def __init__(self):
        self.mp3_player = MP3Player()
    
    def play(self, file):
        if not file.endswith('.mp3'):
            raise ValueError("File must be .mp3 format")
        self.mp3_player.play_mp3(file)

# Adapter for FLAC
class FLACAdapter(MediaPlayer):
    def __init__(self):
        self.flac_decoder = FLACDecoder()
    
    def play(self, file):
        if not file.endswith('.flac'):
            raise ValueError("File must be .flac format")
        self.flac_decoder.decode_flac(file)

# Adapter for AVI
class AVIAdapter(MediaPlayer):
    def __init__(self):
        self.avi_player = AVIPlayer()
    
    def play(self, file):
        if not file.endswith('.avi'):
            raise ValueError("File must be .avi format")
        self.avi_player.play_avi(file)

# Client code
def play_media(player: MediaPlayer, file):
    print(f"\nAttempting to play: {file}")
    try:
        player.play(file)
    except ValueError as e:
        print(f"Error: {e}")

# Usage
mp3_player = MP3Adapter()
flac_player = FLACAdapter()
avi_player = AVIAdapter()

play_media(mp3_player, "song.mp3")
play_media(flac_player, "music.flac")
play_media(avi_player, "movie.avi")

# These will raise errors
play_media(mp3_player, "video.avi")
play_media(flac_player, "sound.mp3")
