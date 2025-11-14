from pynput import mouse
import sqlite3


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    cursor.execute('insert into mouse_log (x_pos, y_pos) VALUES (?, ?)', (str(x), str(y)))
    if (x == 0.0 and y == 0.0):
        return False

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
try: 
    connection = sqlite3.connect('db/focuswatch.db', check_same_thread=False, isolation_level=None)
    connection.execute("PRAGMA journal_mode=WAL;")
    cursor = connection.cursor()
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()
finally:
    print("closing")
    connection.commit()
    connection.close()


# ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()