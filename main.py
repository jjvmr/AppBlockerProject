import time
from tracker import time_spent_on_domain
from blocker import block_app

PRODUCTIVE_DOMAIN = "app.solaro.com"
REQUIRED_TIME_SECONDS = 1800            # 30 minutes
APP_TO_BLOCK = "LeagueClient.exe"

while True:
    if time_spent_on_domain(PRODUCTIVE_DOMAIN) < REQUIRED_TIME_SECONDS:
        block_app(APP_TO_BLOCK)
        print("Access not yet allowed. Stay productive!")

    else:
        print("Reward obtained!")
    time.sleep(60)