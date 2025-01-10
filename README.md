# have-fun
A Python-based fullscreen lock screen application with a custom background image, password authentication,
background music. Additionally, it integrates AutoHotkey to disable specific keyboard keys.


## Password
1234 you can change it 
## Features

- **Fullscreen Mode**: Runs the application in fullscreen mode, making it suitable for locking a computer.
- **Password Protection**: Only exits when the correct 4-digit password is entered.
- **Background Music**: Plays an audio file (`audio.mp3`) on a loop.
- **Custom Background**: Displays an image (`Pic.png`) resized to fit the screen.
- **AutoHotkey Integration**: Runs an AutoHotkey script to disable specific keys.

## Requirements

- Python 3.10 or higher
- Libraries:
  - `tkinter` (comes pre-installed with Python)
  - `Pillow` (for image handling)
  - `pygame` (for audio playback)
- AutoHotkey (for `.ahk` script execution)
