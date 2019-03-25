from bs4 import BeautifulSoup
import requests
import os

def request():
	url_to_parse = os.environ["URL_TO_PARSE_92"]
	headers = {
		"User-Agent": "curl/7.54.0"
	}
	res = requests.get(url_to_parse, headers=headers)
	if res.status_code == 200:
		return BeautifulSoup(res.text, "html.parser")
	return None