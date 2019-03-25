from bs4 import BeautifulSoup
import requests
import os

def request():
	session = requests.Session()
	cookies = get_cookie(session)
	if not cookies:
		return None
	url_to_parse = os.environ["URL_TO_PARSE_94"]
	headers = {
		"Host": "rdv-etrangers-94.interieur.gouv.fr",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:66.0) Gecko/20100101 Firefox/66.0",
		"Accept": "*/*",
		"Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding": "gzip, deflate, br",
		"Referer": "https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/element/jsp/appointment.jsp",
		"Content-Type": "text/plain",
		"Content-Length": "296",
		"Connection": "keep-alive",
		"Cookie": "JSESSIONID={}; ID_ROUTE_GFA=.worker_gfa1"
			.format(cookies["JSESSIONID"]),
		"Pragma": "no-cache",
		"Cache-Control": "no-cache"
	}
	payload = {
		"callCount": 1,
		"page": "/eAppointmentpref94/element/jsp/appointment.jsp",
		"httpSessionId": "",
		"scriptSessionId": "",
		"c0-scriptName": "AjaxMotive",
		"c0-methodName": "motiveMultiSiteSubmit",
		"c0-id": "0",
		"c0-param0": "boolean:false",
		"c0-e1": "number:1",
		"c0-param1": "Object_Object:{120:reference:c0-e1}",
		"batchId": 1
	}
	res = session.post(url_to_parse, headers=headers, data=payload)
	if res.status_code == 200:
		return BeautifulSoup(res.text, "html.parser")
	return None

def get_cookie(session):
	url = "https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/element/jsp/specific/pref94.jsp"
	res = session.get(url)
	if res.status_code == 200:
		cookies = res.cookies.get_dict()
		return cookies
	return None