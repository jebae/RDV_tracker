from bs4 import BeautifulSoup
import requests
import os

def request():
	session = requests.Session()
	enter_site(session)
	url_to_parse = os.environ["URL_TO_PARSE_MARIAGE"]
	data = {
		"condition" : "on",
		"nextButton" : "Effectuer+une+demande+de+rendez-vous"
	}
	headers = {
		"Host": "www.hauts-de-seine.gouv.fr",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:68.0) Gecko/20100101 Firefox/68.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"DNT": "1",
		"Connection": "keep-alive",
		"Upgrade-Insecure-Requests": "1",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
		"Referer": "http://www.hauts-de-seine.gouv.fr/Prendre-un-rendez-vous",
	}

	cookies = [k + "=" + v + ";" for k, v in session.cookies.get_dict().items()][0]
	cookies += " xtvrn=$488932$; xtan488932=-; xtant488932=1"
	headers.update({"Cookie": cookies})
	res = requests.get(url=url_to_parse, headers=headers)
	if res.status_code == 200:
		return BeautifulSoup(res.text, "html.parser")
	return None

def enter_site(session):
	urls = [
		"http://www.hauts-de-seine.gouv.fr",
		"http://www.hauts-de-seine.gouv.fr/Prendre-un-rendez-vous"
	]
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:68.0) Gecko/20100101 Firefox/68.0"
	}
	res = session.get(urls[0], headers=headers)
	res = session.get(urls[1], headers=headers)
	return
