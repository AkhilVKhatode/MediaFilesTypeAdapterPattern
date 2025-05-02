# Media Player Adapter Pattern Implementation

This project demonstrates the Adapter Design Pattern in Python, showing how to create a unified media player interface that can handle different file formats (MP3, FLAC, AVI) through specialized adapters.

## 📌 Overview

The Adapter pattern allows incompatible interfaces to work together. In this media player example, we create a common `MediaPlayer` interface that can work with different media formats through format-specific adapters, even though each underlying player has its own unique interface.

## 🎯 Features

- Unified `MediaPlayer` interface for playing media files
- Adapters for three different media formats:
  - `MP3Adapter` for MP3 files
  - `FLACAdapter` for FLAC audio files
  - `AVIAdapter` for AVI video files
- Proper error handling for incompatible file formats
- Clean separation between client code and media player implementations

### Key Components

1. **Target Interface (`MediaPlayer`)**
   - Defines the common interface expected by client code (`play()` method)

2. **Adaptees (Existing Players)**
   - `MP3Player`: Has `play_mp3()` method
   - `FLACDecoder`: Has `decode_flac()` method
   - `AVIPlayer`: Has `play_avi()` method

3. **Adapters**
   - Each adapter implements `MediaPlayer` and wraps an adaptee
   - Translates the generic `play()` call to the specific player's method

## 📝 Example Output
```
Attempting to play: song.mp3
Playing MP3 file: song.mp3

Attempting to play: music.flac
Decoding FLAC file: music.flac

Attempting to play: movie.avi
Playing AVI video: movie.avi

Attempting to play: video.avi
Error: File must be .mp3 format

Attempting to play: sound.mp3
Error: File must be .flac format
```

## 🧠 Design Pattern Benefits
- Single Responsibility Principle: Each adapter handles one media format
- Open/Closed Principle: Can add new formats without changing existing code
- Loose Coupling: Client code depends only on the MediaPlayer interface
- Reusability: Adapters can be reused across different parts of the application
