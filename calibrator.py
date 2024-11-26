import pyautogui
import time

def print_cursor_position():
    """Print the current cursor coordinates every second."""
    try:
        while True:
            x, y = pyautogui.position()  # Get the current cursor coordinates
            print(f"Cursor coordinates: x={x}, y={y}")
            time.sleep(1)  # Pause for 1 second
    except KeyboardInterrupt:
        print("Program stopped by the user.")

def scroll_down(pixels=1600):
    """Scroll down by a specified number of pixels."""
    time.sleep(10)  # Pause before scrolling
    pyautogui.scroll(-pixels)  # Perform downward scroll

# Uncomment the line below to test scrolling
# scroll_down()

print_cursor_position()
