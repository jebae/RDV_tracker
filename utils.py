from bs4 import BeautifulSoup
import requests
import os
import json
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def crawl(url_to_send, criterias, request, method):
	soup = request()
	if not soup:
		message = "Prefecture 사이트 막힘"
		send_message(message)
		return
	if is_page_opened(soup, criterias):
		message = "체류증 ㄱㄱ!! {}".format(url_to_send)

		# this has to be email
		if method == "LINE":
			send_message(message)
		elif method == "MAIL":
			send_email()
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

def send_message(message):
	LINE_ACCESS_TOKEN = os.environ["LINE_ACCESS_TOKEN"]
	LINE_API_URL = os.environ["LINE_API_URL"]
	payload = {
		"message": message
	}
	for token in LINE_ACCESS_TOKEN.split(","):
		headers = {
			"Authorization" : "Bearer {}".format(token)
		}
		res = requests.post(LINE_API_URL, data=payload, headers=headers)
	return

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_PASSWORD = os.environ["GMAIL_PASSWORD"]

def send_email():
	try:
		# login gmail server
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(GMAIL_USER, GMAIL_PASSWORD)

		sent_from = GMAIL_USER
		msg = MIMEMultipart()
		msg["Subject"] = "RDV 열렸어용"
		msg["from"] = GMAIL_USER
		msg["To"] = GMAIL_USER # this has to be real to
		body = MIMEText("링크 : http://www.hauts-de-seine.gouv.fr/booking/create/4485")
		msg.attach(body)

		# send mail
		server.sendmail(sent_from, msg["To"], msg.as_string())
		server.close()
	except smtplib.SMTPAuthenticationError:
		print("Failed")
