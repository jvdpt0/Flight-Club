import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib

load_dotenv()

TWILLIO_SID = os.environ.get('TWILLIO_SID')
TWILLIO_AUTH_TOKEN = os.environ.get('TWILLIO_AUTH_TOKEN')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, sms_content):
        client = Client(TWILLIO_SID, TWILLIO_AUTH_TOKEN)
        message = client.messages.create(
            body = sms_content,
            from_= '+15074456521',
            to="+5584999533866"
        )
        print(message.status)
    
    def send_emails(self,emails,content):
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            for user_email in emails:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=user_email,
                    msg=f"Subject:New Low Price Flight!\n\n{content}".encode('utf-8')
                )