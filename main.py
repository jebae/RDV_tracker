import os
from utils import crawl

def crawl_92():
	from _92_ import request
	
	url_to_send = os.environ["URL_TO_SEND_92"]
	criterias = ["Aucun rendez-vous n'est disponible"]
	crawl(url_to_send, criterias, request)
	return

def crawl_94():
	from _94_ import request
	
	url_to_send = os.environ["URL_TO_SEND_94"]
	criterias = ["Aucun rendez-vous n\\'est disponible", 'message:"Error"']
	crawl(url_to_send, criterias, request)
	return
