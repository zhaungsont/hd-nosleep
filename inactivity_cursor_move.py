import pyautogui
import time
from pynput import mouse, keyboard

INACTIVITY_LIMIT = 4  # * 60  # 4 minutes in seconds
MOVE_DISTANCE = 5  # Distance to move the cursor

last_activity_time = time.time()


def on_activity(x, y):
    global last_activity_time
    last_activity_time = time.time()


def on_click(x, y, button, pressed):
    global last_activity_time
    last_activity_time = time.time()


def on_key_press(key):
    global last_activity_time
    last_activity_time = time.time()


# Listen to mouse events
mouse_listener = mouse.Listener(on_move=on_activity, on_click=on_click)

# Listen to keyboard events
keyboard_listener = keyboard.Listener(on_press=on_key_press)

mouse_listener.start()
keyboard_listener.start()

try:
    print("Running inactivity_cursor_move.py")
    while True:
        current_time = time.time()
        if current_time - last_activity_time > INACTIVITY_LIMIT:
            pyautogui.moveRel(MOVE_DISTANCE, 0)  # Move cursor right by 5 units
            last_activity_time = current_time  # Reset inactivity timer
        time.sleep(1)
except KeyboardInterrupt:
    print("Script terminated by user")
finally:
    mouse_listener.stop()
    keyboard_listener.stop()
