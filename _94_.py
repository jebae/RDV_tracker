from bs4 import BeautifulSoup
import requests
import os

def request():
	session = requests.Session()
	url_to_parse = os.environ["URL_TO_PARSE_94"]
	get_cookie(session)
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
		"Pragma": "no-cache",
		"Cache-Control": "no-cache"
	}
	headers["Cookie"] = "JSESSIONID={}; ID_ROUTE_GFA=.worker_gfa1".format(session.cookies["JSESSIONID"])
	send_sitekey(session)
	# get_appointement(session)
	# post_motive(session, headers)
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
	headers = {
		"Host": "rdv-etrangers-94.interieur.gouv.fr",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:66.0) Gecko/20100101 Firefox/66.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding": "gzip, deflate, br",
		"Connection": "keep-alive",
		"Upgrade-Insecure-Requests": "1",
		"Cache-Control": "max-age=0"
	}
	res = session.get(url, headers=headers)
	return

def send_sitekey(session):
	url = "https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/appointment.do?sitekey=P943&userZip=94230&mobile=false"
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:66.0) Gecko/20100101 Firefox/66.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding": "gzip, deflate, br",
		"Referer": "https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/element/jsp/specific/pref94.jsp",
		"Connection": "keep-alive",
		"Cookie": "JSESSIONID={}; ID_ROUTE_GFA=.worker_gfa1".format(session.cookies["JSESSIONID"]),
		"Upgrade-Insecure-Requests": "1",
	}
	session.get(url, headers=headers)
	return

def get_appointement(session):
	url = "https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/element/jsp/appointment.jsp"
	headers = {
		"Host": "rdv-etrangers-94.interieur.gouv.fr",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:66.0) Gecko/20100101 Firefox/66.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding": "gzip, deflate, br",
		"Referer": "https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/element/jsp/specific/pref94.jsp",
		"Connection": "keep-alive",
		"Cookie": "JSESSIONID={}; ID_ROUTE_GFA=.worker_gfa1".format(session.cookies["JSESSIONID"]),
		# "Upgrade": "Insecure-Requests: 1"
		"Upgrade-Insecure-Requests": "1",
	}
	session.get(url, headers=headers)
	return

def post_motive(session, headers):
	url = "https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/dwr/call/plaincall/AjaxSelectionFormFeeder.upDateQuantityMotives.dwr"
	payload = {
		"callCount": 1,
		"page": "/eAppointmentpref94/element/jsp/appointment.jsp",
		"httpSessionId": "",
		"scriptSessionId": "BB6E1B4D2AB7A96E0AA9CAA6E9C38DBD51",
		"c0-scriptName": "AjaxSelectionFormFeeder",
		"c0-methodName": "upDateQuantityMotives",
		"c0-id": 0,
		"c0-param0": "boolean:false",
		"c0-param1": "boolean:false",
		"batchId": 0
	}
	session.post(url, headers=headers, data=payload)
	return