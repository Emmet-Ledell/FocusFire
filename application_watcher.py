# watch_active_app.py
import time
from AppKit import NSWorkspace

def get_frontmost_app_name():
    ws = NSWorkspace.sharedWorkspace()
    app = ws.frontmostApplication()
    if app is None:
        return None
    return app.localizedName()

def main():
    last = None
    while True:
        current = get_frontmost_app_name()
        # if current != last:
        print(f"Active app: {current}")
            # last = current
        time.sleep(0.5)  # adjust polling interval as you like

if __name__ == "__main__":
    main()