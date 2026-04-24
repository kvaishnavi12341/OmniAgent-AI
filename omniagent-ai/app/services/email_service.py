import smtplib
from email.mime.text import MIMEText
from app.config import settings


class EmailService:
    def send_email(self, subject, body):
        try:
            if not settings.EMAIL_USER or not settings.EMAIL_PASS or not settings.EMAIL_TO:
                print("EMAIL CONFIG MISSING")
                return

            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = settings.EMAIL_USER
            msg["To"] = settings.EMAIL_TO

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
                server.send_message(msg)

            print("EMAIL SENT SUCCESSFULLY ✅")

        except Exception as e:
            print("EMAIL ERROR:", e)
#print("EMAIL_USER:", settings.EMAIL_USER)
#print("EMAIL_PASS:", settings.EMAIL_PASS)
#print("EMAIL_TO:", settings.EMAIL_TO)
'''
import smtplib
from app.config import settings

class EmailService:
    def send_email(self, subject, body):
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(settings.EMAIL_USER, settings.EMAIL_PASS)

            message = f"Subject:{subject}\n\n{body}"
            s.sendmail(settings.EMAIL_USER, settings.EMAIL_TO, message)
'''
