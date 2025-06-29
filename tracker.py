from browser_history.browsers import Chrome
from datetime import datetime, timedelta, timezone

def time_spent_on_domain(domain: str, hours=24) -> int:
    """ Estimate time spent on domain in the last N hours (in seconds) """
    entries = Chrome().fetch_history().histories    #List of (datetime, URL)
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=hours)
    time_spent = 0

    for timestamp, url, title in entries:
        ts_utc = timestamp.astimezone(timezone.utc)
        if domain in url and ts_utc > cutoff:
            time_spent += 300 # rough estimate: 4 mins per visit
            print(f"Time spent on {title}: {timestamp} {url}")
    return time_spent