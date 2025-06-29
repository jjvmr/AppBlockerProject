from browser_history import get_history
from datetime import datetime, timedelta

def time_spent_on_domain(domain: str, hours=24) -> int:
    """ Estimate time spent on domain in the last N hours (in seconds) """
    outputs = get_history()
    entries = outputs.histories()    #List of *datetime, URL)
    now = datetime.now()
    cutoff = now - timedelta(hours=hours)
    time_spent = 0

    for entry in entries:
        timestamp, url = entry
        if domain in url and timestamp > cutoff:
            time_spent += 300 # rough estimate: 4 mins per visit
            print(f"Time spent on site: {timestamp} {url}")
    return time_spent

if __name__ == "__main__":
    domain = "app.solaro.com"
    seconds = time_spent_on_domain(domain)
    print(f"Estimated time spent on {domain}: {seconds // 60} mins ({seconds} seconds)")