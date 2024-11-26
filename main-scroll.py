import pyautogui
import pyperclip
import time
from config import (
    FILE_NAME,
    START_X,
    START_Y,
    SLEEP_DURATION,
    SCROLL_PIXELS,
    NAME_IMAGE_PATH,
    BACK_IMAGE_PATH,
)


def parse_users(scroll_pixels):
    """Extract usernames from a UI and save to a file."""
    with open(FILE_NAME, 'a') as f:
        time.sleep(4)  # Pause before starting

        while True:
            try:
                # Click on a user at specified coordinates
                pyautogui.click(START_X, START_Y)
                time.sleep(1)  # Wait for the profile to load

                # Try to locate the "username field" image
                info_loc = pyautogui.locateOnScreen(NAME_IMAGE_PATH)
                if info_loc:
                    # If found, click slightly above the username field
                    pyautogui.click(info_loc[0] + 18, info_loc[1] - 9)
                    time.sleep(SLEEP_DURATION)

                    # Copy the username from the clipboard
                    user_name = pyperclip.paste()
                    f.write(f'{user_name}\n')
                    print(f"Found user: {user_name}")

                else:
                    print("Username not found.")

                # Go back and scroll down
                go_back_and_scroll(scroll_pixels)

            except KeyboardInterrupt:
                print("Parsing stopped by user.")
                break
            except Exception as e:
                print(f"Error: {e}")
                go_back_and_scroll(scroll_pixels)


def go_back_and_scroll(scroll_pixels):
    """Click the 'back' button and scroll down."""
    try:
        back_loc = pyautogui.locateOnScreen(BACK_IMAGE_PATH)
        if back_loc:
            pyautogui.click(back_loc[0], back_loc[1])
            time.sleep(SLEEP_DURATION)
        else:
            print("Back button not found.")
        pyautogui.moveTo(START_X, START_Y)
        pyautogui.scroll(-scroll_pixels)
    except Exception as e:
        print(f"Error during navigation: {e}")


if __name__ == "__main__":
    parse_users(scroll_pixels=SCROLL_PIXELS)
