from bs4 import BeautifulSoup
import requests
import os
import json

def crawl(url_to_send, criterias, request):
	soup = request()
	if not soup:
		message = "Prefecture 사이트 막힘"
		send_message(message)
		return
	if is_page_opened(soup, criterias):
		message = "체류증 ㄱㄱ!! {}".format(url_to_send)
		send_message(message)
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
	headers = {
		"Authorization" : "Bearer {}".format(LINE_ACCESS_TOKEN)
	}
	payload = {
		"message": message
	}
	res = requests.post(LINE_API_URL, data=payload, headers=headers)
	return