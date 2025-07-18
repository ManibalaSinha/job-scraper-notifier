import schedule
import time
from scrape_jobs import scrape_and_notify  # your custom function

schedule.every(1).hour.do(scrape_and_notify)

while True:
    schedule.run_pending()
    time.sleep(60)
