from bs4 import BeautifulSoup
import requests
import os
from utils import send_email

def request():
	url_to_parse = os.environ["URL_TO_PARSE_MARIAGE"]
	headers = {
		"User-Agent": "curl/7.54.0"
	}
	data = {
		"condition": "on",
		"nextButton": "Effectuer+une+demande+de+rendez-vous"
	}
	res = requests.post(url_to_parse, data=data, headers=headers)
	if res.status_code == 200:
		return BeautifulSoup(res.text, "html.parser")
	return None
