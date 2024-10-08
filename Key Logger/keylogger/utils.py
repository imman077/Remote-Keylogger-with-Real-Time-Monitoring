import datetime
import time
import pyscreenshot as ImageGrab
import os


def take_screenshot():
    try:
        print("Taking screenshot...")
        image_name = f"screenshot-{str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}.png"
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshot1")
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, image_name)
        screenshot = ImageGrab.grab()
        screenshot.save(filepath)
        print("Screenshot taken...")
        return filepath
    except OSError as e:
        print(f"OS error occurred: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while taking the screenshot: {e}")
        return None