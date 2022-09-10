from twilio.rest import Client
import smtplib
from flask import request
from urllib.parse import urlparse
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def mail_sender(email, random_str, route):
    server = smtplib.SMTP('smtp.stackmail.com', 587)
    server.starttls()
    # server.login('demo@designstime.com', '!E?G{=-!P;l[')
    server.login(os.getenv('SENDER_MAIL'), os.getenv('SENDER_PASSWORD'))
    parsed_uri = urlparse(request.base_url)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    mail_link = f'{result}{route}?q=' + random_str
    # mail_link = 'http://127.0.0.1:5000/email_verification?q=' + random_str
    message = f"Subject:Email Verification\n\nYour email verification link: {mail_link}"
    server.sendmail(os.getenv('SENDER_MAIL'), email, message)


def sms_sender(otp):
    account_sid = 'ACfcff1a3ae1ff2082b05cf8f27b51d59a'
    auth_token = 'dca548abfb1cfdc2c20e7692e3a0a3b5'
    client = Client(account_sid, auth_token)

    message = client.messages \
    .create(
         body=f'Your OTP code is : {otp}',
         from_='+17578565545',
         to='+923142388477'
        )



