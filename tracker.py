from browser_history import get_history
from datetime import datetime, timedelta

def time_spent_on_domain(domain: str, hours=24) -> int:
    """ Estimate time spent on domain in the last N hours (in seconds) """
    history = get_history().histories
    now = datetime.now()
    cutoff = now - timedelta(hours=hours)
    time_spent = 0

    for timestamp, url in history:
        if domain in url and timestamp > cutoff:
            time_spent += 300 # rough estimate: 4 mins per visit

    return time_spent