# YouTube-Downloader
**Smaron Music Player GUI Application**

---

## Table of Contents

1. Project Overview
2. Creation and History
3. Technology Stack and Module Explanations
4. File Structure
5. Environment Setup and Dependencies
6. GUI Layout and Workflow
7. Core Functional Components

   * 7.1 Playlist Management
   * 7.2 Playback Controls (Play, Pause, Stop)
   * 7.3 Navigation (Next, Previous, Play All)
   * 7.4 Volume Control
   * 7.5 Download from YouTube (MP3/MP4)
   * 7.6 Update Playlist
8. Function-by-Function Breakdown

   * 8.1 `update()`
   * 8.2 `playall()`
   * 8.3 `play_music()`
   * 8.4 `stop_music()`
   * 8.5 `pause_music()`
   * 8.6 `nxt()` and `prev()`
   * 8.7 `dwn()` and nested `mp3()`/`mp()` downloads
   * 8.8 `volup()` and `voldown()`
   * 8.9 `exit()`
9. Event Handling and Control Flow
10. Error Handling and Edge Cases
11. Customization and Extensibility
12. Best Practices and Code Quality
13. Testing and Debugging
14. Future Enhancements
15. Licensing and Author Information
16. Keywords

---

## 1. Project Overview

**Smaron Music Player** is a standalone desktop application, originally developed in **2021**, that allows users to browse, play, pause, stop, navigate, and download audio content. Built with **Tkinter** for the graphical interface and **Pygame** for audio playback, it also integrates **Pytube** to fetch music from YouTube directly into the local playlist.

Key features:

* Browse local `.mp3` files as a playlist
* Play, Pause, Stop, Next, Previous, and Play All controls
* Volume Up/Down
* Download songs by search term from YouTube (MP3 or MP4)
* Dynamic playlist update

---

## 2. Creation and History

* **Year:** 2021
* **Author:** Smaron Biswas
* **Evolution:** Started as a simple Tkinter prototype, later integrated Pygame for audio playback and Pytube for download functionality. Updated periodically to fix bugs and add features.

---

## 3. Technology Stack and Module Explanations

* **Tkinter** (std. lib): Provides the GUI window, widgets (Listbox, Buttons, Labels, Entry), layout management, and event loop.
* **Pygame**: Handles audio mixer initialization, loading, playing, pausing, and stopping `.mp3` files via `pygame.mixer.music`.
* **os**: Accesses the local file system to list songs and rename downloaded files.
* **requests**: Sends HTTP GET requests to YouTube search, extracts video IDs from resulting HTML.
* **Pytube**: Downloads YouTube video streams (audio-only or full) based on found URLs.
* **threading**: (Imported but not used here) can allow background download/playback threads for UI responsiveness.

---

## 4. File Structure

```plaintext
smaron_player/
├── player_app.py           # Main application script
├── songs/                  # Local directory of .mp3 files
├── requirements.txt        # Python dependencies (pygame, pytube, requests)
└── README.md               # Documentation
```

---

## 5. Environment Setup and Dependencies

1. **Python 3.6+**
2. Install required packages:

   ```bash
   pip install pygame pytube requests
   ```
3. Ensure the `songs/` directory exists and contains `.mp3` files.

---

## 6. GUI Layout and Workflow

1. **Main Window**: 500×500 window titled “Smaron”
2. **Playlist Listbox**: Displays filenames from `songs/` directory
3. **Control Buttons**:

   * Download
   * Previous, Play, Next
   * Volume Up, Volume Down
   * Stop, Play All, Update, Exit
4. **Labels**: Display current playing song
5. **Download Section**: Opens Entry widget for search term, triggers MP3/MP4 download

---

## 7. Core Functional Components

### 7.1 Playlist Management

* On startup, scans `/home/smaron/Desktop/songs` for `.mp3` files and populates `playlist` list and Listbox.
* `update()`: rescans directory and refreshes Listbox.

### 7.2 Playback Controls

* **play\_music()**: Loads selected song and plays via `pygame.mixer.music`.
* **pause\_music()**: Pauses playback and toggles button to Play.
* **stop\_music()**: Stops playback and clears selection.

### 7.3 Navigation

* **nxt()** and **prev()**: Move index `b` forward or backward, load and play the corresponding song, update label and selection.
* **playall()**: Iterates through all songs, playing each in turn.

### 7.4 Volume Control

* **volup()**/**voldown()**: Increase or decrease `pygame.mixer.music` volume by 0.2 steps.

### 7.5 Download from YouTube

* **dwn()**: Prompts user for search term via Entry widget.
* **mp3()**: Downloads audio-only stream and renames to `<search>.mp3`.
* **mp()**: Downloads default stream (likely video+audio) and saves in `songs/`.

### 7.6 Update Playlist

* **update()**: Refreshes Listbox and shows “Updated” message.

---

## 8. Function-by-Function Breakdown

### 8.1 `update()`

* Clears and repopulates Listbox by scanning `songs/` directory.
* Displays a temporary "Updated" label on GUI.

### 8.2 `playall()`

* Initializes mixer, selects first file, plays sequentially, waits for each to finish using `pygame.time.Clock().tick()`.

### 8.3 `play_music()`

* Retrieves current selection index from Listbox, loads and plays that song.
* If previously paused, unpauses.
* Updates the Pause button and displays song name.

### 8.4 `stop_music()`

* Stops playback and clears Listbox selection.

### 8.5 `pause_music()`

* Pauses playback, toggles button to Play.

### 8.6 `nxt()` and `prev()`

* Updates global index `b`, loads and plays next or previous track.
* Updates GUI selection and label.

### 8.7 `dwn()`

* Presents Entry for search term.
* Defines `mp3()` and `mp()` handlers to fetch YouTube results page, extract first `watch?v=` link, download via Pytube.
* Renames downloaded file to include search term.
* Displays "Download Done" label.

### 8.8 `volup()` and `voldown()`

* Adjusts `pygame.mixer.music` volume, prints new level.

### 8.9 `exit()`

* Calls `window.destroy()` to terminate the application.

---

## 9. Event Handling and Control Flow

* Buttons bound to their respective functions using `command=` parameter.
* GUI runs on `window.mainloop()` to process events.

---

## 10. Error Handling and Edge Cases

* **File Not Found**: If no selection is made, `lbal.curselection()` will fail; catch exceptions in playback functions.
* **Download Failures**: HTTP errors or Pytube exceptions should be caught and shown via `messagebox`.
* **Volume Limits**: Ensure volume remains within \[0.0, 1.0].

---

## 11. Customization and Extensibility

* Change the songs directory path to a configurable setting.
* Add threading for downloads to avoid freezing GUI.
* Enhance download search logic to present multiple choices.
* Persist user preferences (volume, last played index) in a config file.

---

## 12. Best Practices and Code Quality

* Avoid global variables; encapsulate state in a class.
* Use Python’s `logging` module instead of `print()`.
* Validate user input and handle exceptions gracefully.
* Modularize code: separate GUI, playback, and download logic.

---

## 13. Testing and Debugging

* Unit tests for playback functions and download helper.
* Mock Pygame mixer for headless test runs.
* Simulate missing files and invalid selections.

---

## 14. Future Enhancements

* Playlist persistence and drag-and-drop reordering.
* Support for other audio formats.
* Implement search history and suggestions.
* Add equalizer controls and visualizations.
* Internationalize GUI text.

---

## 15. Licensing and Author Information

**Author:** Smaron Biswas
**Created:** 2021
**License:** MIT License

Free to use, modify, and distribute under the MIT License.

---

## 16. Keywords

Tkinter, Pygame, Pytube, Music Player, YouTube Downloader, Python GUI, Audio Playback, MP3 Player, Desktop App, Playlist Manager, Open Source.

Tkinter, Pygame, Pytube, Music Player, YouTube Downloader, Python GUI, Audio Playback, MP3 Player, Desktop App, Playlist Manager, Open Source.

---

*End of Documentation.*
