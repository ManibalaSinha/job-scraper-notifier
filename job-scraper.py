import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from notifier import send_email

load_dotenv()

KEYWORDS = os.getenv("KEYWORDS", "python").split(",")

def fetch_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = soup.find_all("tr", class_="job")
    new_jobs = []

    for job in jobs:
        title_elem = job.find("h2")
        link_elem = job.find("a", class_="preventLink")

        if title_elem and link_elem:
            title = title_elem.text.strip()
            link = f"https://remoteok.com{link_elem['href']}"

            if any(kw.lower() in title.lower() for kw in KEYWORDS):
                new_jobs.append((title, link))

    return new_jobs

if __name__ == "__main__":
    jobs = fetch_jobs()
    if jobs:
        body = "\n".join(f"{title}\n{link}" for title, link in jobs)
        send_email("New Remote Jobs Found", body)
