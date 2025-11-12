from pynput import keyboard
import sqlite3
import atexit
import threading





def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        cursor.execute("INSERT INTO key_log (key, release) VALUES (?, ?)", (str(key), False))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    cursor.execute("INSERT INTO key_log (key, release) VALUES (?, ?)", (str(key), True))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Blocking
# Collect events until released
try:
    connection = sqlite3.connect('db/focuswatch.db', check_same_thread=False)
    cursor = connection.cursor()
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
finally:
    print("closing")
    connection.commit()
    connection.close()


# def onClose():
#     print("closing")
#     connection.commit()
#     connection.close()

# atexit.register(onClose)


# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
