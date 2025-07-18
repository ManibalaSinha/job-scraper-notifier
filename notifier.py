import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(subject, body):
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("scraper", "emxd ifyw zyvn iwgz")
            server.sendmail(EMAIL_FROM, EMAIL_TO, message)
        print("✅ Email sent.")
    except Exception as e:
        print(f"❌ Email failed: {e}")
