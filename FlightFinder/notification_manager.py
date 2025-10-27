import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib
# Using a .env file to retrieve the phone numbers and tokens.
load_dotenv()

class NotificationManager:

    def __init__(self):
        self._bash_app_password = os.environ["BASH_APP_PASSWORD"]
        self.sender = os.environ["SENDER"]

    def send_message(self, message, to_emails):
        for email in to_emails:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.sender, password=self._bash_app_password)
                connection.sendmail(from_addr=self.sender, to_addrs=email, msg=message)