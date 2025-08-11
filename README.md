
#  Job Scraper Notifier

A Python-based automation tool that scrapes job listings from selected job boards (like Indeed, LinkedIn, or others) based on user-defined keywords and locations, and notifies users via email.

Master JSON API Parsing and Website Scraping with Python Automation
https://youtu.be/WF4LtDWpye8
---

##  Features

*  Scrape jobs by keyword and location
*  Filter by posting date (e.g., "last 24 hours")
*  Email job listings directly to your inbox
*  Avoids duplicates by saving job IDs
*  Can be scheduled to run daily via `cron` or Task Scheduler

---

##  Requirements

* Python 3.8+
* `requests`
* `beautifulsoup4`
* `smtplib` or `yagmail` for email notifications
* `dotenv` for managing secrets (optional but recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/job-scraper-notifier.git
   cd job-scraper-notifier
   ```

2. **Create `.env` file** (or edit config in `config.py`)

   ```
   EMAIL_ADDRESS=youremail@example.com
   EMAIL_PASSWORD=yourpassword
   RECIPIENT_EMAIL=recipient@example.com
   JOB_KEYWORDS=frontend developer,react
   JOB_LOCATION=Toronto, ON
   ```

3. **Run the script**

   ```bash
   python job-scraper.py
   ```

---

##  Example Output

The email includes:

* Job Title
* Company
* Location
* Summary
* Direct Link

---

##  Sample Email Format

```plaintext
 New Job Alert: Frontend Developer - Shopify

Location: Toronto, ON  
Company: Shopify  
https://www.indeed.ca/viewjob?jk=abc123

Job Summary:
We are looking for a frontend developer with experience in React...

---
```

---

##  Automation

To run daily:

### On Windows:

Use Task Scheduler to run:

```bash
python C:\path\to\job-scraper.py
```

### On macOS/Linux:

Add a cron job:

```bash
0 9 * * * /usr/bin/python3 /path/to/job-scraper.py
```

---

##  TODO

* Add support for more job boards (LinkedIn, Workopolis, Glassdoor)
* Add Slack/Telegram notifications
* Add UI dashboard for configuring preferences

---

##  Author

**Manibala Sinha**
[LinkedIn](https://linkedin.com/in/yourprofile) • [Portfolio](https://yourportfolio.com)

---

##  License

MIT License
