import time
import json
import os
import psutil
from blocker import block_app
from active_tracker import run_active_tracker
import threading

PRODUCTIVE_KEYWORD = "app.solaro.com"
REQUIRED_TIME_SECONDS = 1800            # 30 minutes
APP_TO_BLOCK = "LeagueClient.exe"

def get_tracked_time(keyword: str) -> int:
    if not os.path.exists("tracked_time.json"):
        return 0
    
    with open("tracked_time.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    total = 0
    for title, seconds in data.items():
        if keyword.lower() in title.lower():
            total += seconds
    return total

# Start active tracker in background
threading.Thread(target=run_active_tracker, daemon=True).start()

# Main enforcement loop
while True:
    productive_time = get_tracked_time(PRODUCTIVE_KEYWORD)

    if productive_time < REQUIRED_TIME_SECONDS:
        block_app(APP_TO_BLOCK)
        print(f"Access not yet allowed!! Only spent {productive_time/60:.1f} mins on {PRODUCTIVE_KEYWORD}. Keep working!!")

    else:
        print("!! SUCCESS !!  Reward obtained!")
    time.sleep(60)