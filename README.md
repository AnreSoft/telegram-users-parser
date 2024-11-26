# Telegram Chat Grabber

A Python script for extracting usernames from a graphical interface (e.g., a Telegram chat) and saving them to a file.

## Overview

This script automates the process of navigating through a graphical user interface to collect usernames and stores them in a `.txt` file. It uses the `pyautogui` library for mouse and keyboard automation and `pyperclip` for clipboard handling.

---

## How It Works

### 1. Starting the Script
- The script waits for 4 seconds before starting to allow you to prepare the application window.
- Clicks are made on pre-defined coordinates (`START_X`, `START_Y`) to select users.

### 2. Extracting Usernames
- The script attempts to locate a specific image (`name.png`) to identify the username field on the screen.
- If found, it clicks slightly above the detected image to copy the username to the clipboard.
- The username is retrieved from the clipboard and saved to a file (`users.txt`).

### 3. Navigation and Scrolling
- After extracting a username (or failing to find one), the script locates the "Back" button (`back.png`) to return to the previous screen.
- The screen is scrolled down by a specified number of pixels (`SCROLL_PIXELS`) to move to the next user.

### 4. Error Handling
- Errors are caught and logged to ensure the script continues running.
- You can interrupt the script at any time with `Ctrl+C`.

---

## Requirements

- Python 3.6+
- Libraries:
  - `pyautogui`
  - `pyperclip`
- Images for UI elements:
  - `name.png` (to identify the username field)
  - `back.png` (to locate the back button)

---

## Configuration

All configurable parameters are stored in `config.py`:

```python
# File to save extracted usernames
FILE_NAME = 'users.txt'

# Starting coordinates for the first click
START_X = 746
START_Y = 145

# Pause durations
SLEEP_DURATION = 0.5

# Scroll settings
SCROLL_PIXELS = 116

# Image paths for locating elements
NAME_IMAGE_PATH = r'C:\path\to\name.png'
BACK_IMAGE_PATH = r'C:\path\to\back.png'
