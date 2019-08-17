from bs4 import BeautifulSoup
import requests
import os
import json
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def crawl(criterias, request, message):
    soup = request()
    if not soup:
        print(datetime.datetime.now(), "site closed")
        return
    if is_page_opened(soup, criterias):
        send_email(message, os.environ["CLIENT"])
    else:
        print(datetime.datetime.now(), "not available")
    return

def is_page_opened(soup, criterias):
    text = soup.getText()
    if len(text) == 0:
        return False
    for c in criterias:
        if c in text:
            return False
    return True

def send_email(message, to):
    GMAIL_USER = os.environ["GMAIL_USER"]
    GMAIL_PASSWORD = os.environ["GMAIL_PASSWORD"]
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    mail_content = MIMEMultipart()
    mail_content["Subject"] = "RDV 열렸어용"
    mail_content["From"] = GMAIL_USER
    mail_content["To"] = to
    message = MIMEText(message, "plain")
    mail_content.attach(message)
    server.sendmail(
		GMAIL_USER, to.split(", "), mail_content.as_string()
	)
    server.close()
