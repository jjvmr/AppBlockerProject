import time
import json
import os 
from datetime import datetime
import win32gui

LOG_FILE = "tracked_time.json"
POLL_INTERVAL = 5           # seconds

def get_active_windows_title():
    ''' Returns title of foreground window '''
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_log(data):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def run_active_tracker():
    print(f"[{datetime.now().isoformat()}] Starting universal active window tracker...")
    tracked_data = load_log()

    try:
        while True:
            title = get_active_windows_title().strip()

            if title:
                tracked_data[title] = tracked_data.get(title, 0) + POLL_INTERVAL
                print(f"[+] +{POLL_INTERVAL}s on ({title})")
                save_log(tracked_data)
            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        print("\n[!] Tracker stopped manually.")
        print("Final tracked time (in seconds):")
        for domain, seconds in tracked_data.items():
            print(f" - {domain}: {seconds}s ({seconds / 60:.1f} mins)" )


if __name__ == "__main__":
    run_active_tracker()