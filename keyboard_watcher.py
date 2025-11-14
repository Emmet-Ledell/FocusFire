from pynput import keyboard
import sqlite3
import atexit
import threading
# Don't think I need to thread lock this since there's just one thread sharing the connection, and sqllite auto locks the connections

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
# Collect events until released, wrapped in a try finally to close the db connection so nothing spins out and keeps it locked
try:
    connection = sqlite3.connect('db/focuswatch.db', check_same_thread=False, isolation_level=None)
    connection.execute("PRAGMA journal_mode=WAL;")
    cursor = connection.cursor()
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
finally:
    print("closing")
    connection.commit()
    connection.close()



# To use this I would have to call it and then have something else block, as this will just keep going through the file and close if 
# nothing blocks it
# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)

# def onClose():
#     print("closing")
#     connection.commit()
#     connection.close()

# atexit.register(onClose)
