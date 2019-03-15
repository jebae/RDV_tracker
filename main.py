from bs4 import BeautifulSoup
import requests
import os
import json

URL_TO_PARSE = os.environ["URL_TO_PARSE"]
URL_TO_OPEN = os.environ["URL_TO_OPEN"]
LINE_ACCESS_TOKEN = os.environ["LINE_ACCESS_TOKEN"]
LINE_API_URL = os.environ["LINE_API_URL"]
CRITERIA = "Aucun rendez-vous n'est disponible"

def main():
	soup = request()
	if not soup:
		message = "Prefecture 사이트 막힘"
		send_message(message)
		return
	if is_page_opened(soup):
		message = "체류증 ㄱㄱ!! {}".format(URL_TO_OPEN)
		send_message(message)
	return

def request():
	headers = {
		"User-Agent": "curl/7.54.0"
	}
	res = requests.get(URL_TO_PARSE, headers=headers)
	if res.status_code == 200:
		return BeautifulSoup(res.text, "html.parser")
	return None

def is_page_opened(soup):
	text = soup.getText()
	if CRITERIA in text:
		return False
	elif len(text) == 0:
		return False
	return True

def send_message(message):
	headers = {
		"Authorization" : "Bearer {}".format(LINE_ACCESS_TOKEN)
	}
	payload = {
		"message": message
	}
	res = requests.post(LINE_API_URL, data=payload, headers=headers)
	return

main()
